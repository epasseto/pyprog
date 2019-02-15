#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$14/08/2012 15:56:47$"


import itertools
#import math

#a = 5
#b = 8
#c = 8.00001

"""if a == b:
    print "ok"
    print "end"
elif a > b:
    print "plus"
    print "end"
else:
    print "no"
    print "end"

if a == b: print "ok"; print "end"
elif a > b: print "plus"; print "end"
else: print "no"; print "end"""""

"""a = a << 1
b = b >> 2
print a, b"""

#print c, math.ceil(c)

#a = ['b', 'a', 'z', '-1a']
#print sorted(a)

"""x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
print zipped
#[(1, 4), (2, 5), (3, 6)]
x2, y2 = zip(*zipped)
print x == list(x2) and y == list(y2)
#True"""

"""items =   [("dog",          46,   35,     13,  280    ),
           ("elephant",     30, 3500,     50, 6250    ),
           ("frog",          5,    0.5,    8,    3    ),
           ("hippopotamus", 45, 1600,     45,  573    ),
           ("horse",        40,  385,     30, 642     ),
           ("human",        27,   80,     78, 2000    ),
           ("lion",         50,  250,     30,  454    ),
           ("mouse",         8,    0.025,  2,    0.625),
           ("rabbit",       25,    4,     12,   40    ),
           ("shark",        26,  230,     20,   92    ),
           ("sparrow",      16,    0.024,  7,    2    )]
weights = (.4,.2,.1,.3)
names = [item[0] for item in items]
scores = [sum([a*b for (a,b) in zip(item[1:], weights)]) for item in items]

print item[1:]
#(16, 0.024, 7, 2)
#print [item[1:] for item in items]
#print zip(item[1:], weights)
print [(a,b) for (a,b) in zip(item[1:], weights)]
#[(16, 0.4), (0.024, 0.2), (7, 0.1), (2, 0.3)]
print [ a*b  for (a,b) in zip(item[1:], weights)]
#[6.4, 0.0048000000000000004, 0.7000000000000001, 0.6]
print sum([a*b for (a,b) in zip(item[1:], weights)])
#7.7048
print [sum([a*b for (a,b) in zip(item[1:], weights)]) for item in items]
[110.7, 2592.0, 3.8000000000000003, 514.4, 288.6, 634.6, 209.2, 
            3.5925000000000002, 24.0, 86.0, 7.7048000000000005]"""

"""list = [21, 43, 48, 49, 50, 51, 75, 77, 89, 87, 93]
midpoint = (list[0]+list[len(list)-1])/2.0
median = list[len(list)/2]
print "midpoint:", midpoint
print "median:", median
print (midpoint+median)/2"""

"""student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10)]

alfa = sorted(student_tuples, key=lambda student: student[2])

print alfa"""

#!/usr/bin/python
# Filename: simplestclass.py

"""class Person:
	def __init__(self, name):
            self.name = name
        def sayHi(self):
            print 'Hello hello hello', self.name

p = Person('Mobo')
p.sayHi()"""

"""class Person:
	'''Represents a person.'''
	population = 0
	def __init__(self, name):
		'''Initializes the person's data.'''
		self.name = name
		print '(Initializing %s)' % self.name
		# When this person is created, he/she
		# adds to the population
		Person.population += 1
	def __del__(self):
		'''I am dying.'''
		print '%s says bye.' % self.name
		Person.population -= 1
		if Person.population == 0:
			print 'I am the last one.'
		else:
			print 'There are still %d people left.' % Person.population
	def sayHi(self):
		'''Greeting by the person.

		Really, that's all it does.'''
		print 'Hi, my name is %s.' % self.name
	def howMany(self):
		'''Prints the current population.'''
		if Person.population == 1:
			print 'I am the only person here.'
		else:
			print 'We have %d persons here.' % Person.population

swaroop = Person('Swaroop')
swaroop.sayHi()
swaroop.howMany()

kalam = Person('Abdul Kalam')
kalam.sayHi()
kalam.howMany()

swaroop.sayHi()
swaroop.howMany()"""

#!/usr/bin/python
# Filename: inherit.py

"""class SchoolMember:
	'''Represents any school member.'''
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print '(Initialized SchoolMember: %s)' % self.name
	def tell(self):
		'''Tell my details.'''
		print 'Name:"%s" Age:"%s"' % (self.name, self.age),

class Teacher(SchoolMember):
	'''Represents a teacher.'''
	def __init__(self, name, age, salary):
		SchoolMember.__init__(self, name, age)
		self.salary = salary
		print '(Initialized Teacher: %s)' % self.name
	def tell(self):
		SchoolMember.tell(self)
		print 'Salary: "%d"' % self.salary

class Student(SchoolMember):
	'''Represents a student.'''
	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		print '(Initialized Student: %s)' % self.name
	def tell(self):
		SchoolMember.tell(self)
		print 'Marks: "%d"' % self.marks

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 22, 75)

print # prints a blank line

members = [t, s]
for member in members:
	member.tell() # works for both Teachers and Students"""

#print list(itertools.permutations([1,2,3]))
#b = ['batman','robin','catwoman']
#a = list(itertools.combinations(b,2))
#while len(a)>0:
#    c = a.pop()
#    d = c[0] + ' - ' + c[1]
#    print d

#b = list(itertools.permutations('0123456789'))
#c = itertools.imap(lambda x: "".join(x), itertools.permutations("0123456789"))
#a = ("".join(x) for x in itertools.permutations("0123456789"))
#for element in a: print element

#decorator - modify language elements
#

"""def soma(a,b):
    return a+b

@soma
def soma(a,b):
    print "teste"

print soma(2,3)"""

"""import time

def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print '%r (%r, %r) %2.2f sec' % \
              (method.__name__, args, kw, te-ts)
        return result

    return timed

class Foo(object):

    @timeit
    def foo(self, a=2, b=3):
        time.sleep(0.2)

@timeit
def f1():
    time.sleep(1)
    print 'f1'

@timeit
def f2(a):
    time.sleep(2)
    print 'f2',a

@timeit
def f3(a, *args, **kw):
    time.sleep(0.3)
    print 'f3', args, kw

f1()
f2(42)
f3(42, 43, foo=2)
Foo().foo()"""

"""class Memoizer(object):
    #Caches the result of a function.

    def __init__(self, function):
        self.function = function
        self.__name__ = function.__name__
        self.__doc__ = function.__doc__

        self.cached_values = {}

    def __call__(self, *fn_args,**fn_kwargs):
        #Wrapper for calling the Cached Function.

        assert not fn_args, ("CachedMethod cannot be used with positional"
                             "arguments.")

        kwargs_sig = self.kwargs_signature(**fn_kwargs)

        if kwargs_sig not in self.cached_values:
            print "Calculating new value."
            self.cached_values[kwargs_sig] = self.function(**fn_kwargs )
        else:
            print "Returning cached value."

        return self.cached_values[kwargs_sig]

    def kwargs_signature(self, **fn_kwargs):
        #Returns kwargs signature--an immutable, given a set of kwargs.
        
        tp = tuple([v for k,v in sorted(fn_kwargs.items())])
        return str(tp.__hash__())

    def clear(self, **fn_kwargs):
        #Clears the cached data.

        if not fn_kwargs:
            # Clear all if a set of kwargs was not specified.
            self.cached_values = {}
        else:
            # Otherwise just clear the value for the specified kwargs
            # combination.
            kwargs_sig = self.kwargs_signature(**fn_kwargs)
            self.cached_values.pop(kwargs_sig, None)"""

#The special syntax, *args and **kwargs in function definitions is used to pass a variable number of arguments to a function. The single asterisk form (*args) is used to pass a non-keyworded, variable-length argument list, and the double asterisk form is used to pass a keyworded, variable-length argument list. Here is an example of how to use the non-keyworded form. This example passes one formal (positional) argument, and two more variable length arguments.
'''def test_var_args(farg, *args):
    print "formal arg:", farg
    for arg in args:
        print "another arg:", arg

test_var_args(1, "two", 3) #variable length argument lists

def test_var_kwargs(farg, **kwargs):
    print "formal arg:", farg
    for key in kwargs:
        print "another keyword arg: %s: %s" % (key, kwargs[key])

test_var_kwargs(farg=1, myarg2="two", myarg3=3)'''

'''
#when calling a function
#This special syntax can be used, not only in function definitions, but also when calling a function
def test_var_args_call(arg1, arg2, arg3):
    print "arg1:", arg1
    print "arg2:", arg2
    print "arg3:", arg3

args = ("two", 3)
test_var_args_call(1, *args)

def test_var_args_call(arg1, arg2, arg3):
    print "arg1:", arg1
    print "arg2:", arg2
    print "arg3:", arg3

kwargs = {"arg3": 3, "arg2": "two"}
test_var_args_call(1, **kwargs)

test_var_args_call(1, "two", 3)'''


'''def my_decorator(funcao):
    #A instructive decorator.

    def wrapper(*args, **kwargs):
        #argumento de antes
        print "This is executed before {}".format(funcao.__name__)
        #argumento de depois
        retorno = funcao(*args, **kwargs)
        print "This is executed after {}".format(funcao.__name__)
        return retorno

    return wrapper

@my_decorator
def sum(a,b):
    return a+b

result = sum(2, b=3)
print result'''

'''def meu_decorador(funcao):
    def decorador(*args,**kargs):
        print "teste antes"
        retorno = funcao(*args,**kargs)
        print "teste depois"
        return retorno
    return decorador

@meu_decorador
def sum(a,b):
    return a+b

result = sum(2,b=3)
print result'''

'''class Memoizer(object): #Caches the result of a function.
    def __init__(self, function):
        self.function = function
        self.__name__ = function.__name__
        self.__doc__ = function.__doc__
        self.cached_values = {}
    def __call__(self, *fn_args,**fn_kwargs): #Wrapper for calling the Cached Function.
        assert not fn_args, ("CachedMethod cannot be used with positional arguments.")
        kwargs_sig = self.kwargs_signature(**fn_kwargs)
        if kwargs_sig not in self.cached_values:
            print "Calculating new value."
            self.cached_values[kwargs_sig] = self.function(**fn_kwargs )
        else:
            print "Returning cached value."
        return self.cached_values[kwargs_sig]
    def kwargs_signature(self, **fn_kwargs): #returns kwargs signature--an immutable, given a set of kwargs.
        tp = tuple([v for k,v in sorted(fn_kwargs.items())])
        return str(tp.__hash__())
    def clear(self, **fn_kwargs): #clears the cached data.
        if not fn_kwargs: #clear all if a set of kwargs was not specified.
            self.cached_values = {}
        else: #otherwise just clear the value for the specified kwargs combination.
            kwargs_sig = self.kwargs_signature(**fn_kwargs)
            self.cached_values.pop(kwargs_sig, None)'''

'''class meu_decorador(object):
    def __init__(self, f):
        print "chamada de dentro da funcao meu_decorador.__init__()"
        f()
    def __call__(self):
        print "chamada de dentro da funcao meu_decorador.__call__()"

@meu_decorador
def minha_funcao():
    print "chamada de dentro da funcao minha_funcao()"

minha_funcao()'''

'''class meu_decorador(object):
    def __init__(self, f):
        print "chamada de dentro da funcao meu_decorador.__init__()"
        self.f = f
    def __call__(self):
        print "chamada de dentro da funcao meu_decorador.__call__()"

@meu_decorador
def minha_funcao():
    print "chamada de dentro da funcao minha_funcao()"

minha_funcao()'''

"""y = 63
y = y >> 1
print y
#print y%2"""

"""while True:
    print "ok"""""


'''x=0
y=1

def fun_a(node):
    if node == 1: return None
    else: return "oh boy!"
    return None

def fun_b(x,y):
    if fun_a(x) == None: print "halt"
    else: print fun_a(x)

fun_b(x,y)'''

'''
rednodes = []

while len(rednodes)>0:
    a = rednodes.pop()
    print a
'''

'''first_list = [1,2,3]

second_list = [3,4,5]

print set(second_list)

print set(first_list)

print first_list + list(set(second_list) - set(first_list))'''

#print chr(97)

'''import scipy;
#a=[1,2,4,3,2,1];
a = [8969, 10783, 6779, 641, 242, 8300, 10004, 12049, 5174, 10455, 8831, 1069, 2922, 2973, 3233, 6440, 3809, 821, 226, 9829, 1031, 8421, 1953, 940, 9741, 5194, 2677, 8316, 4178, 179, 252, 293, 1160, 10890, 6777, 11550, 5803, 1799, 5036, 3251, 5742, 2799, 7501, 7302, 475, 2186, 8949, 6660, 3637, 7033, 4661, 7902, 4774, 602, 1889, 9466, 11970, 10695, 7428, 5320, 887, 10666, 5848, 1212, 2268, 3169, 835, 4000, 11394, 324, 6198, 4659, 4942, 4966, 2741, 10901, 5056, 2048, 6615, 7209, 541, 1461, 11856, 11512, 11762, 6271, 3643, 1875, 1998, 1953, 1984, 10114, 3217, 1214, 1262, 7726, 104, 11975, 974, 7483, 8073, 648, 7954, 3323, 1782, 290, 4587, 480, 3554, 3738, 810, 1834, 1270, 7160, 3999, 166, 533, 12053, 9326, 11758, 2437, 461, 7581, 8945, 1974, 1323, 11086, 215, 9519, 3784, 10869, 7177, 1932, 1258, 745, 1340, 3906, 7638, 9528, 260, 1296, 2553, 728, 7728, 2260, 1238, 3974, 5042, 2791, 8101, 357, 423, 3532, 6018, 339, 10280, 8776, 6627, 10733, 5482, 2238, 11702, 649, 10638, 635, 1664, 10631, 136, 2740]
print(scipy.mean(a));'''

'''H = [[12, 11, 0, 14, 19, 22, 30], [1, 2]]
i = 0
#print H
print H.pop()[1], H
#print H[i][1]'''

import numpy
#numpy.zeros ([3,2])e = d
#numpy.ones([3,2])d+=f
#print 'teste'

p=numpy.zeros([3,2])
print p
p[0,1] = 8.
p[2,1] = 7.
print p

p = 1. + 2.*p
print p