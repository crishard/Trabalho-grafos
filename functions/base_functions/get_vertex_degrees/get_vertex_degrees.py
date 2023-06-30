def get_vertex_degrees(graphs, graph_id):
        for graph in graphs:
            if graph['id'] == graph_id:
                vertices = graph['vertices']
                edges = graph['edges']
                degrees = {vertex: 0 for vertex in vertices}
                for edge in edges:
                    degrees[edge[0]] += 1
                    degrees[edge[1]] += 1
                print("Vertex degrees for graph", graph_id)
                for vertex, degree in degrees.items():
                    print("Vertex:", vertex, "Degree:", degree)
                return
        print("Graph not found:", graph_id)