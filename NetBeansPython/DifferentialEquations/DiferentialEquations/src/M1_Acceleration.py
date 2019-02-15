#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$14/06/2013 11:15:38$"

# QUIZ
#
# Modify the acceleration function so that it returns
# the acceleration vector of the spacecraft.
#
# A sample of how to use the numpy.linalg.norm function
# is given. This computes the length of the vector, and
# it should be the only outside function you need to
# use in your answer.

import numpy

earth_mass = 5.97e24 # kg
moon_mass = 7.35e22 # kg
gravitational_constant = 6.67e-11 # N m2 / kg2

# The origin, or (0,0), is at the center of the earth
# in this example, so it doesn't make any sense to
# set either the moon_position or spaceship_position
# equal to (0,0). Depending on your solution, doing this
# may throw an error!  Please note that moon_position and
# spaceship_position are both numpy arrays, and the
# returned value should also be a numpy array.

def acceleration(moon_position, spaceship_position):
    earth_position = numpy.array([0,0])
    vector_to_moon = moon_position - spaceship_position
    vector_to_earth = - spaceship_position #earth was on origin!
    acceleration_ship = gravitational_constant*(earth_mass/numpy.linalg.norm(vector_to_earth)**3 * vector_to_earth + moon_mass/numpy.linalg.norm(vector_to_moon)**3 + vector_to_moon)
    return acceleration_ship

moon_position = 98372612.
spaceship_position = 834736273.
moon_position = 1.
spaceship_position = 1.
vector_to_earth = -spaceship_position
print numpy.linalg.norm(vector_to_earth)**3


#moon_pos = numpy.array([3,4])
#ship_pos = numpy.array([1,1])
#print moon_pos, ship_pos
#print ship_pos + moon_pos
#print acceleration (moon_pos,ship_pos)

#print numpy.linalg.norm(moon_pos)




'''a=numpy.array([0,1,2])
b=numpy.array([3,4,5])
c = a+b
print c'''
#array([3, 5, 7])
