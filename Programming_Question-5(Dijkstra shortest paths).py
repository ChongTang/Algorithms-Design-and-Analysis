'''
Programming Question 5:

The file contains an adjacency list representation of an undirected weighted graph with 200 vertices labeled 1 to 200. Each row consists of the node tuples that are adjacent to that particular vertex along with the length of that edge. For example, the 6th row has 6 as the first entry indicating that this row corresponds to the vertex labeled 6. The next entry of this row "141,8200" indicates that there is an edge between vertex 6 and vertex 141 that has length 8200. The rest of the pairs of this row indicate the other vertices adjacent to vertex 6 and the lengths of the corresponding edges.

Your task is to run Dijkstra's shortest-path algorithm on this graph, using 1 (the first vertex) as the source vertex, and to compute the shortest-path distances between 1 and every other vertex of the graph. If there is no path between a vertex v and vertex 1, we'll define the shortest-path distance between 1 and v to be 1000000.

You should report the shortest-path distances to the following ten vertices, in order: 7,37,59,82,99,115,133,165,188,197. You should encode the distances as a comma-separated string of integers. So if you find that all ten of these vertices except 115 are at distance 1000 away from vertex 1 and 115 is 2000 distance away, then your answer should be 1000,1000,1000,1000,1000,2000,1000,1000,1000,1000. Remember the order of reporting DOES MATTER, and the string should be in the same order in which the above ten vertices are given. Please type your answer in the space provided.

IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) time implementation of Dijkstra's algorithm should work fine. OPTIONAL: For those of you seeking an additional challenge, try implementing the heap-based version. Note this requires a heap that supports deletions, and you'll probably need to maintain some kind of mapping between vertices and their positions in the heap.

@author: Renat Alimbekov
'''


def readUndirectedGraph(filename):
    
    adjlist = []
    
    lines = open(filename).read().splitlines()
    
    for line in lines:
        
        adjlist.append([])
        data = line.split()
        v = int(data[0])-1
        
        for tpl in data[1:]:
            
            ts, ws = tpl.split(',')
            t = int(ts)-1
            w = int(ws)
            
            adjlist[v].append((t, w))

    return adjlist


def extract_min(pq, weights):
    
    i = 0
    j = 1
    m = weights[pq[0]]
    
    while j < len(pq):
        if weights[pq[j]] < m:
            i = j
            m = weights[pq[j]]
        j += 1
    
    res = pq[i]
    
    pq[i] = pq[-1]
    pq.pop()
    
    return res


def dijkstraShortestPaths(graph, s):
    '''
Works in O(n^2), since we use
an array to maintain the priority queue.
'''
    
    infinity = 1000000
    
    weights = [infinity]*len(graph)
    weights[s] = 0
    
    pqueue = [i for i in range(len(graph))]
    
    visited = [False]*len(graph)
    
    while len(pqueue) > 0:
                
        v = extract_min(pqueue, weights)
        visited[v] = True
    
        for inc, w in graph[v]:
            if not visited[inc]:
                weights[inc] = min(weights[inc], weights[v]+w)
                
    return weights


def main():
    
    desired = [7,37,59,82,99,115,133,165,188,197]
    
    graph = readUndirectedGraph('dijkstraData.txt')
    weights = dijkstraShortestPaths(graph, 0)
    
    res = []
    for i in desired:
        res.append(str(weights[i-1]))
        
    print(','.join(res))
    
    

if __name__ == '__main__':
    main()
