# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$12/06/2013 11:09:55$"

# QUIZ
#
# Fill in the for loop below to set
# the x, y1, and y2 arrays to the
# following values:
#
# - The x array should contain
#   num_points many points evenly
#   spaced between 0 and 2*pi.
#
# - The y1 array should contain
#   the corresponding sine values
#   of the values in the x array.
#
# - The y2 array should contain
#   the corresponding cosine values
#   of the values in the x array.

import math
from udacityplots import *


def sin_cos():
    num_points = 50

    x = numpy.zeros(num_points)
    sin_x = numpy.zeros(num_points)
    cos_x = numpy.zeros(num_points)

    for i in range(num_points):
        #print (i+1)/50.0
        alfa = 2.0*math.pi*((i+1)/(50.0))
        x[i] = alfa
        #print alfa
        sin_x[i] = math.sin(alfa)
        cos_x[i] = math.cos(alfa)
    return x, sin_x, cos_x

x, sin_x, cos_x = sin_cos()

# These lines call the matplotlib package
# to plot the values you input on a graph.
@show_plot
def plot_me():
    matplotlib.pyplot.plot(x, sin_x)
    matplotlib.pyplot.plot(x, cos_x)
plot_me()