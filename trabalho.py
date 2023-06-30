#!/usr/bin/python3

from command_handler import command_handler

import readline
import os
import atexit
from pathlib import Path
# print(Path('C:', '/', 'Users'))

# Configurar histórico do readline
histfile = os.path.join(os.path.expanduser("~"), ".command_history")
try:
    readline.read_history_file(histfile)
    readline.set_history_length(1000)
except FileNotFoundError:
    pass
atexit.register(readline.write_history_file, histfile)


class GraphTool:
    def __init__(self):
        self.graphs = []

    def run_command(self, command):
        self.graphs = command_handler(command, self.graphs)


def main():
    graph_tool = GraphTool()
    while True:
        try:
            user_input = input()
            command = user_input.split()
            graph_tool.run_command(command)
        except EOFError:
            break
        except KeyboardInterrupt:
            print("Program interrupt")
            break

if __name__ == '__main__':
    main()
