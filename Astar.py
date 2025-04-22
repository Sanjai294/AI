import heapq

class Graph:
    def __init__(self):
        self.vertices = {}
        self.positions = {}

    def add_vertex(self, name, neighbors):
        self.vertices[name] = neighbors
        self.positions[name] = neighbors[name] if name in neighbors else (0, 0)

    def heuristic(self, start, goal):
        (x1, y1) = self.positions[start]
        (x2, y2) = self.positions[goal]
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    def a_star(self, start, goal):
        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {vertex: float('inf') for vertex in self.vertices}
        g_score[start] = 0
        f_score = {vertex: float('inf') for vertex in self.vertices}
        f_score[start] = self.heuristic(start, goal)

        while open_set:
            current = heapq.heappop(open_set)[1]

            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                path.reverse()
                return path

            for neighbor in self.vertices[current]:
                tentative_g_score = g_score[current] + self.heuristic(current, neighbor)

                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return None

# Create the graph
graph = Graph()

# Coordinates for each node
coordinates = {
    'A': (0, 0),
    'B': (1, 1),
    'C': (2, 2),
    'D': (3, 3),
    'E': (4, 4),
    'F': (5, 5)
}

# Add all vertices
graph.positions = coordinates  # Assign node positions

graph.add_vertex('A', {'B': coordinates['B'], 'C': coordinates['C']})
graph.add_vertex('B', {'A': coordinates['A'], 'D': coordinates['D'], 'E': coordinates['E']})
graph.add_vertex('C', {'A': coordinates['A'], 'E': coordinates['E']})
graph.add_vertex('D', {'B': coordinates['B'], 'F': coordinates['F']})
graph.add_vertex('E', {'B': coordinates['B'], 'C': coordinates['C'], 'F': coordinates['F']})
graph.add_vertex('F', {'D': coordinates['D'], 'E': coordinates['E']})

# Find the shortest path
start_vertex = 'A'
goal_vertex = 'F'
shortest_path = graph.a_star(start_vertex, goal_vertex)

# Print the result
if shortest_path:
    print(f"Shortest path from {start_vertex} to {goal_vertex}:")
    print(shortest_path)
else:
    print(f"No path found from {start_vertex} to {goal_vertex}.")
