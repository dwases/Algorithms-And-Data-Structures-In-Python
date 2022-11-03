import time
# tabela krawedzi


class Graph:
    def __init__(self, v, e):

        self.v = v
        self.e = e
        # tabela krawedzi
        self.kr = []

    # dziala - dodawanie dla tabeli krawedzi
    def addEdge(self, v1, v2):
        self.kr.append([v1, v2])

    # bfs dla listy krawedzi
    def BFSkr(self, v):
        visited = [False] * self.v
        tab = [v]
        visited[v] = True
        while tab:
            pierwszy = tab[0]
            #print(pierwszy, end=', ')
            tab.pop(0)
            for i in range(self.v):
                if (([pierwszy, i] in self.kr) and (not visited[i])):
                    tab.append(i)
                    visited[i] = True

    # dfs dla listy krawedzi
    def DFSkr(self, v, visited):
        #print(v, end=', ')
        visited[v] = True
        for i in range(self.v):
            if (([v, i] in self.kr) and (not visited[i])):
                self.DFSkr(i, visited)

    # sortowanie kahna dla tabeli krawedzi
    def top_sortBFSkr(self):
        posortowane = []
        # stopien wejsciowy
        licznosci = [0] * self.v
        for i in range(len(self.kr)):
            licznosci[self.kr[i][1]] += 1
        # print(licznosci)
        # do teraz dziala
        while licznosci != (["zuzyte"] * self.v):
            for i in range(len(licznosci)):
                if licznosci[i] == 0:
                    if i not in posortowane:
                        posortowane.append(i)
                        licznosci[i] = "zuzyte"
                    for j in range(len(self.kr)):
                        if self.kr[j][0] == i:
                            licznosci[self.kr[j][1]] -= 1
                    break
        return posortowane
###

    def pomocniczakr(self, v, visited, stack):
        visited[v] = True
        for i in self.kr:
            if self.kr[0] == v:
                if visited[i] == False:
                    self.pomocniczakr(i, visited, stack)
        stack.append(v)

    def top_sortDFSkr(self):
        visited = [False]*self.v
        stack = []
        for i in range(self.v):
            if visited[i] == False:
                self.pomocniczakr(i, visited, stack)
        # print(stack)
###


v, e = 6, 7
G = Graph(v, e)
G.addEdge(0, 1)
G.addEdge(1, 2)
G.addEdge(2, 3)
G.addEdge(1, 4)
G.addEdge(4, 2)
G.addEdge(4, 5)
G.addEdge(5, 3)
print(G.kr)
"""
G.BFSkr(0)
visited = [False] * v
print("\n")
G.DFSkr(0, visited)
print("\nsortowanie")
print(G.top_sortBFSkr())
print("\nsortowanie")
print(G.top_sortDFSkr())
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
    G.top_sortDFSkr()
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
