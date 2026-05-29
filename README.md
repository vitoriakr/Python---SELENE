# 🌌 Project Selene – Sistema Orbital de Monitoramento Climático

## 📖 Descrição da Solução
O **Project Selene** é um sistema computacional desenvolvido em Python no contexto da **Indústria Espacial**.  
Ele integra dados climáticos reais da **NASA POWER API** com conceitos de **engenharia orbital**, como **Newton-Raphson** e **derivadas**, para validar a eficiência de comunicação entre satélite e antena antes de processar os dados climáticos.  

O sistema integra:

* dados climáticos reais da NASA POWER API;
* análise computacional de riscos climáticos;
* cálculo de eficiência orbital de sinal;
* validação matemática utilizando derivadas;
* aplicação do método numérico de Newton-Raphson;
* geração de gráficos para dashboards web.

O objetivo principal do projeto é simular um ambiente real de monitoramento climático espacial, permitindo analisar condições meteorológicas críticas e validar se a comunicação orbital possui estabilidade suficiente para processar os dados coletados.

---

# 🌎 Problema Resolvido

Sistemas de monitoramento climático dependem de comunicação estável entre sensores terrestres e satélites.

Durante eventos extremos, como:

* enchentes;
* tempestades;
* tornados;
* alta umidade atmosférica;

a comunicação pode sofrer instabilidades.

O Project Selene resolve esse problema através de:

✅ análise automática de dados climáticos;
✅ classificação de riscos;
✅ validação computacional do sinal orbital;
✅ cálculo matemático da altura ideal da antena;
✅ geração de dados estruturados para dashboards web.

---

# 🛰️ Tecnologias Utilizadas

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

# 📊 Funcionalidades do Sistema

## ✅ Coleta de Dados Climáticos da NASA

O sistema consome dados reais da NASA POWER API contendo:

* temperatura;
* volume de chuva;
* umidade relativa do ar.

Os dados são obtidos utilizando coordenadas geográficas reais.

Exemplo utilizado:

* Porto Alegre/RS

---

## ✅ Estruturação e Processamento de Dados

Os dados recebidos pela API são transformados em um DataFrame Pandas para facilitar:

* análise estatística;
* cálculos;
* filtragens;
* classificação de risco;
* geração de gráficos.

---

## ✅ Análise Climática Automatizada

O sistema calcula automaticamente:

* temperatura média;
* temperatura máxima;
* temperatura mínima;
* chuva média;
* maior volume de chuva;
* umidade média.

---

## ✅ Sistema Inteligente de Risco Climático

O Project Selene classifica automaticamente os riscos climáticos em:

* SEGURO
* RISCO MODERADO
* RISCO ALTO
* RISCO EXTREMO

A classificação considera:

* volume de chuva;
* umidade relativa do ar.

---

# 📐 Aplicação Matemática

## Função de Eficiência Orbital

A eficiência do sinal orbital é representada pela função:

E(x) = -x² + 50x

Onde:

* E(x) representa a eficiência do sinal;
* x representa a altura da antena.

---

## Derivada da Função

A derivada foi utilizada para medir a variação da eficiência do sinal.

Derivando a função:

E(x) = -x² + 50x

obtém-se:

E'(x) = -2x + 50

Os pontos críticos da função ocorrem quando:

E'(x) = 0

---

# 🔢 Método de Newton-Raphson

O método numérico de Newton-Raphson foi utilizado para encontrar computacionalmente o ponto crítico da função.

Fórmula utilizada:

xₙ₊₁ = xₙ - f(xₙ)/f'(xₙ)

Esse método realiza aproximações sucessivas até encontrar um valor suficientemente próximo da raiz da derivada.

O resultado encontrado representa a altura ideal da antena para maximizar a estabilidade do sinal.

---

# 📡 Validação Orbital do Sinal

Após encontrar a altura ideal, o sistema realiza uma validação orbital computacional.

A validação analisa:

* eficiência do sinal;
* estabilidade operacional;
* variação da derivada.

O sistema classifica o sinal em:

* ESTÁVEL
* MODERADO
* INSTÁVEL

Caso o sinal seja considerado instável, o processamento climático é interrompido para evitar dados incorretos.

---

# 📈 Geração de Gráficos

O sistema gera automaticamente gráficos em PNG para integração com dashboards web.

Gráficos disponíveis:

* gráfico de temperatura;
* gráfico de chuva;
* gráfico de umidade;
* gráfico de risco climático.

Esses gráficos podem ser utilizados em:

* HTML;
* CSS;
* JavaScript;
* dashboards web;
* sistemas de monitoramento em tempo real.

---

# 🌐 Integração com Front-End

O sistema exporta os dados processados para estruturas compatíveis com front-end.

Os gráficos gerados podem ser utilizados diretamente em:

* sites;
* dashboards;
* painéis administrativos;
* sistemas de monitoramento climático.

---

# 📂 Estrutura do Projeto

```bash
python-selene/
│
├── selene.py
├── README.md
├── grafico_temperatura.png
├── grafico_chuva.png
├── grafico_umidade.png
├── grafico_risco.png
└── requirements.txt
```

---

# ▶️ Como Executar o Projeto

## 1. Instalar o Python

Download:
https://www.python.org/downloads/

---

## 2. Instalar as bibliotecas

Execute no terminal:

```bash
pip install requests pandas matplotlib numpy
```

---

## 3. Executar o sistema

```bash
python main.py
```

---

# 📊 Benefícios Mensuráveis da Solução

O Project Selene oferece diversos benefícios computacionais e operacionais:

✅ automatização da análise climática;

✅ identificação rápida de riscos;

✅ redução de falhas em comunicação orbital;

✅ apoio à tomada de decisão;

✅ integração com dashboards web;

✅ processamento de dados em tempo real;

✅ aplicação prática de cálculo diferencial e métodos numéricos;

✅ simulação de ambientes reais da indústria espacial.

---

# 🧠 Conceitos Aplicados

O projeto utiliza conceitos estudados em:

## Matemática

* derivadas;
* máximos e mínimos locais;
* cálculo diferencial;
* método de Newton-Raphson.

## Programação

* consumo de APIs;
* análise de dados;
* manipulação de DataFrames;
* geração de gráficos;
* automação computacional.

## Indústria Espacial

* monitoramento climático;
* validação orbital;
* comunicação via satélite;
* processamento de dados ambientais.

---

# ✅ Conclusão

O Project Selene demonstrou como técnicas matemáticas e computacionais podem ser aplicadas em problemas reais da indústria espacial e do monitoramento climático.

A integração entre:

* APIs da NASA;
* análise de dados;
* cálculo diferencial;
* métodos numéricos;
* validação orbital;

permitiu desenvolver uma solução funcional, organizada e aplicável a sistemas reais de comunicação e prevenção de desastres climáticos.

Além disso, o projeto evidencia a importância da programação e da matemática na construção de sistemas inteligentes voltados à tomada de decisão e análise ambiental.

---
