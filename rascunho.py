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


    def run_command(self, command):
        if command[0] == 'grafos':
            if len(command) >= 4 and command[1] == 'dfs':
                try:
                    graph_id = int(command[2].split('=')[1])
                    start_vertex = command[3].split('=')[1].strip('"')
                    end_vertex = command[4].split('=')[1].strip('"')
                    self.dfs(graph_id, start_vertex, end_vertex)
                except (ValueError, IndexError):
                    print("Invalid command")
            elif len(command) >= 3 and command[1] == 'conectados':
                try:
                    graph_id = int(command[2].split('=')[1])
                    start_vertex = command[3].split('=')[1].strip('"')
                    self.count_connected_vertices(graph_id, start_vertex)
                except (ValueError, IndexError):
                    print("Invalid command")
            elif len(command) >= 3 and command[1] == 'ciclo':
                try:
                    graph_id = int(command[2].split('=')[1])
                    start_vertex = command[3].split('=')[1].strip('"')
                    self.check_cycle(graph_id, start_vertex)
                except (ValueError, IndexError):
                    print("Invalid command")
            elif len(command) == 3 and command[1] == 'ciclos':
                try:
                    graph_id = int(command[2].split('=')[1])
                    self.find_cycles(graph_id)
                except (ValueError, IndexError):
                    print("Invalid command")
            elif len(command) == 3 and command[1] == 'carregar':
                self.load_graphs_from_file(command[2])
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
