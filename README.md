# Bayesian methods


This project is based on the idea of using bayesian optimizatian for different optimization tasks:
 - Searching for the local minimum of the Rosenbrock function;
 - Reproducing the parameters of free energy landscape of translocated polymer using the time distribution of translocation.

# Instructions



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

## Free energy landscape
------------------------------------
### Description of the problem


