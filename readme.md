# StoreKeeperGame

This project implements a Python algorithm to solve the StoreKeeperGame, a puzzle game where the player controls a character to push boxes to designated target locations.

**Purpose**

The purpose of this project is to provide a fun and challenging game that exercises problem-solving and logical thinking skills.

**Contents**

This repository contains a Python script `store_keeper_game.py` that implements the solution to the StoreKeeperGame puzzle. The main components of the script include:

- `Solution` class: Implements the algorithm to solve the StoreKeeperGame puzzle.
- `minPushBox` method: Finds the minimum number of pushes required to solve the puzzle.
- Example usage: Demonstrates how to use the `Solution` class to solve a specific instance of the StoreKeeperGame.

**Usage**

To use the StoreKeeperGame solver, follow these steps:

1. Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/).

2. Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/store-keeper-game.git
```

3. Navigate to the directory containing the Python script:

```bash
cd store-keeper-game
```

4. Open the `store_keeper_game.py` file in your preferred code editor to explore the implementation of the StoreKeeperGame solver.

5. Execute the Python script to solve a specific instance of the StoreKeeperGame puzzle:

```bash
python store_keeper_game.py
```

This will run the solver and print the minimum number of pushes required to solve the puzzle for the given instance.

**Example**

```python
# Example usage of the StoreKeeperGame solver
grid = [
    ["#", "#", "#", "#", "#", "#"],
    ["#", "T", "#", "#", "T#", "#"],
    ["#", ".", ".", "B", ".", "#"],
    ["#", ".", "#", "#", ".", "#"],
    ["#", ".", ".", ".", "S", "#"],
    ["#", "#", "#", "#", "#", "#"]
]

sol = Solution()
print(sol.minPushBox(grid))  # Expected output: 3
```

This example demonstrates how to use the `Solution` class to find the minimum number of pushes required to solve the StoreKeeperGame puzzle for a specific grid configuration.

Feel free to explore and modify the code to create your own instances of the StoreKeeperGame puzzle or integrate the solver into larger projects as needed.

**Disclaimer**

This project was created for educational and entertainment purposes and may not represent the most optimized or efficient solution for solving the StoreKeeperGame puzzle.