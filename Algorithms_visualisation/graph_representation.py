from abc import ABC, abstractmethod

"""In this section you can create your graph representation by adjacency list
or adjacency matrix. You can add/delete vertexes and edges. Your vertexes name could be whatever
you want and it will be mapped into integer (0, 1, 2, ...). You have also function get_vertex_idx or 
get_vertex. It return good thing when you add opposite argument. Function neighbours need to take vertex_idx and it
returns list of neighbours indexes with their cost. Size return number od edges in graph, order returns 
number of vertexes. Print functions are here to help you and see some important things clearly. :)"""

"""Important!"""
"""Adding edges is possible if you added both vertexes before."""
"""My functions is to directed graphs with weight, so if you want to create undirected graph
you can add directed edges in both ways and if you want create graph without cost you can make
your all edges with the same cost for example equal 1."""


class Node:

    def __init__(self, key):
        self.key = key

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        if self.key == other:
            return True
        return False


class Graph(ABC):

    @abstractmethod
    def __init__(self):
        self.lst = []
        self.dct = {}

    def insert_vertex(self, vertex):
        v = Node(vertex)
        if v not in self.lst:
            self.lst.append(v.key)

        n = len(self.lst)
        self.dct = {self.lst[i]: i for i in range(n)}

    @abstractmethod
    def insert_edge(self, vertex1, vertex2, edge):
        pass

    @abstractmethod
    def delete_vertex(self, vertex):
        pass

    @abstractmethod
    def delete_edge(self, vertex1, vertex2):
        pass

    def get_vertex_idx(self, vertex):
        if vertex in self.lst:
            return self.dct[vertex]
        else:
            return "Nie ma takiego węzła"

    def get_vertex(self, vertex_idx):
        n = self.order() - 1
        if vertex_idx > n or vertex_idx < 0:
            return 'Nie ma węzła o takim indeksie'
        else:
            for key, value in self.dct.items():
                if vertex_idx == value:
                    return key

    @abstractmethod
    def neighbours(self, vertex_idx):
        pass

    def order(self):
        return len(self.lst)

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def edges(self):
        pass

    @ staticmethod
    def print_graph(g):
        n = g.order()
        print("------GRAPH------", n)
        for i in range(n):
            v = g.get_vertex(i)
            print(v, end=" -> ")
            neighbours = g.neighbours(i)
            for (j, w) in neighbours:
                print(g.get_vertex(j), w, end=";")
            print()
        print("-------------------")


class AdjacencyList(Graph):

    def __init__(self):
        super().__init__()
        self.lst_nei = {}

    def insert_vertex(self, vertex):
        super().insert_vertex(vertex)
        n = self.order()

        if len(self.lst_nei) == 0:
            self.lst_nei = {0: []}
        else:
            self.lst_nei[n - 1] = []

    def insert_edge(self, vertex1, vertex2, edge_weight):
        if vertex1 and vertex2 in self.lst:
            idx_v1 = self.get_vertex_idx(vertex1)
            idx_v2 = self.get_vertex_idx(vertex2)
            if idx_v2 not in self.lst_nei[idx_v1]:
                self.lst_nei[idx_v1] += [(idx_v2, edge_weight)]

    def delete_vertex(self, vertex):
        del_idx = self.get_vertex_idx(vertex)  # zapamiętujemy usuwany indeks
        self.lst.pop(del_idx)
        self.dct = {self.lst[i]: i for i in range(len(self.lst))}  # nowy słownik

        # Dwie niemal identyczne pętle ponieważ przy 1 się coś psuło
        for key in self.lst_nei.keys():
            for i, el in enumerate(self.lst_nei[key]):
                neighbour_key, w = el
                if neighbour_key == del_idx:
                    self.lst_nei[key].pop(i)

        for key in self.lst_nei.keys():
            for i, el in enumerate(self.lst_nei[key]):
                neighbour_key, w = el
                if neighbour_key > del_idx:
                    self.lst_nei[key][i] = neighbour_key - 1, w

        n = self.order()

        for key, val in self.lst_nei.items():  # przesuwamy klucze elementów wyższe niż usunięty
            if key > del_idx:
                self.lst_nei[key - 1] = val

        self.lst_nei.pop(n)  # ostatni wywalamy bo się zmieniejsza o 1

    def delete_edge(self, vertex1, vertex2):
        if vertex1 and vertex2 in self.lst:
            idx_v1 = self.get_vertex_idx(vertex1)
            idx_v2 = self.get_vertex_idx(vertex2)
            for j, el in enumerate(self.lst_nei[idx_v1]):
                key, weight = el  # tuple unpacking klucz i waga wierzchołka
                if key == idx_v2:
                    self.lst_nei[idx_v1].pop(j)

    def neighbours(self, vertex_idx):
        return self.lst_nei[vertex_idx]

    # zakładamy graf skierowany
    def size(self):
        how_many_edges = 0
        for idx in self.lst_nei.keys():
            how_many_edges += len(self.lst_nei[idx])

        return how_many_edges

    def edges(self):
        result_lst = []
        for idx in self.lst_nei.keys():
            for w, weight in self.lst_nei[idx]:  # w - klucz, weight - waga krawedzi
                key_v1 = self.get_vertex(idx)
                key_v2 = self.get_vertex(w)
                result_lst.append((key_v1, key_v2, weight))

        return result_lst

    def print_neighbour_list(self):
        print(self.lst_nei)


class AdjacencyMatrix(Graph):

    def __init__(self):
        super().__init__()
        self.matrix = [[]]
        self.edge_weight = [[]]

    def insert_vertex(self, vertex):
        super().insert_vertex(vertex)
        n = len(self.lst)

        if len(self.matrix[0]) == 0:  # mamy 0 wierzchołków
            self.matrix = [[0]]
            self.edge_weight = [[0]]
        else:  # 1 lub więcej wierzchołków
            self.matrix = [[0]*n for _ in range(n)]
            self.edge_weight = [[0]*n for _ in range(n)]

    def insert_edge(self, vertex1, vertex2, edge_weight):
        if vertex1 and vertex2 in self.lst:
            idx1, idx2 = int(self.get_vertex_idx(vertex1)), int(self.get_vertex_idx(vertex2))

            self.matrix[idx1][idx2] = 1
            self.edge_weight[idx1][idx2] = edge_weight
        else:
            return "Podanych wierzchołków nie ma w grafie!"

    def delete_vertex(self, vertex):
        if vertex in self.lst:
            del_idx = self.get_vertex_idx(vertex)
            self.lst.pop(del_idx)
            self.dct = {self.lst[i]: i for i in range(len(self.lst))}  # nowy słownik

            for row in self.matrix:
                row.pop(del_idx)

            for row in self.edge_weight:
                row.pop(del_idx)

            self.matrix.pop(del_idx)
            self.edge_weight.pop(del_idx)

    def delete_edge(self, vertex1, vertex2):
        v1, v2 = int(self.get_vertex_idx(vertex1)), int(self.get_vertex_idx(vertex2))

        self.matrix[v1][v2] = 0
        self.edge_weight[v1][v2] = 0

    # Zwraca indeksy sąsiadów
    def neighbours(self, vertex_idx):
        n, lst = self.order() - 1, []
        if vertex_idx > n or vertex_idx < 0:
            return "Nie ma węzła o takim indeksie"
        else:
            for i, el in enumerate(self.matrix[vertex_idx]):
                if el == 1:
                    lst.append(i)
            return lst

    # Zakładamy graf skierowany
    def size(self):
        how_many_edges = 0
        n = self.order()
        for i in range(n):
            for j in range(n):
                if self.matrix[i][j] == 1:
                    how_many_edges += 1

        return how_many_edges

    # Zwraca parami klucze krawędzi
    def edges(self):
        n, edges = self.order(), []
        for i in range(n):
            for j in range(n):
                if self.matrix[i][j] == 1:
                    key1, key2 = self.get_vertex(i), self.get_vertex(j)
                    edges.append((key1, key2))

        return edges

    def print_adjacency_matrix(self):
        for row in self.matrix:
            print(row)

    def print_weight_of_edges(self):
        for row in self.edge_weight:
            print(row)