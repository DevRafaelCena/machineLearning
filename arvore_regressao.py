import pandas as pd
from tabulate import tabulate
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import export_graphviz


def printTable(table):
    df = pd.DataFrame(table)  # transforma dataframe
    table = tabulate(df, headers='keys', tablefmt='psql')  # formata para saida

    print(table)
    return


base = pd.read_excel("jogadores.xlsx")  # le excell

del base['Unnamed: 0']  # apaga coluna
printTable(base.head())

x = base.iloc[:, :-1]
y = base.iloc[:, -1]

tree = DecisionTreeRegressor(min_samples_leaf=2)

tree.fit(x, y)

amostra = base.sample()
printTable(amostra)

print(tree.predict(amostra.iloc[:, :-1]))
print(tree.predict([[1, 0, 1, 0, 1, 1]]))

# export_graphviz and check in http://www.webgraphviz.com/
arquivo = open("arvoreRegressao.dot", 'w')

export_graphviz(tree, out_file=arquivo, feature_names=x.columns)

arquivo.close()