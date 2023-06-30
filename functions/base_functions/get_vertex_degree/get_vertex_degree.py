def get_vertex_degree(graphs, graph_id, vertex):
        for graph in graphs:
            if graph['id'] == graph_id:
                edges = graph['edges']
                degree = 0
                for edge in edges:
                    if edge[0] == vertex:
                        degree += 1
                    if edge[1] == vertex:
                        degree += 1
                print("Degree of vertex", vertex, "in graph", graph_id, "is", degree)
                return
        print("Graph not found:", graph_id)