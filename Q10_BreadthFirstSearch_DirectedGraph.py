# Code by Lightning Monster❤️
"""
Q.10) Write a Python program to implement Breadth First Search (BFS) algorithm.
Refer the following directed graph as an Input for the program.
[Initial node = 1, Goal node = 8]
[20 Marks]
"""

from collections import deque

# Directed graph based on the given diagram
graph = {
    1: [2, 4],
    2: [3],
    3: [2, 5, 6],
    4: [3],
    5: [7, 8],
    6: [8],
    7: [],
    8: []
}

def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])  # store paths instead of single nodes

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            visited.add(node)

            # If goal is found, return path
            if node == goal:
                return path

            # Explore all directed neighbors
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None


# --- Main Program ---
start_node = 1
goal_node = 8

path = bfs(graph, start_node, goal_node)

if path:
    print("Breadth First Search Path:", " → ".join(map(str, path)))
else:
    print("No path found from", start_node, "to", goal_node)
