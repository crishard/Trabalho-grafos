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

    def run_command(self, command):
        if command[0] == 'grafos':
            if len(command) == 3 and command[1] == 'carregar':
                self.load_graphs_from_file(command[2])
            elif command[1] == 'multigrafos':
                self.check_multigraphs()
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
