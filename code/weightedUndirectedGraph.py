from heapq import heappush, heappop


class Graph:
    # e.g.,: Graph(n = 3, edges = [[0,1,3],[1,2,1],[0,2,6]])
    # creates a graph with 3 nodes indexed 0, 1, 2,
    # with 0 - 1 (weight 3), 0 - 2 (weight 6), 1 - 2 (weight 1)
    def __init__(self, n: int, edges: list[list[int]]):
        self.n = n
        self.edges = edges

        self.adjList = [[] for _ in range(n)]
        for u, v, weight in edges:
            self.adjList[u].append((v, weight))
            self.adjList[v].append((u, weight))

        self.adjMatrix = [[float("inf") for _ in range(n)] for _ in range(n)]
        for i in range(v):
            self.adjMatrix[i][i] = 0
        for u, v, w in edges:
            self.adjMatrix[u][v] = weight
            self.adjMatrix[v][u] = weight

    def dijkstra(self, s):
        dist = [float("inf")] * self.n
        prev = [-1] * self.n

        dist[s] = 0
        q = [(0, s)]

        while q:
            priority, u = heappop(q)

            if priority == dist[u]:  # or p <= dist[u]
                for w, weight in self.adjList[u]:
                    candidate = dist[u] + weight
                    if candidate < dist[w]:
                        dist[w] = candidate
                        prev[w] = u
                        heappush(q, (candidate, w))

        return dist, prev

    def floydWarshall(self):
        dist = [row[:] for row in self.adjMatrix]

        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        return dist


def testDijkstra():
    """
       (0)
      /   \
    1     1
    /       \
    (1) ---1--- (2)
    """
    g1 = Graph(3, [
        [0, 1, 1],
        [1, 2, 1],
        [0, 2, 1]
    ])
    dist1, prev1 = g1.dijkstra(0)
    print("Test Case 1 - Simple Triangle")
    print("Distances:", dist1)  # Expected: [0, 1, 1]
    print("Prev:", prev1)       # Expected: [-1, 0, 0]

    """
       (0)
      /   \
    5     2
    /       \
    (1) ---1--- (2)
    """
    g2 = Graph(3, [
        [0, 1, 5],
        [1, 2, 1],
        [0, 2, 2]
    ])
    dist2, prev2 = g2.dijkstra(0)
    print("\nTest Case 2 - Unequal Weights")
    print("Distances:", dist2)  # Expected: [0, 3, 2]
    print("Prev:", prev2)       # Expected: [-1, 2, 0]

    """
    (0) —1— (1)    (2)
    """
    g3 = Graph(3, [
        [0, 1, 1]
    ])
    dist3, prev3 = g3.dijkstra(0)
    print("\nTest Case 3 - Disconnected Node")
    print("Distances:", dist3)  # Expected: [0, 1, inf] or large number
    print("Prev:", prev3)       # Expected: [-1, 0, None or -1]

    """
        (0)
        /   \
      1      2
      /       \
    (1) —1— (2)
     \\       /
        1   2
         \\ /
          (3)
    """
    g4 = Graph(4, [
        [0, 1, 1],
        [1, 3, 1],
        [0, 2, 2],
        [2, 3, 2],
        [1, 2, 1]
    ])
    dist4, prev4 = g4.dijkstra(0)
    print("\nTest Case 4 - Multiple Paths")
    print("Distances:", dist4)  # Expected: [0, 1, 2, 2]
    print("Prev:", prev4)       # Expected: [-1, 0, 1, 1] or [-1, 0, 0, 1]


def testFloydWarshall():
    g4 = Graph(4, [
        [0, 1, 1],
        [1, 3, 1],
        [0, 2, 2],
        [2, 3, 2],
        [1, 2, 1]
    ])
    dist4 = g4.floydWarshall()
    print("\nTest Case 4 - Multiple Paths")
    # [0, 1, 2, 2]
    # [inf, 0, 1, 1]
    # [inf, inf, 0, 2]
    # [inf, inf, inf, 0]
    print("Distances:", dist4)

    """
      (0)
     /   \
   1     -2
   /       \
   (1) —2— (2)
    """
    # g5 = Graph(3, [
    #     [0, 1, 1],
    #     [1, 2, 2],
    #     [0, 2, -2]
    # ])
    # dist5 = g5.floydWarshall()  # Use bellman_ford for negative weights
    # print("\nTest Case 5 - Negative Edge")
    # print("Distances:", dist5)  # Expected: [0, 1, -2]


testDijkstra()
testFloydWarshall()
