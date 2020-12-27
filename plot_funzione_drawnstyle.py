#
# How To Make Hand-Drawn Style Plots In Python
#

import numpy as np
import matplotlib.pyplot as plt


# Python gives us the option to make xkcd style 
# plots using the matplotlib library. 


#f(x) = sin(x)

f = lambda x:np.sin(x)

xi=0
xf= 2*np.pi
n=100
x=np.linspace(xi,xf,n)

y = f(x)

with plt.xkcd():
	plt.figure(1)
	plt.title('f(x)')
	plt.plot(x,y)
	plt.xlabel('x')
	plt.ylabel('y')
	plt.grid(True)

	plt.show()
