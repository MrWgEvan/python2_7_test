#coding=utf-8
print ('hello,world')
print ("hello")
#10
#52.4E-4
name = "wg"
age  = 23
print ("{0}'s year is {1}".format(name,age))
print ("""sadsadsadsda'ssadsadds'dsadsad
sadsadsadsadasd""")

print ('{0:.3f}'.format(1.0/3))
print ('{0:_^18}'.format("hello"))
print ("{name} is {age} year".format(name = "wg",age='saa545'))

print ('a')
print ('b')
#print ('a', end = '')
#print ('b', end = '')
print ("askkjashkjhasdjkhkjdsha\ngsadjsagdjadg")
print ('what\'s your name?')
print ("hahhahahhahaha\
ddddddddddddddddddddddd")

for i in range(1,5):
    print (i)
else:
    print ('game over')

range(1,9,3)

def say(message,time = 1):
    print (message * time)
say("hello")
say("world",5)

def max_value(x,y):

    """Dsjhfjkdshjhfjdshfjhdjskh.

    Jskdfhdsjkhfjkdjshfjkhkhds."""
    x = int(x)
    y = int(y)
    if(x > y):
        print (x,' is max')
    elif(x < y):
        print (y,'is max')
    else:
        print ('x = y')
max_value(3,5)
#左右分别两个_
print (max_value.__doc__)

import sys
print ('the argument is : ')
for i in sys.argv:
    print (i)
print ("\n\nthe path is ", sys.path, '\n')
print (dir())
#sqrt(15)

from math import sqrt
print (int(sqrt(16)))