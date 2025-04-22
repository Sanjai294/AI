class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

    def depth_first_search(self, start, goal):
        visited = set()
        path = []

        # Recursive DFS function
        def dfs(node):
            visited.add(node)
            path.append(node)

            if node == goal:
                return True

            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True

            path.pop()  # Backtrack if goal not found
            return False

        # Call the recursive DFS function
        if dfs(start):
            return path

        return None


# Create a graph
graph = Graph()
graph.add_edge('A', ['B', 'C'])
graph.add_edge('B', ['D', 'E'])
graph.add_edge('C', ['F'])
graph.add_edge('D', [])
graph.add_edge('E', ['F'])
graph.add_edge('F', [])

# Solve the problem using depth-first search
start_node = 'A'
goal_node = 'F'
solution = graph.depth_first_search(start_node, goal_node)

# Print the solution
if solution:
    print(f"Path from {start_node} to {goal_node}: {solution}")
else:
    print(f"No path found from {start_node} to {goal_node}.")
