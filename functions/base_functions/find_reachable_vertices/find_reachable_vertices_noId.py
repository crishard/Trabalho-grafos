def find_reachable_vertices_noId(graphs, starting_vertex):
    for graph in graphs:
        graph_id = graph['id']
        vertices = graph['vertices']
        edges = graph['edges']
        reachable_vertices = [starting_vertex.strip('"')]
        queue = [starting_vertex]
        while queue:
            current_vertex = queue.pop(0)
            for edge in edges:
                if edge[0] == current_vertex and edge[1] not in reachable_vertices:
                    reachable_vertices.append(edge[1])
                    queue.append(edge[1])
                elif edge[1] == current_vertex and edge[0] not in reachable_vertices:
                    reachable_vertices.append(edge[0])
                    queue.append(edge[0])
        print("Reachable vertices from", starting_vertex, "in graph", graph_id, "are:", reachable_vertices)