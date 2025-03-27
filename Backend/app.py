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

    # Sort x and y values based on x
    sorted_indices = np.argsort(x)
    x = np.array(x)[sorted_indices]
    y = np.array(y)[sorted_indices]
    
    interpolated_points = []
    if(x[0] == x[1]):
        m = (y[1]-y[0])/(0.1) # to avoid division by zero
        x_range = [x[0]] * 50
        y_range = np.linspace(y[0], y[1], 50)
        interpolated_points.extend(zip(x_range, y_range))
    else:
        m = (y[1] - y[0]) / (x[1] - x[0])
        x_range = np.linspace(x[0], x[1], 50)
        y_range = m*(x_range - x[0]) + y[0]
        interpolated_points.extend(zip(x_range, y_range))
    
    for i in range(1, size - 1):
        # if x[i] == x[i+1], then it is a vertical segment
        if x[i] == x[i+1]:
            m = (y[i+1] - y[i]) / (0.1)
            x_range = [x[i]] * 50
            y_range = np.linspace(y[i], y[i + 1], 50)
            interpolated_points.extend(zip(x_range, y_range))
            continue
       
    
        a = ((y[i+1]-y[i]) - m*(x[i+1]-x[i]))/(x[i+1]-x[i])**2
        b = m - 2*a*x[i]
        c = y[i+1] - a*x[i+1]**2 + 2*a*x[i]*x[i+1] - m*x[i+1]
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