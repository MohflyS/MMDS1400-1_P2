import numpy as np
from functions import d

#Find the neighbors of a point
def findNeighbors(win, minPts, currentclusterArr):
  if len(currentclusterArr) >= minPts:
    winDistN = []
    for cluster in currentclusterArr:
      winDistN.append(d(cluster.centroid, win.centroid))
    winDistN.sort()
    k_dist = winDistN[minPts-1]
    winDistN = np.argsort(winDistN)
    win.radius = k_dist
    winNN = [currentclusterArr[i] for i in winDistN[0:(minPts)]]
    return winNN
  else:
    return []

