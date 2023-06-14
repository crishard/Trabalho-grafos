def check_pseudographs(graphs):
        pseudographs = []
        for graph in graphs:
            vertices = graph['vertices']
            edges = graph['edges']
            for edge in edges:
                if edge[0] == edge[1] and edge[0] in vertices:
                    pseudographs.append(graph['id'])
                    break
        if pseudographs:
            print("Pseudographs found:", pseudographs)
        else:
            print("No pseudographs found")