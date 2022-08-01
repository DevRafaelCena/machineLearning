import pandas as pd
from tabulate import tabulate
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

def printTable(table):
    df = pd.DataFrame(table)  # transforma dataframe
    table = tabulate(df, headers='keys', tablefmt='psql')  # formata para saida

    print(table)
    return


base = pd.read_csv("compras_supermercado.csv", sep=",")  # le excell

printTable(base.head())

kmeans = KMeans(n_clusters=4, max_iter=1000)

kmeans.fit(base)

print(kmeans.labels_)

centroids = pd.DataFrame(kmeans.cluster_centers_, columns=base.columns)

printTable(centroids)

grupo , frequencia = np.unique(kmeans.labels_, return_counts=True)

print(grupo)
print(frequencia)
h = base[kmeans.labels_ ==0].hist()

plt.savefig("graphKmeans.png")


