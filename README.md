# Toy Robot Simulator

## Overview

The Toy Robot Simulator is a command-line application that simulates the movement of a toy robot on a 5x5 tabletop. The robot follows a set of commands while ensuring it does not fall off the table.

## Features

- The robot can be placed on a 5x5 grid.
- The robot moves one step forward in its current direction.
- The robot can rotate left or right by 90 degrees.
- The robot reports its current position and facing direction.
- All commands issued before a valid `PLACE` command are ignored.
- The robot does not move beyond the table boundaries.

## Commands

The application processes the following commands:

```
PLACE X,Y,FACING
MOVE
LEFT
RIGHT
REPORT
```

- `PLACE X,Y,FACING` - Places the robot at coordinates (X,Y) facing `NORTH`, `EAST`, `SOUTH`, or `WEST`.
- `MOVE` - Moves the robot one unit in the direction it is facing.
- `LEFT` - Rotates the robot 90 degrees counterclockwise.
- `RIGHT` - Rotates the robot 90 degrees clockwise.
- `REPORT` - Outputs the robot's current X, Y, and FACING direction.

## Example Input & Output

### **Example 1:**

```
PLACE 0,0,NORTH
MOVE
REPORT
```

**Output:**

```
0,1,NORTH
```

### **Example 2:**

```
PLACE 0,0,NORTH
LEFT
REPORT
```

**Output:**

```
0,0,WEST
```

### **Example 3:**

```
PLACE 1,2,EAST
MOVE
MOVE
LEFT
MOVE
REPORT
```

**Output:**

```
3,3,NORTH
```

## Installation & Setup

### **Requirements:**

- Python 3.9+

## Running the Application

Run the simulator using:

```sh
python main.py
```

This reads commands from `commands.txt` and executes them.

## Running Tests

Unit tests are provided in the `tests/` directory. To run all tests:

```sh
python -m unittest discover tests
```

To run a specific test file:

```sh
python -m unittest tests/test_robot.py
```

## Future Enhancements

- Interactive command-line mode.
- GUI visualization of the robot's movement.
- Ability to load/save robot positions.

## License

This project is licensed under the MIT License.
