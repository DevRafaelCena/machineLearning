import pandas as pd
from tabulate import tabulate
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

## ajudou para conf ambiente https://stackoverflow.com/questions/56656777/userwarning-matplotlib-is-currently-using-agg-which-is-a-non-gui-backend-so
## https://stackoverflow.com/questions/29042276/plotting-a-dataframe-pandas-in-pycharm-not-displaying

base = pd.read_excel('casas.xlsx')


def printTable(table):
    df = pd.DataFrame(table)  # transforma dataframe
    table = tabulate(df, headers='keys', tablefmt='psql')  # formata para saida

    print(table)
    return


del base['Unnamed: 0']  # apaga coluna
printTable(base)

base.plot(kind='scatter', x='metros quadrados', y='preco')

plt.savefig("mygraph.png")

x = base[['metros quadrados']]
y = base[['preco']]

regressao = LinearRegression()

regressao.fit(x, y)

# coef = regressao.coef_
# intercept = regressao.intercept_

# y = coef*x * intercept

print(regressao.predict([[1500]]))
print(regressao.coef_[0] * 1500 + regressao.intercept_[0])

base2 = pd.read_excel('casas_mult.xlsx')

del base2['Unnamed: 0']  # apaga coluna
printTable(base2.head())

x2 = base2[['metros quadrados', 'banheiros', 'metros sem porao', 'nota']]

y2 = base2[['preco']]

regressao2 = LinearRegression()

regressao2.fit(x2, y2)

print(regressao2.coef_)
print(regressao2.intercept_)

print(regressao2.predict([[1500, 1, 160, 7]]))
