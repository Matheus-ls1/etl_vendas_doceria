import pandas as pd
import random 
from datetime import datetime, timedelta

#informações dos produtos com nome e preço
produtos_info = {
    'Banoffee': 14.0,
    'Morangoffee': 14.0,
    'Churros': 12.0,
    'Bolo': 12.0,
    'Pudim' : 8.0
}

#lista com os nomes dos produtos
lista_produtos = list(produtos_info.keys())

#simulação do período
data_inicio = datetime(2025, 1, 1)
data_final = datetime(2025, 12, 31)
dias_totais = (data_final - data_inicio).days

dados_vendas = []
gerador_encomendas = 2000

for i in range(gerador_encomendas):

    #criando datas aleatórias
    dias_aleatorios = random.randint(0, dias_totais)
    hora_aleatoria = random.randint(11,23)
    minutos_aleatorios = random.randint(0, 59)

    data_encomenda = data_inicio + timedelta(days=dias_aleatorios, hours=hora_aleatoria, minutes=minutos_aleatorios)

    #simular que 90% das enconmendas foram entregues
    estado = random.choices(['Entregue', 'Cancelada'], weights=[0.90, 0.10])[0]

    # simular alguns dados da encomenda
    produto_escolhido = random.choice(list(produtos_info.keys()))
    quantidade = random.randint(1,10)
    preco_unitario = produtos_info[produto_escolhido]

    # Adicionar o registo à lista
    dados_vendas.append({
        'ID_Encomenda': f'ENC-{1000 + i}',
        'Data_Calendario': data_encomenda.strftime('%Y-%m-%d %H:%M:%S'),
        'Produto': produto_escolhido,
        'Quantidade': quantidade,
        'Preco_Unitario': preco_unitario,
        'Estado_Encomenda': estado
    })

    #transformar a lista em um DataFrame
    df_vendas = pd.DataFrame(dados_vendas)

    #ordenar por ordem cronológica
    df_vendas = df_vendas.sort_values(by='Data_Calendario').reset_index(drop=True)

    #salva o dataframe em .csv na mesma pasta do projeto
    df_vendas.to_csv('vendas_doceria_2025.csv', index=False)

    print( "DataFrame 'vendas_doceria.csv' salvado com sucesso!", len(df_vendas), "registros!")