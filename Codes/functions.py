import numpy as np

#Required code functions that are introduced mathematically in the article file
def d(vector1, vector2):
    return np.sqrt(((vector1 - vector2) ** 2).sum())


def weighted(ai, bi, wi, wj):
    return ((wi * ai + wj * bi)/(wi + wj))


def minDist(vt, clusters):
    clusterD = 99999.99999
    win = None
    for cluster in clusters:
        dist = d(vt, cluster.centroid)
        if dist <= clusterD:
            clusterD = dist
            win = cluster

    return win
