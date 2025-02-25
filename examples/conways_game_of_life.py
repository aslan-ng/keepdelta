"""
In this example, the difference of saving the state of simulation at each step is compared to saving only the deltas plus the initial state.
The simulation is simple implementation of Conway’s Game of Life.
"""


class Model:

    def __init__(self, grid_size: int = 10):
        self.grid_size = grid_size
        self.grid = [
            [0 for _ in range(self.grid_size)] for _ in range(self.grid_size)
        ]  # Grid world, 0 represents dead cells.

    def add(self, i: int, j: int):
        """
        Add live cell to the grid
        """
        self.grid[i][j] = 1

    def count_neighbors(self, x, y):
        """
        Count the number of live neighbors around a given cell.
        """
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),  # Above
            (0, -1),
            (0, 1),  # Left and Right
            (1, -1),
            (1, 0),
            (1, 1),  # Below
        ]
        count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < self.grid_size and 0 <= ny < self.grid_size
            ):  # Check boundaries
                count += self.grid[nx][ny]
        return count

    def update(self):
        """
        Update the grid to the next generation.
        """
        new_grid = [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                alive_neighbors = self.count_neighbors(x, y)
                if self.grid[x][y] == 1:  # Live cell
                    if alive_neighbors in [2, 3]:
                        new_grid[x][y] = 1  # Survives
                else:  # Dead cell
                    if alive_neighbors == 3:
                        new_grid[x][y] = 1  # Becomes alive
        self.grid = new_grid

    def show(self):
        """
        Print the current grid to the console.
        """
        for row in self.grid:
            print("".join(str(cell) for cell in row))
        print()

    def serialize(self) -> dict:
        """
        Export the current state of the model
        """
        return {
            "grid": self.grid,
            "grid_size": self.grid_size,
        }

    def deserialzie(self, data: dict):
        """
        Load the state of model
        """
        self.grid = data["grid"]
        self.grid_size = data["grid_size"]


if __name__ == "__main__":

    import sys
    import keepdelta as kd

    # Initialize the model
    model = Model(grid_size=30)

    # Add initial live cells (Glider pattern)
    initial_live_cells = [(1, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
    for i, j in initial_live_cells:
        model.add(i, j)

    old_var = model.serialize()  # Initial state of model

    # This will save the states of the model at each step
    result_states = [old_var]

    # This will save the initial state of the model, and then saves the deltas (changes) of model at each step
    result_deltas = {
        "initial_state": old_var,
        "deltas": [],
    }

    # Run the simulation
    steps = 100
    for _ in range(steps):
        model.update()
        new_var = model.serialize()
        result_states.append(new_var)
        result_deltas["deltas"].append(kd.create(old_var, new_var))
        old_var = new_var

    # Compare their sizes
    size_states = sys.getsizeof(result_states)
    size_deltas = sys.getsizeof(result_deltas)
    print(f">>> Size of saving the results by states: {size_states} bytes")
    print(f">>> Size of saving the results by deltas: {size_deltas} bytes")
    comparison = 100 * (size_states - size_deltas) / size_states
    print(f">>> Saving the results using deltas takes {comparison:.0f}% less space")
