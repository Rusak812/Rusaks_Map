import os
import matplotlib.pyplot as plt
import numpy as np
import re
from scipy import interpolate
from matplotlib import animation
from my_functions import average_population, Pareto

#First part
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

# Reading data files'''
data_Foundation = np.genfromtxt('population_data/'+"Foundation.data",names=True)

nombres = []
f = open('population_data/'+"Foundation.data")
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
pop = data_Foundation['Population']

print(average_population(pop))
Pareto(pop)
j = 0
for _ in Foundation:
    file_name = 'population_data/'+nombres[j]+'.txt'
    if os.path.isfile(file_name):
        data = np.genfromtxt(file_name,names=True)
        Year = data['Year']
        Population = data['Population']

        tck = interpolate.splrep(Year, Population)
        for year in range(int (Foundation[j]), 2016, 1):
            plt.scatter(year, interpolate.splev(year, tck))
        plt.title(nombres[j] + " Population Dynamics")
        plt.xlabel("Year")
        plt.ylabel("Population")
        directoryname = 'population_data/results/'
        createFolder(directoryname)
        plt.savefig(directoryname + nombres[j] + " Population Dynamics" + '.png', format = 'png')
        print(nombres[j] + " Population Dynamics" + '.png' + ' was drawn')
        #plt.show()
        plt.clf()
    j += 1


#'''Second Part'''

#''' Reading data files'''
file_name = 'population_data/'+"Foundation.data"
data = np.genfromtxt(file_name,names=True)
nombres = []
f = open(file_name)
i = 0
for line in f:
    if i > 0:
        line = re.sub(r'[^\w\s]+|[\d]+', r'', line).strip()
        nombres.append(line)
        print(line, ' ', i)
    i = i + 1


Longitude = data['Longitude'] #Longitude
Latitude = data['Latitude'] #Latitude
Population = data['Population'] #Population
Foundation = data['Foundation'] #Foundation

#'''Graphics'''
fig = plt.figure(figsize=(16,9))
n = 34
x = Longitude
y = Latitude
m = 1
def ani(i, x, y, nombres, m = 1):
    #plt.clf()
    plt.scatter(x[i], y[i], Population[i]/np.log10(Population[i]), lw = 3)
    plt.text(x[i]-0.01, y[i]-0.02, nombres[i] + ' ' + str(int(Foundation[i])))
    plt.axis([45.1, 46.2, 55.2, 55.9])
    plt.title('Dynamics Foundation Map ' + str(int(Foundation[i])))
    plt.xlabel("Longitude, deg")
    plt.ylabel("Latitude, deg")

    print(nombres[i], Foundation[i])

anim = animation.FuncAnimation(fig, ani, fargs = (x, y, nombres), frames = n, interval = 10)
directoryname = 'population_data/results/'
createFolder(directoryname)
anim.save(directoryname + 'Maps.gif', writer='imagemagick', fps = 1, dpi = 150)
print ('Painting animation was finished')

