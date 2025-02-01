import math

def root_two_approx(tol = 0.000001, x0=1.5):
    i = 0
    diff = x0
    x = x0

    print(i, ":", x)

    while (diff >= tol):
        i += 1
        y = x
        x = (x / 2) + (1 / x)
        print(i, ":", x)
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

def fixed_point(tol, x0, max, f):
    i = 1
    while i <= max:
        x = f(x0)
        # print(i, ":", x)
        if (math.isnan(x)):
            return -1, -1
        
        if (math.fabs(x - x0) < tol):
            return x, i
        
        i += 1
        x0 = x
    return -1, -1

def newtons(tol, x0, max, f, df):
    i = 1
    while (i <= max ):
        if (df(x0) != 0):
            x = x0 - f(x0) / df(x0)
            if (math.fabs(x - x0) < tol):
                return x, i
            i += 1
            x0 = x
        else:
            return -1, -1
    return -1, -1

if __name__ == "__main__":
    print("Root Two Approximation with tolerance 0.000001, and starting value 1.5")
    root_two_approx()

    b_x, b_i = bisect(0.0001, -4, 7, 100, lambda x: x*x*x + 4*x*x - 10)
    print()
    print("Bisection (tol=0.0001, a=-4, b=7, max=100, f=lambda x: x*x*x + 4*x*x - 10)")
    print("\tx=" + str(b_x), "\tIterations:", b_i)

    print()
    print("The following are from the powerpoint slides (2.2, slide 15)")
    fi_x, fi_i = fixed_point(0.000001, 1.5, 50, lambda x: x - x*x*x - 4*x*x + 10)
    print()
    print("Fixed Point Approximation (tol=0.000001, x0=1.5, max=50, f=lambda x: x - x*x*x - 4*x*x + 10)")
    print("This should diverge and thus iterations is -1")
    print("\tx=" + str(fi_x), "\tIterations:", fi_i)

    fi_x, fi_i = fixed_point(0.000001, 1.5, 50, lambda x: (10 - x*x*x)**(1/2) / 2)
    print()
    print("Fixed Point Approximation (tol=0.000001, x0=1.5, max=50, f=lambda x: (10 - x*x*x)**(1/2) / 2)")
    print("\tx=" + str(fi_x), "\tIterations:", fi_i)

    n_x, n_i = newtons(0.0001, -4, 100, lambda x: x*x*x + 4*x*x - 10, lambda x: 3*x*x + 8*x)
    print()
    print("Newtons (tol=0.0001, x0=-4, max=100, f=lambda x: x*x*x + 4*x*x - 10)")
    print("\tx=" + str(n_x), "\tIterations:", n_i)
    