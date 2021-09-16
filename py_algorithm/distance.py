#use euclidean distance 
#brute force
import math
def distance (p1, p2):
    return math.sqrt((p1[0]-p2[0]) + (p1[1]-p2[1]))
#algorithm and 복잡도
def closest_pair(p):
    n = len(p)
    mindist = float('inf')
    for i in range(n-1):
        for j in range(i+1, n):
            dist = format(distance(p[i],p[j]))
            if dist < mindist:
                mindist = dist
                minp1 = i
                minp2 = j
    return mindist ,minp1,minp2




p = [(2,3), (12,30), (40,50), (5,1), (12,10), (3,4)]
print("최근접 거리: ", closest_pair(p))