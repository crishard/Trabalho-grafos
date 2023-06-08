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


def main():
    graph_tool = GraphTool()

if __name__ == '__main__':
    main()
