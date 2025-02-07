from tabletop import Tabletop
from robot import Robot
from command_processor import CommandProcessor


def read_file(filename):
    """
    Read commands from a file and return them as a list of strings.

    Args:
    filename (str): The name of the file to read.

    Returns:
    list: A list of command strings, with whitespace stripped.
    """
    try:
        with open(filename) as file:
            # Read all lines, strip whitespace, and return as a list
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        # Handle the case where the file is not found
        print(f"Error: File '{filename}' was not found.")
        return []

def main():
    # Create a 5x5 tabletop, robot, and command processor
    tabletop = Tabletop(5, 5)
    robot = Robot()
    processor = CommandProcessor(tabletop, robot)

    # Read commands from the file and process them
    lines = read_file("commands.txt")
    processor.process_commands(lines)

if __name__ == '__main__':
    main()