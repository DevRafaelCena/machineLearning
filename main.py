import pandas as pd
from tabulate import tabulate
from sklearn.neighbors import KNeighborsClassifier


def printTable(table):
    df = pd.DataFrame(table.head())  # transforma dataframe
    table = tabulate(df, headers='keys', tablefmt='psql')  # formata para saida

    print(table)
    return


base = pd.read_excel("funcionarios.xlsx")  # le excell

print(base.shape)  # retornar n colunas

del base['Unnamed: 0']  # apaga coluna

printTable(base)

x = base.iloc[:, :-1]
y = base.iloc[:, -1]

printTable(y)

knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(x, y)

amostra = base.sample()
print(amostra)
amostra = amostra.iloc[:, :-1]

printTable(amostra)

print(knn.predict(amostra))
print(knn.predict([[2, 1, 0, 0, 1, 0]]))
