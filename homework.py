import numpy as np 
import pandas as pd
import sympy as sp
import math

tolerance = 0.00002

def f(x) :
    return math.pow(x,4) - 2 * math.pow(x,3) - 10

def df(x) :
    return 4*math.pow(x,3) - 6 * math.pow(x,2)

def g(x):
    return None

def bisection(a,b):
    ya = f(a)
    yb = f(b)
    approx = []
    err = []
    error = 100
    if ya < 0 and yb > 0 :
        while error > tolerance:
            c = (a + b)/2
            yc = f(c)
            if yc == 0 :
                a = c
                b = c
            elif yc < 0 :
                a = c
            elif yc > 0 :
                b = c
            ya = f(a)
            yb = f(b)
            error = abs(yb-ya) / 2
            approx.append(c)
            err.append(error)
        return(pd.DataFrame({ "Approximations" : approx, "Errors" : err}))
    elif ya == 0 :
        return(f"The root of this equation is a : {a}")
    else :
        return(f"The root of this equation is b : {b}")
        
def FalsePositive(a,b):
    return None


print(bisection(1,3))