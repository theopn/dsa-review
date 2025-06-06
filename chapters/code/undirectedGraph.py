from collections import deque


class Graph:
    # e.g.,: Graph(n = 3, edges = [[0,1],[1,2],[0,2]])
    # creates a graph with 3 nodes indexed 0, 1, 2,
    # with each connected to each other
    def __init__(self, n: int, edges: list[list[int]]):
        self.n = n

        self.adjList = [[] for _ in range(n)]
        for u, v in edges:
            self.adjList[u].append(v)
            self.adjList[v].append(u)

        self.adjMatrix = [[float("inf") for _ in range(n)] for _ in range(n)]
        for i in range(v):
            self.adjMatrix[i][i] = 0
        for u, v in edges:
            self.adjMatrix[u][v] = 1
            self.adjMatrix[v][u] = 1

    def bfs(self, v: int):  # v is the starting node
        q = deque()
        dist = [-1] * self.n
        path = [[] for _ in range(self.n)]
        visited = [False] * self.n

        q.append(v)
        dist[v] = 0
        path[v] = [0]
        visited[v] = True

        while q:
            u = q.pop()

            for w in self.adjList[u]:
                if not visited[w]:
                    q.append(w)
                    dist[w] = dist[u] + 1
                    path[w] = path[u] + [w]
                    visited[w] = True

        return dist, path, visited

    def dfs_iterative(self, v: int):  # v is the starting node
        st = []
        dist = [-1] * self.n
        path = [[] for _ in range(self.n)]
        visited = [False] * self.n

        st.append(v)
        dist[v] = 0
        path[v] = [0]
        visited[v] = True

        while st:
            u = st.pop()

            for w in self.adjList[u]:
                if not visited[w]:
                    st.append(w)
                    dist[w] = dist[u] + 1
                    path[w] = path[u] + [w]
                    visited[w] = True

        return dist, path, visited

    # helper function for finding connected components using recursive DFS
    def dfs_recursive_driver(self, v: int,
                             visited,
                             connectedComponents,
                             currConnectedCompIdx):
        visited[v] = True
        connectedComponents[currConnectedCompIdx].append(v)
        for w in self.adjList[v]:
            if not visited[w]:
                self.dfs_recursive_driver(
                    w, visited, connectedComponents, currConnectedCompIdx)

    def find_connected_comp(self):
        visited = [False] * self.n

        connectedComponents = []
        currConnectedCompIdx = -1
        for v in range(self.n):
            if not visited[v]:
                currConnectedCompIdx += 1
                connectedComponents.append([])
                self.dfs_recursive_driver(
                    v, visited, connectedComponents, currConnectedCompIdx)

        return connectedComponents


def testBFS():
    g = Graph(5, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]])
    print(g.bfs(0))


def testConnectedComp():
    g = Graph(5, [[0, 1], [1, 2], [2, 3]])
    print(g.find_connected_comp())


testBFS()
testConnectedComp()
