import random
import math

def Metric(M1, M2): #задаём метрику
    mod = []

    #TODO: переопределить метрику на случай нескольких точек, методом среднего расстояния

    for i in range(0,3):
        d = round(math.fabs(M1[i]-M2[i]),2)
        mod.append(d)
    return max(mod)

def GetListOfPoints(n): #генерируем список из n рандомных точек с координатами xyz
    points = []
    point = []

    for i in range(0, n):
        for j in range(0,3):
            point.append(round(random.random(), 2))
        point.append(i)
        points.append(point)
        point = []

    print("Start. Points Matrix:")
    for point in points:
        print(point)
    print()

    return points

def GetMassCenter(claster):
    massCenter = []
    x_mc = 0.
    y_mc = 0.
    z_mc = 0.

    for point in claster:
        x_mc += point[0]
        y_mc += point[1]
        z_mc += point[2]
    
    x_mc = round(x_mc / len(claster), 2)
    y_mc = round(y_mc / len(claster), 2)
    z_mc = round(y_mc / len(claster), 2)

    massCenter.append(x_mc)
    massCenter.append(y_mc)
    massCenter.append(z_mc)    
    
    return massCenter