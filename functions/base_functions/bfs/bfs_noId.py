def bfs_noId(graphs, start_vertex, end_vertex):
    for graph in graphs:
        graph_id = graph['id']
        vertices = graph['vertices']
        edges = graph['edges']
        queue = [[start_vertex]]
        visited = set()
        found_path = None
        while queue:
            path = queue.pop(0)
            current_vertex = path[-1]
            if current_vertex == end_vertex:
                found_path = path
                break
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
        if found_path:
            print("BFS path in graph", graph_id)
            print("Path:", found_path)
        else:
            print("No BFS path found in graph", graph_id)

    print("End of BFS search")
