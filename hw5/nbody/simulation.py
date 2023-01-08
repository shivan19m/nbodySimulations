from calculations import forceVec

def sumOfForces(objects):
    '''Given an Nx5 array of objects of the form (x, y, mass, xvel, yvel), return an Nx2 array of the cumulative force acting on each object in x and y'''
    xf=0
    yf=0
    l=[]
    for x,vec1 in enumerate(objects):
        xf,yf=0,0
        for y,vec2 in enumerate(objects):
            if (x==y):
                continue
            xr,yr=forceVec(vec1,vec2)
            xf+=xr
            yf+=yr
        l.append([xf,yf])
    return l