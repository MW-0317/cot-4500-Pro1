# Precursor
To be honest I am a bit confused on how the folder structure is utilized and how functions are tested. Note that the reason this was done was because I was short on time from procrastination so I apologize.

# To Run
In this directory: `py src/main/assignment_1.py`. This should output example outputs for the given functions below.

# Documentation
``root_two_approx(tol = 0.000001, x0=1.5)``
**tol** - The allowed tolerance.
**x0** The starting value.

returns null, instead prints out number of iterations it took, alongside the values.

``bisect(tol, a, b, max, f)``
**tol** - The allowed tolerance.
**a** - left approximation.
**b** - right approximation.
**max** - max number of allowed iterations.
**f** - a function with a single number input and a single number output.

returns a tuple like the following: (the approximate value, the number of iterations).

``fixed_point(tol, x0, max, f)``
**tol** - The allowed tolerance.
**x0** The starting value.
**max** - max number of allowed iterations.
**f** - a function with a single number input and a single number output.

returns a tuple like the following: (the approximate value, the number of iterations). If the number of iterations is -1 then there was a failure.

``newtons(tol, x0, max, f, df)``
**tol** - The allowed tolerance.
**x0** The starting value.
**max** - max number of allowed iterations.
**f** - a function with a single number input and a single number output.
**df** - f's derivative.

returns a tuple like the following: (the approximate value, the number of iterations). If the number of iterations is -1 then there was a failure.