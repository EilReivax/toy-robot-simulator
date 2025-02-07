from tabletop import Tabletop
from robot import Robot
from command_processor import CommandProcessor

def read_file(filename):
    try:
        with open(filename) as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: File '{filename}' was not found.")
        return []

def main():
    tabletop = Tabletop(5, 5)
    robot = Robot()
    processor = CommandProcessor(tabletop, robot)

    lines = read_file("commands.txt")
    processor.process_commands(lines)

if __name__ == '__main__':
    main()