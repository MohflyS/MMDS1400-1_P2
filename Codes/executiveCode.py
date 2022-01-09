import time
import sostream
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Add time to check the amount of time spent
start1 = time.time()
#Reading is dataset
data1 = pd.read_csv("Dataset_1.csv", header=None, engine='python')
#Build an object of a sostream class and process the vectors one by one
objectData1 = sostream.sostream(alpha = 0, minPts = 3, threshold = 5)
print('For Dataset_1:')
objectData1.make(data1)
end1 = time.time()
start2 = time.time()
#Repeat the steps for the second dataset
data2 = pd.read_csv("Dataset_2.csv", header=None, engine='python')
objectData2 = sostream.sostream(alpha = 0, minPts = 3, threshold = 5)
print('For Dataset_2:')
objectData2.make(data2)
end2 = time.time()
#Show the required items in case of practice
print(f"Time Dataset_1: {end1 - start1}.")
print(f"Time Dataset_2: {end2 - start2}.")
centroids1 = np.array([cluster.centroid for cluster in objectData1.clusterArr[len(objectData1.clusterArr)-1]])
centroids2 = np.array([cluster.centroid for cluster in objectData2.clusterArr[len(objectData2.clusterArr)-1]])
print(f"Cluster Number Dataset_1: {len(centroids1)}.")
print(f"Cluster Number Dataset_2: {len(centroids2)}.")
#Show Plot
plt.scatter(data1[:][0], data1[:][1], color='blue',s=100)
plt.scatter(centroids1[:,0], centroids1[:,1], color='red',s=100)
plt.scatter(data2[:][0], data2[:][1], color='blue',s=100)
plt.scatter(centroids2[:,0], centroids2[:,1], color='red',s=100)
plt.show()