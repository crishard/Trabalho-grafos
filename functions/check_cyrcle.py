def check_cycle(self, graph_id, start_vertex):
    for graph in self.graphs:
        if graph['id'] == graph_id:
            vertices = graph['vertices']
            edges = graph['edges']
            stack = [[start_vertex, None, []]]  # Including parent vertex and path to check for cycles
            visited = set()
            while stack:
                path = stack.pop()
                current_vertex = path[0]
                parent_vertex = path[1]
                current_path = path[2]
                current_path.append(current_vertex)
                if current_vertex in visited:
                    print("Cycle found in graph", graph_id)
                    print("Cycle path:", " -> ".join(current_path))
                    return
                visited.add(current_vertex)
                for edge in edges:
                    if edge[0] == current_vertex and edge[1] != parent_vertex:
                        stack.append([edge[1], current_vertex, list(current_path)])
                    elif edge[1] == current_vertex and edge[0] != parent_vertex:
                        stack.append([edge[0], current_vertex, list(current_path)])
    print("No cycle found in graph", graph_id)