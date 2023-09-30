from points import *

def GetStartCentroids(points):
    centroids = []
    M=[]

    for i in range(0, 9, 3):
        for j in range(0,3):
            cords = round((points[i][j] + points[i+1][j]+points[i+2][j])/3, 2) 
            M.append(cords)
        centroids.append(M)
        print(M)
        M=[]

    return centroids 

def GetNewCentroids(clusters):
    newCentroids = []
    M=[]

    for k in range(3):
        for i in range(3):
            for j in range(0,len(clusters)):
                cords += (clusters[j][i]) 
            cords = round(cords / len(clusters), 2)
            M.append(cords)
        newCentroids.append(M)
        M = []

    print(newCentroids)

    return newCentroids

def ClosestCentroid(point, centroids):
    distant = 0

    for i in range(3):
        if distant < Metric(point, centroids[i]):
            numOfClosets = i

    return numOfClosets

def GetNewClusters(points, centriods):
    K1 = []
    K2 = []
    K3 = []
    clusters = [K1, K2, K3]

    for point in points:
        clusters[ClosestCentroid].append(point)
    
    return clusters

def F_1(custers, points):
#TODO:
    res = 0

    return res

def F_2(custers, points):
#TODO:
    res = 0
    
    return res