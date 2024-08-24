import pandas as pd
from sympy import symbols, Sum, diff, lambdify, Function

# Import points from CSV
points = list(pd.read_csv("https://bit.ly/2KF29Bd").itertuples())

# Define symbols
m, b, i, n = symbols('m b i n')
x, y = symbols('x y', cls=Function)

# Define sum of squares
sum_of_squares = Sum((m*x(i) + b - y(i)) ** 2, (i, 0, n))

# Compute partial derivatives
d_m = diff(sum_of_squares, m).subs(n, len(points) - 1).doit().replace(x, lambda i: points[i].x).replace(y, lambda i: points[i].y)
d_b = diff(sum_of_squares, b).subs(n, len(points) - 1).doit().replace(x, lambda i: points[i].x).replace(y, lambda i: points[i].y)

# Compile using lambdify for faster computation
d_m = lambdify([m, b], d_m)
d_b = lambdify([m, b], d_b)

# Initialize parameters
m = 0.0
b = 0.0

# Learning rate
L = 0.001

# Number of iterations
iterations = 100_000

# Perform Gradient Descent
for i in range(iterations):
    m -= d_m(m, b) * L
    b -= d_b(m, b) * L

# Print the resulting linear equation
print("y = {0}x + {1}".format(m, b))