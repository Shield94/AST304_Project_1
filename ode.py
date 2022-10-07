########################################################################
# Team Apollo 13: Nathan Shields, Brenna Chetan, Maya Joyce
# AST 304, Fall 2022
# Michigan State University
########################################################################

"""
This module is useed for implimenting differnet intergration techniques to solve ODE's. The techniques are forward euler, 2nd order kunge-kutta and 4th order kunge-kutta. All functions require a function, time array, positon/velocity arrays, and a time step.
"""

# all routines that take a single step should have the same interface
# fEuler is complete, except for documentation. you can use this as a pattern 
# for the other two routines.
def fEuler(f,t,z,h,args=()):
    """
    This is the forward Euler method to solve ODE's. Input a time array, a postion/velocity array, and a time step to recieve an estimated value of the function you are approximating.
    
    Arguments
        f(t,z,...)
            function that contains the RHS of the equation dz/dt = f(t,z,...)
    
        t (array-like)
            time array
        
        z(array-like)
            position and velocity vectors
    
        args (tuple, optional)
            additional arguments to pass to f
    
    Returns
        znew = z(t+h)
    """
    if not isinstance(args,tuple):
        args = (args,)

    return z + h*f(t,z,*args)


def rk2(f,t,z,h,args=()):
    """
    This is the 2nd order Runge-Kutta method to solve ODE's. Input a time array, a postion/velocity array, and a time step to recieve an estimated value of the function you are approximating.
    
    Arguments
        f(t,z,...)
            function that contains the RHS of the equation dz/dt = f(t,z,...)
    
        t (array-like)
            time array
        
        z(array-like)
            position and velocity vectors
    
        args (tuple, optional)
            additional arguments to pass to f
    
    Returns
        znew = z(t+h)
    """
    
    if not isinstance(args,tuple):
        args = (args,)
    
    Zmp = z + (h/2)*f(t,z,*args)
    
    return z + h*f(t + h/2,Zmp,*args)


def rk4(f,t,z,h,args=()):
    """
    This is the 4th order Runge-Kutta method to solve ODE's. Input a time array, a postion/velocity array, and a time step to recieve an estimated value of the function you are approximating.
    
    Arguments
        f(t,z,...)
            function that contains the RHS of the equation dz/dt = f(t,z,...)
    
        t (array-like)
            time array
        
        z(array-like)
            position and velocity vectors
    
        args (tuple, optional)
            additional arguments to pass to f
    
    Returns
        znew = z(t+h)
    """
   
    if not isinstance(args,tuple):
        args = (args,)
    
    k1 = f(t,z,*args)
    
    k2 = f(t + (h/2),z + k1*(h/2),*args)
    
    k3 = f(t + (h/2),z + k2*(h/2),*args)
    
    k4 = f(t + h,z + k3*h,*args)
    
    return z + (h/6)*(k1+2*k2+2*k3+k4)
