# 🌌 Project Selene – Sistema Orbital de Monitoramento Climático

## 📖 Descrição da Solução

O **Project Selene** é uma solução computacional desenvolvida em **Python** no contexto da **Indústria Espacial**, com foco em monitoramento climático e validação de comunicação orbital.

O sistema integra:

* dados climáticos reais obtidos da **NASA POWER API**;
* análise computacional de riscos ambientais;
* modelagem matemática da eficiência de sinal;
* aplicação de derivadas (primeira e segunda);
* utilização do método numérico de Newton-Raphson;
* geração de gráficos para dashboards web.

O objetivo principal do projeto é simular um sistema inteligente de monitoramento climático capaz de:

* coletar dados meteorológicos;
* analisar riscos de desastres naturais;
* validar a estabilidade do sinal orbital;
* auxiliar na tomada de decisão em sistemas críticos.

---

## 🌎 Problema Proposto

Sistemas de monitoramento climático dependem de comunicação estável entre satélites e estações terrestres.

Durante eventos extremos, como:

* enchentes;
* tempestades severas;
* alta umidade atmosférica;
* ventos intensos;

podem ocorrer falhas na transmissão de dados, comprometendo a confiabilidade do sistema.

Além disso:

* torres muito altas aumentam o custo estrutural;
* regiões próximas a máximos locais podem gerar instabilidade operacional;
* pequenas variações podem provocar grandes oscilações no sinal.

Dessa forma, o desafio consiste em encontrar uma altura adequada para a antena, equilibrando:

✅ eficiência do sinal;  
✅ estabilidade operacional;  
✅ menor custo estrutural possível.

---

## 🛰️ Objetivos do Projeto

O Project Selene foi desenvolvido com os seguintes objetivos:

* consumir dados climáticos reais da NASA;
* automatizar análises meteorológicas;
* detectar riscos ambientais;
* aplicar cálculo diferencial em um problema real;
* implementar o método de Newton-Raphson em Python;
* simular validação orbital de comunicação;
* gerar dados para dashboards web;
* auxiliar sistemas de monitoramento climático.

---

## ⚙️ Tecnologias Utilizadas

### Linguagem

* Python 3

### Bibliotecas

* `requests` — consumo da NASA POWER API
* `pandas` — estruturação e análise dos dados climáticos
* `matplotlib` — geração de gráficos
* `numpy` — suporte a operações numéricas

### APIs e Fontes de Dados

* [NASA POWER API](https://power.larc.nasa.gov/)

---

## 📡 Funcionamento Geral do Sistema

O sistema segue o seguinte fluxo computacional:

1. coleta dados climáticos reais da NASA;
2. organiza os dados em DataFrames;
3. realiza análise estatística automática;
4. classifica riscos climáticos;
5. calcula a eficiência orbital do sinal com polinômio de grau 6;
6. aplica primeira e segunda derivadas;
7. aplica Newton-Raphson para encontrar a altura ideal da antena;
8. valida a estabilidade da comunicação orbital;
9. gera gráficos em PNG;
10. exporta os dados para integração web.

---

## 🌦️ Coleta de Dados Climáticos

Os dados climáticos são obtidos através da **NASA POWER API**.

O sistema coleta automaticamente:

* temperatura média (`T2M`);
* volume de chuva (`PRECTOTCORR`);
* umidade relativa do ar (`RH2M`).

Coordenadas utilizadas como exemplo:

```python
# Porto Alegre – RS
latitude  = -30.03
longitude = -51.23
```

---

## 📊 Estruturação e Processamento de Dados

Os dados recebidos da API são convertidos para um **DataFrame Pandas**, permitindo:

* análise estatística;
* manipulação de séries temporais;
* cálculos automáticos;
* geração de gráficos;
* classificação de riscos.

```python
dados_climaticos = pd.DataFrame({
    "Temperatura": parametros_nasa["T2M"],
    "Chuva":       parametros_nasa["PRECTOTCORR"],
    "Umidade":     parametros_nasa["RH2M"]
})
```

---

## 📈 Análise Climática Automatizada

O sistema calcula automaticamente:

* temperatura média, máxima e mínima;
* média e maior volume de chuva registrado;
* umidade média do período.

Essas análises permitem identificar padrões meteorológicos e condições extremas.

---

## 🚨 Sistema Inteligente de Risco Climático

O Project Selene possui um sistema automatizado de classificação de risco climático.

| Categoria      | Condição                              |
|----------------|---------------------------------------|
| SEGURO         | Chuva ≤ 10 mm                         |
| RISCO MODERADO | Chuva > 10 mm                         |
| RISCO ALTO     | Chuva > 20 mm **e** Umidade > 80%     |
| RISCO EXTREMO  | Chuva > 30 mm **e** Umidade > 85%     |

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

## 📐 Aplicação Matemática

### Função de Eficiência Orbital

A eficiência do sinal orbital foi modelada por um polinômio de **grau 6**:

```
E(x) = -x⁶/6 + 15x⁵/5 - 85x⁴/4 + 225x³/3 - 274x²/2 + 120x
```

Onde:
* `E(x)` representa a eficiência do sinal orbital;
* `x` representa a altura da antena.

Essa função captura o comportamento não-linear do sinal conforme a altura varia, incluindo múltiplos pontos críticos locais.

---

## 📘 Aplicação das Derivadas

Para identificar os pontos críticos da função, foram calculadas a **primeira** e a **segunda** derivada.

### Primeira derivada — E'(x)

Identifica onde a eficiência é máxima ou mínima (taxa de variação = 0):

```
E'(x) = -x⁵ + 15x⁴ - 85x³ + 225x² - 274x + 120
```

O ponto crítico ocorre quando `E'(x) = 0`.

### Segunda derivada — E''(x)

Confirma a natureza do ponto crítico (máximo, mínimo ou inflexão) e é usada como derivada no método de Newton-Raphson:

```
E''(x) = -5x⁴ + 60x³ - 255x² + 450x - 274
```

---

## 🔢 Método de Newton-Raphson

Para encontrar automaticamente o zero de `E'(x)` — ou seja, a altura ideal da antena — foi aplicado o método numérico de **Newton-Raphson**:

```
x_(n+1) = x_n - E'(x_n) / E''(x_n)
```

Onde:
* `x_n` é a aproximação atual;
* `E'(x_n)` é a primeira derivada avaliada em `x_n`;
* `E''(x_n)` é a segunda derivada avaliada em `x_n` (jacobiano local).

O método realiza aproximações sucessivas até que a diferença entre iterações seja menor que a tolerância definida (`1e-6`).

---

## 💻 Implementação em Python

```python
def E(x):
    return (
        -(x**6)/6 + (15*x**5)/5 - (85*x**4)/4 +
        (225*x**3)/3 - (274*x**2)/2 + 120*x
    )

def dE(x):
    return (
        -x**5 + 15*x**4 - 85*x**3 + 225*x**2 - 274*x + 120
    )

def ddE(x):
    return (
        -5*x**4 + 60*x**3 - 255*x**2 + 450*x - 274
    )

def newton_raphson(x0, tolerancia=1e-6, max_iteracoes=100):
    x = x0
    for i in range(max_iteracoes):
        fx  = dE(x)
        dfx = ddE(x)
        if dfx == 0:
            break
        x_new = x - fx / dfx
        if abs(x_new - x) < tolerancia:
            return x_new
        x = x_new
    return x

altura_ideal = newton_raphson(x0=0.5)
```

---

## 📡 Validação Orbital do Sinal

Após encontrar a altura ideal, o sistema valida a comunicação orbital considerando:

* `E(altura_ideal)` — eficiência do sinal naquele ponto;
* `|E'(altura_ideal)|` — variação do sinal (quanto menor, mais estável).

| Status    | Condição                              |
|-----------|---------------------------------------|
| ESTÁVEL   | Eficiência > 40 e variação < 1        |
| MODERADO  | Eficiência > 20                        |
| INSTÁVEL  | Demais casos                           |

Se o sinal for **INSTÁVEL**, o sistema entra em modo de segurança e interrompe o processamento climático.

---

## 📉 Geração de Gráficos

O sistema exporta automaticamente os seguintes gráficos em PNG:

| Arquivo                  | Conteúdo                        |
|--------------------------|---------------------------------|
| `grafico_temperatura.png`| Série temporal de temperatura   |
| `grafico_chuva.png`      | Volume diário de chuva          |
| `grafico_umidade.png`    | Umidade relativa do ar          |
| `grafico_risco.png`      | Distribuição de categorias de risco |

---

## 🌐 Integração com Front-End

Os dados processados e os gráficos PNG podem ser integrados diretamente em:

* dashboards HTML/CSS/JavaScript;
* sistemas web de monitoramento;
* relatórios automáticos.

---

## 📂 Estrutura do Repositório

```
python-selene/
├── selene.py
├── requirements.txt
└── README.md
```

---

## ▶️ Como Executar o Projeto

### 1. Instalar o Python 3

Download oficial: [python.org/downloads](https://www.python.org/downloads/)

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

| Benefício | Descrição |
|---|---|
| ⚡ Automatização | Análise climática sem intervenção manual |
| 🚨 Detecção de riscos | Identificação imediata de condições extremas |
| 🛰️ Validação orbital | Garantia de integridade na comunicação via satélite |
| 📊 Visualização | Gráficos prontos para dashboards web |
| 🔢 Precisão numérica | Newton-Raphson com tolerância de 1e-6 |
| 🔗 Integração | JSON exportável para qualquer front-end |

---

## 🧠 Conceitos Aplicados

### Matemática
* derivadas (primeira e segunda);
* cálculo diferencial;
* máximos e mínimos locais;
* método numérico de Newton-Raphson.

### Programação
* consumo de APIs REST;
* análise de dados com Pandas;
* geração de gráficos com Matplotlib;
* automação computacional.

### Indústria Espacial
* monitoramento climático;
* comunicação via satélite;
* validação orbital;
* prevenção de desastres climáticos.

---

## ✅ Conclusão

O Project Selene demonstrou como técnicas matemáticas e computacionais podem ser aplicadas em problemas reais da indústria espacial e do monitoramento climático.

A integração entre NASA POWER API, análise de dados, derivadas de polinômios de grau 6, método de Newton-Raphson e validação orbital resultou em uma solução funcional, organizada e aplicável a sistemas modernos de monitoramento ambiental.

O projeto evidencia a importância da programação, da matemática e da análise de dados na construção de sistemas inteligentes voltados à prevenção de desastres e apoio à tomada de decisão.
