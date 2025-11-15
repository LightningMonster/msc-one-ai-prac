# Code by Lightning Monster❤️
"""
Q.12) Write a Python program to implement Breadth First Search algorithm.
Refer the following graph as an Input for the program.
[Initial node = 1, Goal node = 7]
[20 Marks]
"""

from collections import deque

# Undirected graph based on the given diagram
graph = {
    1: [2, 3, 4],
    2: [1, 4, 5],
    3: [1, 4],
    4: [1, 2, 3, 7],
    5: [2, 6, 7],
    6: [5, 7],
    7: [4, 5, 6]
}

def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])  # store complete paths

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            visited.add(node)

            # If goal node found, return the path
            if node == goal:
                return path

            # Add unvisited neighbors to queue
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None


# --- Main Program ---
start_node = 1
goal_node = 7

path = bfs(graph, start_node, goal_node)

if path:
    print("Breadth First Search Path:", " → ".join(map(str, path)))
else:
    print("No path found from", start_node, "to", goal_node)
