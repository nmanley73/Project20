# Python Project - Analysis of the Iris Flower Dataset


## Summary/Description
The Python Project consists of an analysis of Ronald Fisher's Iris Flower Dataset. The dataset consists of 50 samples each of three different species of the Iris Flower (Iris setosa, Iris virginica, Iris Versicolor). There are four features/variables measured in cm of the Iris Flower (sepal length, sepal width, petal length, petal width). Through visualization and analysis of these features we are able to distinguish each species of from each other.


## Investigation/Analysis

By splitting the Iris Flower Dataset into three seperate datasets for each species of Iris Flower(setosa, virginica, versicolor) one can analyse each seperate dataset, identify the differences in the four variables of the three species and identify which species of Iris flower based upon its dimensions.

From reviewing scatter plots Fig 6.5, Fig 7.5 and Fig 10.5 we can identify that petal length (cm) of Iris Setosa is considerably smaller than the other two species. The stats of all three Iris species confirm that. Iris Setosa has an average petal length of 1.46cm compared to Iris Virginica (5.55cm) and Iris Versicolor (4.26cm).
Petal width (cm) of Iris Setosa is also smaller than the other species but not by as much 0.24cm compared to 1.33cm and 2.03cm for Versicolor and Virginica respectively. That difference can be visualised using Scatter plots of Fig 6.5, Fig 8.5 and Fig 9.5. Fig 6.5 Petal length vs petal width displays the difference in petal dimensions 
in greater detail. The Iris Setosa population are aligned in the bottom left corner of the scatter plot whereas Versicolor and Virginica are distributed in the middle and top right. Its much more difficult to seperate Irish setosa from the other two species in terms of sepal length and sepal width individually as there is some overlap
between the species (Fig 7.5 & Fig 8.5). However in Fig 5.5 by using a multivariate analysis using both sepal length and sepal width as the variables of analysis (with the exception of one outlier) the Iris setosa species is linearly seperable from the other two species. Individually sepal length of setosa are smaller and the
sepal width is the largest of the other species. Given all those differences in attributes it is should be straighforward to identify a setosa species of the Iris flower.

Distinguishing between the Versicolor and Virginica species is more difficult as there is a lot of overlap between the two populations and they are not linearly seperable on any of the four variables. However using the statistical data and the scatter plots some patterns can be identified to differentiate between the two species.
From the statistical data whe comparing between Virginica and Versicolor we can see that Virginica has the longest sepals with an average of 6.59 cm, 0.65 cm longer than the Versicolor average. Virginica has wider sepals (average 2.97 cm) 0.2 cm wider than the average of versicolor. Virginica also has longer and wider petals than versicolor 
by on average 1.29 cm and 0.7 cm respectively. Petal length displays the greatest divergence with little overlap between the two species. This pattern can also be visualised  in the sscatter plots of the two species. Fig 5.5 shows much overlap for sepal width and sepal length however some of the virginica species have larger and wider petals 
than their Versicolor counterparts. Fig 6.5, Fig 7.5, Fig 8.5, Fig 9.5 and Fig 10.5 which all feature the petal attribute confirms the statistical data with the Virginica Iris Flower species longer and wider than Versicolor.

In summary if an Iris flower has short sepal, relatively wide sepal, short petals and very narrow petals it is likely to be from the setosa species of the flower. If the flower has a long sepal, a long petal and a wide petal it is likely to be from the Virginica species of the flower. If the flower does not fit into either of those categories
and has an intermediate sepal length and width and petal length and width it is most likely to be from the Versicolor species.

In terms of the Iris virginica and Iris versicolor species and the overlap between the two species it is extremely difficult to understand how some of the individuals flowers are classified as one species over another.The main disguishing factor between the two species are the petal attribute dimensions. However in Fig 7.5 there are approximately
15/20 flowers which overlap and could be defined as either species of flower. There are some of the virginica species within the versicolor population and vice versa. Were some of these flowers classified incorrectly? From my viewpoint i would either merge both virginica and versicolor into one Iris species or create an addition species whereby 
those that overlap would be one species of Iris and the outliers on both sides would be two seperate species. That would create it's own issues in terms of callification of species. Its an inexact science however visualization of the data in terms of plots and graphs is assisting in helping to identifying the species something that Fisher and Anderson
probably didn't have back when they were identifying the species of the flower.



## Python Code

- Import the required libraries

import pandas as pd

import matplotlib.pyplot as plt

import numpy as np

import seaborn as sn

- Create the summary.txt file to get overall statistics of dataset

df.describe().astype(float).to_csv("Summary.txt", sep=';', decimal=',', float_format="%.2f")

- Split the sample into a sample for each species of Iris Flower

iris_setosa = df.loc[df["species"]=="Iris-setosa"]

iris_virginica = df.loc[df["species"]=="Iris-virginica"]

iris_versicolor = df.loc[df["species"]=="Iris-versicolor"]

- Create histogram for all variables. Add title, x label, y label, save and clear

plt.hist(df["sepal_length"])

plt.title("Sepal length")

plt.xlabel("Sepal length")

plt.ylabel("number")

plt.savefig("Fig 1. Sepal length.png")

plt.clf()

- Create scatter plot for two variables together. Add title, xlabel, ylabel, save and clear

plt.plot(df["sepal_length"], df["sepal_width"],'b.')

plt.title("sepal length vs sepal width (cm)")

plt.ylabel("sepal width (cm)")

plt.xlabel("sepal length (cm)")

plt.savefig("Fig 5. Sepal length vs sepal width.png")

plt.clf()


## References

Background information - https://en.wikipedia.org/wiki/Iris_flower_data_set https://archive.ics.uci.edu/ml/datasets/iris

Downloaded Iris Flower Dataset - https://archive.ics.uci.edu/ml/datasets/iris

Help with Readme - https://medium.com/@meakaakka/a-beginners-guide-to-writing-a-kickass-readme-7ac01da88ab3

Code to split dataset - https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d

Code to output describe - https://stackoverflow.com/questions/43044740/pandas-float64-dataframe-column-not-behaving-like-one-wrt-describe-and-to-csv-f

Data Visualization and explanation - https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation

Data two-dimensional representations - https://books.google.ie/books?id=Obs8BAAAQBAJ&pg=PA45&lpg=PA45&dq

Data Visualization - Patrick Hoeys Data Visualization paper.pdf

Iris Dataset Analysis (Python) - http://d4t4.biz/ml-with-scikit-learn/support-vector-machines-project-wip/



## Change log

25/04/2020 - Created the project repository and downloaded a version of the Iris Flower Dataset to the repository. 

26/04/2020 - Updated the downloaded version of the dataset as the initial version didn't have the headers/attribute values. 

27/04/2020 - Started writing the README file of research conduction, change log and Project plan.

29/04/2020 – Had some issues with the link between the local repository and the GitHub repository which I couldn’t resolve so created a new repository and finally got the link working. Wrote some of the analysis.py code that creates the histograms and the scatter plots. For the scatter plots wasn’t sure whether the requirement was for completing the plots for the full sample or to complete plot by species. Divided the dataset into each species and completed plot which for each set of variables by each species of Iris Flower.

30/04/2020 - Fixed a bug in python code, ran tthe code which generated updated histograms and scatter plots. Amended code to incude creation of summary.txt file. Add some new scatter plots. Added statistical data. Updated README file. Unfortunately couldn't get images of plots inserted on README file.


## Project Plan

25/04/2020 - Late getting to this project but have a week to research and complete the project. Start project research, create new GitHub Repository for the project and download the Iris Flower dataset in text format. 

26/04/2020 - Review the course videos on plots and read some supplementary material from Real Python and Pandas. Complete some examples in commander to refamiliarise myself with the libraries and the plot information. 

27/04/2020 - Continue researching the Iris Flower Dataset. Do up a template to be used for the README file. 

28/04/2020 - Conduct an analysis of the data and formulate an approach to display the data.

30/04/2020 - Complete the project to as high a standard as possible given the time constraints. Ensure all the files, code are up to date and committed to GitHub. Ensure README has been completed and submit the project.


## Uploaded files

Iris_flower_dataset – Ronald Fisher’s Iris Flower Dataset downloaded from https://archive.ics.uci.edu/ml/datasets/iris

Readme.md – Containing details of the project (Summary, investigations, change log, references, project plan, Python code)

analysis.py – See Python Code section above for details.

Summary.txt – output of the summary of the dataset

Stats.png - Statistics of the three Iris species of flower

Iris_flower_dataset – Ronald Fisher’s dataset 

Fig 1 – Histogram of Sepal length

Fig 2 – Histogram of Sepal width

Fig 3 – Histogram of Petal length

Fig 4 – Histogram of Petal width

Fig 5 – Scatter plot of the full sample of Sepal length vs sepal width

Fig 5.5 – Scatter plot of Sepal length vs sepal width by Iris Flower species

Fig 6 – Scatter plot of the full sample of Petal length vs Petal width

Fig 6.5 – Scatter plot of Petal length vs petal width by Iris Flower species

Fig 7 – Scatter plot of the full sample of Sepal length vs petal length

Fig 7.5 – Scatter plot of Sepal length vs petal length by Iris Flower species

Fig 8 – Scatter plot of the full sample of Sepal width vs petal width

Fig 8.5 – Scatter plot of Sepal width vs petal width by Iris Flower species

Fig 9 – Scatter plot of the full sample of Sepal length vs petal width

Fig 9.5 – Scatter plot of Sepal length vs petal width by Iris Flower species

Fig 10 – Scatter plot of the full sample of Sepal width vs petal length

Fig 10.5 – Scatter plot of Sepal width vs petal length by Iris Flower species




