# Bayesian methods


This project is based on the idea of using bayesian optimizatian for different optimization tasks:
 - Searching for the local minimum of the Rosenbrock function;
 - Reproducing the parameters of free energy landscape of translocated polymer using the time distribution of translocation.

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

## Free energy landscape
------------------------------------
### Description of the problem
In this project it the translocation of polymers will be considered. The chain transfer is described by the Fokker-Plank (FP) formalism of random walk across the free energy landscape.

The main idea was to be able to reconstruct the initial (true) free energy landscape, that was parametrized by a Chebyshev polynomial of n degree (https://en.wikipedia.org/wiki/Chebyshev_polynomials). In addition to true free energy landscape initial dataset of different free energy frofiles is presented. For each profile the corresponding time translocation distribution for successeful and unsuccessful translocation and translocation rate are considered.

Several experiments were conducted for different true free energy landscapes.

\\3 pictures of initials\\
\\1 picture of the results\\



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



