from functions import d, weighted
from newCluster import newCluster

#Merge clusters
def mergeClusters(win, overlaps, threshold):
    merged = None
    deleted = list()
    for cluster in overlaps:
        if d(cluster.centroid, win.centroid) < threshold:
            if len(deleted) == 0:
                deleted.append(win)
                merged = newCluster(win.centroid, pointsN=win.pointsN, radius=win.radius)
            merged = merge(cluster, merged)
            deleted.append(cluster)
    return merged, deleted


def merge(Ci, Cj):
    NclusterC = weighted(Ci.centroid, Cj.centroid, Ci.pointsN, Cj.pointsN)
    NclusterR = d(Ci.centroid, Cj.centroid) + max(Ci.radius, Cj.radius)
    merged = newCluster(centroid=NclusterC, pointsN=Ci.pointsN + Cj.pointsN, radius=NclusterR)
    return merged
