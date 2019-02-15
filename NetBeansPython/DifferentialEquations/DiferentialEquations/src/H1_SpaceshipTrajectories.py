#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$17/06/2013 16:21:50$"

# PROBLEM 3
#
# Modify the below functions acceleration and
# ship_trajectory to plot the trajectory of a
# spacecraft with the given initial position
# and velocity. Use the Forward Euler Method
# to accomplish this.

from udacityplots import *

h = 1.0 # s
earth_mass = 5.97e24 # kg
gravitational_constant = 6.67e-11 # N m2 / kg2

def acceleration(spaceship_position):
    ###Your code here.

def ship_trajectory():
    num_steps = 13000
    x = numpy.zeros([num_steps + 1, 2]) # m
    v = numpy.zeros([num_steps + 1, 2]) # m / s

    x[0, 0] = 15e6
    x[0, 1] = 1e6
    v[0, 0] = 2e3
    v[0, 1] = 4e3

	###Your code here. This code should call the above
	###acceleration function.

    return x, v

x, v = ship_trajectory()

@show_plot
def plot_me():
    matplotlib.pyplot.plot(x[:, 0], x[:, 1])
    matplotlib.pyplot.scatter(0, 0)
    matplotlib.pyplot.axis('equal')
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Longitudinal position in m')
    axes.set_ylabel('Lateral position in m')
plot_me()



