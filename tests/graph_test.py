import unittest

from logic.Graph import Graph


class GraphTest(unittest.TestCase):

    def setUp(self) -> None:

        self.firstGraph = Graph()

        self.firstGraph.create_edges_from_vertexes(1, 3, 10)
        self.firstGraph.create_edges_from_vertexes(3, 4, 80)
        self.firstGraph.create_edges_from_vertexes(4, 5, 50)
        self.firstGraph.create_edges_from_vertexes(5, 6, 20)
        self.firstGraph.create_edges_from_vertexes(2, 3, 40)
        self.firstGraph.create_edges_from_vertexes(2, 4, 100)


        self.secondGraph = Graph()

        self.secondGraph.create_edges_from_vertexes(1, 2, 20)
        self.secondGraph.create_edges_from_vertexes(2, 3, 20)
        self.secondGraph.create_edges_from_vertexes(3, 6, 20)
        self.secondGraph.create_edges_from_vertexes(6, 9, 20)
        self.secondGraph.create_edges_from_vertexes(9, 8, 20)
        self.secondGraph.create_edges_from_vertexes(8, 7, 20)
        self.secondGraph.create_edges_from_vertexes(7, 4, 20)
        self.secondGraph.create_edges_from_vertexes(4, 1, 20)
        self.secondGraph.create_edges_from_vertexes(5, 2, 10)
        self.secondGraph.create_edges_from_vertexes(5, 4, 10)
        self.secondGraph.create_edges_from_vertexes(5, 6, 10)
        self.secondGraph.create_edges_from_vertexes(5, 8, 10)


        self.thirdGraph = Graph()

        self.thirdGraph.create_edges_from_vertexes(1, 2, 50)
        self.thirdGraph.create_edges_from_vertexes(2, 3, 1000000000)

