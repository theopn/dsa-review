from collections import deque


class Graph:
    # e.g.,: Graph(n = 3, edges = [[0,1],[1,2],[0,2]])
    # creates a graph with 3 nodes indexed 0, 1, 2,
    # with 0 -> 1, 0 -> 2, 1 -> 2
    def __init__(self, n: int, edges: list[list[int]]):
        self.n = n
        self.edges = edges

        self.adjList = [[] for _ in range(n)]
        for u, v in edges:
            self.adjList[u].append(v)

        self.adjMatrix = [[float("inf") for _ in range(n)] for _ in range(n)]
        for i in range(v):
            self.adjMatrix[i][i] = 0
        for u, v in edges:
            self.adjMatrix[u][v] = 1

    def dfs(self, v, visited, path):
        visited[v] = True
        path.append(v)

        for w in self.adjList[v]:
            if not visited[w]:
                self.dfs(w, visited, path)

    def kojaraju(self):
        # Run DFS to make a stack of vertices based on exit time
        visited = [False] * self.n
        indegreePriorityStack = []

        def visit(v):
            visited[v] = True

            for w in self.adjList[v]:
                if not visited[w]:
                    visit(w)
            indegreePriorityStack.append(v)

        for v in range(self.n):
            if not visited[v]:
                visit(v)

        # DFS on the transposed graph, in the order of exit time
        transposedG = Graph(self.n, [[v, u] for u, v in self.edges])
        visitedTranspose = [False] * self.n
        scc = []
        while indegreePriorityStack:
            v = indegreePriorityStack.pop()
            if not visitedTranspose[v]:
                path = []
                transposedG.dfs(v, visitedTranspose, path)
                scc.append(sorted(path))

        return scc

    def kahnTopologicalSort(self):
        indeg = [0] * self.n

        for u, v in self.edges:
            indeg[v] += 1

        q = deque()
        for v in range(self.n):
            if indeg[v] == 0:
                q.append(v)

        ordering = []
        while q:
            u = q.pop()
            ordering.append(u)

            for w in self.adjList[u]:
                indeg[w] -= 1  # "removing" the edge
                if indeg[w] == 0:
                    q.append(w)

        # if we do not have all the nodes in the ordering list,
        # it means that the graph is not DAG.
        # It is because if the graph is DAG, all nodes will eventually have
        # zero indegree after edge removal
        return [] if len(ordering) != self.n else ordering


def testTopologicalSort():
    # this graph is DAG
    graph = Graph(3, [[0, 1], [1, 2], [0, 2]])
    assert graph.kahnTopologicalSort() == [0, 1, 2]

    # this graph is not DAG
    graph = Graph(3, [[0, 1], [1, 2], [2, 0]])
    assert graph.kahnTopologicalSort() == []


def testKosaraju():
    graph = Graph(4, [[0, 1], [1, 2], [2, 3]])
    print(graph.kojaraju())  # 0, 1, 2, 3

    # https://www.baeldung.com/cs/kosaraju-algorithm-scc
    # second example but zero-indexed
    graph = Graph(8, [[0, 1], [1, 2], [1, 3], [1, 4], [2, 0], [2, 3],
                      [4, 5], [4, 6], [5, 7], [6, 5], [7, 6]])
    print(graph.kojaraju())  # [0, 1, 2], [3], [4], [5, 6, 7]

    # https://cp-algorithms.com/graph/strongly-connected-components.html
    graph = Graph(10, [[0, 7], [0, 1],
                       [1, 1], [1, 2],
                       [2, 1], [2, 5],
                       [3, 2], [3, 4],
                       [4, 9],
                       [5, 3], [5, 6], [5, 9],
                       [6, 2],
                       [7, 0], [7, 6], [7, 8],
                       [8, 6], [8, 9],
                       [9, 4]])
    print(graph.kojaraju())  # [0, 7], [1, 2, 3, 5, 6], [4, 9], [8]


testTopologicalSort()
testKosaraju()
