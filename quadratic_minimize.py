import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

#simple quadratic function to find minimum
def quad(x):
    return(x**2-2*x+4)

#running scipy minimize function with initial guess 0 
result = minimize(quad,0)
x_coor = result.x[0]
value = quad(x_coor)

print('Minimum value of function:',value)

#plotting function and minimum value
x = np.linspace(-10,10,100)
y = []
for i in range(len(x)):
    y.append(quad(x[i]))
    
plt.plot(x,y,label='function')
plt.plot(x_coor,value,'o',label='minimum value')
plt.legend()
plt.title('x**2-2*x+4 and its minimum value')
plt.show()


