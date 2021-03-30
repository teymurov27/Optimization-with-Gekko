from gekko import GEKKO
import numpy as np
import matplotlib.pyplot as plt


# Initialize Model
m = GEKKO(remote=True)

# define parameter
eq1 = m.Param(value=28)
eq2 = m.Param(value=24)

# initialize variables
x1, x2 = [m.Var() for i in range(2)]

# initial values
# x1.value = InitialValue_x1
# x2.value = InitialValue_x2

# lower bounds
x1.lower = 0
x2.lower = 0

# upper bounds
# x1.upper = upperBound_x1
# x2.upper = upperBound_x2

# Equations
m.Equation(7 * x1 + 2 * x2 >= eq1)
m.Equation(2 * x1 + 12 * x2 >= eq2)

# Objective
m.Obj(50 * x1 + 100 * x2)

# Set global options
m.options.IMODE = 3  # steady state optimization

# Solve simulation
m.solve(disp=False)  # solve on public server


# Results
print('')
print('Results')
print('x1: ' + str(x1.value))
print('x2: ' + str(x2.value))


