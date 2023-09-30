import random
import math
from points import *
from hierarchical import *
from k_avrg import *


def main():
    n = 9
    points = GetListOfPoints(n)

# Выполнение иерархического алгоритма кластеризации
    newPoint = points
    pointsAndClusters = GetPointsAndClusters(newPoint)

    for i in range(n-1):
        print(f"Step {i+1} from {n-1}")
        
        dMatrix = GetDMatrix(pointsAndClusters)
        minIndex = MinMatrix(dMatrix)
        newPoint = ReBuild(newPoint, minIndex)
        pointsAndClusters = GetPointsAndClusters(newPoint)

#Выполнение метода к-средних
    newCentroids = GetStartCentroids(points)
    i = 0

    while(True):

        i += 1
        print(f"Step {i}")

        centroids = newCentroids
        clusters = GetNewClusters(points, centroids)

        print(f"F_1 = {F_1(clusters, points)}")
        print(f"F_2 = {F_2(clusters, points)}")
        
        newCentroids = GetNewCentroids(clusters)

        if centroids == newCentroids:
            break







    
if __name__ == '__main__':
    main()