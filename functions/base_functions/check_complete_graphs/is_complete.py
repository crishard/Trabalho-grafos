# função auxiliar
def is_complete(vertices, edges):
    if not vertices:
        return False
    max_edges = len(vertices) * (len(vertices) - 1) // 2
    return len(edges) == max_edges