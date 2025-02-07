class CommandProcessor:
    def __init__(self, tabletop, robot):
        self.tabletop = tabletop
        self.robot = robot

    def process_commands(self, lines):
        for line in lines:
            command = line.split()
            if not command or not self.robot.is_placed:
                continue

            action = command[0]

            if action == "PLACE":
                try:
                    x, y, facing = command[1].split(',')
                    self.robot.place(int(x), int(y), facing, self.tabletop)
                except ValueError:
                    print(f"Invalid command: '{line}'")
                    break
            elif action == "MOVE":
                self.robot.move(self.tabletop)
            elif action == "LEFT":
                self.robot.left()
            elif action == "RIGHT":
                self.robot.right()
            elif action == "REPORT":
                print(self.robot.report())