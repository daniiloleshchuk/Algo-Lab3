import multimethod


class Graph:

    def __init__(self):
        self.connections = {}

    def create_edges_from_vertexes(self, first_vertex_id: int, second_vertex_id: int, weight: int):
        # create vertex
        self.__create_edge(first_vertex_id, second_vertex_id, weight)
        # create vertex in reverse order
        self.__create_edge(second_vertex_id, first_vertex_id, weight)

    def __create_edge(self, vertex_from, vertex_to, weight):
        # check if vertex not exists already
        if vertex_from in self.connections.keys():
            # check if the connection between these two vertexes not exists already
            if (vertex_to, weight) not in self.connections[vertex_from]:
                # add connection from 'vertex_from' to 'vertex_to with' weight 'weight'
                self.connections[vertex_from].append((vertex_to, weight))
        else:
            self.connections[vertex_from] = [(vertex_to, weight),]

    def print_graph(self):
        for el in self.connections:
            print(el, self.connections[el])

