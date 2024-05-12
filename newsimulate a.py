# -*- coding: utf-8 -*-
"""
Created on Sun May 12 17:46:53 2024

@author: gaosh
"""

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

phi= sp.symbols('phi')
# Define range for 'a'
a_values = np.linspace(0, 1, 10)  # Adjust range as needed

# Initialize an empty list to store solutions
solutions = []
solutions2 = []

# Iterate over 'a' values
for a in a_values:
    # Calculate f0 and f1 for the current 'a'
    f0 = a**2 * sp.cos((phi / 2) * sp.pi)**2
    f1 = a**2 * sp.sinc((a / 2) * sp.pi)**2 * sp.sin((phi / 2) * sp.pi)**2

    # Solve equation and apply modulo operation
    equation = sp.Eq(f1, f0)
    solution = sp.solve(equation, phi)
    print(solution,"...")
    # Append the first solution (if exists) to the list
    if solution:
        solutions.append(solution[0] % 2)
        solutions2.append(solution[1] % 2)
    else:
        solutions.append(None)  # Append None if no solution found
        solutions.append(None)
# Plot 'a' vs 'phi' for each solution
print(solutions,"...",solutions2)
plt.figure(figsize=(10, 6))
plt.plot(a_values, solutions, label='Solution')
plt.plot(a_values, solutions2, label='Solution')
plt.xlabel('a')
plt.ylabel('phi (mod 2)')
plt.title('Solutions mod 2 for Different Values of a')
plt.legend()
plt.grid(True)
plt.show()
