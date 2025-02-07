class CommandProcessor:
    def __init__(self, tabletop, robot):
        # Initialize the CommandProcessor with a tabletop and a robot
        self.tabletop = tabletop
        self.robot = robot

    def process_commands(self, lines):
        # Process each line of commands and split
        for line in lines:
            command = line.split()

            # Skip empty lines or commands if the robot is not placed
            if not command or not self.robot.is_placed:
                continue

            # Get the action (first word of the command)
            action = command[0]

            # Process different types of commands
            if action == "PLACE":
                try:
                    x, y, facing = command[1].split(',')
                    self.robot.place(int(x), int(y), facing, self.tabletop)
                except ValueError:
                    # If parsing fails, print an error message and stop processing
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