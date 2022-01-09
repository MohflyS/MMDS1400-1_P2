import numpy as np
import matplotlib.pyplot as pp
from functions import minDist, d
from newCluster import newCluster
from findOverlap import findOverlap
from findNeighbors import findNeighbors
from mergeClusters import mergeClusters
from updateCluster import updateCluster

class sostream:

    #Create required code values

    def __init__(self, alpha = 0.01, minPts = 5, threshold = 30):
        self.alpha = alpha
        self.minPts = minPts
        self.clusterArr = [[]]
        self.centroidsArr = []
        self.threshold = threshold
        self.Ndeleted = 0
        self.Nmerged = 0

    #The processing function of each vector for placement in clusters

    def sostream(self, vector):
        centroids = np.array([cluster.centroid for cluster in self.clusterArr[len(self.clusterArr) - 1]])
        self.centroidsArr.append(len(centroids))
        win = minDist(vector, self.clusterArr[len(self.clusterArr)-1])
        currentclusterArr = self.clusterArr[len(self.clusterArr)-1].copy()
        if len(currentclusterArr) >= self.minPts:
            winnerN = findNeighbors(win, self.minPts, currentclusterArr)
            if d(vector, win.centroid) < win.radius:
                updateCluster(win, vector, self.alpha, winnerN)
            else:
                currentclusterArr.append(newCluster(vector))
            overlap = findOverlap(win, winnerN)
            if len(overlap) > 0:
                self.Nmerged += 1
                merged, deleted = mergeClusters(win, overlap, self.threshold)
                for i in deleted:
                    currentclusterArr.remove(i)
                    self.Ndeleted += 1
                if merged is not None:
                    currentclusterArr.append(merged)
        else:
            currentclusterArr.append(newCluster(vector))
        self.clusterArr.append(currentclusterArr)
    pass

    def make(self, data):
        for row in data.values:
            self.sostream(row)
        print(f"Deleted Cluster Number: {self.Ndeleted}.")
        print(f"Merged Cluster Number: {self.Nmerged}.")
        pp.plot(self.centroidsArr)
        pp.show()
    pass