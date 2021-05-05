# -*- coding: utf-8 -*-
"""
Created on Tue May  4 12:01:44 2021

@author: nina_
"""

import numpy.polynomial.legendre as leg
import numpy as np
import matplotlib.pyplot as plt

def hermite_approx (X_e, n):
    X_parametr_pol_e = np.zeros([X_e.shape[0], n+1])
    for i in range (X_e.shape[0]):
        le = leg.Legendre.fit(np.arange(51),X_e[i], n, window=[0,51])
        X_parametr_pol_e[i] = le.coef
        if i % 1 == 0:
          xx, yy = p.linspace(n=51)
          plt.figure(dpi = 80)
          plt.plot(xx, yy,'go--', linewidth=4, markersize=2, color = 'red', label = 'fitted by chebyshev pol')
          plt.plot(np.arange(51),X_e[i],label = 'real X')
    
          plt.legend()
          
    return X_parametr_pol_e