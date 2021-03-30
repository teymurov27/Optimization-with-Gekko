from gekko import GEKKO
import numpy as np
import matplotlib.pyplot as plt


# Initialize Model
m = GEKKO(remote=True)

# define parameter
eq1 = m.Param(value=12)
eq2 = m.Param(value=8)
eq3 = m.Param(value=24)

# initialize variables
x1, x2 = [m.Var() for i in range(2)]

# initial values
# x1.value = InitialValue_x1
# x2.value = InitialValue_x2

# lower bounds
x1.lower = 0
x2.lower = 0

# upper bounds
x1.upper = 5
x2.upper = 5

# Equations
m.Equation(6 * x1 + x2 >= eq1)
m.Equation(3 * x1 + x2 >= eq2)
m.Equation(4 * x1 + 6 * x2 >= eq3)

# Objective
m.Obj(180 * x1 + 160 * x2)

# Set global options
m.options.IMODE = 3  # steady state optimization

# Solve simulation
m.solve()  # solve on public server


# Results
print('')
print('Results')
print('x1: ' + str(x1.value))
print('x2: ' + str(x2.value))
