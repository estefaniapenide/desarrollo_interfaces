import sys

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random
import time

veces =13
cont=0

tiempo = random.uniform(0.1, 3)

colores = ['hot', 'binary', 'spring', 'winter', 'autumn', 'summer','bone','copper','gist_heat','afmhot','Wistia','cool','pink','gray']
i = len(colores)

plt.figure()

while cont < veces:
    tiempo = random.uniform(0.1, 3)
    indice = random.randint(0, i - 1)
    color = colores[indice]

    plt.pcolormesh(np.random.rand(20,20),cmap=color)
    plt.pause(tiempo)

    cont=cont+1

