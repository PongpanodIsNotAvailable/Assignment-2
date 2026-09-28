import pandas as pd
import math

tolerance = 0.00002

def f(x) :
    return - 20 + 3*(x**(-1)) + 4*(x**(-2))+ 5*(x**(-3))+6*(x**(-4))+7*(x**(-5)) 
def df(x) :
    return - 3*(x**(-2)) - 8*(x**(-3)) - 15*(x**(-4)) - 24*(x**(-5)) - 35*(x**(-6))

def g(x):
    return ( (3/20)*(x**4) + (4/20)*(x**3) + (5/20)*(x**2) + (6/20)*(x) + (7/20))**(1/5)

def bisection(a,b):
    ya = f(a)
    yb = f(b)
    approxX = []
    approxR = []
    err = []
    error = 100
    if ya * yb < 0 :
        while error > tolerance:
            c = (a + b)/2
            yc = f(c)
            if yc == 0 :
                approxX.append(c)
                approxR.append(c-1)
                err.append(0)
                break
            elif ya * yc < 0 :
                b = c
            else :
                a = c
            ya = f(a)
            yb = f(b)
            error = abs(b-a) / 2
            approxX.append(c)
            approxR.append(c-1)
            err.append(error)
        return([pd.DataFrame({ "Approximations of X " : approxX, " R " : approxR,"Errors" : err}), c-1])
    elif ya == 0 :
        return(f"The root of this equation is a : {a}")
    elif yb == 0 :
        return(f"The root of this equation is b : {b}")
    else :
        return (f"The is no root of this equation between the interval {a} -> {b}")
        
def FalsePositive(a,b):
    ya = f(a)
    yb = f(b)
    approxX = []
    approxR = []
    err = []
    error = 100
    prevC  = None
    if ya * yb < 0 :
        while error > tolerance:
            c = (a * yb - b * ya)/ (yb - ya)
            yc = f(c)
            if yc == 0 :
                approxX.append(c)
                approxR.append(c-1)
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
            approxX.append(c)
            approxR.append(c-1)
            err.append(error)
            prevC = c
        return([pd.DataFrame({ "Approximations of X " : approxX, " R " : approxR,"Errors" : err}), c-1])
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

    approxX = [x]
    approxR = [x-1]
    err = [error]

    while error > tolerance:
        x = x - (f(x)/df(x))

        error = abs(prevX - x)
        approxX.append(x)
        approxR.append(x-1)
        err.append(error)
        prevX = x
    
    return([pd.DataFrame({ "Approximations of X " : approxX, " R " : approxR,"Errors" : err}), x-1])

def Secant(x0, x1):
 
    approxX = []
    approxR = []
    err = []
    error = abs(x1 - x0)
    while error > tolerance:
        m = (f(x1) - f(x0))/ (x1 - x0)
        a = x0
        x0 = x1
        x1 = a - f(a)/m

        error = abs(x1 - x0)
        approxX.append(x1)
        approxR.append(x1-1)
        err.append(error)

    return([pd.DataFrame({ "Approximations of X " : approxX, " R " : approxR,"Errors" : err}), x1-1])


def FixedPoint(x0):

    if f(x0) == 0 :
        return (f"The root of this equation is : {x0}")

    error = 1000
    approxX = []
    approxR = []
    err  = []

    while error > tolerance :
        x = g(x0)
        error = abs(x - x0)
        approxX.append(x)
        approxR.append(x-1)
        err.append(error)
        x0 = x

    return([pd.DataFrame({ "Approximations of X " : approxX, " R " : approxR,"Errors" : err}), x-1])

print(f"\nTolerance for error is set as <= {tolerance:5f}")

bisec = bisection(1,1.2)
print("\n-------- USING BISECTION METHOD ---------\n")
print(bisec[0])
print(f"\n From Bisection method, the value of IRR is : {bisec[1]}\n")


falsi = FalsePositive(1,1.2)
print("\n-------- USING FALSE POSITIVE METHOD ---------\n")
print(falsi[0])
print(f"\n From False Positive method, the value of IRR is : {falsi[1]}\n")

newt = Newton(1.2)
print("\n-------- USING NEWTON-RAPHSON METHOD ---------\n")
print(newt[0])
print(f"\n From Newton-Raphson method, the value of IRR is : {newt[1]}\n")

seca = Secant(1.2,1.1)
print("\n-------- USING SECANT METHOD ---------\n")
print(seca[0])
print(f"\n From Secant method, the value of IRR is : {seca[1]}\n")

fixp = FixedPoint(1.2)
print("\n-------- USING FIXED-POINT METHOD ---------\n")
print(fixp[0])
print(f"\n From Fixed-Point method, the value of IRR is : {fixp[1]}\n")
