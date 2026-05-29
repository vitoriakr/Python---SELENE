# 🌌 Project Selene – Sistema Orbital de Monitoramento Climático

## 📖 Descrição da Solução

O **Project Selene** é uma solução computacional desenvolvida em **Python** no contexto da **Indústria Espacial**, com foco em monitoramento climático e validação de comunicação orbital.

O sistema integra:

* dados climáticos reais obtidos da **NASA POWER API**;
* análise computacional de riscos ambientais;
* modelagem matemática da eficiência de sinal;
* aplicação de derivadas;
* utilização do método numérico de Newton-Raphson;
* geração de gráficos para dashboards web.

O objetivo principal do projeto é simular um sistema inteligente de monitoramento climático capaz de:

* coletar dados meteorológicos;
* analisar riscos de desastres naturais;
* validar a estabilidade do sinal orbital;
* auxiliar na tomada de decisão em sistemas críticos.

---

# 🌎 Problema Proposto

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

# 🛰️ Objetivos do Projeto

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

# ⚙️ Tecnologias Utilizadas

## Linguagem

* Python 3

## Bibliotecas

* requests
* pandas
* matplotlib
* numpy

## APIs e Fontes de Dados

* NASA POWER API

---

# 📡 Funcionamento Geral do Sistema

O sistema segue o seguinte fluxo computacional:

1. coleta dados climáticos reais da NASA;
2. organiza os dados em DataFrames;
3. realiza análise estatística automática;
4. classifica riscos climáticos;
5. calcula a eficiência orbital do sinal;
6. aplica derivadas e Newton-Raphson;
7. valida a estabilidade da comunicação;
8. gera gráficos;
9. exporta os dados para integração web.

---

# 🌦️ Coleta de Dados Climáticos

Os dados climáticos são obtidos através da **NASA POWER API**.

O sistema coleta automaticamente:

* temperatura média;
* volume de chuva;
* umidade relativa do ar.

Exemplo de coordenadas utilizadas:

* Porto Alegre – RS

```python
latitude = -30.03
longitude = -51.23
```

---

# 📊 Estruturação e Processamento de Dados

Os dados recebidos da API são convertidos para um **DataFrame Pandas**, permitindo:

* análise estatística;
* manipulação de séries temporais;
* cálculos automáticos;
* geração de gráficos;
* classificação de riscos.

Exemplo:

```python
dados_climaticos = pd.DataFrame({
    "Temperatura": parametros_nasa["T2M"],
    "Chuva": parametros_nasa["PRECTOTCORR"],
    "Umidade": parametros_nasa["RH2M"]
})
```

---

# 📈 Análise Climática Automatizada

O sistema calcula automaticamente:

* temperatura média;
* temperatura máxima;
* temperatura mínima;
* média de chuva;
* maior volume de chuva;
* umidade média.

Essas análises permitem identificar padrões meteorológicos e condições extremas.

---

# 🚨 Sistema Inteligente de Risco Climático

O Project Selene possui um sistema automatizado de classificação de risco climático.

As categorias utilizadas são:

* SEGURO
* RISCO MODERADO
* RISCO ALTO
* RISCO EXTREMO

A classificação considera:

* índice de chuva;
* umidade relativa do ar.

Exemplo da lógica utilizada:

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

# 📐 Aplicação Matemática

## Função de Eficiência Orbital

A eficiência do sinal orbital foi modelada matematicamente pela função:

[
E(x) = -x^2 + 50x
]

Onde:

* (E(x)) representa a eficiência do sinal;
* (x) representa a altura da antena.

Essa função foi utilizada para simular o comportamento do sinal conforme a altura da antena aumenta.

---

# 📘 Aplicação das Derivadas

Para identificar os pontos críticos da função, foi necessário calcular sua derivada.

A derivada representa a taxa de variação da função.

Derivando:

[
E(x) = -x^2 + 50x
]

obtém-se:

[
E'(x) = -2x + 50
]

Os pontos críticos ocorrem quando:

[
E'(x) = 0
]

Substituindo:

[
-2x + 50 = 0
]

[
-2x = -50
]

[
x = 25
]

Assim, o ponto crítico da função ocorre em:

[
x = 25
]

---

# 🔢 Método de Newton-Raphson

Como forma de automatizar o cálculo do ponto crítico, foi utilizado o método numérico de Newton-Raphson.

A fórmula utilizada é:

[
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
]

Onde:

* (x_n) representa a aproximação atual;
* (x_{n+1}) representa a nova aproximação;
* (f(x)) representa a derivada da função;
* (f'(x)) representa a segunda derivada.

O método realiza aproximações sucessivas até encontrar uma raiz suficientemente próxima de zero.

---

# 💻 Implementação do Método em Python

```python
def E(x):
    return -x**2 + 50*x

def dE(x):
    return -2*x + 50

def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):

    x = x0

    for _ in range(max_iter):

        x_new = x - f(x)/df(x)

        if abs(x_new - x) < tol:
            return x_new

        x = x_new

    return x

altura_ideal = newton_raphson(dE, lambda x: -2, 10)
```

---

# 📡 Validação Orbital do Sinal

Após encontrar a altura ideal da antena, o sistema realiza uma validação computacional da comunicação orbital.

A validação considera:

* eficiência do sinal;
* estabilidade operacional;
* variação da derivada.

O sistema classifica o sinal em:

* ESTÁVEL
* MODERADO
* INSTÁVEL

Caso o sinal seja considerado instável, o sistema interrompe o processamento climático para evitar falhas de comunicação.

---

# 📉 Geração de Gráficos

O sistema gera automaticamente gráficos para visualização dos dados.

Gráficos gerados:

* temperatura;
* chuva;
* umidade;
* risco climático.

Os gráficos são exportados em PNG para integração com dashboards web.

Exemplo:

```python
plt.savefig("grafico_temperatura.png")
```

---

# 🌐 Integração com Front-End

Os dados processados podem ser utilizados em:

* HTML;
* CSS;
* JavaScript;
* dashboards;
* sistemas web.

Os gráficos exportados podem ser incorporados diretamente em interfaces web.

---

# 📂 Estrutura do Projeto

```bash
python-selene/
│
├── selene.py
└── requirements.txt
README.md
```

---

# ▶️ Como Executar o Projeto

## 1. Instalar o Python

Download oficial:

[Python](https://www.python.org/downloads/?utm_source=chatgpt.com)

---

## 2. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/python-selene.git
```

---

## 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

## 4. Executar o sistema

```bash
python selene.py
```

---

# 📦 requirements.txt

```txt
requests
pandas
matplotlib
numpy
```

---

# 📊 Benefícios Mensuráveis da Solução

O Project Selene oferece diversos benefícios:

✅ automatização da análise climática;

✅ identificação rápida de riscos ambientais;

✅ apoio computacional à tomada de decisão;

✅ redução de falhas em comunicação orbital;

✅ integração com dashboards web;

✅ processamento automatizado de dados;

✅ aplicação prática de cálculo diferencial;

✅ utilização de métodos numéricos;

✅ simulação de ambientes reais da indústria espacial.

---

# 🧠 Conceitos Aplicados

## Matemática

* derivadas;
* cálculo diferencial;
* máximos e mínimos locais;
* método de Newton-Raphson.

## Programação

* consumo de APIs;
* análise de dados;
* DataFrames;
* automação computacional;
* geração de gráficos.

## Indústria Espacial

* monitoramento climático;
* comunicação via satélite;
* validação orbital;
* análise ambiental;
* prevenção de desastres climáticos.

---

# ✅ Conclusão

O Project Selene demonstrou como técnicas matemáticas e computacionais podem ser aplicadas em problemas reais da indústria espacial e do monitoramento climático.

A integração entre:

* APIs da NASA;
* análise de dados;
* derivadas;
* métodos numéricos;
* validação orbital;

permitiu desenvolver uma solução funcional, organizada e aplicável a sistemas modernos de monitoramento ambiental.

Além disso, o projeto evidencia a importância da programação, da matemática e da análise de dados na construção de sistemas inteligentes voltados à prevenção de desastres e apoio à tomada de decisão.

---
