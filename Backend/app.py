import matplotlib.pyplot as plt
import numpy as np
from database import fetch_x, fetch_y, mean, median, mode

def best_fit(x, y):
    m, b = np.polyfit(x, y, deg=1)
    return m, b

def quadInterpolation():
    x = []
    y = []
    xValue = fetch_x()
    yValue = fetch_y()
    size=len(xValue)
    for row in range(size):
        x.append(np.array(xValue[row][0]))
        y.append(np.array(yValue[row][0]))

    interpolated_points = []
    m = (y[1] - y[0]) / (x[1] - x[0])
    f = m(x-x[0]) + y[0]

    for i in range(size - 1):
        # if x[i] == x[i+1], then it is a vertical segment
        if x[i] != x[i+1]:
            a = (m*(x[i+1]-x[i])+(y[i+1]-y[i]))/(x[i+1]-x[i])**2
            b = m - 2*a*x[i+1]
            c = y[i+1] - a*x[i+1]**2 - m*x[i+1]
            x_range = np.linspace(x[i], x[i+1], 50)
            y_range = a*(x_range)**2 + b*(x_range) + c
            interpolated_points.extend(zip(x_range, y_range))
            m = 2*a*x[i+1] + b

    return interpolated_points

def main():
    x = []
    y = []
    
    xValue = fetch_x()
    yValue = fetch_y()
    size=len(xValue)
    
    for row in range(size):
        x.append(np.array(xValue[row][0]))
        y.append(np.array(yValue[row][0]))

    m, b = best_fit(x, y)
    xseq = np.linspace(0, 10, num=100)
    plt.scatter(x, y)
    plt.plot(b + m*xseq)


    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Plot Example")

    #plt.show()


main()