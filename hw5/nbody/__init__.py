from calculations import forceVec, nextPositionAndVelocity
from data import generateObjects, generateObjectsNormal
from plotting import plotObjects
from simulation import sumOfForces
from utils import exp, perms, isPalindrome

print(exp(2, 4))  # 16
print(exp(3, 2)) # 9
print(isPalindrome("abcba"))  # True
print(isPalindrome("abcb"))  # False
print(perms("cab"))


data = generateObjects(10)
print(data[0])

obj = [0, 0, 100, 100, 0]
nextPositionAndVelocity(obj,[-100, 100],0.05)
print(obj)
vec1 = [0, 0, 1935, 0, 0]
vec2 = [3, 4, 1936, 0, 0]

forces = sumOfForces([vec1, vec2])

print(forces[0])
print(forces[1])



