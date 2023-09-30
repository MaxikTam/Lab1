import math
from points import *

def GetDMatrix(points): #составляем матрицу расстояний между точками
    dMatrix = []
    dLine = []

    for i in range(0,len(points)):
        for j in range(0,len(points)):
            dLine.append(Metric(points[i], points[j]))
        dMatrix.append(dLine)
        dLine = []

    print("d matrix:")
    for line in dMatrix:
        print(line)
    print()

    return dMatrix

def MinMatrix(dMatrix): #находим индексы двух точек с наименишей метрикой
    min = dMatrix[0][1]
    minIndex = [0,1]
    
    for i in range(0,len(dMatrix)):
        for j in range(i+1, len(dMatrix)):
            if dMatrix[i][j] - min < 0 :
                min = dMatrix[i][j]
                minIndex = [i,j]
    
    print(f"Min value of d matrix: {min}")
    print(f"closest points: {minIndex}")
    print()

    return minIndex

def ReBuild(points, minIndex): #пересобираем список точек, объединяем найденные точки в один объект
    newPoints = []
    cluster = []
    #TODO: обнавлять массив точек без потерь этих точекж
    

    for index in minIndex:
        if isinstance(points[index][0], list):

            for point in points[index]:
                cluster.append(point)
        else:
            cluster.append(points[index])

    newPoints.append(cluster)

    for index in range(0, len(points)):
        if not (index in minIndex):
            newPoints.append(points[index])
    
    print("New Points matrix:")
    for point in newPoints:
        print(point)
    print()
        
    return newPoints

def GetPointsAndClusters(pointsAndClusters):
    newPoints = []
    for point in pointsAndClusters:
        if isinstance(point[0], list):
            newPoints.append(GetMassCenter(point))

        else:
            newPoints.append(point)
    
    return newPoints