from graph_representation import AdjacencyList, AdjacencyMatrix
from MST_algorithms import MinimumSpanningTree
import time
import poland


"""Here you can see all results. You can test any function you want in main and 
 uncomment other. Vertexes are the capitals of all voivodeships in Poland and cost are distance
 between them in km."""


# Wizualizacja wierzchołków sąsiadujących ze sobą, bazuje na liście sąsiedztwa
def visualize_poland_voivodeship_by_adjacency_list():
    l1 = AdjacencyList()

    for _, _, vertex in poland.polska:
        l1.insert_vertex(vertex)

    for v_start, v_end, _ in poland.graf:
        l1.insert_edge(v_start, v_end, 1)

    all_edges_from_lst = l1.edges()
    poland.draw_map(all_edges_from_lst)


# Wizualizacja wierzchołków sąsiadujących ze sobą, bazuje na macierzy sąsiedztwa
def visualize_poland_voivodeship_by_adjacency_matrix():
    m1 = AdjacencyMatrix()

    for _, _, vertex in poland.polska:
        m1.insert_vertex(vertex)

    for v_start, v_end, _ in poland.graf:
        m1.insert_edge(v_start, v_end, 1)

    all_edges_from_matrix = m1.edges()
    poland.draw_map(all_edges_from_matrix)


def mst_prime_for_poland_voivodeships():
    p = MinimumSpanningTree()

    for _, _, vertex in poland.polska:
        p.insert_vertex(vertex)

    for v_start, v_end, weight in poland.graf:
        p.insert_edge(v_start, v_end, weight)

    all_edges = p.edges()

    t_start = time.perf_counter()
    mst_edges, cost = p.prime_algorithm('Z')
    t_stop = time.perf_counter()

    # Pomocnicze informacje do wypisania w lewym dolnym rogu
    mst_info = ['Prime algorithm', f'{(t_stop - t_start):.7f}', cost]

    poland.draw_map(all_edges, 'red', mst_edges, mst_info)


def mst_kruskal_for_poland_voivodeships():
    p = MinimumSpanningTree()

    for _, _, vertex in poland.polska:
        p.insert_vertex(vertex)

    for v_start, v_end, weight in poland.graf:
        p.insert_edge(v_start, v_end, weight)

    all_edges = p.edges()
    t_start = time.perf_counter()
    mst_edges, cost = p.kruskal_algorithm()
    t_stop = time.perf_counter()

    mst_info = ['Kruskal algorithm', f'{(t_stop - t_start):.7f}', cost]
    poland.draw_map(all_edges, 'red', mst_edges, mst_info)


def main():
    # visualize_poland_voivodeship_by_adjacency_list()
    # visualize_poland_voivodeship_by_adjacency_matrix()
    # mst_prime_for_poland_voivodeships()
    mst_kruskal_for_poland_voivodeships()


if __name__ == '__main__':
    main()