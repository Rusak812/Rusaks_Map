import os
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from astropy.io import ascii
from astropy.table import Table
import re
import csv
import time
from scipy import interpolate
from scipy.interpolate import interp1d


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

''' Reading data files'''
data_Foundation = np.genfromtxt('C:/Astrophysics/other/Scientific_Python/SciencePitsa/Second/population_data/'+"Foundation.data",names=True)

nombres = []
f = open('C:/Astrophysics/other/Scientific_Python/SciencePitsa/Second/population_data/'+"Foundation.data")
i = 0
for line in f:
    if i > 0:
        line = re.sub(r'[^\w\s]+|[\d]+', r'', line).strip()
        nombres.append(line)
        #print(line)
    i = i + 1

print (nombres[9])


Foundation = data_Foundation['Foundation']
Latitude = data_Foundation['Latitude'] #Latitude
Longitude = data_Foundation['Longitude'] #Population
#D = data[Dname] #population

j = 0
for _ in Foundation:
    file_name = 'C:/Astrophysics/other/Scientific_Python/SciencePitsa/Second/population_data/'+nombres[j]+'.txt'
    if os.path.isfile(file_name):
        data = np.genfromtxt(file_name,names=True)
        Year = data['Year']
        Population = data['Population']

        plt.plot(Year, Population, '--')
        plt.title(nombres[j] + " Population Dynamics")
        plt.xlabel("Year")
        plt.ylabel("Population")
        directoryname = 'C:/Astrophysics/other/Scientific_Python/SciencePitsa/Second/population_data/results/'
        createFolder(directoryname)
        plt.savefig(directoryname + nombres[j] + " Population Dynamics" + '.png', format = 'png')
        print(nombres[j] + " Population Dynamics" + '.png' + ' was drawn')
        plt.clf()
    j += 1

'''
tck_splrep = interpolate.splrep(Year, Population)#, kind = 'linear')
f = interp1d(Year, Population, kind = 'linear')
#interp1d@param

#tck_square = interpolate.interp1d(Year, Population, kind = 'square')
x = np.linspace(1610, 2000, num = 400)
plt.scatter(Year, Population, color = 'green')
print(f(x))


for year in range(1610, 2012, 1):
    #plt.scatter(year, interpolate.interp1d(year, tck_linear), color='blue')
    #plt.scatter(year, f(year), color='green')
    plt.scatter(year, interpolate.splev(year, tck_splrep), color='black')
    #plt.scatter(year, tck_splrep[year], color='black')
plt.scatter(Year, Population, color = 'green')
#print(f(x))
plt.plot(x, f(x), '-', color = 'blue')
plt.xlabel("Year")
plt.ylabel("Population")
plt.yscale('linear')
plt.show()

'''
