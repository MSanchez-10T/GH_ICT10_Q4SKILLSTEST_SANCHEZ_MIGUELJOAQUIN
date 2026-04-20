# Numerical Python and MATLAB Plotting Library 
from pyscript import document, display #type:ignore 
import numpy as np  #type:ignore np is just a common alias 

import logging # gets rid of the loading thingy for the graph 
logging.getLogger('matplotlib').setLevel(logging.ERROR)
import matplotlib.pyplot as plt #type:ignore

# Preload to avoid font cache message during user action
plt.figure()
plt.plot([0,1], [0,1])
plt.close()


def graph (e):
    document.getElementById('output').innerHTML = ' '

    absences = np.array([int(document.getElementById('input1').value)])
    month = np.array([str(document.getElementById('month').value)])

    Topaz_graph = plt.bar(month, absences)

    plt.show(Topaz_graph)
    plt.title('Topaz Absences A.Y. 25-26')
    plt.xlabel('Months')
    plt.ylabel('Number of Absences')

