import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json

# ==========================================
# PROJECT SELENE
# Sistema Orbital de Monitoramento Climático
# ==========================================
# Integra dados climáticos reais da NASA POWER API com validação
# orbital baseada em cálculo diferencial e método de Newton-Raphson.
# O sistema classifica riscos climáticos, valida a estabilidade do
# sinal orbital e exporta dados e gráficos para dashboards web.

# ------------------------------------------
# COORDENADAS E PERÍODO DE COLETA
# ------------------------------------------
LATITUDE  = -30.03   # Porto Alegre – RS
LONGITUDE = -51.23
DATA_INICIO = "20230101"
DATA_FIM    = "20251231"

# ==========================================
# 1. COLETA DE DADOS — NASA POWER API
# ==========================================
# Parâmetros coletados:
#   T2M          → temperatura média a 2 metros (°C)
#   PRECTOTCORR  → precipitação corrigida (mm)
#   RH2M         → umidade relativa a 2 metros (%)

print("Conectando à NASA POWER API...")

url = (
    f"https://power.larc.nasa.gov/api/temporal/daily/point"
    f"?start={DATA_INICIO}&end={DATA_FIM}"
    f"&latitude={LATITUDE}&longitude={LONGITUDE}"
    f"&community=RE&parameters=T2M,PRECTOTCORR,RH2M&format=JSON"
)

resposta = requests.get(url)
dados_brutos = resposta.json()
parametros_nasa = dados_brutos["properties"]["parameter"]

print("Dados recebidos com sucesso.")

# ==========================================
# 2. ESTRUTURAÇÃO DOS DADOS EM DATAFRAME
# ==========================================
# Organiza os dados em série temporal para análise estatística,
# classificação de risco e geração de gráficos.

dados_climaticos = pd.DataFrame({
    "Temperatura": parametros_nasa["T2M"],
    "Chuva":       parametros_nasa["PRECTOTCORR"],
    "Umidade":     parametros_nasa["RH2M"]
})

dados_climaticos.index = pd.to_datetime(dados_climaticos.index)

# ==========================================
# 3. FUNÇÕES DE EFICIÊNCIA ORBITAL
# ==========================================
# E(x)   → eficiência do sinal em função da altura x da antena
# E'(x)  → primeira derivada: taxa de variação da eficiência
# E''(x) → segunda derivada: usada como f'(x) no Newton-Raphson

def E(x):
    """Função de eficiência orbital — polinômio de grau 6."""
    return (
        -(x**6)/6
        + (15*x**5)/5
        - (85*x**4)/4
        + (225*x**3)/3
        - (274*x**2)/2
        + 120*x
    )

def dE(x):
    """Primeira derivada de E(x): E'(x) = -x^5 + 15x^4 - 85x^3 + 225x^2 - 274x + 120."""
    return (
        -x**5
        + 15*x**4
        - 85*x**3
        + 225*x**2
        - 274*x
        + 120
    )

def ddE(x):
    """Segunda derivada de E(x): E''(x) = -5x^4 + 60x^3 - 255x^2 + 450x - 274."""
    return (
        -5*x**4
        + 60*x**3
        - 255*x**2
        + 450*x
        - 274
    )

# ==========================================
# 4. MÉTODO DE NEWTON-RAPHSON
# ==========================================
# Encontra a raiz de E'(x) = 0, ou seja, o ponto onde a eficiência
# do sinal é máxima (ponto crítico). Usa E''(x) como derivada de E'(x).
# Fórmula: x_(n+1) = x_n - E'(x_n) / E''(x_n)

def newton_raphson(x0, tolerancia=1e-6, max_iteracoes=100):
    """
    Aplica o método de Newton-Raphson sobre E'(x) para encontrar
    o ponto crítico (altura ideal da antena).

    Parâmetros:
        x0            → estimativa inicial
        tolerancia    → critério de parada (padrão: 1e-6)
        max_iteracoes → limite de iterações (padrão: 100)

    Retorna:
        x → altura ideal da antena
    """
    x = x0

    print("\n=== MÉTODO DE NEWTON-RAPHSON ===\n")

    for i in range(max_iteracoes):
        fx  = dE(x)
        dfx = ddE(x)

        if dfx == 0:
            print("Derivada segunda nula. Método interrompido.")
            break

        x_novo = x - fx / dfx

        print(f"Iteração {i+1:>3}: x = {x_novo:.6f} | E'(x) = {dE(x_novo):.8f}")

        if abs(x_novo - x) < tolerancia:
            print(f"\nConvergência atingida na iteração {i+1}.")
            return x_novo

        x = x_novo

    return x

# Ponto inicial escolhido próximo ao máximo global da função
altura_ideal = newton_raphson(x0=0.5)

# ==========================================
# 5. VALIDAÇÃO ORBITAL DO SINAL
# ==========================================
# Avalia eficiência e estabilidade do sinal com base na altura ideal.
# Limiares calibrados para o polinômio de grau 6 utilizado:
#   ESTÁVEL  → E > 35 e variação < 1  (operação normal)
#   MODERADO → E > 25                 (atenção)
#   INSTÁVEL → demais casos           (interrompe o sistema)

print("\n==============================")
print("VALIDAÇÃO ORBITAL DO SINAL")
print("==============================")

eficiencia_sinal  = E(altura_ideal)
variacao_sinal    = abs(dE(altura_ideal))

print(f"\nAltura ideal da antena : {altura_ideal:.4f}")
print(f"Altura aproximada      : {altura_ideal * 100:.2f} metros")
print(f"\nEficiência do sinal    : {eficiencia_sinal:.4f}")
print(f"Variação do sinal (E') : {variacao_sinal:.8f}")

if eficiencia_sinal > 35 and variacao_sinal < 1:
    status_sinal = "ESTÁVEL"
elif eficiencia_sinal > 25:
    status_sinal = "MODERADO"
else:
    status_sinal = "INSTÁVEL"

print(f"\nStatus do sinal: {status_sinal}")

if status_sinal == "INSTÁVEL":
    print("\nERRO: Falha na comunicação orbital. Dados climáticos não são confiáveis.")
    sistema_operacional = False
else:
    print("\nComunicação orbital validada. Processamento climático autorizado.")
    sistema_operacional = True

# ==========================================
# 6. ANÁLISE CLIMÁTICA
# ==========================================
if sistema_operacional:

    print("\n========== ANÁLISE CLIMÁTICA ==========\n")

    temp_media    = dados_climaticos["Temperatura"].mean()
    temp_maxima   = dados_climaticos["Temperatura"].max()
    temp_minima   = dados_climaticos["Temperatura"].min()
    chuva_media   = dados_climaticos["Chuva"].mean()
    chuva_maxima  = dados_climaticos["Chuva"].max()
    umidade_media = dados_climaticos["Umidade"].mean()

    print(f"Temperatura média    : {temp_media:.2f} °C")
    print(f"Temperatura máxima   : {temp_maxima:.2f} °C")
    print(f"Temperatura mínima   : {temp_minima:.2f} °C")
    print(f"\nChuva média          : {chuva_media:.2f} mm")
    print(f"Maior volume de chuva: {chuva_maxima:.2f} mm")
    print(f"\nUmidade média        : {umidade_media:.2f} %")

    # ==========================================
    # 7. CLASSIFICAÇÃO DE RISCO CLIMÁTICO
    # ==========================================
    # Categorias baseadas em índices de chuva e umidade:
    #   SEGURO         → chuva ≤ 10 mm
    #   RISCO MODERADO → chuva > 10 mm
    #   RISCO ALTO     → chuva > 20 mm e umidade > 80%
    #   RISCO EXTREMO  → chuva > 30 mm e umidade > 85%

    def classificar_risco(chuva, umidade):
        """Classifica o risco climático do dia com base em chuva e umidade."""
        if chuva > 30 and umidade > 85:
            return "RISCO EXTREMO"
        elif chuva > 20 and umidade > 80:
            return "RISCO ALTO"
        elif chuva > 10:
            return "RISCO MODERADO"
        else:
            return "SEGURO"

    dados_climaticos["Risco"] = dados_climaticos.apply(
        lambda row: classificar_risco(row["Chuva"], row["Umidade"]), axis=1
    )

    print("\n========== ALERTAS CLIMÁTICOS ==========\n")
    print(dados_climaticos["Risco"].value_counts().to_string())

    # ==========================================
    # 8. GERAÇÃO DE GRÁFICOS
    # ==========================================
    # Gráficos exportados em PNG para uso em dashboards web.
    # IMPORTANTE: plt.savefig() ANTES de plt.show() para garantir
    # que a figura seja salva antes de ser liberada da memória.

    # --- Temperatura ---
    plt.figure(figsize=(12, 5))
    plt.plot(dados_climaticos.index, dados_climaticos["Temperatura"],
    color="#E05C3A", linewidth=0.8, label="Temperatura (°C)")
    plt.title("Temperatura Média Diária — Porto Alegre (2023–2025)", fontsize=13)
    plt.xlabel("Data")
    plt.ylabel("°C")
    plt.legend()
    plt.grid(True, alpha=0.4)
    plt.tight_layout()
    plt.savefig("grafico_temperatura.png", dpi=150)
    plt.show()
    plt.close()

    # --- Chuva ---
    plt.figure(figsize=(12, 5))
    plt.bar(dados_climaticos.index, dados_climaticos["Chuva"],
    color="#3A7EE0", width=1.0, label="Precipitação (mm)")
    plt.title("Volume de Chuva Diário — Porto Alegre (2023–2025)", fontsize=13)
    plt.xlabel("Data")
    plt.ylabel("mm")
    plt.legend()
    plt.grid(True, alpha=0.4)
    plt.tight_layout()
    plt.savefig("grafico_chuva.png", dpi=150)
    plt.show()
    plt.close()

    # --- Umidade ---
    plt.figure(figsize=(12, 5))
    plt.plot(dados_climaticos.index, dados_climaticos["Umidade"],
    color="#3ABA6E", linewidth=0.8, label="Umidade Relativa (%)")
    plt.title("Umidade Relativa do Ar — Porto Alegre (2023–2025)", fontsize=13)
    plt.xlabel("Data")
    plt.ylabel("Umidade (%)")
    plt.legend()
    plt.grid(True, alpha=0.4)
    plt.tight_layout()
    plt.savefig("grafico_umidade.png", dpi=150)
    plt.show()
    plt.close()

    # --- Risco Climático ---
    ordem_categorias = ["SEGURO", "RISCO MODERADO", "RISCO ALTO", "RISCO EXTREMO"]
    cores_risco = ["#4CAF50", "#FFC107", "#FF5722", "#B71C1C"]
    contagem_risco = dados_climaticos["Risco"].value_counts().reindex(ordem_categorias, fill_value=0)

    plt.figure(figsize=(10, 6))
    plt.bar(contagem_risco.index, contagem_risco.values,
            color=cores_risco, edgecolor="white")
    plt.title("Distribuição de Risco Climático — Porto Alegre (2023–2025)", fontsize=13)
    plt.xlabel("Categoria de Risco")
    plt.ylabel("Quantidade de Dias")
    plt.grid(True, axis="y", alpha=0.4)
    plt.tight_layout()
    plt.savefig("grafico_risco.png", dpi=150)
    plt.show()
    plt.close()

    # --- Curva de Eficiência Orbital ---
    x_vals = np.linspace(0.1, 5.9, 500)
    y_vals = [E(x) for x in x_vals]

    plt.figure(figsize=(10, 5))
    plt.plot(x_vals, y_vals, color="#7B2FBE", linewidth=2, label="E(x) — Eficiência")
    plt.axvline(x=altura_ideal, color="red", linestyle="--", linewidth=1.5,
                label=f"Altura ideal: x = {altura_ideal:.2f}")
    plt.scatter([altura_ideal], [eficiencia_sinal],
                color="red", zorder=5, s=80)
    plt.title("Curva de Eficiência Orbital E(x)", fontsize=13)
    plt.xlabel("Altura da Antena (x)")
    plt.ylabel("Eficiência E(x)")
    plt.legend()
    plt.grid(True, alpha=0.4)
    plt.tight_layout()
    plt.savefig("grafico_sinal.png", dpi=150)
    plt.show()
    plt.close()

    print("\nGráficos gerados e salvos com sucesso.")

    # ==========================================
    # 9. EXPORTAÇÃO JSON PARA INTEGRAÇÃO WEB
    # ==========================================
    # Estrutura completa exportada em arquivo JSON para uso em
    # dashboards HTML/CSS/JavaScript ou APIs externas.

    dados_json = {
        "periodo": {
            "inicio": DATA_INICIO,
            "fim": DATA_FIM
        },
        "localizacao": {
            "latitude": LATITUDE,
            "longitude": LONGITUDE,
            "cidade": "Porto Alegre – RS"
        },
        "validacao_orbital": {
            "altura_ideal": float(altura_ideal),
            "eficiencia_sinal": float(eficiencia_sinal),
            "variacao_sinal": float(variacao_sinal),
            "status_sinal": status_sinal
        },
        "resumo_climatico": {
            "temp_media": round(temp_media, 2),
            "temp_maxima": round(temp_maxima, 2),
            "temp_minima": round(temp_minima, 2),
            "chuva_media": round(chuva_media, 2),
            "chuva_maxima": round(chuva_maxima, 2),
            "umidade_media": round(umidade_media, 2)
        },
        "distribuicao_risco": dados_climaticos["Risco"].value_counts().to_dict(),
        "series_temporais": {
            "temperatura": dados_climaticos["Temperatura"].tolist(),
            "chuva": dados_climaticos["Chuva"].tolist(),
            "umidade": dados_climaticos["Umidade"].tolist(),
            "risco": dados_climaticos["Risco"].tolist()
        },
        "graficos": {
            "temperatura": "grafico_temperatura.png",
            "chuva": "grafico_chuva.png",
            "umidade": "grafico_umidade.png",
            "risco": "grafico_risco.png",
            "sinal": "grafico_sinal.png"
        }
    }

    with open("dados_selene.json", "w", encoding="utf-8") as arquivo_json:
        json.dump(dados_json, arquivo_json, ensure_ascii=False, indent=4)

    print("Arquivo 'dados_selene.json' exportado com sucesso.")
    print("\nSistema Selene finalizado com sucesso.")

else:
    print("\nSistema em modo de segurança. Análise climática interrompida.")