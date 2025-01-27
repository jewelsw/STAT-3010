# Case Study - Exploratory Data Analysis
# Author - Jewels Wolter
# STAT 3010 - Statistics for Engineers and Scientists

# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# P0: Data Import
data = pd.read_csv('mpg.csv')

# P1: Summary Statistics

# calculate five number summary
def fiveNumSum(x):
    mean = np.mean(x)
    median = np.median(x)
    min = np.min(x)
    max = np.max(x)
    q1 = np.percentile(x, 25)
    q3 = np.percentile(x, 75)
    stdDev = np.std(x)
    return mean, median, min, q1, q3, max, stdDev

# calculate for each column
mpg = data['mpg']
horsepower = data['horsepower']
weight = data['weight']

mpgStats = fiveNumSum(mpg)
horsepowerStats = fiveNumSum(horsepower)
weightStats = fiveNumSum(weight)

# group data by origin
origin = data.groupby('origin')

#calculate average mpg, horsepoweer, and weight for each origin
avgMpg = origin['mpg'].mean()
avgHorsepower = origin['horsepower'].mean()
avgWeight = origin['weight'].mean()

# print summary statistics
print('Summary Statistics:')
print('mpg: mean =', mpgStats[0], ', median =', mpgStats[1], ', std dev =', mpgStats[6])
print('horsepower: mean =', horsepowerStats[0], ', median =', horsepowerStats[1], ',std dev =', horsepowerStats[6])
print('weight: mean =', weightStats[0], ', median =', weightStats[1], ', std dev =', weightStats[6])
print('Average mpg by origin: \n', avgMpg)
print('Average horsepower by origin: \n', avgHorsepower)
print('Average weight by origin: \n', avgWeight)

print('Reigon with most fuel-efficient cars:', avgMpg.idxmax())

# P2: Data Visualization

# P2.1: Univariate Analysis

# create a histogram of mpg
plt.hist(mpg, bins=15, color='mediumvioletred', edgecolor='black')
plt.title('Histogram of MPG')
plt.xticks(np.arange(10, 50, 2))
plt.xlabel('MPG')
plt.ylabel('Frequency')
plt.show()

# create a boxplot of weight grouped by cylinders
data.boxplot(column='weight', by='cylinders')
plt.xlabel('Cylinders')
plt.ylabel('Weight')
plt.show()

# # P2.2: Bivariate Analysis

# create a scatterplot of horsepower vs mpg
plt.scatter(horsepower, mpg, color='hotpink')
plt.title('Horsepower vs MPG')
plt.xlabel('Horsepower')
plt.ylabel('MPG')
plt.show()

# create a scatterplot of weight vs mpg
plt.scatter(weight, mpg, color='deeppink')
plt.title('Weight vs MPG')
plt.xlabel('Weight')
plt.ylabel('MPG')
plt.show()
