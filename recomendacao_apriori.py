import pandas as pd
from tabulate import tabulate


def printTable(table):
    df = pd.DataFrame(table)  # transforma dataframe
    table = tabulate(df, headers='keys', tablefmt='psql')  # formata para saida

    print(table)
    return


base_transacional = pd.read_csv('lista_compras.csv')

printTable(base_transacional.head())

sup = base_transacional.sum() / len(base_transacional)

printTable(sup)

sup_itens = sup[sup >= 0.05]

printTable(sup_itens)


def regras_tam_2(base, itens, taxa_sup, taxa_conf):
    for i, item in enumerate(itens):
        for j in range(i + 1, len(itens)):
            count_regra = len(base[(base[item] == 1) & (base[itens[j]] == 1)])
            suporte = count_regra / len(base)
            if suporte >= taxa_sup:
                count_a = len(base[base[item] == 1])
                confianca = count_regra / count_a
                if confianca >= taxa_conf:
                    print(item, "-->", itens[j],
                          "| suporte : ", suporte,
                          "| confianca : ", confianca, )


regras_tam_2(base_transacional, sup_itens.index, 0.01, 0.3)
