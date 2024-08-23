import pandas as pd
# Import points
points = pd.read_csv('https://bit.ly/3goOAnt', delimiter=",").itertuples()
# Test with a given line
m = 1.93939
b = 4.73333
# Calculate the residuals
for p in points:
    y_actual = p.y
    y_predict = m*p.x + b
    residual = y_actual - y_predict
    print(residual)
'''
Points above the line will have a positive residual, and points below the line will
have a negative residual. In other words, it is the subtracted difference between the
predicted y-values (derived from the line) and the actual y-values (which came from
the data). Another name for residuals are errors, because they reflect how wrong our
line is in predicting the data.
'''