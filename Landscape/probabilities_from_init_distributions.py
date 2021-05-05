# -*- coding: utf-8 -*-
"""
Created on Tue May  4 11:51:54 2021

@author: Nina Konovalova

"""
import subprocess
subprocess.call(["gfortran","-o","outputic","F.f90"]) #just for compile the programm

import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.chebyshev as cheb
import pandas as pd


def probabilities_from_init_distributions (x_end):
    f = open('./new_input.txt', 'w')
    N = 51
    t = 1
    num1 = 50000
    f.write(str(N-1) + '\t'+ str(t) + '\n' + str(num1)+ '\t'+ str(t) +'\t' + str(10000)+ '\t'+ str(t) + '\n' )
    x = []
    y = []
    for i in range (N-1):
          f.write(str(i) + '\t' + str(np.real(np.polynomial.chebyshev.chebval(i,np.array(x_end)))) + '\n')
    f.write (str(50) + '\t' + str(np.polynomial.chebyshev.chebval(50,np.array(x_end[0]))))
    f.close()

    plt.plot(np.polynomial.chebyshev.chebval(np.arange(51),np.array(x_end)))

        #fortran programm - making new distributions
    subprocess.check_output(["./outputic"])
        #saving new output data
    dat = pd.read_csv('./new_output.txt', sep=' ',skiprows=[0,1,2], header=None)
    dat.drop(dat.columns[0], axis = 1, inplace = True)
    rate = float(np.array(pd.read_csv('./new_output.txt', sep=' ',nrows=1, header=None).fillna(1e+20)[11]))
        #if str(rate).find('E')==0:
        #  rate = float(str(rate).split('-')[0]) + 'E' + '-' + (str(rate).split('-')[1])

        #if rate == 'nan':
        #  rate = 1e+20

    Y_pos_new = np.array(dat[1][:], dtype = float)
    Y_neg_new = np.array(dat[2][:], dtype = float)
    
    return Y_pos_new, Y_neg_new, rate
      