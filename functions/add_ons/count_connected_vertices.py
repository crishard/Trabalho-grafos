def count_connected_vertices(graphs, graph_id, start_vertex):
        for graph in graphs:
            if graph['id'] == graph_id:
                vertices = graph['vertices']
                edges = graph['edges']
                queue = [start_vertex]
                visited = set()
                while queue:
                    current_vertex = queue.pop(0)
                    if current_vertex in visited:
                        continue
                    visited.add(current_vertex)
                    for edge in edges:
                        if edge[0] == current_vertex and edge[1] not in visited:
                            queue.append(edge[1])
                        elif edge[1] == current_vertex and edge[0] not in visited:
                            queue.append(edge[0])
                print("Number of connected vertices from", start_vertex, "in graph", graph_id, "is:", len(visited))
                return
        print("Graph not found:", graph_id)