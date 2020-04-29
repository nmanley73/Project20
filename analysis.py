import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn

df = pd.read_csv("iris_flower_dataset.txt")

iris_setosa = df.loc[df["species"]=="Iris-setosa"]
iris_virginica = df.loc[df["species"]=="Iris-virginica"]
iris_versicolor = df.loc[df["species"]=="Iris-versicolor"]
print(Iris_setosa)
#plt.plot(iris_setosa["sepal_length"],'r.',label = 'Iris Setosa')
#plt.plot(iris_versicolor["sepal_length"],'g.', label = 'Iris versicolor')
#plt.plot(iris_virginica["sepal_length"],'b.', label = 'Iris virginica')

#plt.legend()
#plt.title("Sepal Length")
#plt.xlabel("sample")
#plt.ylabel("sepal length")
#plt.savefig("sepal_length.png")