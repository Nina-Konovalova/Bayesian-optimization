# Bayesian methods


This project is based on the idea of using bayesian optimizatian for searching for the local minimum of the Rosenbrock function;
 - 
 
# Instructions
Installation:

        ! pip install GPy gpyopt
        
Necessary libraries:

        import GPy
        import GPyOpt
        import numpy as np
        import matplotlib.pyplot
        import pandas as pd
        import subprocess
        import sklearn

If you want Rosenbrock function optimization - the https://github.com/Nina-Konovalova/Bayesian-optimization/blob/main/Rosenbrock_function_optimization/Rosenbrock_BO_optimization.ipynb can be launched. 

# Obtained results

## Rosenbrock function optimization
------------------------------------
Rosenbrock function:

*f(x,y) = (1-x) ^2 + 100(y - x ^2) ^2*

has global minimum in (1,1)

![Функция Розенброка](https://github.com/Nina-Konovalova/Bayesian-optimization/raw/main/pictures/розенброк.png)

To use BO to solve this problem, we need to create a GPyOpt object in which we need to specify the following elements:
 - The function to optimize: Rosenbrock function;
 - The box constraints of the problem: (-3,3)(-3,3);
 - The model, by default we use a GP with a Mattern32 kernel;
 - 3 restarts for each iteration of optimization;
 - Initial_design_numdata - number of initial data (use initial_design_type = 'random');
 - normalize_Y (whether to normalize the outputs before performing any optimization);
 - The acquisition function - MPI.


![Иллюстрация к проекту](https://github.com/Nina-Konovalova/Bayesian-optimization/raw/main/pictures/minimum1.png)

**Minimum of the function in point**  (1.01;1.02).



