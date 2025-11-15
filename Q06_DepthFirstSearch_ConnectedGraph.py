# Code by Lightning Monster❤️
"""
Q.2) Write a Python program to implement Depth First Search algorithm.
Refer the following graph as an Input for the program.
[Initial node = 2, Goal node = 7]
[20 Marks]
"""

# Undirected graph based on the given diagram (no 4–5 connection)
graph = {
    1: [2, 3, 4],
    2: [1, 4, 5],
    3: [1, 4],
    4: [1, 2, 3, 7],
    5: [2, 6, 7],
    6: [5, 7],
    7: [4, 5, 6]
}

def dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    # Goal found
    if start == goal:
        return path

    # Explore unvisited neighbors
    for neighbor in graph[start]:
        if neighbor not in visited:
            new_path = dfs(graph, neighbor, goal, visited.copy(), path.copy())
            if new_path:
                return new_path

    return None


# --- Main ---
start_node = 2
goal_node = 7

path = dfs(graph, start_node, goal_node)

if path:
    print("Depth First Search Path:", " → ".join(map(str, path)))
else:
    print("No path found from", start_node, "to", goal_node)
