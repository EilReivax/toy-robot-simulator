from tabletop import Tabletop
from toy_robot import ToyRobot

def read_commands(filename):
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []

def main():
    tabletop = Tabletop(5, 5)
    robot = ToyRobot()

    commands = read_commands("commands.txt")

    for command in commands:
        parts = command.split()
        if not parts:
            continue

        action = parts[0]

        if action == "PLACE" and len(parts) == 2:
            try:
                x, y, facing = parts[1].split(',')
                robot.place(int(x), int(y), facing, tabletop)
            except ValueError:
                print(f"Invalid PLACE command: {command}")
        elif action == "MOVE":
            robot.move(tabletop)
        elif action == "LEFT":
            robot.left()
        elif action == "RIGHT":
            robot.right()
        elif action == "REPORT":
            print(robot.report())

if __name__ == '__main__':
    main()