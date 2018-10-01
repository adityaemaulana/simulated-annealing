import math
import numpy as np
import plotly as py
import plotly.graph_objs as go

# calculate objective function
def objective(x1 ,x2):
    return -(abs(math.sin(x1) * math.cos(x2) * math.exp(abs(1 - (math.sqrt(x1*x1 + x2*x2) / math.pi)))))

# generate a solution Matrix
def solMatrix():
    mX = np.arange(-10.0, 10.0, 0.1)
    mY = np.arange(-10.0, 10.0, 0.1)
    mZ = []

    for i in range(len(mX)):
        mSeq = []
        for j in range(len(mY)):
            mSeq.append(objective(mX[i], mY[j]))
        mZ.append(mSeq)
       
    return mZ

# using contour for visualizing the solution
def visualize():
    mx = np.arange(-10.0, 10.0, 0.1)
    my = np.arange(-10.0, 10.0, 0.1)
    mz = solMatrix()

    data = [
        go.Contour(
            z = mz,
            x = mx,
            y = my,
            colorscale='Jet'
        )
    ]

visualize()