def find_cycles(graphs, graph_id):
    max_cycle_length = 0
    max_cycle = []
    cycle_count = 0

    for graph in graphs:
        if graph['id'] == graph_id:
            vertices = graph['vertices']
            edges = graph['edges']
            for start_vertex in vertices:
                stack = [[start_vertex, None, []]] 
                visited = set()
                while stack:
                    path = stack.pop()
                    current_vertex = path[0]
                    parent_vertex = path[1]
                    current_path = path[2]
                    current_path.append(current_vertex)
                    if current_vertex in visited:
                        cycle_count += 1
                        if len(current_path) > max_cycle_length:
                            max_cycle_length = len(current_path)
                            max_cycle = current_path
                        break
                    visited.add(current_vertex)
                    for edge in edges:
                        if edge[0] == current_vertex and edge[1] != parent_vertex:
                            stack.append([edge[1], current_vertex, list(current_path)])
                        elif edge[1] == current_vertex and edge[0] != parent_vertex:
                            stack.append([edge[0], current_vertex, list(current_path)])

    print("Number of cycles in graph", graph_id, "is", cycle_count)
    if cycle_count > 0:
        print("Cycle with maximum length:", " -> ".join(max_cycle))
