import math

def root_two_approx():
    x0 = 1.5
    tol = 0.000001

    i = 0
    diff = x0
    x = x0

    print(i + " : " + x)

    while (diff >= tol):
        i += 1
        y = x
        x = (x / 2) + (1 / x)
        print(i + " : " + x)
        diff = abs(x - y)

    print("Convergence after", i, "iterations")

def bisect(tol, a, b, max, f):
    i = 0

    while (math.fabs(b - a) > tol and i < max):
        i += 1
        p = (a + b) / 2

        if (f(a) < 0 and f(p) > 0) or (f(a) > 0 and f(p) < 0):
            b = p
        else:
            a = p
    
    return p, i

def newtons(tol, pprev, max, f, df):
    i = 1
    while (i <= max ):
        if (df(pprev) != 0):
            pnext = pprev - f(pprev) / df(pprev)
            if (math.fabs(pnext - pprev) < tol):
                return pnext, i
            i += 1
            pprev = pnext
        else:
            return -1, -1
    return -1, -1