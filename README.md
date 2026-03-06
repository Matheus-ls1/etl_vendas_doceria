# 📊 Pipeline ETL: Relatório Automatizado de Vendas (Doceria)

## 🎯 Sobre o Projeto
Este projeto é uma simulação de um pipeline de dados ponta a ponta (ETL - Extract, Transform, Load) construído em Python. O objetivo principal é demonstrar a capacidade de extrair dados brutos de um sistema de encomendas, aplicar regras de negócio para limpeza e transformação, e gerar relatórios gerenciais automatizados em Excel.

Este tipo de automação substitui horas de trabalho manual em planilhas, entregando inteligência de negócio de forma rápida e formatada.

## 🛠️ Tecnologias Utilizadas
* **Python 3.x:** Linguagem base do projeto.
* **Pandas:** Para manipulação de grandes volumes de dados, limpeza e agregações complexas.
* **Openpyxl:** Engine para criação e formatação avançada de arquivos `.xlsx` nativamente pelo Python.
* **Datetime & Random:** Para geração de dados sintéticos e simulação de cenários reais.

## ⚙️ Arquitetura do Processo (ETL)

O projeto foi estruturado em quatro fases principais:

1. **Extração (Extract):** Criação de um script (`gerador_dados.py`) que simula a exportação de um banco de dados de um ano inteiro de vendas de uma doceria (com produtos como Banoffee, Churros e Brigadeiros), gerando um arquivo CSV com milhares de registros.
2. **Transformação (Transform):** Leitura do CSV bruto, filtragem de pedidos cancelados (limpeza de dados inconsistentes) e criação de novas métricas, como o cálculo do faturamento total por pedido e extração de dias da semana para análise de sazonalidade.
3. **Análise (Business Logic):** Agrupamento de dados para responder a perguntas de negócio:
   * Faturamento total mensal.
   * Ranking de produtos que geraram mais receita.
   * Volume de vendas por dia da semana.
4. **Carregamento (Load):** Exportação dos DataFrames analisados diretamente para um arquivo Excel (`Relatorio_Gerencial_Doceria.xlsx`). O script cria múltiplas abas, ajusta a largura das colunas e aplica formatação monetária (R$) automaticamente.

## 🚀 Como Executar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/Matheus-ls1/etl_vendas_doceria
