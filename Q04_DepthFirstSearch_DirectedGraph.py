"""
Q.2) Write a Python program to implement Depth First Search algorithm.
Refer the following directed graph as an input for the program.
[Initial node = 1, Goal node = 7]
[20 Marks]
"""

# Directed graph represented using adjacency list
graph = {
    1: [2, 3],
    2: [4],
    3: [],
    4: [5, 6],
    5: [3, 7],
    6: [7],
    7: []
}

# Depth First Search function
def dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    # If goal node found
    if start == goal:
        return path

    # Explore neighbors
    for neighbor in graph[start]:
        if neighbor not in visited:
            new_path = dfs(graph, neighbor, goal, visited.copy(), path.copy())
            if new_path:
                return new_path

    return None

# Main program
start_node = 1
goal_node = 7

path = dfs(graph, start_node, goal_node)

if path:
    print("Depth First Search Path:", " → ".join(map(str, path)))
else:
    print("No path found from", start_node, "to", goal_node)
