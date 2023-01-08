import numpy as np
import random as r


def generateObjects(count, center=0, width=10, massmult=100,vcenter=0,vwidth=10):
    positions=[]
    i=0
    while i<=count:
        l=[]
        x=width*r.random()-((width/2)-center)
        l.append(x)
        y=width*r.random()-((width/2-center))
        l.append(y)
        objectMass=massmult*r.random()
        l.append(objectMass)
        positions.append(l)
        xv=(vwidth*r.random())-((vwidth/2)-vcenter)
        l.append(xv)
        yv=(vwidth*r.random())-((vwidth/2)-vcenter)
        l.append(yv)
        l=[]
        i+=1
    return(positions)
   


def generateObjectsNormal(count, center=0, width=10, massmult=100, vcenter=0, vwidth=10):
    return np.random.multivariate_normal([center, center, massmult, vcenter, vcenter],
                                         [[width/2, 0, 0, 0, 0],
                                          [0, width/2, 0, 0, 0],
                                          [0, 0, massmult*10, 0, 0],
                                          [0, 0, 0, vwidth/2, 0],
                                          [0, 0, 0, 0, vwidth/2]],
                                         count).tolist()
