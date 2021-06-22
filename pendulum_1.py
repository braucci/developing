import numpy as np
import matplotlib.pyplot as plt

N = 100         # in how much sub pieces we should break a 1sec interval
T = 15          # total duration of the simulation
dt = 1 / N      # dt
g = 9.81        # acceleration of gravity
L = 1           # pendulum rope length
k = 0.8         # air resistance coefficient
m = 1           # mass of the pendulum

theta = [np.pi / 2]     # initial angle
theta_dot = [0]         # initial angular velocity
t = [0]

for i in range(N * T):
    theta_dot.append(theta_dot[-1] - theta_dot[-1] * dt * k / m - np.sin(theta[-1]) * dt * g / L)
    theta.append(theta_dot[-1] * dt + theta[-1])
    t.append((i + 1) * dt)

# parametri per la stampa
plt.rcParams['text.usetex'] = True
plt.rcParams['font.size'] = 15
plt.rcParams['font.family'] = "serif"


plt.plot(t, theta, label= r'$\theta$')
plt.plot(t, theta_dot, label= r'$\dot \theta$')
plt.axis('equal')
plt.xlabel('$t$ (sec)')

plt.legend()
plt.savefig('pendulum.png', dpi = 300, bbox_inches = 'tight', facecolor='w')
plt.show()
