#!/usr/bin/env python3

from command_handler import command_handler

class GraphTool:
    def __init__(self):
        self.graphs = []

    def run_command(self, command):
        self.graphs = command_handler(command, self.graphs)


def main():
    graph_tool = GraphTool()
    while True:
        user_input = input()
        command = user_input.split()
        graph_tool.run_command(command)

if __name__ == '__main__':
    main()
