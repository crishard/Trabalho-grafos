import json
import sys

class GraphTool:
    def __init__(self):
        self.graphs = []

    def load_graphs_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.graphs = data['graphs']
                print("Graphs loaded successfully from", filename)
        except FileNotFoundError:
            print("File not found:", filename)

    def check_multigraphs(self):
        multigraphs = []
        for graph in self.graphs:
            edges = [tuple(edge) for edge in graph['edges']]
            if len(graph['edges']) != len(set(edges)):
                multigraphs.append(graph['id'])
        if multigraphs:
            print("Multigraphs found id's:", multigraphs)
        else:
            print("No multigraphs found")
    
    def check_pseudographs(self):
        pseudographs = []
        for graph in self.graphs:
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

    def check_disconnected_graphs(self):
        disconnected_graphs = []
        for graph in self.graphs:
            vertices = graph['vertices']
            edges = graph['edges']
            if not self.is_connected(vertices, edges):
                disconnected_graphs.append(graph['id'])
        if disconnected_graphs:
            print("Disconnected graphs found:", disconnected_graphs)
        else:
            print("No disconnected graphs found")

    def check_complete_graphs(self):
        complete_graphs = []
        for graph in self.graphs:
            vertices = graph['vertices']
            edges = graph['edges']
            if self.is_complete(vertices, edges):
                complete_graphs.append(graph['id'])
        if complete_graphs:
            print("Complete graphs found:", complete_graphs)
        else:
            print("No complete graphs found")

    def get_vertex_degrees(self, graph_id):
        for graph in self.graphs:
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

    
    def get_vertex_degree(self, graph_id, vertex):
        for graph in self.graphs:
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

    def find_reachable_vertices(self, graph_id, starting_vertex):
        for graph in self.graphs:
            if graph['id'] == graph_id:
                vertices = graph['vertices']
                edges = graph['edges']
                reachable_vertices = [starting_vertex.strip('"')]
                queue = [starting_vertex]
                while queue:
                    current_vertex = queue.pop(0)
                    for edge in edges:
                        if edge[0] == current_vertex and edge[1] not in reachable_vertices:
                            reachable_vertices.append(edge[1])
                            queue.append(edge[1])
                        elif edge[1] == current_vertex and edge[0] not in reachable_vertices:
                            reachable_vertices.append(edge[0])
                            queue.append(edge[0])
                print("Reachable vertices from", starting_vertex, "in graph", graph_id, "are:", reachable_vertices)
                return
        print("Graph not found:", graph_id)

    # função com bug
    def find_unreachable_vertices(self, graph_id, starting_vertex):
        for graph in self.graphs:
            if graph['id'] == graph_id:
                vertices = graph['vertices']
                edges = graph['edges']
                reachable_vertices = [starting_vertex]
                queue = [starting_vertex]
                while queue:
                    current_vertex = queue.pop(0)
                    for edge in edges:
                        if edge[0] == current_vertex and edge[1] not in reachable_vertices:
                            reachable_vertices.append(edge[1])
                            queue.append(edge[1])
                        elif edge[1] == current_vertex and edge[0] not in reachable_vertices:
                            reachable_vertices.append(edge[0])
                            queue.append(edge[0])
                unreachable_vertices = [vertex for vertex in vertices if vertex not in reachable_vertices]
                print("Unreachable vertices from", starting_vertex, "in graph", graph_id, "are:", unreachable_vertices)
                return
        print("Graph not found:", graph_id)


    # função auxiliar
    def is_connected(self, vertices, edges):
        if not vertices:
            return False
        reachable_vertices = set()
        queue = [vertices[0]]
        while queue:
            current_vertex = queue.pop(0)
            reachable_vertices.add(current_vertex)
            for edge in edges:
                if edge[0] == current_vertex and edge[1] not in reachable_vertices:
                    reachable_vertices.add(edge[1])
                    queue.append(edge[1])
                elif edge[1] == current_vertex and edge[0] not in reachable_vertices:
                    reachable_vertices.add(edge[0])
                    queue.append(edge[0])
        return len(reachable_vertices) == len(vertices)

    # função auxiliar
    def is_complete(self, vertices, edges):
        if not vertices:
            return False
        max_edges = len(vertices) * (len(vertices) - 1) // 2
        return len(edges) == max_edges

    def run_command(self, command):
        if command[0] == 'grafos':
            if len(command) == 3 and command[1] == 'carregar':
                self.load_graphs_from_file(command[2])
            elif command[1] == 'multigrafos':
                self.check_multigraphs()
            elif command[1] == 'pseudografos':
                self.check_pseudographs()
            elif command[1] == 'desconexos':
                self.check_disconnected_graphs()
            elif command[1] == 'completos':
                self.check_complete_graphs()
            elif command[1] == 'graus' and len(command) == 3:
                graph_id = int(command[2].split('=')[1])
                self.get_vertex_degrees(graph_id)
            elif command[1] == 'grau' and len(command) == 4:
                graph_id = int(command[2].split('=')[1])
                vertex = command[3].split('=')[1].strip('"')
                self.get_vertex_degree(graph_id, vertex)
            elif command[1] == 'alcancaveis' and len(command) == 4:
                graph_id = int(command[2].split('=')[1])
                starting_vertex = command[3].split('=')[1].strip("'").strip('"')
                self.find_reachable_vertices(graph_id, starting_vertex)
            elif command[1] == 'sair':
                sys.exit()
            else:
                print("Invalid command")
        else:
            print("Invalid command")

def main():
    graph_tool = GraphTool()
    while True:
        user_input = input("Enter a command: ")
        command = user_input.split()
        graph_tool.run_command(command)

if __name__ == '__main__':
    main()
