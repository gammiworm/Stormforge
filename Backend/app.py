import matplotlib.pyplot as plt
import numpy as np
from database import fetch_x, fetch_y, mean, median, mode

def best_fit(x, y):
    m, b = np.polyfit(x, y, deg=1)
    return m, b


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

    plt.show()


main()