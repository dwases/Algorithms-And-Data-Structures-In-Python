# Zaimplementuj algorytm z powracaniem
# znajdujący cykl Hamiltona
# w grafie nieskierowanym (na macierzy sąsiedztwa)
import sys
import time
# adjacency matrix


class Graph:
    adj = []

    def __init__(self, v, e):
        self.v = v
        self.e = e
        self.kr = []
        self.succ = [[i] for i in range(v)]
        Graph.adj = [[0 for i in range(v)]
                     for j in range(v)]

    # nowy wierzcholek
    def addEdge(self, v1, v2):
        Graph.adj[v1][v2] = 1
        self.kr.append([v1, v2])
        for i in range(len(self.succ)):
            if self.succ[i][0] == v1:
                self.succ[i].append(v2)

    # dfs dla macierzy incydencji
    def DFS(self, v, visited):
        #print(v, end=', ')
        visited[v] = True
        for i in range(self.v):
            if (Graph.adj[v][i] == 1 and
                    (not visited[i])):
                self.DFS(i, visited)

    # bfs dla macierzy incydencji
    def BFS(self, v):
        visited = [False] * self.v
        tab = [v]
        visited[v] = True
        while tab:
            pierwszy = tab[0]
            #print(pierwszy, end=', ')
            tab.pop(0)
            for i in range(self.v):
                if (Graph.adj[pierwszy][i] == 1 and
                        (not visited[i])):
                    tab.append(i)
                    visited[i] = True

    # algorytm kahna dla macierzy incydencji
    def top_sortBFS(self):
        transadj = [[0]*v] * v
        transadj = [[Graph.adj[j][i]
                     for j in range(len(Graph.adj))] for i in range(len(Graph.adj[0]))]
        posortowane = []
        # do tego momentu jest ok
        while transadj != [[0]*self.v]*self.v:
            for i in range(len(transadj)):
                if not 1 in transadj[i]:
                    if i not in posortowane:
                        posortowane.append(i)
                    for j in range(len(transadj)):
                        transadj[j][i] = 0
        return posortowane

    def pomocnicza(self, v, visited, stack):
        visited[v] = True
        for i in self.adj:
            for j in i:
                if i == 1:
                    self.pomocnicza(i, visited, stack)
        stack.append(v)

    def top_sortDFS(self):
        visited = [False]*self.v
        stack = []
        for i in range(self.v):
            if visited[i] == False:
                self.pomocnicza(i, visited, stack)
        # print(stack)
###

    def czy_isc(self, v, wskaznik, path):
        if self.adj[path[wskaznik-1]][v] == 0:
            return False
        for u in path:
            if u == v:
                return False
        return True

    def hamilton_pomocnicza(self, path, wskaznik):
        if wskaznik == self.v:
            if self.adj[path[wskaznik-1]][path[0]] == 1:
                return True
            else:
                return False
        for vi in range(1, self.v):
            if self.czy_isc(vi, wskaznik, path):
                path[wskaznik] = vi
                if self.hamilton_pomocnicza(path, wskaznik+1) == True:
                    return True
                path[wskaznik] = -1
        return False

    def hamilton(self):
        path = [-1] * self.v
        path[0] = 0
        if not self.hamilton_pomocnicza(path, 1):
            print("BRAK ROZW")
            return
        # wykomentowane zeby nie przeszkadzalo w tescie
        # print(path)

    def euler(self, v, stos):
        for i in range(len(self.adj)):
            if self.adj[v][i] == 1:
                self.adj[i][v] = 0
                self.adj[v][i] = 0
                self.euler(i, stos)
        stos.append(v)
        return stos


sys.setrecursionlimit(1000000)
# dla nasycenia = 50%
v = 12
e = int((((v*(v-1))/2)*0.5)*2)
counter = 0
G = Graph(v, e)
for i in range(v-1):
    G.addEdge(i, i+1)
    G.addEdge(i+1, i)
    counter += 2
#G.addEdge(i+1, 0)
#G.addEdge(0, i+1)
#counter += 2
while(counter <= e):
    for i in range(v):
        for j in range(v):
            if (G.adj[i][j] == 0) and (i != j) and (i != 0) and (j != 0):
                G.addEdge(i, j)
                counter += 1
t0 = time.time()
print(G.hamilton())
t1 = time.time() - t0
print("czas hamiltona dla 30%:", t1)
#t0 = time.time()
#G.euler(0, [])
#t1 = time.time() - t0
#print("czas eulera dla 30%:", t1)


"""
v, e = 5, 5
G = Graph(v, e)
G.addEdge(0, 1)
G.addEdge(1, 0)
G.addEdge(1, 2)
G.addEdge(2, 1)
G.addEdge(2, 4)
G.addEdge(4, 2)
G.addEdge(4, 3)
G.addEdge(3, 4)
G.addEdge(3, 0)
G.addEdge(0, 3)
G.hamilton()
print(G.euler(0, []))
"""


"""
v, e = 5, 6
G = Graph(v, e)
G.addEdge(0, 1)
G.addEdge(1, 0)
G.addEdge(1, 2)
G.addEdge(2, 1)
G.addEdge(2, 4)
G.addEdge(4, 2)
G.addEdge(1, 4)
G.addEdge(4, 1)
G.addEdge(4, 3)
G.addEdge(3, 4)
G.addEdge(3, 0)
G.addEdge(0, 3)
"""
"""
# testowo
#v = 50
#e = v*(v-1)//2

# koniec testowo
print("Macierz incydencji")
print(G.adj)
visited = [False] * v
print("DFS:")
G.DFS(0, visited)
print("\nBFS:")
G.BFS(0)
#print("algortym kahna")
# algortym kahna
# G.Kahn_Sort()
#print([[i] for i in range(10)])
print("\nSortowanie topologiczne metoda Kahna:")
print(G.top_sortBFS())
print("\nSortowanie topologiczne metoda wglab:")
print(G.top_sortDFS())

# print(0==False)
"""

"""
for a in range(100, 1100, 100):
    krawedzie = 0
    v = a  # tu zmieniac dla innych ilosci wierzcholkow
    e = (v * (v-1))//2
    G = Graph(v, e)
    for i in range(v-1):
        G.addEdge(i, i+1)
    for i in range(v):
        for j in range(v):
            if (j > i+1) and (krawedzie < e):
                G.addEdge(i, j)
                krawedzie += 1
    start = time.time()
    #visited = [False] * v
    G.top_sortDFS()
    end = time.time()
    print(end-start)
    #print(" czas przejscia bfs: ")
    #visited = [False] * v
    #G.DFS(0, visited)
    #print(" czas przejscia dfs: ")
    # G.top_sortBFS()
    #print(" czas sortowania kahna: ")
    # G.top_sortDFS()
    #print(" czas sortowania wglab: ")
input()
"""
