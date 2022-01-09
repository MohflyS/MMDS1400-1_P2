from math import exp
from functions import d

#Cluster update function as needed

def updateCluster(win, vt, alpha, winN):
    win.centroid = (win.pointsN * win.centroid + vt) / (win.pointsN+1)
    win.pointsN += 1
    winthN = win.radius ** 2
    for Ni in winN:
        influence = exp(-(d(Ni.centroid, win.centroid)/(2 * winthN)))
        Ni.centroid = Ni.centroid + alpha*influence*(win.centroid-Ni.centroid)
