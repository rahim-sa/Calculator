# calculator.py
#import time
#import pandas as pd
#__version__ = "0.1.0"


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b

def division(a, b):
	if b != 0:
		return a/b
	else:
		print("b shouldn't be equal zero")

print(add(23,45))
print(subtract(23,45))
print(division(23,45))
