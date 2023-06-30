from functions.base.check_complete_graphs.is_complete import is_complete

def check_complete_graphs(graphs):
    complete_graphs = []
    for graph in graphs:
        vertices = graph['vertices']
        edges = graph['edges']
        if is_complete(vertices, edges):
            complete_graphs.append(graph['id'])
    if complete_graphs:
        print("Complete graphs found:", complete_graphs)
    else:
        print("No complete graphs found")
