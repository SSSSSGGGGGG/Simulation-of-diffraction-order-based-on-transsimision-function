# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 11:28:11 2024

@author: SG
"""
import sympy as sp
# Define the symbol
n = sp.Symbol('n')

# Define the terms of the series
term = (0.96*(-1)**(n))/(2*n+1)

# Define the series sum
series_sum = sp.Sum(term, (n, 0, sp.oo))

# Evaluate the series
evaluated_sum = series_sum.doit()

# Print the evaluated sum
print("The sum of the alternating series is:", evaluated_sum)