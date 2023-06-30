def check_multigraphs(graphs):
    multigraphs = []
    for graph in graphs:
        edges = [tuple(edge) for edge in graph['edges']]
        if len(graph['edges']) != len(set(edges)):
            multigraphs.append(graph['id'])
    if multigraphs:
        print("Multigraphs found id's:", multigraphs)
    else:
        print("No multigraphs found")
