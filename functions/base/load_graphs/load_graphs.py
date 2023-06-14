import json

def load_graphs_from_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            graphs = data['graphs']
            print("Graphs loaded successfully from", filename)
            return graphs
    except FileNotFoundError:
        print("File not found:", filename)
        return None
