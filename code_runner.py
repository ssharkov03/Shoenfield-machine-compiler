from parser import parse_data
import numpy as np


def initialize_register_and_commands(commands, register_data):
    pass


def run_code(command_file, register_file):
    commands, register_data = parse_data(command_file, register_file)
    initialize_register_and_commands(commands, register_data)


if __name__ == '__main__':
    run_code('commandInput', 'registerInput')