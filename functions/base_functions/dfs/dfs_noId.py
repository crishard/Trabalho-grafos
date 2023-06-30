def dfs_noId(graphs, start_vertex, end_vertex):
    found_paths = False  # Flag para indicar se pelo menos um caminho foi encontrado
    for graph in graphs:
        graph_id = graph['id']
        vertices = graph['vertices']
        edges = graph['edges']
        stack = [[start_vertex]]
        visited = set()
        while stack:
            path = stack.pop()
            current_vertex = path[-1]
            if current_vertex == end_vertex:
                found_paths = True
                print("DFS path from", start_vertex, "to", end_vertex, "in graph", graph_id, "is:", path)
                continue
            if current_vertex in visited:
                continue
            visited.add(current_vertex)
            for edge in edges:
                if edge[0] == current_vertex and edge[1] not in visited:
                    new_path = list(path)
                    new_path.append(edge[1])
                    stack.append(new_path)
                elif edge[1] == current_vertex and edge[0] not in visited:
                    new_path = list(path)
                    new_path.append(edge[0])
                    stack.append(new_path)
    if not found_paths:
        print("No DFS paths found.")
