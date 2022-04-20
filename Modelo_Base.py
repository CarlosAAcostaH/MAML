# -*- coding: utf-8 -*-
"""

@author: david.hernandez & Carlos.Acosta
"""

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

Dir  = 'C:/Users/david.hernandez/Documents/MAML/'
Datos = pd.read_excel(Dir + 'BaseDatosMAML_Pry.xlsx')
Datos.columns
Datos.dtypes


filtro = Datos['Ingresos'] != 0
Datos = Datos[filtro]


df = Datos.drop(['Año', 'Trim', 'Nombre EAPB'], axis = 1)


krango = range (1,10)
sse = []

for k in krango:
	Kmeans = KMeans(n_clusters = k).fit(df)
	sse.append(Kmeans.inertia_)


Kmeans = KMeans(n_clusters=5).fit(df)

Centroids = Kmeans.cluster_centers_
print(Centroids)

plt.scatter(df['Utilidad Neta'],df['Siniestralidad'], c = Kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(Centroids[:,0], Centroids[:,1], c='red', s = 50)
plt.show()


plt.scatter(df['Utilidad Neta'],df['Número de Afiliados'], c = Kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(Centroids[:,0], Centroids[:,1], c='red', s = 50)
plt.show()


Lables = pd.DataFrame(Kmeans.labels_)
df_final = pd.merge(Datos, Lables, how='inner', left_index=True, right_index=True)
df_final.columns


from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


# Creating figure
fig = plt.figure(figsize = (10, 7))
ax = plt.axes(projection ="3d")

ax.set_xlabel('Utilidad Neta', fontweight ='bold')
ax.set_ylabel('Número de Afiliados', fontweight ='bold')
ax.set_zlabel('Siniestralidad', fontweight ='bold')

 
# Creating plot
sc = ax.scatter3D(df_final['Utilidad Neta'],df_final['Número de Afiliados'], df_final['Siniestralidad'], c = df_final[0])
plt.title("Clusters EAPB")
plt.legend(*sc.legend_elements())

df_final.to_excel(Dir+ 'Modelo_Base.xlsx')

