import pandas as pd
from tabulate import tabulate
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz


def printTable(table):
    df = pd.DataFrame(table)  # transforma dataframe
    table = tabulate(df, headers='keys', tablefmt='psql')  # formata para saida

    print(table)
    return


base = pd.read_excel("funcionarios.xlsx")  # le excell

del base['Unnamed: 0']  # apaga coluna
printTable(base)

x = base.iloc[:, :-1]
y = base.iloc[:, -1]

tree = DecisionTreeClassifier()

tree.fit(x, y)

amostra = base.sample()
printTable(amostra)

print(tree.predict(amostra.iloc[:, :-1]))
print(tree.predict([[2, 0, 0, 1, 1, 0]]))


# export_graphviz and check in http://www.webgraphviz.com/

arquivo = open("arvore.dot", 'w')

export_graphviz(tree, out_file=arquivo, feature_names=x.columns,class_names=base.linguagem.unique())

arquivo.close()
