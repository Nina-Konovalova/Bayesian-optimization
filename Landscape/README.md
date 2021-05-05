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



# Obtained results

## Free energy landscape
------------------------------------
### Description of the problem
In this project it the translocation of polymers will be considered. The chain transfer is described by the Fokker-Plank (FP) formalism of random walk across the free energy landscape. The main idea was to be able to reconstruct the initial (true) free energy landscape

The whole task can be described the following way:

1) Parametrize the free enegry landscapes by a Chebyshev polynomial of n degree (https://en.wikipedia.org/wiki/Chebyshev_polynomials). 
2) For each known profile find the corresponding time translocation distribution for successeful and unsuccessful translocation and translocation rate are considered using F.f90 fortran programm.
3) Using the initial dataset and Gaussian Processes - build the model.
4) 

## Several experiments were conducted for different true free energy landscapes.
------------------------------------------------

#### Experiment 0

![0 experiment](https://github.com/Nina-Konovalova/Bayesian-optimization/raw/main/pictures/0.png)

       Predicted params 
       [-3.57162912e-01, -1.06302558e-01,  3.59453619e-03, -6.89576136e-04, 2.91195832e-05, -4.84155631e-07,  3.59652159e-09, -1.00193649e-11]
       
       Real params 
       [-7.47744177e-01, -1.19378116e-01,  1.25200942e-03, -2.73809079e-04, 1.15978176e-05, -1.79769715e-07,  1.22421902e-09, -3.12022457e-12]


#### Experiment 1

![1 experiment](https://github.com/Nina-Konovalova/Bayesian-optimization/raw/main/pictures/1.png)

    Predicted params 
     [ 1.83209789e+00,  1.89781034e-01, -1.42745482e-02,  6.94173423e-04, -1.66576059e-05,  1.87557356e-07, -9.52137707e-10,  1.68339766e-12]
     
    Real params 
     [ 1.09513698e+00,  2.11332250e-01, -1.87853725e-02,  1.61184050e-03, -5.41858513e-05,  8.17071299e-07, -5.73664048e-09,  1.53723244e-11]


#### Experiment 2

![2 experiment](https://github.com/Nina-Konovalova/Bayesian-optimization/raw/main/pictures/2.png)

    Predicted params 
     [ 1.64171311e+00,  9.45254839e-02,  3.04486627e-02, -2.18163829e-03, 5.49195874e-05, -6.64682127e-07,  3.94158223e-09, -9.22299397e-12]
     
    Real params 
     [ 7.17234188e-01, -1.68136119e-01,  7.05164608e-02, -4.27578874e-03,  1.07848094e-04, -1.35978046e-06,  8.51143806e-09, -2.11240142e-11]


#### Experiment 3

![4 experiment](https://github.com/Nina-Konovalova/Bayesian-optimization/raw/main/pictures/4.png)

    Predicted params 
     [ 1.64171311e+00,  9.45254839e-02,  3.04486627e-02, -2.18163829e-03, 5.49195874e-05, -6.64682127e-07,  3.94158223e-09, -9.22299397e-12]
     
    Real params 
     [ 7.17234188e-01, -1.68136119e-01,  7.05164608e-02, -4.27578874e-03,  1.07848094e-04, -1.35978046e-06,  8.51143806e-09, -2.11240142e-11]
     
 
#### Experiment 4
     
 ![8 experiment](https://github.com/Nina-Konovalova/Bayesian-optimization/raw/main/pictures/8.png)

    Predicted params 
     [ -1.62705673e-01,  1.87259174e-01, -3.17743676e-02,  -5.54472170e-05,  7.69193317e-07, -4.96158986e-09,  1.19505984e-11]
     
    Real params 
     [ -2.04872616e-01,  2.76446883e-01, -3.93215002e-02,  -4.65475377e-05,  4.47834968e-07, -1.40308593e-09, -1.10686906e-12]


#### Experiment 5

     
 ![hills experiment](https://github.com/Nina-Konovalova/Bayesian-optimization/raw/main/pictures/hills.png)

    Predicted params 
    [-3.43324469e-01,  6.17752473e-01, -1.20234937e-01,  8.52576610e-03, -2.58173099e-04,  3.81715953e-06, -2.73483920e-08,  7.61112473e-11]
     
    Real params 
    [-2.42693006e-01,  4.77669412e-01, -9.49614930e-02,  7.25829537e-03,  -2.35424643e-04,  3.70589913e-06, -2.80836978e-08,  8.21135781e-11]
     
     
#### Experiment 6

     
 ![6 experiment](https://github.com/Nina-Konovalova/Bayesian-optimization/raw/main/pictures/6.png)

    Predicted params 
    [-5.85554671e-01,  8.99116148e-01, -1.48649523e-01,  9.09031884e-03, -2.46937726e-04,  3.32522630e-06, -2.18838823e-08,  5.63270393e-11]
     
    Real params 
    [-1.14355207e+00,  8.92442119e-01, -1.49523450e-01,  7.45068188e-03,  -1.70415657e-04,  2.01097596e-06, -1.19400628e-08,  2.82926800e-11]


#### Experiment 7

     
 ![7 experiment](https://github.com/Nina-Konovalova/Bayesian-optimization/raw/main/pictures/7.png)

    Predicted params 
    [3.80570041e-02,  5.16110468e-03,  3.14102343e-04, -4.33284001e-06, 2.73223872e-07, -3.85004218e-09,  1.45122680e-11,  1.29205563e-15]
     
    Real params 
    [ 7.00247782e-02, -1.24593742e-02,  1.60815465e-03, -3.28225475e-05, -1.11931294e-06,  5.30467180e-08, -6.64011006e-10,  2.64005115e-12]


