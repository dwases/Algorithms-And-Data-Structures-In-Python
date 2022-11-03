import copy
import time


class Graph:
    def __init__(self, v, e):

        self.v = v
        self.e = e
        # lista nastepnikow
        self.succ = [[i] for i in range(v)]

    #dobra, dziala
    def addEdge(self, v1, v2):
        for i in range(len(self.succ)):
            if self.succ[i][0] == v1:
                self.succ[i].append(v2)

    # dziala - bfs dla listy nastepnikow
    def BFSsucc(self, v):
        visited = [False] * self.v
        tab = [v]
        visited[v] = True
        while tab:
            pierwszy = tab[0]
            #print(pierwszy, end=", ")
            tab.pop(0)
            for i in range(self.v):
                if (not visited[i]) and (i in self.succ[pierwszy]):
                    tab.append(i)
                    visited[i] = True

    # dfs dla listy nastepnikow - tez dziala
    def DFSsucc(self, v, visited):
        #print(v, end=", ")
        visited[v] = True
        for i in range(self.v):
            if (i in self.succ[v] and (not visited[i])):
                self.DFSsucc(i, visited)

    # dziala w koncu :)))))
    def top_sortBFSsucc(self):
        posortowane = []
        # stopien wejsciowy
        licznosci = [-1] * self.v
        for el in self.succ:
            for sub_el in el:
                licznosci[sub_el] += 1
        succ_copy = copy.deepcopy(self.succ)
        # print(succ_copy)
        while licznosci != (["zuzyte"] * self.v):
            for el in succ_copy:
                if licznosci[el[0]] == 0:
                    posortowane.append(el[0])
                    licznosci[el[0]] = "zuzyte"
                    for i in range(len(el)):
                        if i == 0:
                            pass
                        else:
                            licznosci[el[i]] -= 1
        # print(posortowane)

###
    def pomocniczasucc(self, v, visited, stack):
        visited[v] = True
        for el in self.succ[v]:
            if visited[el] == False:
                self.pomocniczasucc(el, visited, stack)
        stack.append(v)

    def top_sortDFSsucc(self):
        visited = [False]*self.v
        stack = []
        for i in range(self.v):
            if visited[i] == False:
                self.pomocniczasucc(i, visited, stack)
        # print(stack[::-1])
###

###
# poprawic
    def czy_isc(self, v, wskaznik, path):
        # if self.adj[path[wskaznik-1]][v] == 0:
        if v not in self.succ[path[wskaznik-1]]:
            return False
        for u in path:
            if u == v:
                return False
        return True

    def hamilton_pomocnicza(self, path, wskaznik):
        if wskaznik == self.v:
            # if self.adj[path[wskaznik-1]][path[0]] == 1:
            if path[0] in self.succ[path[wskaznik-1]]:
                return True
            else:
                return False
        for vi in range(1, self.v):
            if self.czy_isc(vi, wskaznik, path) == True:
                path[wskaznik] = vi
                if self.hamilton_pomocnicza(path, wskaznik+1) == True:
                    return True
                path[wskaznik] = -1
        return False

    def hamilton(self):
        path = [-1] * self.v
        path[0] = 0
        if self.hamilton_pomocnicza(path, 1) == False:
            print("BRAK ROZW")
            return
        print(path)

###


v, e = 5, 12
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
G.hamilton()

"""
print(G.succ)
G.BFSsucc(0)
visited = [False] * v
print("\n")
G.DFSsucc(0, visited)
print("\nsortowanie")
G.top_sortBFSsucc()
print("\nsortowanie")
G.top_sortDFSsucc()
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
    G.top_sortDFSsucc()
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
