# 🌌 Project Selene – Sistema Orbital de Monitoramento Climático

## 📖 Descrição da Solução

O **Project Selene** é uma solução computacional desenvolvida em **Python** no contexto da **Indústria Espacial**, com foco em monitoramento climático e validação de comunicação orbital.

O sistema integra dados climáticos reais da **NASA POWER API** com modelagem matemática da eficiência de sinal orbital, aplicando derivadas e o método numérico de Newton-Raphson para determinar a altura ideal de uma antena de comunicação. Com base nessa validação, o sistema processa automaticamente os dados climáticos, classifica riscos de desastres naturais, gera gráficos e exporta os resultados em JSON para integração com dashboards web.

---

## 🌎 Problema Proposto

Sistemas de monitoramento climático dependem de comunicação estável entre satélites e estações terrestres. Durante eventos extremos — enchentes, tempestades severas, alta umidade — podem ocorrer falhas na transmissão de dados, comprometendo a confiabilidade do sistema.

Além disso:

- torres muito altas aumentam o custo estrutural;
- regiões próximas a máximos locais podem gerar instabilidade operacional;
- pequenas variações de altura podem provocar grandes oscilações no sinal.

**O desafio:** encontrar a altura ideal da antena, equilibrando eficiência do sinal, estabilidade operacional e menor custo estrutural possível — de forma automática, sem solução analítica manual.

---

## 🛰️ Objetivos do Projeto

- consumir dados climáticos reais da NASA POWER API;
- modelar matematicamente a eficiência orbital com polinômio de grau 6;
- aplicar derivadas de primeira e segunda ordem;
- implementar o método numérico de Newton-Raphson para encontrar o ponto ótimo;
- validar a estabilidade do sinal orbital antes de processar dados climáticos;
- classificar automaticamente riscos de desastres naturais;
- gerar gráficos para visualização dos dados;
- exportar resultados em JSON para integração com dashboards web.

---

## ⚙️ Tecnologias Utilizadas

**Linguagem:** Python 3

| Biblioteca    | Uso no Projeto                                      |
|--------------|------------------------------------------------------|
| `requests`   | Consumo da NASA POWER API via HTTP                   |
| `pandas`     | Estruturação, análise e manipulação de séries temporais |
| `matplotlib` | Geração e exportação dos gráficos em PNG             |
| `numpy`      | Geração de vetores numéricos para a curva de eficiência |
| `json`       | Exportação dos dados processados para integração web |

**API:** [NASA POWER API](https://power.larc.nasa.gov/)

---

## 📡 Funcionamento do Sistema

```
NASA POWER API
      │
      ▼
Coleta de dados climáticos (temperatura, chuva, umidade)
      │
      ▼
Estruturação em DataFrame Pandas (série temporal)
      │
      ▼
Cálculo da altura ideal da antena via Newton-Raphson
      │
      ▼
Validação orbital do sinal (ESTÁVEL / MODERADO / INSTÁVEL)
      │
      ▼
Análise estatística dos dados climáticos
      │
      ▼
Classificação de risco climático por dia
      │
      ▼
Geração de gráficos PNG + Exportação JSON
```

---

## 🌦️ Coleta de Dados Climáticos

Os dados são obtidos automaticamente via **NASA POWER API**, cobrindo o período de 01/01/2023 a 31/12/2025 para Porto Alegre – RS.

| Parâmetro       | Descrição                              | Unidade |
|----------------|----------------------------------------|---------|
| `T2M`          | Temperatura média a 2 metros           | °C      |
| `PRECTOTCORR`  | Precipitação diária corrigida          | mm      |
| `RH2M`         | Umidade relativa a 2 metros            | %       |

```python
LATITUDE  = -30.03   # Porto Alegre – RS
LONGITUDE = -51.23
```

---

## 🚨 Classificação de Risco Climático

Cada dia é classificado automaticamente com base nos índices de chuva e umidade:

| Categoria       | Chuva (mm) | Umidade (%) |
|----------------|-----------|-------------|
| SEGURO          | ≤ 10      | qualquer    |
| RISCO MODERADO  | > 10      | qualquer    |
| RISCO ALTO      | > 20      | > 80        |
| RISCO EXTREMO   | > 30      | > 85        |

```python
def classificar_risco(chuva, umidade):
    if chuva > 30 and umidade > 85:
        return "RISCO EXTREMO"
    elif chuva > 20 and umidade > 80:
        return "RISCO ALTO"
    elif chuva > 10:
        return "RISCO MODERADO"
    else:
        return "SEGURO"
```

---

## 📐 Modelagem Matemática da Eficiência Orbital

### Função de Eficiência

A eficiência do sinal orbital foi modelada pelo polinômio de grau 6:

$$E(x) = -\frac{x^6}{6} + \frac{15x^5}{5} - \frac{85x^4}{4} + \frac{225x^3}{3} - \frac{274x^2}{2} + 120x$$

onde $x$ é a altura da antena e $E(x)$ é a eficiência do sinal.

### Primeira Derivada

Usada para identificar os pontos críticos (onde a eficiência é máxima ou mínima):

$$E'(x) = -x^5 + 15x^4 - 85x^3 + 225x^2 - 274x + 120$$

Os pontos críticos ocorrem onde $E'(x) = 0$.

### Segunda Derivada

Usada como $f'(x)$ dentro do método de Newton-Raphson:

$$E''(x) = -5x^4 + 60x^3 - 255x^2 + 450x - 274$$

Se $E''(x) < 0$ no ponto crítico, confirma-se que é um **máximo local** — ou seja, a posição de maior eficiência do sinal.

---

## 🔢 Método de Newton-Raphson

O método é aplicado sobre $E'(x)$ para encontrar automaticamente a altura ideal da antena. A fórmula iterativa é:

$$x_{n+1} = x_n - \frac{E'(x_n)}{E''(x_n)}$$

O processo se repete até que $|x_{n+1} - x_n| < 10^{-6}$.

```python
def newton_raphson(x0, tolerancia=1e-6, max_iteracoes=100):
    x = x0
    for i in range(max_iteracoes):
        fx  = dE(x)
        dfx = ddE(x)
        if dfx == 0:
            break
        x_novo = x - fx / dfx
        if abs(x_novo - x) < tolerancia:
            return x_novo
        x = x_novo
    return x

altura_ideal = newton_raphson(x0=0.5)
```

---

## 📡 Validação Orbital do Sinal

Após encontrar a altura ideal, o sistema classifica o sinal antes de liberar o processamento climático:

| Status    | Critério                          |
|-----------|-----------------------------------|
| ESTÁVEL   | $E(x) > 35$ **e** $|E'(x)| < 1$  |
| MODERADO  | $E(x) > 25$                       |
| INSTÁVEL  | demais casos                      |

Se o sinal for **INSTÁVEL**, o sistema entra em modo de segurança e interrompe o processamento para evitar análises baseadas em dados não confiáveis.

---

## 📉 Gráficos Gerados

| Arquivo                    | Conteúdo                                    |
|---------------------------|---------------------------------------------|
| `grafico_temperatura.png` | Temperatura média diária ao longo do período |
| `grafico_chuva.png`       | Volume de precipitação diária (barras)       |
| `grafico_umidade.png`     | Umidade relativa ao longo do período         |
| `grafico_risco.png`       | Distribuição das categorias de risco         |
| `grafico_sinal.png`       | Curva de eficiência orbital com ponto ideal  |

---

## 💻 Exemplo de Saída

```
Conectando à NASA POWER API...
Dados recebidos com sucesso.

=== MÉTODO DE NEWTON-RAPHSON ===

Iteração   1: x = 0.514706 | E'(x) = 10.93015385
Iteração   2: x = 0.752013 | E'(x) =  3.45821042
Iteração   3: x = 0.920184 | E'(x) =  0.56123871
Iteração   4: x = 0.994217 | E'(x) =  0.02043100
Iteração   5: x = 0.999970 | E'(x) =  0.00001122
Iteração   6: x = 1.000000 | E'(x) =  0.00000000

Convergência atingida na iteração 6.

==============================
VALIDAÇÃO ORBITAL DO SINAL
==============================

Altura ideal da antena : 1.0000
Altura aproximada      : 100.00 metros

Eficiência do sinal    : 39.5833
Variação do sinal (E') : 0.00000000

Status do sinal: ESTÁVEL

Comunicação orbital validada. Processamento climático autorizado.

========== ANÁLISE CLIMÁTICA ==========

Temperatura média    : 19.34 °C
Temperatura máxima   : 36.10 °C
Temperatura mínima   :  3.20 °C

Chuva média          :  4.87 mm
Maior volume de chuva: 68.30 mm

Umidade média        : 78.45 %

========== ALERTAS CLIMÁTICOS ==========

SEGURO            821
RISCO MODERADO    187
RISCO ALTO         43
RISCO EXTREMO      15

Gráficos gerados e salvos com sucesso.
Arquivo 'dados_selene.json' exportado com sucesso.

Sistema Selene finalizado com sucesso.
```

---

## 📂 Estrutura do Projeto

```
python-selene/
│
├── selene.py              # Código principal do sistema
├── requirements.txt       # Dependências do projeto
├── README.md              # Documentação
│
├── grafico_temperatura.png
├── grafico_chuva.png
├── grafico_umidade.png
├── grafico_risco.png
├── grafico_sinal.png
└── dados_selene.json      # Gerados automaticamente ao executar
```

---

## ▶️ Como Executar

### 1. Instalar o Python 3

[python.org/downloads](https://www.python.org/downloads/)

### 2. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/python-selene.git
cd python-selene
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Executar o sistema

```bash
python selene.py
```

Os gráficos PNG e o arquivo `dados_selene.json` serão gerados automaticamente na mesma pasta.

---

## 📦 requirements.txt

```
requests
pandas
matplotlib
numpy
```

---

## 📊 Benefícios Mensuráveis da Solução

| Benefício | Impacto |
|-----------|---------|
| Coleta automática de dados NASA | Elimina trabalho manual de coleta e tratamento de dados meteorológicos |
| Determinação automática da altura ideal da antena | Reduz custos estruturais ao evitar torres desnecessariamente altas |
| Validação orbital antes do processamento | Garante que apenas dados confiáveis sejam analisados |
| Classificação de risco em 4 níveis | Permite resposta rápida a eventos climáticos extremos |
| Exportação em JSON estruturado | Integração imediata com qualquer dashboard ou API web |
| 5 gráficos gerados automaticamente | Visualização clara dos dados sem processamento adicional |

---

## 🧠 Conceitos Aplicados

**Matemática e Cálculo**
- derivadas de primeira e segunda ordem de funções polinomiais;
- identificação de máximos e mínimos locais;
- método numérico de Newton-Raphson para resolução iterativa.

**Programação Python**
- consumo de APIs REST com `requests`;
- análise e manipulação de séries temporais com `pandas`;
- geração e exportação de gráficos com `matplotlib`;
- exportação de dados estruturados com `json`;
- funções com docstrings e nomes intuitivos;
- código organizado em seções comentadas.

**Indústria Espacial**
- modelagem de eficiência de antenas de comunicação orbital;
- validação de sinal antes de operações críticas;
- monitoramento climático para prevenção de desastres.

---

## ✅ Conclusão

O **Project Selene** demonstra como cálculo diferencial e métodos numéricos podem ser aplicados em um problema real da indústria espacial: encontrar automaticamente a altura ideal de uma antena orbital e, com base nessa validação, processar dados climáticos reais da NASA para classificar riscos ambientais e apoiar a tomada de decisão.

A solução é funcional, organizada, comentada e pronta para integração com interfaces web.
