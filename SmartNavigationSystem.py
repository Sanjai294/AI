import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position  # (row, col)
        self.parent = parent
        self.g = 0  # Cost from start to current
        self.h = 0  # Heuristic (estimated cost from current to end)
        self.f = 0  # Total cost

    def __lt__(self, other):
        return self.f < other.f

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, end):
    open_list = []
    closed_set = set()
    start_node = Node(start)
    end_node = Node(end)

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_set.add(current_node.position)

        if current_node.position == end_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        # Get neighbors
        neighbors = [
            (0, -1), (-1, 0), (0, 1), (1, 0)  # Left, Up, Right, Down
        ]

        for offset in neighbors:
            row = current_node.position[0] + offset[0]
            col = current_node.position[1] + offset[1]
            neighbor_pos = (row, col)

            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                continue  # Out of bounds
            if grid[row][col] == 1:
                continue  # Obstacle
            if neighbor_pos in closed_set:
                continue

            neighbor_node = Node(neighbor_pos, current_node)
            neighbor_node.g = current_node.g + 1
            neighbor_node.h = heuristic(neighbor_pos, end_node.position)
            neighbor_node.f = neighbor_node.g + neighbor_node.h

            # If node with same position is already in open list with lower f, skip
            if any(open_node.position == neighbor_node.position and open_node.f <= neighbor_node.f for open_node in open_list):
                continue

            heapq.heappush(open_list, neighbor_node)

    return None  # No path found

def print_grid_with_path(grid, path):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) in path:
                print("●", end=" ")
            elif grid[row][col] == 1:
                print("█", end=" ")
            else:
                print(".", end=" ")
        print()

# Example usage
if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)
    end = (4, 4)

    path = astar(grid, start, end)

    if path:
        print("Found path:")
        print(path)
        print_grid_with_path(grid, path)
    else:
        print("No path found.")
