import pandas as pd

# ==== FILTRAR E AJUSTAR ALGUMAS COLUNAS =====

#carregar dados do arquivo
dados = pd.read_csv('vendas_doceria_2025.csv')

print( f'Total de vendas registradas: {len(dados)} ')

dados_filtrados = dados[dados['Estado_Encomenda'] == 'Entregue'].copy()

print(f"Total de registros após filtrar cancelamentos: {len(dados_filtrados)}")

# cria uma nova coluna com o faturamento total
dados_filtrados['Faturamento_Total'] = dados_filtrados['Quantidade'] * dados_filtrados['Preco_Unitario']

#preparar as datas
dados_filtrados['Data_Calendario'] = pd.to_datetime(dados_filtrados['Data_Calendario'])

#extrair o nome do mes e dia da semana
dados_filtrados['Mes'] = dados_filtrados['Data_Calendario'].dt.month
dados_filtrados['Dia_da_Semana'] = dados_filtrados['Data_Calendario'].dt.day_name()

print("\nPrimeiras linhas do DataFrame transformado:")
print(dados_filtrados[['Data_Calendario', 'Produto', 'Quantidade', 'Faturamento_Total', 'Dia_da_Semana']].head())

# ===== ANALISAR E AGRUPAR DADOS =====

faturamento_mensal = dados_filtrados.groupby('Mes')['Faturamento_Total'].sum().reset_index()

faturamento_mensal['Faturamento_Total'] = faturamento_mensal['Faturamento_Total'].round(2)

top_produtos = dados_filtrados.groupby('Produto').agg(
    Quantidade_Vendida=('Quantidade', 'sum'),
    Receita_Gerada=('Faturamento_Total', 'sum')
).reset_index()

print("\n--- Desempenho dos Produtos ---")
print(top_produtos)

dias_ordem = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
dados_filtrados['Dia_da_Semana'] = pd.Categorical(dados_filtrados['Dia_da_Semana'], categories=dias_ordem, ordered=True)

vendas_por_dia = dados_filtrados.groupby('Dia_da_Semana').size().reset_index(name='Total_Encomendas')

print("\n--- Volume de Encomendas por Dia da Semana ---")
print(vendas_por_dia)

caminho_excel = 'Relatorio_Doceria_2025.xlsx'

with pd.ExcelWriter(caminho_excel, engine='openpyxl') as writer:

    faturamento_mensal.to_excel(writer, sheet_name='Resumo Mensal', index=False)
    top_produtos.to_excel(writer, sheet_name='Produtos mais vendidos', index=False)
    vendas_por_dia.to_excel(writer, sheet_name='Vendas diarias', index=False)

    workbook = writer.book

    worksheet_mensal = writer.sheets['Resumo Mensal']
    worksheet_mensal.column_dimensions['A'].width = 15 # Coluna Mês
    worksheet_mensal.column_dimensions['B'].width = 20 # Coluna Faturamento
    
    # Aplicar formato de moeda (R$) na coluna B (Faturamento)
    for cell in worksheet_mensal['B']: 
        if cell.row != 1: # Ignorar o cabeçalho
            cell.number_format = 'R$ #,##0.00'
            
    # Formatar Aba: Top Produtos
    worksheet_produtos = writer.sheets['Produtos mais vendidos']
    worksheet_produtos.column_dimensions['A'].width = 25 # Coluna Produto
    worksheet_produtos.column_dimensions['B'].width = 20 # Coluna Quantidade
    worksheet_produtos.column_dimensions['C'].width = 20 # Coluna Receita
    
    # Aplicar formato de moeda na coluna C (Receita Gerada)
    for cell in worksheet_produtos['C']:
        if cell.row != 1:
            cell.number_format = 'R$ #,##0.00'
            
    # Formatar Aba: Sazonalidade
    worksheet_sazonal = writer.sheets['Vendas diarias']
    worksheet_sazonal.column_dimensions['A'].width = 20 # Coluna Dia da Semana
    worksheet_sazonal.column_dimensions['B'].width = 20 # Coluna Total Encomendas