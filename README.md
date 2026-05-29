# 🌌 Project Selene – Sistema Orbital de Monitoramento Climático

## 📖 Descrição da Solução
O **Project Selene** é um sistema computacional desenvolvido em Python no contexto da **Indústria Espacial**.  
Ele integra dados climáticos reais da **NASA POWER API** com conceitos de **engenharia orbital**, como **Newton-Raphson** e **derivadas**, para validar a eficiência de comunicação entre satélite e antena antes de processar os dados climáticos.  

A solução simula o fluxo:  
**SATÉLITE → ANTENA → PROCESSAMENTO → DASHBOARD**  

## ⚙️ Funcionalidades
- Coleta automática de dados climáticos da NASA (temperatura, chuva, umidade).  
- Validação orbital do sinal da antena usando cálculo de eficiência e derivadas.  
- Classificação do sinal: **Estável, Moderado ou Instável**.  
- Bloqueio da análise climática em caso de falha orbital.  
- Análise estatística dos dados (médias, máximos e mínimos).  
- Classificação automática de risco climático (**Seguro, Moderado, Alto, Extremo**).  
- Exportação de resultados em **JSON** para integração com front-end.  
- Geração de gráficos em **PNG** para o dashboard:  
  - Temperatura  
  - Chuva  
  - Umidade  
  - Risco Climático  
  - Eficiência do Sinal  

## 📊 Benefícios Mensuráveis
- **Confiabilidade**: validação orbital garante que os dados só são processados se o sinal estiver estável.  
- **Prevenção**: classificação de risco climático permite identificar dias com potencial de enchente ou tempestade.  
- **Integração**: JSON e gráficos prontos para uso em dashboards interativos.  
- **Aplicação prática**: une dados reais da NASA com conceitos matemáticos e computacionais estudados na disciplina.  

## 🚀 Instruções de Execução
1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/project-selene.git
   cd project-selene
   ```
2. Instale as dependências:
   ```bash
   pip install requests pandas matplotlib numpy
   ```
3. Execute o script:
   ```bash
   python selene.py
   ```
4. Resultados:
   - Arquivo JSON gerado com dados e status orbital.  
   - Gráficos salvos em PNG:  
     - `grafico_temperatura.png`  
     - `grafico_chuva.png`  
     - `grafico_umidade.png`  
     - `grafico_risco.png`  
     - `grafico_sinal.png`  

## 📂 Organização do Repositório
```
project-selene/
│── selene.py              # Código-fonte principal
│── README.md              # Documentação do projeto
│── grafico_temperatura.png
│── grafico_chuva.png
│── grafico_umidade.png
│── grafico_risco.png
│── dados.json             # Exportação dos dados climáticos
