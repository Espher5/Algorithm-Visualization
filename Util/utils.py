import networkx as nx
import random


def generateRandomGraph(maxNodes):
    pass


def generateCompleteGraph(nodes):
    G = nx.complete_graph(nodes)
    return G


def generateTree(nodeNumber, edgeNumber):
    n = random.randrange(0, nodeNumber)

    B = nx.Graph()
    B.add_nodes_from([i for i in range(nodeNumber)])

    ''' Add edges from the first subset to the second '''
    for _ in range(edgeNumber):
        source = random.randrange(1, n)
        target = random.randrange(n + 1, nodeNumber)
        B.add_edge(source, target)

    return B



def generateBipartiteGraph(nodeNumber, edgeNumber):
    pass
