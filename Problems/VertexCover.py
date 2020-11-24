import networkx as nx
from itertools import combinations
import matplotlib.pyplot as plt


def brute_force_k_VC(G: nx.Graph, k: int):
    solution = None

    # Checks all of the subsets of 1 to k elements
    for i in range(1, k+1):
        # Gets all the possible combinations of i elements
        subsets = list(combinations(G.nodes, i))

        # Iterates each combination of nodes
        for subset in subsets:
            is_VC = True
            print('Checking if the subset {} is a vertex cover of size {}'.format(subset, i))
            for edge in G.edges:
                if edge[0] not in subset and edge[1] not in subset:
                    is_VC = False
                    print('Edge ({}, {}) is not covered'.format(edge[0], edge[1]))
            if is_VC:
                solution = subset
    return solution


def brute_force_opt_VC(G: nx.Graph, k: int):
    print('Nodes: {}'.format(G.nodes))
    print('Edges: {}'.format(G.edges))
    opt = len(G.nodes)
    solution = set()

    # Checks all of the subsets of 1 to k elements
    for i in range(1, k + 1):
        # Gets all the possible combinations of i elements
        subsets = list(combinations(G.nodes, i))

        # Iterates each combination of nodes
        for subset in subsets:
            is_VC = True
            print('Checking if the subset {} is a vertex cover of size {}'.format(subset, i))
            for edge in G.edges:
                if edge[0] not in subset and edge[1] not in subset:
                    is_VC = False
                    print('Edge ({}, {}) is not covered'.format(edge[0], edge[1]))
            if is_VC and len(subset) < opt:
                solution = subset
                opt = len(subset)
    return solution



def tree_VC(G: nx.Graph, k):
    # Check if the graph is a tree
    pass




def approx_opt_VC(G, k):
    '''
    solution = {}
    tempSet = G.edges
    while tempSet.size != 0:
        pass
    '''


def setup() -> nx.Graph:
    g = nx.Graph()
    g.add_nodes_from(range(1, 10))
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 1)
    g.add_edge(3, 5)
    g.add_edge(5, 6)
    g.add_edge(5, 7)
    g.add_edge(5, 8)
    g.add_edge(5, 9)
    g.add_edge(6, 9)
    return g


if __name__ == '__main__':
    G = setup()
    result = brute_force_k_VC(G, 4)
    print('Result: {}'.format(result))

    pos = nx.spring_layout(G)
    red_vertices = [vertex for vertex in G.nodes if vertex in result]
    blue_vertices = [vertex for vertex in G.nodes if vertex not in red_vertices]

    nx.draw_networkx_nodes(G, pos, nodelist=red_vertices, node_color='r', node_size=500)
    nx.draw_networkx_nodes(G, pos, nodelist=blue_vertices, node_color='b', node_size=500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, arrows=False)
    plt.show()




