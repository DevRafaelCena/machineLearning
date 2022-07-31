import pandas as pd
from tabulate import tabulate

base = pd.read_excel("funcionarios.xlsx")  # le excell

print(base.shape)  # retornar n colunas

del base['Unnamed: 0']  # apaga coluna

df = pd.DataFrame(base.head())  # transforma dataframe

table = tabulate(df, headers='keys', tablefmt='psql')  # formata para saida

print(table)

x = base.iloc[:, :-1]
y = base.iloc[:, -1]

df = pd.DataFrame(y)  # transforma dataframe

table = tabulate(df, headers='keys', tablefmt='psql')  # formata para saida

print(table)
