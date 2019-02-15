#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$13/09/2012 09:11:53$"

import csv
import sys

def listPopularName():
    namelist = []
    nameunit = ()
    file = "C://YOB1995.txt"
    babies = open(file, 'rb')
    babyname = ''
    numname = 0
    try:
        reader = csv.reader(babies, delimiter=',', quotechar='"')
        for row in reader:
            if row[1] == "F":
                try:
                    numname  = int(row[2])
                except ValueError:
                    numname  = 999999 #prevents bad entries
                babyname = row[0]
                nameunit = (numname, babyname)
                namelist.append(nameunit)
    finally:
        babies.close
    return namelist

def mostPopularName():
    females = listPopularName()
    print females
    alfa = sorted(females, key=lambda girl: girl[0])
    for girl in alfa:
        print girl
    
mostPopularName()

def popularName():
    file = "C://YOB1995.txt"
    babies = open(file, 'rb')
    babyname = ''
    numname = 0
    try:
        reader = csv.reader(babies, delimiter=',', quotechar='"')
        for row in reader:
            if row[1] == "F":
                if row[2] > numname:
                    babyname = row[0]
                    numname  = row[2]
                    #print "name: ", babyname, "numname: ", numname
    finally:
        babies.close
    return [babyname, numname]

#print popularName()

def readfile():
    file = "C://YOB1995.txt"
    babies = open(file, 'rb')
    try:
        reader = csv.reader(babies, delimiter=',', quotechar='"')
        for row in reader:
            print row
    finally:
        f.close

#readfile()

'''class csv.DictReader(csvfile, fieldnames=None, restkey=None, restval=None,
                        dialect='excel', *args, **kwds)
Create an object which operates like a regular reader but maps the information
read into a dict whose keys are given by the optional fieldnames parameter.
If the fieldnames parameter is omitted, the values in the first row of the
csvfile will be used as the fieldnames. If the row read has more fields than
the fieldnames sequence, the remaining data is added as a sequence keyed by the
value of restkey. If the row read has fewer fields than the fieldnames sequence,
the remaining keys take the value of the optional restval parameter.
Any other optional or keyword arguments are passed to the underlying reader
instance.

def readnames(f):
    # Read mode opens a file for reading only.
    #string = []
    line = []
    #lines = []
    try:
        f = open("C://YOB1995.txt", "r")
        print 'file opened'
        #string = f.read() #Read the entire contents of a file at once.
        #print string
        line = f.readline()
        print line
        #lines = f.readlines() #Read all the lines into a list
        #print lines
        f.close()
        return 'string'
    except IOError:
        print 'IO error'
'''
z = open("yob1995.txt", "r")
maxname = "none"
maxval = 0
max2name = "none"
max2val = 0
for line in f:
        (name, sex, count) = line.rsplit(",")
        count = int(count)
        if sex == "F":
            if count == maxval:
                max2name = maxname
                max2val = maxval
                maxval = count
                maxname = name
            elif count > max2val:
                max2name = name
                max2val = count
print maxname, max2name
print maxval, max2val