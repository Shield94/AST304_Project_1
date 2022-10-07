Kepler
======

Project directory for comparison of ODE solvers and usage of the solvers to integrate orbits of two point particles (Kepler's problem). A description of the integration methods, Kepler's problem, and instructions for completing this project is available on D2L.

Contents of this directory
--------------------------

*  `README.md`  
This file

*  `ode.py`  
Routines to advance the solution of a system of first-order ODEs by one step

*  `kepler.py`  
Routines to integrate orbits and compute energies for two particles interacting 
via an attractive 1/r potential

* `Shields_AST304_Project.ipynb`
Uses kepler.py and ode.py to graph and analyize the orbits of two particles interacting
via an attractive 1/r potential

Report/closeout
---------------

To run my code, you must first import the modules to obtain important intialization and integration functions.
Next, you must intialize your system with the `set_initial_conditions` function. From there, you can use the 
`integrate_orbit` function to solve the ODE and obtain the orbit and energies of the system. It is also important 
to take advantage of the 3 different methods (forward euler, 2nd Order Runge-Kutta, and 4th order Runge-Kutta)
available in `intergrate_orbit`. Finally, simply plot the solution.
   
Resources
---------
Coding standards are posted on D2L.
