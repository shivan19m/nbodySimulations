import numpy as np
import math

# Original G is 6.6742*10**-11
# So if our units are in the millions
G = 6.6742 * 10 ** -5


def distance(s1, s2):
    # return math.sqrt(sum((s1[0] - s2[0])**2, (s1[1], - s2[1])**2))
    # return np.sqrt(np.sum(np.square(s1-s2)))
    return np.linalg.norm([s1, s2])


def force(m1, m2, s):
    return (G * m1 * m2) / s**2


def angle(vec1, vec2):
    # return math.atan2(vec2[1] - vec1[1], vec2[0] - vec1[0])
    return np.arctan2(vec2[1] - vec1[1], vec2[0] - vec1[0])


def forceVec(vec1, vec2):
    '''Calculate the force vector between vec1 and vec2, where vec1 and vec2 are like [x, y, mass]

    The force vector should be of the form [Fx, Fy]
    '''
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    mass1 = vec1[2]
    mass2 = vec2[2]
    F = force(mass1, mass2, distance(vec1[:2], vec2[:2]))
    θ = angle(vec1[:2], vec2[:2])
    # return np.array([F * np.cos(θ), F * np.sin(θ)])  # array
    # return [F * np.cos(θ), F * np.sin(θ)]  # list
    return F * np.cos(θ), F * np.sin(θ)  # tuple


def nextPosition(vec, forcevec, delta_t):
    # Calculate the next position in x and y using the same strategy as the trajectory example
    xr=vec[0]+(vec[3]*delta_t)
    yr=vec[1]+vec[4]*delta_t
    r=[xr,yr]
    return r


def nextVelocity(vec, forcevec, delta_t):
    # Calculate the next velocity in x and y using the same strategy as the trajectory example
    xv=vec[3]+(forcevec[0]/vec[2])*delta_t
    yv=vec[4]+(forcevec[1]/vec[2])*delta_t
    v=[xv,yv]
    return v


def nextPositionAndVelocity(vec, forcevec, delta_t):
    '''Calculate the next velocity and position of vector based on the forces acting on it'''
    r=nextPosition(vec,forcevec,delta_t)
    v=nextVelocity(vec,forcevec,delta_t)
    vec[0]=r[0]
    vec[1]=r[1]
    vec[3]=v[0]
    vec[4]=v[1]
    return vec