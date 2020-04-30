# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn

# set data frame to the Iris Flower dataset in text format
df = pd.read_csv("iris_flower_dataset.txt")

# Split the sample into a sample for each species of Iris Flower
# Got code from 
iris_setosa = df.loc[df["species"]=="Iris-setosa"]
iris_virginica = df.loc[df["species"]=="Iris-virginica"]
iris_versicolor = df.loc[df["species"]=="Iris-versicolor"]

# Create histogram for Sepal Length. Add title, x label, y label and save 
plt.hist(df["sepal_length"])
plt.title("Sepal length")
plt.xlabel("Sepal length")
plt.ylabel("number")
plt.savefig("Fig 1. Sepal length.png")
plt.clf()

# Create histogram for Sepal Width. Add title, x label, y label and save 
plt.hist(df["sepal_width"])
plt.xlabel("Sepal width")
plt.ylabel("number")
plt.title("Sepal width")
plt.savefig("Fig 2. Sepal width.png")
plt.clf()

# Create histogram for Petal Length. Add title, x label, y label and save 
plt.hist(df["petal_length"])
plt.title("petal length")
plt.ylabel("number")
plt.xlabel("Petal length")
plt.savefig("Fig 3. Petal length.png")
plt.clf()

# Create histogram for Petal width. Add title, x label, y label and save 
plt.hist(df["petal_width"])
plt.ylabel("number")
plt.xlabel("Petal width")
plt.title("Petal width")
plt.savefig("Fig 4. Petal width.png")
plt.clf()

# Create scatter plot of sepal length against sepal width. Add title, xlabel, ylabel and save
plt.plot(df["sepal_length"], df["sepal_width"],'b.')
plt.title("sepal length vs sepal width (cm)")
plt.ylabel("sepal width (cm)")
plt.xlabel("sepal length (cm)")
plt.savefig("Fig 5. Sepal length vs sepal width.png")
plt.clf()

# Create scatter plot of sepal length against sepal width by the 3 different species. Add title, legend, xlabel, ylabel and save
plt.plot(iris_setosa["sepal_length"],iris_setosa["sepal_width"],'r.',label = 'Iris Setosa')
plt.plot(iris_virginica["sepal_length"],iris_virginica["sepal_width"],'b.', label = 'Iris virginica')
plt.plot(iris_versicolor["sepal_length"],iris_versicolor["sepal_width"],'g.', label = 'Iris versicolor')
plt.legend()
plt.xlabel("Sepal length (cm)")
plt.ylabel("Sepal width (cm)")
plt.title("Sepal length vs sepal width comparison by species type")
plt.savefig("Fig 5.5 Sepal length vs sepal width by species.png")
plt.clf()

# Create scatter plot of petal length against petal width. Add title, xlabel, ylabel and save
plt.plot(df["petal_length"], df["petal_width"],'b.')
plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")
plt.title("petal length vs petal width (cm)")
plt.savefig("Fig 6. Petal length vs petal width.png")
plt.clf()

# Create scatter plot of petal length against petal width by the 3 different species. Add title, legend, xlabel, ylabel and save
plt.plot(iris_setosa["petal_length"], iris_setosa["petal_width"],'r.', label = 'Iris setosa')
plt.plot(iris_virginica["petal_length"],iris_virginica["petal_width"],'b.', label = 'Iris virginica')
plt.plot(iris_versicolor["petal_length"],iris_versicolor["petal_width"],'g.', label = 'Iris versicolor')
plt.legend()
plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")
plt.title("Petal length vs Petal width comparison by species type")
plt.savefig("Fig 6.5 Petal length vs petal width by species.png")
plt.clf()

# Create scatter plot of sepal length against petal length. Add title, xlabel, ylabel and save
plt.plot(df["sepal_length"], df["petal_length"],'b.')
plt.title("Sepal length vs petal length (cm)")
plt.xlabel("sepal length (cm)")
plt.ylabel("petal length (cm)")
plt.savefig("Fig 7. Sepal length vs petal length.png")
plt.clf()

# Create scatter plot of sepal length against petal length by the 3 different species. Add title, legend, xlabel, ylabel and save
plt.plot(iris_setosa["sepal_length"], iris_setosa["petal_length"],'r.', label = 'Iris setosa')
plt.plot(iris_versicolor["sepal_length"],iris_versicolor["petal_length"],'g.', label = 'Iris versicolor')
plt.plot(iris_virginica["sepal_length"],iris_virginica["petal_length"],'b.', label = 'Iris virginica')
plt.title("Sepal length vs Petal length comparison by species type")
plt.xlabel("sepal length (cm)")
plt.ylabel("petal length (cm)")
plt.legend()
plt.savefig("Fig 7.5 Sepal length vs petal length by species.png")
plt.clf()

# Create scatter plot of sepal width against petal width. Add title, xlabel, ylabel and save
plt.plot(df["sepal_width"], df["petal_width"],'b.')
plt.title("Sepal width vs petal width (cm)")
plt.ylabel("petal width (cm)")
plt.xlabel("sepal width (cm)")
plt.savefig("Fig 8. Sepal width vs petal width.png")
plt.clf()

# Create scatter plot of sepal width against petal width by the 3 different species. Add title, legend, xlabel, ylabel and save
plt.plot(iris_setosa["sepal_width"], iris_setosa["petal_width"],'r.', label = 'Iris setosa')
plt.plot(iris_versicolor["sepal_width"],iris_versicolor["petal_width"],'g.', label = 'Iris versicolor')
plt.plot(iris_virginica["sepal_width"],iris_virginica["petal_width"],'b.', label = 'Iris virginica')
plt.legend()
plt.title("Sepal width vs Petal width comparison by species type")
plt.ylabel("petal width (cm)")
plt.xlabel("sepal width (cm)")
plt.savefig("Fig 8.5 Sepal width vs petal width by species.png")
plt.clf()

# Create scatter plot of sepal length against petal width. Add title, xlabel, ylabel and save
plt.plot(df["sepal_length"], df["petal_width"],'b.')
plt.title("Sepal length vs petal width (cm)")
plt.ylabel("petal width (cm)")
plt.xlabel("sepal length (cm)")
plt.savefig("Fig 9. Sepal length vs petal width.png")
plt.clf()

# Create scatter plot of sepal length against petal width by the 3 different species. Add title, legend, xlabel, ylabel and save
plt.plot(iris_setosa["sepal_length"], iris_setosa["petal_width"],'r.', label = 'Iris setosa')
plt.plot(iris_versicolor["sepal_length"],iris_versicolor["petal_width"],'g.', label = 'Iris versicolor')
plt.plot(iris_virginica["sepal_length"],iris_virginica["petal_width"],'b.', label = 'Iris virginica')
plt.legend()
plt.title("Sepal length vs Petal width comparison by species type")
plt.ylabel("petal width (cm)")
plt.xlabel("sepal length (cm)")
plt.savefig("Fig 9.5 Sepal length vs petal width by species.png")
plt.clf()

# Create scatter plot of sepal width against petal length. Add title, xlabel, ylabel and save
plt.plot(df["sepal_width"], df["petal_length"],'b.')
plt.title("Sepal width vs petal length (cm)")
plt.ylabel("petal length (cm)")
plt.xlabel("sepal width (cm)")
plt.savefig("Fig 10. Sepal width vs petal length.png")
plt.clf()

# Create scatter plot of sepal width against petal length by the 3 different species. Add title, legend, xlabel, ylabel and save
plt.plot(iris_setosa["sepal_width"], iris_setosa["petal_length"],'r.', label = 'Iris setosa')
plt.plot(iris_versicolor["sepal_width"],iris_versicolor["petal_length"],'g.', label = 'Iris versicolor')
plt.plot(iris_virginica["sepal_width"],iris_virginica["petal_length"],'b.', label = 'Iris virginica')
plt.legend()
plt.title("Sepal width vs Petal length comparison by species type")
plt.ylabel("petal length (cm)")
plt.xlabel("sepal width (cm)")
plt.savefig("Fig 10.5 Sepal width vs petal length by species.png")
plt.clf()









