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
    if ya * yb < 0 :
        while error > tolerance:
            c = (a + b)/2
            yc = f(c)
            if yc == 0 :
                approx.append(c)
                err.append(0)
                break
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
    elif yb == 0 :
        return(f"The root of this equation is b : {b}")
    else :
        return (f"The is no root of this equation between the interval {a} -> {b}")
        
def FalsePositive(a,b):
    ya = f(a)
    yb = f(b)
    approx = []
    err = []
    error = 100
    prevC  = None
    if ya * yb < 0 :
        while error > tolerance:
            c = (a * yb - b * ya)/ (yb - ya)
            yc = f(c)
            if yc == 0 :
                approx.append(c)
                err.append(0)
                break
            elif ya * yc < 0 :
                b = c
                yb = yc
            else :
                a = c
                ya = yc
            if prevC is None:
                error = abs(c)
            else :
                error = abs(prevC - c)            
            approx.append(c)
            err.append(error)
            prevC = c
        return(pd.DataFrame({ "Approximations" : approx, "Errors" : err}))
    elif ya == 0 :
        return(f"The root of this equation is a : {a}")
    elif yb == 0 :
        return(f"The root of this equation is b : {b}")
    else :
        return (f"The is no root of this equation between the interval {a} -> {b}")

def Newton(x):

    if f(x) == 0 :
        return (f"The root of this equation is : {x}")

    error = abs(x)
    prevX = x

    approx = [x]
    err = [error]

    while error > tolerance:
        x = x - (f(x)/df(x))

        error = abs(prevX - x)
        approx.append(x)
        err.append(error)
        prevX = x
    
    return(pd.DataFrame({"Approximations" : approx, "Errors" : err}))

def Secant(x0, x1):
 
    approx = []
    err = []
    error = abs(x1 - x0)
    while error > tolerance:
        m = (f(x1) - f(x0))/ (x1 - x0)
        a = x0
        x0 = x1
        x1 = a - f(a)/m

        error = abs(x1 - x0)
        approx.append(x1)
        err.append(error)

    return(pd.DataFrame({"Approximations" : approx, "Errors" : err}))

# def FixedPoint(x0):

#     approx = []
#     err  =[]

#     while error > tolerance :
#         x = g(x0)
#         error = abs(x - x0)
#         approx.append(x)
#         err.append(error)
#         x = x0

# print(bisection(1,3))
# print(FalsePositive(1,3))
# print(Newton(1))
print(Secant(1,3))