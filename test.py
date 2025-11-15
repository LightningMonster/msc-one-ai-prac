import random
import matplotlib.pyplot as plt
import numpy as np

# Function definition
def f(x):
    return -x**2 + 4*x

# Hill Climbing algorithm (stores path for visualization)
def hill_climbing(start_x, step_size=0.1, max_iterations=1000):
    current_x = start_x
    current_value = f(current_x)

    path_x = [current_x]
    path_y = [current_value]

    for i in range(max_iterations):
        new_x = current_x + random.uniform(-step_size, step_size)
        new_value = f(new_x)

        if new_value > current_value:
            current_x = new_x
            current_value = new_value
            path_x.append(current_x)
            path_y.append(current_value)

    return current_x, current_value, path_x, path_y


# --------- RUN ALGORITHM ---------
start_x = random.uniform(0, 4)
best_x, best_value, path_x, path_y = hill_climbing(start_x)

print(f"Starting point: {start_x:.4f}")
print(f"Maximum at x = {best_x:.4f}, f(x) = {best_value:.4f}")

# --------- VISUALIZATION ---------
# Create x range
x_vals = np.linspace(-1, 5, 300)
y_vals = f(x_vals)

plt.figure(figsize=(10, 6))

# Plot the function curve
plt.plot(x_vals, y_vals, label="f(x) = -x² + 4x", linewidth=2)

# Plot the hill climbing path
plt.plot(path_x, path_y, marker='o', linestyle='--', label="Hill Climbing Path")

# Highlight start & end points
plt.scatter(path_x[0], path_y[0], color='green', s=80, label="Start")
plt.scatter(path_x[-1], path_y[-1], color='red', s=80, label="Reached Maximum")

plt.title("Hill Climbing Visualization")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
