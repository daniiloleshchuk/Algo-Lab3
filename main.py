from logic.dejkstra import dejkstra
from logic.get_data import get_data


def main():
    n, m, clients, graph = get_data('in/in1')
    min_max_latency = None
    for vertex_id in graph.connections:
        if vertex_id not in clients:
            current_latencies = dejkstra(graph, vertex_id)
            current_max_latency = max([current_latencies[client] for client in clients])
            if min_max_latency is None:
                min_max_latency = current_max_latency
            elif current_max_latency < min_max_latency:
                min_max_latency = current_max_latency

    return min_max_latency


if __name__ == '__main__':
    print(main())
