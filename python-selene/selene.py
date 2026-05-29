import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# PROJECT SELENE
# Sistema Orbital de Monitoramento Climático
# ==========================================
# Este sistema integra dados climáticos da NASA com validação orbital,
# aplicando conceitos de cálculo numérico (Newton-Raphson), derivadas
# e análise de riscos para simular um ambiente espacial realista.

# Coordenadas de Porto Alegre (exemplo de aplicação prática)
latitude = -30.03
longitude = -51.23

# Intervalo de datas para coleta dos dados
start = "20230101"
end = "20251231"

# ==========================================
# COLETA DE DADOS NASA POWER
# ==========================================
# API da NASA POWER fornece dados climáticos diários (temperatura, chuva, umidade)
url = f"https://power.larc.nasa.gov/api/temporal/daily/point?start={start}&end={end}&latitude={latitude}&longitude={longitude}&community=RE&parameters=T2M,PRECTOTCORR,RH2M&format=JSON"

response = requests.get(url)
data = response.json()

# Extraindo parâmetros da resposta
parametros_nasa = data["properties"]["parameter"]

# ==========================================
# DATAFRAME DE DADOS CLIMÁTICOS
# ==========================================
# Estrutura organizada para análise dos dados
dados_climaticos = pd.DataFrame({
    "Temperatura": parametros_nasa["T2M"],
    "Chuva": parametros_nasa["PRECTOTCORR"],
    "Umidade": parametros_nasa["RH2M"]
})

dados_climaticos.index = pd.to_datetime(dados_climaticos.index)

# ==========================================
# FUNÇÕES DE EFICIÊNCIA ORBITAL
# ==========================================
# E(x) representa a eficiência do sinal da antena em função da altura
# dE(x) é a derivada, usada para medir a estabilidade do sinal
def E(x):
    return -x**2 + 50*x

def dE(x):
    return -2*x + 50

# Método de Newton-Raphson para encontrar altura ideal da antena
def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    for _ in range(max_iter):
        x_new = x - f(x)/df(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

altura_ideal = newton_raphson(dE, lambda x: -2, 10)

# ==========================================
# 8. VALIDAÇÃO ORBITAL DO SINAL
# ==========================================
print("\n==============================")
print("VALIDAÇÃO ORBITAL DO SINAL")
print("==============================")

eficiencia = E(altura_ideal)
estabilidade = abs(dE(altura_ideal))

print(f"\nAltura ideal da antena: {altura_ideal:.4f}")
print(f"Altura aproximada: {altura_ideal * 100:.2f} metros")
print(f"\nEficiência do sinal: {eficiencia:.2f}")
print(f"Variação do sinal (derivada): {estabilidade:.6f}")

# Classificação do sinal orbital
if eficiencia > 40 and estabilidade < 1:
    status_sinal = "ESTÁVEL"
elif eficiencia > 20:
    status_sinal = "MODERADO"
else:
    status_sinal = "INSTÁVEL"

print(f"\nStatus do sinal: {status_sinal}")

# Liberação dos dados climáticos condicionada ao sinal
if status_sinal == "INSTÁVEL":
    print("\nERRO: Falha na comunicação orbital. Dados climáticos não são confiáveis.")
    sistema_operacional = False
else:
    print("\nComunicação orbital validada. Processamento climático autorizado.")
    sistema_operacional = True

# ==========================================
# 9. PROCESSAMENTO CONDICIONAL
# ==========================================
if sistema_operacional:
    print("\nSistema operacional ativo. Análise climática concluída com sucesso.")
else:
    print("\nSistema em modo de segurança.")

# ==========================================
# ANÁLISE DE DADOS CLIMÁTICOS
# ==========================================
print("\n========== ANÁLISE CLIMÁTICA ==========\n")

temp_media = dados_climaticos["Temperatura"].mean()
temp_max = dados_climaticos["Temperatura"].max()
temp_min = dados_climaticos["Temperatura"].min()
chuva_media = dados_climaticos["Chuva"].mean()
chuva_max = dados_climaticos["Chuva"].max()
umidade_media = dados_climaticos["Umidade"].mean()

print(f"Temperatura média: {temp_media:.2f} °C")
print(f"Temperatura máxima: {temp_max:.2f} °C")
print(f"Temperatura mínima: {temp_min:.2f} °C")
print(f"\nChuva média: {chuva_media:.2f} mm")
print(f"Maior volume de chuva: {chuva_max:.2f} mm")
print(f"\nUmidade média: {umidade_media:.2f}%")

# ==========================================
# DETECÇÃO DE RISCO CLIMÁTICO
# ==========================================
print("\n========== ALERTAS ==========\n")

def classificar_risco(chuva, umidade):
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

print(dados_climaticos["Risco"].value_counts())

# ==========================================
# EXPORTAR JSON MELHORADO
# ==========================================
dados_json = {
    "temperatura": dados_climaticos["Temperatura"].tolist(),
    "chuva": dados_climaticos["Chuva"].tolist(),
    "vento": [],  # placeholder (API não fornece vento)
    "umidade": dados_climaticos["Umidade"].tolist(),
    "risco": dados_climaticos["Risco"].tolist(),
    "altura_ideal": float(altura_ideal),
    "eficiencia_sinal": float(eficiencia),
    "variacao_sinal": float(estabilidade),
    "status_sinal": status_sinal,
    "sistema_operacional": sistema_operacional,
    "graficos": {
        "temperatura": "grafico_temperatura.png",
        "chuva": "grafico_chuva.png",
        "umidade": "grafico_umidade.png",
        "risco": "grafico_risco.png",
        "sinal": "grafico_sinal.png"
    }
}

print("\nJSON pronto para integração com o front-end!")

# ==========================================
# GRÁFICOS EXPORTADOS PARA PNG
# ==========================================

# Temperatura
plt.figure(figsize=(12,5))
plt.plot(dados_climaticos.index, dados_climaticos["Temperatura"], label="Temperatura")
plt.title("Temperatura Média")
plt.xlabel("Data")
plt.ylabel("°C")
plt.legend()
plt.grid(True)
plt.show()
plt.savefig("grafico_temperatura.png")
plt.close()

# Chuva
plt.figure(figsize=(12,5))
plt.plot(dados_climaticos.index, dados_climaticos["Chuva"], label="Chuva")
plt.title("Volume de Chuva")
plt.xlabel("Data")
plt.ylabel("mm")
plt.legend()
plt.grid(True)
plt.show()
plt.savefig("grafico_chuva.png")
plt.close()

# Umidade
plt.figure(figsize=(12,6))
plt.plot(dados_climaticos.index, dados_climaticos["Umidade"], label="Umidade")
plt.title("Umidade Relativa do Ar")
plt.xlabel("Data")
plt.ylabel("Umidade (%)")
plt.legend()
plt.grid(True)
plt.show()
plt.savefig("grafico_umidade.png")
plt.close()

# Risco Climático
risco_contagem = dados_climaticos["Risco"].value_counts()
plt.figure(figsize=(10,6))
plt.bar(risco_contagem.index, risco_contagem.values)
plt.title("Classificação de Risco Climático")
plt.xlabel("Categoria")
plt.ylabel("Quantidade de Dias")
plt.grid(True)
plt.show()
plt.savefig("grafico_risco.png")
plt.close()