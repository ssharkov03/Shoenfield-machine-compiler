import numpy as np


def single_command_parser(command):
    command = command.split(')')[0]  # remove )
    command_number, command_raw = command.split(".")
    command_number = int(command_number)
    command_func, command_params = command_raw.split("(")
    command_params = np.array([int(i) for i in command_params.split(',')], dtype=int)
    return np.array([command_number, command_func, command_params], dtype=object)


def single_register_line_parser(line):
    line_idx, line_data = [int(i) for i in line.split(":")]
    return np.array([line_idx, line_data])


def parse_data(command_file, register_file):
    command_input = open("commandInput", "r")
    register_input = open("registerInput", "r")
    commands = command_input.readlines()
    lines = register_input.readlines()
    commands = np.array([single_command_parser(command) for command in commands], dtype=object)
    register_data = np.array([single_register_line_parser(line) for line in lines], dtype=object)
    return commands, register_data


if __name__ == '__main__':
    print(parse_data('commandInput', 'registerInput'))