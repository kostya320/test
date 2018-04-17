#-------------------------------------
#	Нет тут майнкрафта
#-------------------------------------
import random

a = 10
b = 12

def add(a, b):
 return a+b

def func(func, a, b):
 return func(func(a, b), func(a, b))


func(add, a, b)
