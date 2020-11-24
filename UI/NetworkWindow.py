import sys
from PyQt5.QtWidgets import (QApplication, QPushButton, QLabel,
                             QVBoxLayout, QHBoxLayout, QDialog,
                             QTextEdit, QInputDialog, QLineEdit)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import networkx as nx

from Problems import VertexCover
from Util import utils


''' Generic network class '''
class NetworkWindow(QDialog):
    _X = 50
    _Y = 50
    _W = 1920
    _H = 1080

    _nodes = 0
    _edges = 0

    def __init__(self, title='Graph Problem'):
        super().__init__()
        self.setWindowTitle(title)
        self._title = title
        self._info = ''
        self.setGeometry(self._X, self._Y, self._W, self._H)

        self.figure = None
        self.canvas = None
        self.initUI()


    ''' UI initialization '''
    def initUI(self):
        mainLayout = QHBoxLayout()
        topButtonLayout = QHBoxLayout()
        bottomButtonLayout = QHBoxLayout()
        verticalLayout = QVBoxLayout()

        graphLabel = QLabel(self)
        graphLabel.setText('Seleziona un tipo di grafo su cui eseguire l\'algoritmo')
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        randomGraphButton = QPushButton('Random graph')
        completeGraphButton = QPushButton('Complete graph')
        treeGraphButton = QPushButton('Tree')
        bipartiteGraphButton = QPushButton('Bipartite graph')
        randomGraphButton.clicked.connect(lambda: self.generateGraph(randomGraphButton.text()))
        completeGraphButton.clicked.connect(lambda: self.generateGraph(completeGraphButton.text()))
        treeGraphButton.clicked.connect(lambda: self.generateGraph(treeGraphButton.text()))
        bipartiteGraphButton.clicked.connect(lambda: self.generateGraph(bipartiteGraphButton.text()))


        ''' Solution methods setup '''
        if self._title == 'VertexCover':
            bruteForceButton = QPushButton('Brute force')
            approxButton = QPushButton('Approx solution')

            bottomButtonLayout.addWidget(bruteForceButton)
            bottomButtonLayout.addWidget(approxButton)
        else:
            bruteForceButton = QPushButton('Brute force')
            approxButton = QPushButton('Approx solution')

            bottomButtonLayout.addWidget(bruteForceButton)
            bottomButtonLayout.addWidget(approxButton)

        topButtonLayout.addWidget(randomGraphButton)
        topButtonLayout.addWidget(completeGraphButton)
        topButtonLayout.addWidget(treeGraphButton)
        topButtonLayout.addWidget(bipartiteGraphButton)

        verticalLayout.addWidget(graphLabel)
        verticalLayout.addLayout(topButtonLayout)
        verticalLayout.addWidget(self.canvas, 3)
        verticalLayout.addLayout(bottomButtonLayout)

        consoleArea = QTextEdit('')
        consoleArea.setReadOnly(True)
        mainLayout.addLayout(verticalLayout, 3)
        mainLayout.addWidget(consoleArea, 1)
        self.setLayout(mainLayout)


    def plot(self, G):
        self.figure.clear()
        '''
        result = VertexCover.brute_force_k_VC(G, 4)
        print('Result: {}'.format(result))
        
        pos = nx.spring_layout(G)
        red_vertices = [vertex for vertex in G.nodes if vertex in result]
        blue_vertices = [vertex for vertex in G.nodes if vertex not in red_vertices]

        nx.draw_networkx_nodes(G, pos, nodelist=red_vertices, node_color='r', node_size=500)
        nx.draw_networkx_nodes(G, pos, nodelist=blue_vertices, node_color='b', node_size=500)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edges(G, pos, ax=self.figure.add_subplot(111), arrows=False)
        
        self.canvas.draw()
        '''
        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos, nodelist=G.edges, node_color='b', node_size=500)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edges(G, pos, ax=self.figure.add_subplot(111), arrows=False)

        self.canvas.draw()

    def generateGraph(self, graphType):
        G = None
        if graphType == 'Random graph':
            pass
        else:
            nodes, ok = QInputDialog.getInt(self, 'Get integer', 'Number of nodes:', 5, 0, 100, 1)
            if graphType == 'Complete graph':
                G = utils.generateCompleteGraph(nodes)
            else:
                edges, ok = QInputDialog.getInt(self, 'Get integer', 'Number of edges:', 0, 0, 100, 1)
                if graphType == 'Tree':
                    G = utils.generateTree(nodes, edges)
                elif graphType == 'Bipartite graph':
                    G = utils.generateBipartiteGraph(nodes, edges)
        k = QInputDialog.getInt(self, 'Get integer', 'k:', 5, 0, 100, 1)
        self.plot(G)



    def executeStep(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = NetworkWindow()
    window.show()
    sys.exit(app.exec_())

