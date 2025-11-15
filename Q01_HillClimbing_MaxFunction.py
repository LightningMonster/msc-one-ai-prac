# Python program that demonstrates the hill climbing algorithm to find the maximum of a 
# mathematical function.(For example f(x) = -x^2 + 4x) 

import random

# Define the function
def f(x):
    return -x**2 + 4*x

# Hill Climbing algorithm
def hill_climbing(start_x, step_size=0.1, max_iterations=1000):
    current_x = start_x
    current_value = f(current_x)

    for i in range(max_iterations):
        # Generate a new neighbor (small random move)
        new_x = current_x + random.uniform(-step_size, step_size)
        new_value = f(new_x)

        # If the new value is better, move there
        if new_value > current_value:
            current_x = new_x
            current_value = new_value

    return current_x, current_value

# Starting point
start_x = random.uniform(0, 4)
best_x, best_value = hill_climbing(start_x)

print(f"Starting point: {start_x:.4f}")
print(f"Maximum at x = {best_x:.4f}, f(x) = {best_value:.4f}")
