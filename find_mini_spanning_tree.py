"""
Question 3
Given an undirected graph G, find the minimum spanning tree within G. 
A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. 
Your function should take in and return an adjacency list structured like this:
{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}
Vertices are represented as unique strings. The function definition should be question3(G)

We use breadth first search + Dijkstra algorithm to find the minimum spanning tree. 
To implement the Dijkstra algorithm, we use priority queue (i.e. heap) to find the edge with minimum weight.

Suppose the set of vertexs and edges are V and E respectively. The time complexity is |E|+|V|log|V|
and the space complexity is |V| + |E|
"""
from heapq import heappush, heappop
def question3(G):
    if not G:  # empty graph
        return G
    root = None
    # pick a starting point randomly
    spanning_tree = {}
    for k in G:
        root = k
        break
    spanning_tree = {}
    pq = []
    heappush(pq, (0, root, None))
    while pq:
        u = pq[0]
        heappop(pq)
        e, v, vv = u
        if v in spanning_tree:
            continue
        if vv:
            spanning_tree[v] = [(vv, e)]
            if vv not in spanning_tree:
                spanning_tree[vv] = [(v, e)]
            else:
                spanning_tree[vv].append((v, e))
        for node, distance in G[v]:
            if node not in spanning_tree:
                heappush(pq, (distance, node, v))     
    return spanning_tree           

G1 = {
    'A': [('B', 2),('C', 10)],
    'B': [('A', 2), ('C', 5)], 
    'C': [('B', 5), ('A', 10)]
}
print(question3(G1))

G2 = {
    'A': [('B', 2),('C', 1)],
    'B': [('A', 2), ('C', 5)], 
    'C': [('B', 5), ('A', 1)]
}
print(question3(G2))
G3 = {}
print(question3(G3))

# test case 1
# expect to print out bab
# print(question2("babad")) 


#test case 2
# expect to print out bb
# print(question2("cbbd"))  

# test case 3
# expect to print out false
# print(question2())
