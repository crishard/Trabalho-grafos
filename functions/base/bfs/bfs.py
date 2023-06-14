def bfs(graphs, graph_id, start_vertex, end_vertex):
    for graph in graphs:
        if graph['id'] == graph_id:
            vertices = graph['vertices']
            edges = graph['edges']
            queue = [[start_vertex]]
            visited = set()
            while queue:
                path = queue.pop(0)
                current_vertex = path[-1]
                if current_vertex == end_vertex:
                    print("BFS path from", start_vertex, "to",
                            end_vertex, "in graph", graph_id, "is:", path)
                    return
                if current_vertex in visited:
                    continue
                visited.add(current_vertex)
                for edge in edges:
                    if edge[0] == current_vertex and edge[1] not in visited:
                        new_path = list(path)
                        new_path.append(edge[1])
                        queue.append(new_path)
                    elif edge[1] == current_vertex and edge[0] not in visited:
                        new_path = list(path)
                        new_path.append(edge[0])
                        queue.append(new_path)
            print("No BFS path found from", start_vertex,
                    "to", end_vertex, "in graph", graph_id)
            return
    print("Graph not found:", graph_id)