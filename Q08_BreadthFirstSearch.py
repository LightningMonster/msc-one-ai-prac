# Code by Lightning Monster❤️
"""
Q.8) Write a Python program to implement Breadth First Search algorithm.
Refer the following graph as an Input for the program.
[Initial node = 1, Goal node = 8]
[20 Marks]
"""

from collections import deque

# Undirected graph based on the given diagram
graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6, 7],
    4: [2, 8],
    5: [2, 8],
    6: [3, 8],
    7: [3, 8],
    8: [4, 5, 6, 7]
}

def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])  # store paths instead of single nodes

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            visited.add(node)

            # Goal found
            if node == goal:
                return path

            # Add unvisited neighbors
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
