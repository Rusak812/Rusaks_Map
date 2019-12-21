import os

import matplotlib.pyplot as plt
import numpy as np
#from astropy.io import ascii
#from astropy.table import Table
#import pandas as pd
import re
import time
from scipy import interpolate

'''By Leshea Nikon'''
#mport matplotlib.patches as mpatches
#from matplotlib.path import Path
#from matplotlib.text import OffsetFrom
from matplotlib import animation


print ('hello World')

''' Reading data files'''
file_name = 'C:/Astrophysics/other/Scientific_Python/SciencePitsa/Second/population_data/'+"Foundation.data"
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

###Graphics
#fig = plt.figure(figsize=(9,8))
fig = plt.figure(figsize=(16,9))
#plt.add_axes(rect)
n = 34
x = Longitude
y = Latitude
m = 1
def ani(i, x, y, nombres, m = 1):
    #plt.clf()
    plt.scatter(x[i], y[i], Population[i]/np.log10(Population[i]), lw = 3)
    plt.text(x[i]-0.01, y[i]-0.02, nombres[i] + ' ' + str(int(Foundation[i])))
    plt.axis([45.1, 46.2, 55.2, 55.9])
    plt.title('Nizhgar Tatar Map ' + str(int(Foundation[i])))
    plt.xlabel("Longitude, deg")
    plt.ylabel("Latitude, deg")

    print(nombres[i], Foundation[i])

anim = animation.FuncAnimation(fig, ani, fargs = (x, y, nombres), frames = n, interval = 10)
anim.save('test.gif', writer='imagemagick', fps = 1, dpi = 150)
print ('Painting animation was finished')

