from functions.base.check_disconnected_graphs.is_connected import is_connected

def check_disconnected_graphs(graphs):
        disconnected_graphs = []
        for graph in graphs:
            vertices = graph['vertices']
            edges = graph['edges']
            if not is_connected(vertices, edges):
                disconnected_graphs.append(graph['id'])
        if disconnected_graphs:
            print("Disconnected graphs found:", disconnected_graphs)
        else:
            print("No disconnected graphs found")