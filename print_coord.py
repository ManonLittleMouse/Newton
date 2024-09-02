import matplotlib.pyplot as plt
import numpy as np
import os
import statistics as st



x_random = []
y_random = []

file = "coord_random.csv"

f = open(file, 'r')
for l in f :
    v = l.split(',') 
    x_random.append(float(v[0]))
    y_random.append(float(v[1].replace("\n", '')))

plt.scatter(x_random, y_random, alpha= 0.5)
plt.show()



x_vivaldi = []
y_vivaldi = []

file = "coord_vivaldi.csv"

f = open(file, 'r')
for l in f :
    v = l.split(',') 
    x_vivaldi.append(float(v[0]))
    y_vivaldi.append(float(v[1].replace("\n", '')))

plt.scatter(x_vivaldi, y_vivaldi, alpha= 0.5)
plt.show()


x_geo = []
y_geo = []

file = "geolocation.txt"

f = open(file, 'r')
n = int(f.readline())
for l in f :
    v = l.split(' ') 
    x_geo.append(float(v[0]))
    y_geo.append(float(v[1].replace("\n", '')))

plt.scatter(x_geo, y_geo, alpha= 0.5)
plt.show()