import matplotlib.pyplot as plt
from numpy import array, pi, exp, log
from math import gcd
import datetime

dd=9
mm=6
yy=72

#lcm (Lowest Common Multiple = mcm ) is the smallest positive integer that is perfectly divisible by the given numbers. 

a = [dd, mm, yy]
lcm = a[0]
for i in a[1:]:
  lcm = lcm*i//gcd(lcm, i)

N = 2*lcm+1

def f(n):
#	return log(n)**4
	return n/dd + n**2/mm+ n**3/yy 
    
z = array( [exp( 2*pi*1j*f(n) ) for n in range(1, N)] )
z = z.cumsum()

plt.plot(z.real, z.imag, color='#333399')
#plt.axes().set_aspect(1)

stringa = str(dd)+ "/" + str(mm) + "/" + str(yy)

plt.text(2.0, 0, stringa,fontsize=9)

plt.show()