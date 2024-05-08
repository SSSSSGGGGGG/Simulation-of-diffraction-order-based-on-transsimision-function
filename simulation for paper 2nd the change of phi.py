# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:08:29 2024

@author: gaosh
"""
import numpy as np
from scipy import special
import matplotlib.pyplot as plt
from scipy.stats import norm

# plt.grid(True)

k=4  # period
delta=6.4E-6
N=-1 # the resulting order
n=np.arange(-50,50,1)
m=N-k*n
u=(m+k*n)/(k*delta)

a=0.96 # fill factor
# phi=np.linspace(0,2,100)
phi_r=np.linspace(0, 2,20)

# print(f"the period is {k}, the order {N} is calculated, m={m} is for grating order, and n={n} is for SLM.")
# print(f"the spatial frequences are {u}")
I=[]
for i, phi in enumerate(phi_r):
    a_sinc=a*np.sinc((a/k)*(m+k*n))
    cos=np.cos(0.5*m*np.pi)*np.cos(0.5*phi*np.pi)
    sin=np.sin(0.5*m*np.pi)*np.sin(0.5*phi*np.pi)
    diff=cos-sin
    
    G=a_sinc*diff*np.sinc(0.5*m)*pow(-1.0,n)
    G_sum=sum(G)
    Intensity=G_sum**2
    I.append(Intensity)

plt.plot(phi_r,I)
plt.ylim(0, 1)
plt.xlim(0, 2)

plt.yticks(np.arange(0, 1.2, 0.2))
plt.minorticks_on()
print(f'I={I}')
