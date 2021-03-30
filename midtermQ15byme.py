from gekko import GEKKO
import math

# Initialize Model
m = GEKKO(remote=True)

# help(m)

# define parameter
# eq = m.Param(value=40)

# initialize variables
r, R, h = [m.Var() for i in range(3)]

# initial values
R.value = 4
# x2.value = 5
# x3.value = 5
# x4.value = 1

# lower bounds
# h.lower = 0
# R.lower = r
# r.lower = 0

# upper bounds
# x1.upper = 5
# x2.upper = 5
# x3.upper = 5
# x4.upper = 5

# Equations
m.Equation(h <= R + m.sqrt(R ** 2 - r ** 2))
m.Equation(r ** 2 + h ** 2 < 4 * R ** 2)
m.Equation(r <= R)
m.Equation(0 <= h)
m.Equation(h <= 2 * R)

# Objective
m.Obj(- ((math.pi * r * r * h) / 3))

# Set global options
m.options.SOLVER = 1  # steady state optimization

# Solve simulation
m.solve(disp=False)  # solve on public server

# Results
print('')
print('Results')
print('r: ' + str(r.value))
print('R: ' + str(R.value))
print('h: ' + str(h.value))

