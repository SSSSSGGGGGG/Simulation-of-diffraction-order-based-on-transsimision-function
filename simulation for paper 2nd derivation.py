# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:08:29 2024

@author: gaosh
"""
import numpy as np
from scipy import special
import matplotlib.pyplot as plt
from scipy.stats import norm
import sympy as sp

import sympy as sp

# Define symbolic variables
N,delta,u,a, phi = sp.symbols('N delta u a phi')
# N=m+kn

# Define the constraint equation
n = sp.Symbol('n', integer=True)
k = sp.Symbol('k', integer=True) 
m = sp.Symbol('m', integer=True) # Define n as an integer
constraint_eq = sp.Eq(n + k * m, sp.Integer(0))

# Define the expression to be summed
expr = (-1)**n * a * (-sp.sin(sp.pi * m / 2) * sp.sin(sp.pi * phi / 2) +
                        sp.cos(sp.pi * m / 2) * sp.cos(sp.pi * phi / 2)) * sp.sinc(m/2) * sp.sinc(a * (k * n + m) / k)*sp.DiracDelta(u-(N/k/delta))

# Compute the summation for each solution of n

result_sub=expr.subs({k:2,N:2,m:2-2*n}) #!!!! change N and m at the same time.
result = sp.Sum(sp.Sum(result_sub, (n, -sp.oo, sp.oo)),(m, -sp.oo, sp.oo))

final_result = sum(result_sub.subs({n: i}) for i in range(-50, 50))# numerical evaluate

print("G=")
sp.pprint(sp.simplify(result_sub))
sp.pprint(sp.simplify(result))
# sp.pprint(result_sub.doit().simplify())
# sp.pprint(result_sub.evalf())
print("I=")

sp.pprint(sp.simplify(result**2))


# print(f"the period is {k}, the order {N} is calculated, m={m} is for grating order, and n={n} is for SLM.")
# print(f"the spatial frequences are {u}")

# a_sinc=a*sp.sinc((a/k)*(m+k*n))
# cos=sp.cos(0.5*m*sp.pi)*sp.cos(0.5*phi*sp.pi)
# sin=sp.sin(0.5*m*sp.pi)*sp.sin(0.5*phi*sp.pi)
# diff=cos-sin

# G=a_sinc*diff*sp.sinc(0.5*m)*pow(-1.0,n)

# print(G)
# G_sum=sp.Sum(G)
# Intensity=G_sum**2


