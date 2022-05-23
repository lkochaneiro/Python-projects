from graph_representation import AdjacencyList
from math import inf

"""Here is class which allow find minimum spanning tree. I implemented two most popular methods. It's based
on adjacency list because it's easier for me to operate with than adjacency matrix."""


class MinimumSpanningTree(AdjacencyList):

    def __init__(self):
        super().__init__()

    def prime_algorithm(self, start_vertex):
        start_idx = self.get_vertex_idx(start_vertex)

        n = self.order()
        visited = {idx: False for idx in range(n)}
        added_edges, total_cost = 0, 0
        edges_lst_result = []

        visited[start_idx] = True

        while added_edges < n - 1:
            min_cost = inf
            act_vertex, neighbour_of_act_vertex = -1, -1
            for idx_vertex in range(n):
                if visited[idx_vertex]:
                    for neighbour, weight in self.lst_nei[idx_vertex]:
                        if not visited[neighbour]:
                            if min_cost > weight:
                                min_cost = weight
                                act_vertex, neighbour_of_act_vertex = idx_vertex, neighbour

            visited[neighbour_of_act_vertex] = True
            added_edges += 1
            total_cost += min_cost

            v1 = self.get_vertex(act_vertex)
            v2 = self.get_vertex(neighbour_of_act_vertex)
            edges_lst_result.append((v1, v2, min_cost))

        return edges_lst_result, total_cost

    def kruskal_algorithm(self):
        n = self.order()
        added_edges, total_cost = 0, 0
        result_edges = []

        # Sortowanie krawędzi
        all_edges = self.edges()
        all_edges.sort(key=lambda x: x[2])

        # Dodajemy n - wierzchołków do naszej struktury
        sets = UnionFind()
        for _ in range(n):
            sets.add_vertex()

        while added_edges < n - 1:
            for v_start, v_end, weight in all_edges:
                idx_start = self.get_vertex_idx(v_start)
                idx_end = self.get_vertex_idx(v_end)
                if not sets.same_components(idx_start, idx_end):
                    sets.union(idx_start, idx_end)

                    result_edges += [(v_start, v_end, weight)]
                    total_cost += weight
                    added_edges += 1

        return result_edges, total_cost


# Help class to improve Kruskal algorithm
class UnionFind:

    def __init__(self):
        self.parents = []
        self.rank = []

    def find(self, v):
        if self.parents[v] == -1:  # -1 oznacza, że wierzchołek jest korzeniem
            return v
        return self.find(self.parents[v])

    def union(self, v1, v2):
        if not self.same_components(v1, v2):
            if self.parents[v1] == -1 and self.parents[v2] == -1:  # Dwa korzenie zbiorów
                if self.rank[v1] == self.rank[v2]:
                    self.parents[v1] = v2
                    self.rank[v2] += 1
                else:
                    if self.rank[v1] > self.rank[v2]:
                        self.parents[v2] = v1
                    else:  # ..v2 > ..v1
                        self.parents[v1] = v2
            else:
                new_parent1, new_parent2 = self.find(v1), self.find(v2)

                if self.parents[v1] != -1:
                    self.parents[v1] = new_parent1
                if self.parents[v2] != -1:
                    self.parents[v2] = new_parent2

                self.union(new_parent1, new_parent2)

    def same_components(self, v1, v2):
        if self.find(v1) == self.find(v2):
            return True
        return False

    def add_vertex(self):
        self.parents.append(-1)
        self.rank.append(0)