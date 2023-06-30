import sys
from functions.base_functions.load_graphs.load_graphs import load_graphs_from_file
from functions.base_functions.check_multigraphs.check_multigraphs import check_multigraphs
from functions.base_functions.check_pseudographs.cheack_pseudographs import check_pseudographs
from functions.base_functions.check_disconnected_graphs.check_disconnected_graphs import check_disconnected_graphs
from functions.base_functions.check_complete_graphs.check_complete_graphs import check_complete_graphs
from functions.base_functions.get_vertex_degrees.get_vertex_degrees import get_vertex_degrees
from functions.base_functions.get_vertex_degree.get_vertex_degree import get_vertex_degree
from functions.base_functions.find_reachable_vertices.find_reachable_vertices import find_reachable_vertices
from functions.base_functions.find_reachable_vertices.find_reachable_vertices_noId import find_reachable_vertices_noId
from functions.base_functions.find_unreachable_vertices.find_unreachable_vertices import find_unreachable_vertices
from functions.base_functions.find_unreachable_vertices.find_unreachable_vertices_noId import find_unreachable_vertices_noId
from functions.base_functions.bfs.bfs_id import bfs
from functions.base_functions.bfs.bfs_noId import bfs_noId
from functions.base_functions.dfs.dfs_id import dfs
from functions.base_functions.dfs.dfs_noId import dfs_noId

import os
import glob

from functions.add_ons.check_cyrcle import check_cycle
from functions.add_ons.count_connected_vertices import count_connected_vertices
from functions.add_ons.find_cycles import find_cycles

def list_files_and_directories():
    current_directory = os.getcwd()
    directories = []
    files = []

    for entry in os.scandir(current_directory):
        if entry.is_dir():
            directories.append(entry.name)
        elif entry.is_file():
            files.append(entry.name)

    for directory in directories:
        print(directory)
    for file in files:
        print(file)



def clear_terminal():
    # Verifica o sistema operacional
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/Mac
        os.system('clear')

def command_handler(command, graphs):
    if command[0] == 'grafos':
        if len(command) == 3 and command[1] == 'carregar':
            graphs = load_graphs_from_file(command[2])
        elif command[1] == 'multigrafos':
            check_multigraphs(graphs)
        elif command[1] == 'pseudografos':
            check_pseudographs(graphs)
        elif command[1] == 'desconexos':
            check_disconnected_graphs(graphs)
        elif command[1] == 'completos':
            check_complete_graphs(graphs)
        elif command[1] == 'graus' and len(command) == 3:
            graph_id = int(command[2].split('=')[1])
            get_vertex_degrees(graphs, graph_id)
        elif command[1] == 'grau' and len(command) == 4:
            graph_id = int(command[2].split('=')[1])
            vertex = command[3].split('=')[1].strip('"')
            get_vertex_degree(graphs, graph_id, vertex)
        elif command[1] == 'alcancaveis' and len(command) == 4:
            graph_id = int(command[2].split('=')[1])
            starting_vertex = command[3].split('=')[1].strip("'").strip('"')
            find_reachable_vertices(graphs, graph_id, starting_vertex)
        elif command[1] == 'alcancaveis' and len(command) == 3:
            starting_vertex = command[2].split('=')[1].strip("'").strip('"')
            find_reachable_vertices_noId(graphs, starting_vertex)
        elif command[1] == 'inalcancaveis' and len(command) == 4:
            graph_id = int(command[2].split('=')[1])
            starting_vertex = command[3].split('=')[1].strip("'").strip('"')
            find_unreachable_vertices(graphs, graph_id, starting_vertex)
        elif command[1] == 'inalcancaveis' and len(command) == 3:
            starting_vertex = command[2].split('=')[1].strip("'").strip('"')
            find_unreachable_vertices_noId(graphs, starting_vertex)
        elif command[1] == 'bfs' and len(command) == 5:
            graph_id = int(command[2].split('=')[1])
            start_vertex = command[3].split('=')[1].strip('"')
            end_vertex = command[4].split('=')[1].strip('"')
            bfs(graphs, graph_id, start_vertex, end_vertex)
        elif command[1] == 'bfs' and len(command) == 4:
            start_vertex = command[2].split('=')[1].strip('"')
            end_vertex = command[3].split('=')[1].strip('"')
            bfs_noId(graphs, start_vertex, end_vertex)
        elif command[1] == 'dfs' and len(command) == 5:
            graph_id = int(command[2].split('=')[1])
            start_vertex = command[3].split('=')[1].strip('"')
            end_vertex = command[4].split('=')[1].strip('"')
            dfs(graphs, start_vertex, end_vertex)
        elif command[1] == 'dfs' and len(command) == 4:
            start_vertex = command[2].split('=')[1].strip('"')
            end_vertex = command[3].split('=')[1].strip('"')
            dfs_noId(graphs, start_vertex, end_vertex)
        

        # funções extras
        elif command[1] == 'cycles' and len(command) == 4:
            graph_id = int(command[2].split('=')[1])
            starting_vertex = command[3].split('=')[1].strip("'").strip('"')
            check_cycle(graphs, graph_id, starting_vertex)
        elif command[1] == 'strange' and len(command) == 3:
            graph_id = int(command[2].split('=')[1])
            find_cycles(graphs, graph_id)

        elif command[1] == 'connected' and len(command) == 4:
            graph_id = int(command[2].split('=')[1])
            starting_vertex = command[3].split('=')[1].strip("'").strip('"')
            count_connected_vertices(graphs, graph_id, starting_vertex)
        elif command[1] == 'ls':
            list_files_and_directories()
        elif command[1] == 'clear':
            clear_terminal()
        elif command[1] == '--help':
            print("Lista de comandos disponíveis:")
            print("grafos carregar <nome_arquivo>")
            print("grafos multigrafos")
            print("grafos pseudografos")
            print("grafos desconexos")
            print("grafos completos")
            print("grafos graus id=<id>")
            print("grafos grau id=<id> vertice=<vértice>")
            print("grafos alcancaveis id=<id> partida=<vértice>")
            print("grafos inalcancaveis id=<id> partida=<vértice>")
            print("grafos alcancaveis partida=<vértice>")
            print("grafos inalcancaveis partida=<vértice>")
            print("grafos bfs id=<id> partida=<vértice> chegada=<vértice>")
            print("grafos dfs id=<id> partida=<vértice> chegada=<vértice>")
            print("grafos bfs partida=<vértice> chegada=<vértice>")
            print("grafos dfs partida=<vértice> chegada=<vértice>")
            print("grafos sair")
        
        elif command[1] == 'sair':
            sys.exit()
        else:
            print("Invalid command")
    else:
        print("Invalid command")
    return graphs
