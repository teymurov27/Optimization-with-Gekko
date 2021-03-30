from gekko import GEKKO

# Initialize Model
m = GEKKO(remote=True)

#help(m)

#define parameter
# eq = m.Param(value=40)

#initialize variables
x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12 = [m.Var() for i in range(12)]

#initial values
# x1.value = 1

#lower bounds
x1.lower = 0
x2.lower = 0
x3.lower = 0
x4.lower = 0
x5.lower = 0
x6.lower = 0
x7.lower = 0
x8.lower = 0
x9.lower = 0
x10.lower = 0
x11.lower = 0
x12.lower = 0


#upper bounds



#Equations
m.Equation(x1 + x2 + x3 + x4 <= 135)
m.Equation(x5 + x6 + x7 + x8  <= 56)
m.Equation(x9 + x10 + x11 + x12 <= 93)

m.Equation(x1 + x5 + x9 == 62)
m.Equation(x2 + x6 + x10 == 83)
m.Equation(x3 + x7 + x11 == 39)
m.Equation(x4 + x8 + x12 == 91)

m.Equation(x2 == 0)
m.Equation(x6 == 0)
m.Equation(x7 == 0)

#Objective
m.Obj(132*x1 + 97*x3 + 103*x4 + 85*x5 + 91*x6 + 106*x9 + 89*x10 + 100*x11 + 98*x12)


#Set global options
m.options.IMODE = 3 #steady state optimization

#Solve simulation
m.solve() # solve on public server

# Objective Values
obj1 = x1[0] + x2[0] + x3[0] + x4[0]
obj2 = x5[0] + x6[0] + x7[0] + x8[0]
obj3 = x9[0] + x10[0] + x11[0] + x12[0]
obj_value = 132*x1[0] + 97*x3[0] + 103*x4[0] + 85*x5[0] + 91*x6[0] + 106*x9[0] + 89*x10[0] + 100*x11[0] + 98*x12[0]

#Results
print('')
print('Results')
print('x1: ' + str(x1.value))
print('x2: ' + str(x2.value))
print('x3: ' + str(x3.value))
print('x4: ' + str(x4.value))
print('x5: ' + str(x5.value))
print('x6: ' + str(x6.value))
print('x7: ' + str(x7.value))
print('x8: ' + str(x8.value))
print('x9: ' + str(x9.value))
print('x10: ' + str(x10.value))
print('x11: ' + str(x11.value))
print('x12: ' + str(x12.value))
print('\nFirst Row: ' + str(obj1))
print('Second Row: ' + str(obj2))
print('Third Row: ' + str(obj3))
print('\nObjective: ', m.options.OBJFCNVAL)
