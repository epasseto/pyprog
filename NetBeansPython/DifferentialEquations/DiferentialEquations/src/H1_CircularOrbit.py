# PROBLEM 1
#
# Modify the orbit function below to model
# one revolution of the moon around the earth,
# assuming that the orbit is circular.
#
# Use the math.cos(angle) and math.sin(angle)
# functions in order to accomplish this.

import math
from udacityplots import *

moon_distance = 384e6 # m

def orbit():
    num_steps = 50
    x = numpy.zeros([num_steps+1, 2])
    frac = 2.*math.pi/num_steps
    for n in range(num_steps+1):
        x[n] = [math.cos(frac*n), math.sin(frac*n)]
    return x

x = orbit()

@show_plot
def plot_me():
    matplotlib.pyplot.axis('equal')
    matplotlib.pyplot.plot(x[:, 0], x[:, 1])
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Longitudinal position in m')
    axes.set_ylabel('Lateral position in m')
plot_me()
