import numpy as np
import matplotlib.pyplot as plt


def plotObjects(objects):
    '''Draw a matplotlib chart of our objects. `objects` argument is an Nx3 matrix of (x,y,mass) coordinates'''
    objects = np.array(objects)
    plt.figure(figsize=(14, 8))
    plt.scatter(objects[:, 0], objects[:, 1], s=objects[:, 2], alpha=0.5)
    plt.show()
