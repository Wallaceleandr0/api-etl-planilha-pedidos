import pandas as pd
import numpy as np


def tratar_planilha_saldo(df):    
    df_inicial = pd.read_excel(df)
    colunas_preco = ['Qtd(CX)', 'Qtd(PC)', 'Prc Venda', 'Prc Orçamento', 'Valor', 'Valor Orçamento', 'Saldo', 'Sld Emb', 'Sld Cp.', 'P Bruto', 'Volume']

    for col in colunas_preco:
        df_inicial[col] = (df_inicial[col].str
                        .replace('.', '', regex=False)
                        .str.replace(',', '.', regex=False)
                        .astype(float)
                        )

    df_inicial['Status_Saldo'] = ''

    df_inicial['Status_Saldo'] = np.where(df_inicial['Saldo'] >= 20, 'Aprovado', 'Reprovado')

    df_inicial['Valor_Item'] = df_inicial['Qtd(PC)'] * df_inicial['Prc Venda']

    valor_total = (df_inicial.groupby('Pedido')['Valor_Item']
                .sum()
                .reset_index(name='Valor_Total_Pedido')
                )

    df_inicial['Valor_Total'] =  df_inicial.groupby('Pedido')['Valor_Item'].sum()

    df_saldo_final = (df_inicial[df_inicial['Status_Saldo'] == 'Aprovado']
                        .groupby(['Pedido'])['Valor_Item']
                        .sum()
                        .reset_index(name='Valor_Total_Saldo')
                        .merge(valor_total, on='Pedido')
                    )

    df_saldo_final['Representatividade'] = (df_saldo_final['Valor_Total_Saldo'] / df_saldo_final['Valor_Total_Pedido']) * 100

    resumo = df_saldo_final.to_dict(orient='records')

    itens = (
        df_inicial[[
            'Pedido',
            'Emissão',
            'Item',
            'Produto',
            'Descrição',
            'Galpão',
            'Qtd(CX)',
            'Qtd(PC)',
            'Prc Venda',
            'Prc Orçamento',
            'Valor',
            'Valor Orçamento',
            'Saldo',
            'Sld Emb',
            'Sld Cp.',
            'P Bruto',
            'Volume'
        ]]
        .to_dict(orient='records')
    )

    return {
        'resumo': resumo,
        'itens': itens
    }