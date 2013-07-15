'''
Algorithms - design and analysis (Stanford), Part I.

Programming Question 3:

The file contains the adjacency list representation of a simple undirected graph. There are 200 vertices labeled 1 to 200. The first column in the file represents the vertex label, and the particular row (other entries except the first column) tells all the vertices that the vertex is adjacent to. So for example, the 6th row looks like : "6 155 56 52 120 ......". This just means that the vertex with label 6 is adjacent to (i.e., shares an edge with) the vertices with labels 155,56,52,120,......,etc

Your task is to code up and run the randomized contraction algorithm for the min cut problem and use it on the above graph to compute the min cut. (HINT: Note that you'll have to figure out an implementation of edge contractions. Initially, you might want to do this naively, creating a new graph from the old every time there's an edge contraction. But you should also think about more efficient implementations.) (WARNING: As per the video lectures, please make sure to run the algorithm many times with different random seeds, and remember the smallest cut that you ever find.) Write your numeric answer in the space provided. So e.g., if your answer is 5, just type 5 in the space provided.

@author: Renat Alimbekov
'''

import collections
import math
import random
import copy

def remove_all(y,fromlist):
    for x in fromlist:
        print(x)
        if x == y: fromlist.remove(y)

def replace_all(x,y,fromlist):
    for z in fromlist:
        if z == x:
            fromlist.remove(x)
            fromlist.append(y)

def edgeContraction(dic, nodeA, nodeB):
    dic[nodeA] = dic[nodeA] + dic[nodeB]
    dic.pop(nodeB)
    # Cleanup of loopback nodes
    for i in dic:
        for j in range(len(dic[i])):
            if dic[i][j] == nodeB:
                 dic[i][j] = nodeA
    dic[nodeA] = list(filter(lambda x: x != nodeA, dic[nodeA]))
            
    return dic

def findMinCut(dic):
    if len(dic) == 2:
        return len(list(dic.values())[0])
    else:
        nodeA = random.choice(list(dic.keys()))
        nodeB = random.choice(dic[nodeA])
        findMinCut(edgeContraction(dic, nodeA, nodeB))
        return len(list(dic.values())[0])

if __name__=="__main__":
    with open("kargerMinCut.txt", 'r') as f:
        original_graph = {}
        for line in f:
            dic = list(map(int,line.strip().split("\t")))
            original_graph[dic.pop(0)] = dic

    i = 0
    length = len(original_graph)
    mincuts = length**2

    while i < length**2*math.log(length):
        graph = copy.deepcopy(original_graph)
        newMinCut = findMinCut(graph)
        if newMinCut < mincuts:
            mincuts = newMinCut
            print(mincuts)
        i += 1
        

