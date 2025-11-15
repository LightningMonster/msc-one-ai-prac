"""
Q.2) Write a Python program to implement Depth First Search algorithm. 
Refer the following graph as an Input for the program. 
[Initial node = 1, Goal node = 8]
[20 Marks]
"""

# Define the graph using adjacency list representation
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [8],
    5: [8],
    6: [8],
    7: [8],
    8: []
}

# Depth First Search function
def dfs(graph, start, goal, path=None, visited=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    
    path.append(start)
    visited.add(start)
    
    # If goal node found
    if start == goal:
        return path
    
    # Recursive search through neighbors
    for neighbor in graph[start]:
        if neighbor not in visited:
            new_path = dfs(graph, neighbor, goal, path.copy(), visited.copy())
            if new_path:
                return new_path

    return None

# Main program
start_node = 1
goal_node = 8

path = dfs(graph, start_node, goal_node)

if path:
    print("Depth First Search Path:", " → ".join(map(str, path)))
else:
    print("No path found from", start_node, "to", goal_node)
