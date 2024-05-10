# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 11:28:11 2024

@author: SG
"""

import sympy as sp
n = sp.Symbol('n', integer=True)
a = sp.Symbol('a', integer=True)
expr_sinc=sp.sinc((n/2+1/4)*sp.pi)
evaluate_sinc=sp.Sum(expr_sinc, (n, -50, 50))
print(f"The value of summation of {expr_sinc}")
sp.pprint(evaluate_sinc.doit())