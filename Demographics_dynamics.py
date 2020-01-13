import os
import sys
import matplotlib.pyplot as plt
import numpy as np
import re
from scipy import interpolate
from matplotlib import animation
from my_functions import average_population, Pareto

#First part
def createFolder(directory):
    os.makedirs(directory, exist_ok=True)
    
# Reading data files'''
name_of_file = sys.argv[1]
#file_name = "Foundation.data"
#data_Foundation = np.genfromtxt('population_data/'+"Foundation.data",names=True)
data_Foundation = np.genfromtxt(name_of_file,names=True)

nombres = []
#f = open(name_of_file)
with open(name_of_file) as f: 
    #f = open('population_data/'+"Foundation.data")
    i = 0
    for line in f:
        if i > 0:
            line = re.sub(r'[^\w\s]+|[\d]+', r'', line).strip()
            nombres.append(line)
            #print(line)
        i = i + 1


    Foundation = data_Foundation['Foundation']
    Latitude = data_Foundation['Latitude'] #Latitude
    Longitude = data_Foundation['Longitude'] #Population
    Population = data_Foundation['Population']

    print(average_population(pop))
    Pareto(pop)


#'''Second Part'''
#'''Graphics'''
fig = plt.figure(figsize=(16,9))
n = 34
x = Longitude
y = Latitude
m = 1
def ani(i, x, y, nombres, m = 1):
    #plt.clf()
    plt.scatter(x[i], y[i], Population[i]/np.log10(Population[i]), lw = 3)
    #plt.text(x[i]-0.01, y[i]-0.02, nombres[i] + ' ' + str(int(Foundation[i])))
    plt.text(x[i]-0.01, y[i]-0.02, '{} {}'.format(nombres[i], int(Foundation[i])))
    plt.axis([45.1, 46.2, 55.2, 55.9])
    plt.title('{} {}'.format('Dynamics Foundation Map ', int(Foundation[i])))
    plt.xlabel("Longitude, deg")
    plt.ylabel("Latitude, deg")

    print(nombres[i], Foundation[i])

anim = animation.FuncAnimation(fig, ani, fargs = (x, y, nombres), frames = n, interval = 10)
directoryname = 'population_data/results/'
createFolder(directoryname)
anim.save(directoryname + 'Maps.gif', writer='imagemagick', fps = 1, dpi = 150)
print ('Painting animation was finished')

