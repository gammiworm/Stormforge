import matplotlib.pyplot as plt
import numpy as np
from database import fetch_x, fetch_y
from config import connection_pool

def best_fit(x, y):
    m, b = np.polyfit(x, y, deg=1)
    return m, b

def quadInterpolation(xValue, yValue):

    x = []
    y = []
    x2 = []
    y2 = []

    xValue2 = [x[0] for x in fetch_x()]
    yValue2 = [y[0] for y in fetch_y()]
    
    print("xValue2 == xValue ", xValue2 == xValue)
    print("yValue2 == yValue ", yValue2 == yValue)
    print("xValue2: ", xValue2)
    print("xValue: ", xValue)

    print("yValue: ", yValue)
    print("yValue2: ", yValue2)


    
    size=len(xValue)
    
    for row in range(size):

        x.append(np.array(xValue[row]))
        y.append(np.array(yValue[row]))

    size2=len(xValue2)
    for row in range(size2):

        x2.append(np.array(xValue2[row]))
        y2.append(np.array(yValue2[row]))
    print("Appended=====")
    print("x2 == x ", x2 == x)
    print("y2 == y ", y2 == y)
    print("x2: ", x2)
    print("x: ", x)

    print("y2: ", y2)
    print("y: ", y)
    # Sort x and y values based on x
    sorted_indices = np.argsort(x)
    x = np.array(x)[sorted_indices]
    y = np.array(y)[sorted_indices]
    
    sorted_indices2 = np.argsort(x2)
    x2 = np.array(x2)[sorted_indices2]
    y2 = np.array(y2)[sorted_indices2]
    print("Sorted=====")
    print("x2 == x ", x2 == x)
    print("y2 == y ", y2 == y)
    print("x2: ", x2)
    print("x: ", x)

    print("y2: ", y2)
    print("y: ", y)
    
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
        z = 5

    with open("output.txt", "a") as f:
        print(interpolated_points, file=f)
    print("interpolated_points: ", interpolated_points)
    
    interpolated_points2 = []
    if(x2[0] == x2[1]):
        m2 = (y2[1]-y2[0])/(0.1) # to avoid division by zero
        x_range2 = [x2[0]] * 50
        y_range2 = np.linspace(y2[0], y2[1], 50)
        interpolated_points2.extend(zip(x_range2, y_range2))
    else:
        m2 = (y2[1] - y2[0]) / (x2[1] - x2[0])
        x_range2 = np.linspace(x2[0], x2[1], 50)
        y_range2 = m2*(x_range2 - x2[0]) + y2[0]
        interpolated_points2.extend(zip(x_range2, y_range2))
    
    for i in range(1, size2 - 1):
        # if x[i] == x[i+1], then it is a vertical segment
        if x2[i] == x2[i+1]:
            m2 = (y2[i+1] - y2[i]) / (0.1)
            x_range2 = [x2[i]] * 50
            y_range2 = np.linspace(y2[i], y2[i + 1], 50)
            interpolated_points2.extend(zip(x_range2, y_range2))
            continue
       
    
        a2 = ((y2[i+1]-y2[i]) - m2*(x2[i+1]-x2[i]))/(x2[i+1]-x2[i])**2
        b2 = m2 - 2*a2*x2[i]
        c2 = y2[i+1] - a2*x2[i+1]**2 + 2*a2*x2[i]*x2[i+1] - m2*x2[i+1]
        x_range2 = np.linspace(x2[i], x2[i+1], 50)
        y_range2 = a2*(x_range2)**2 + b2*(x_range2) + c2
        interpolated_points2.extend(zip(x_range2, y_range2))
        m2 = 2*a2*x2[i+1] + b2

    print("interpolated_points2: ", interpolated_points2)

    return interpolated_points

def quadInterpolation2(xValue, yValue):

    x2 = []
    y2 = []

    xValue2 = [x[0] for x in fetch_x()]
    yValue2 = [y[0] for y in fetch_y()]
    
    size2=len(xValue2)
    for row in range(size2):

        x2.append(np.array(xValue2[row]))
        y2.append(np.array(yValue2[row]))
  

    sorted_indices2 = np.argsort(x2)
    x2 = np.array(x2)[sorted_indices2]
    y2 = np.array(y2)[sorted_indices2]
   
    
    interpolated_points2 = []
    if(x2[0] == x2[1]):
        m2 = (y2[1]-y2[0])/(0.1) # to avoid division by zero
        x_range2 = [x2[0]] * 50
        y_range2 = np.linspace(y2[0], y2[1], 50)
        interpolated_points2.extend(zip(x_range2, y_range2))
    else:
        m2 = (y2[1] - y2[0]) / (x2[1] - x2[0])
        x_range2 = np.linspace(x2[0], x2[1], 50)
        y_range2 = m2*(x_range2 - x2[0]) + y2[0]
        interpolated_points2.extend(zip(x_range2, y_range2))
    
    for i in range(1, size2 - 1):
        # if x[i] == x[i+1], then it is a vertical segment
        if x2[i] == x2[i+1]:
            m2 = (y2[i+1] - y2[i]) / (0.1)
            x_range2 = [x2[i]] * 50
            y_range2 = np.linspace(y2[i], y2[i + 1], 50)
            interpolated_points2.extend(zip(x_range2, y_range2))
            continue
       
    
        a2 = ((y2[i+1]-y2[i]) - m2*(x2[i+1]-x2[i]))/(x2[i+1]-x2[i])**2
        b2 = m2 - 2*a2*x2[i]
        c2 = y2[i+1] - a2*x2[i+1]**2 + 2*a2*x2[i]*x2[i+1] - m2*x2[i+1]
        x_range2 = np.linspace(x2[i], x2[i+1], 50)
        y_range2 = a2*(x_range2)**2 + b2*(x_range2) + c2
        interpolated_points2.extend(zip(x_range2, y_range2))
        m2 = 2*a2*x2[i+1] + b2

    print("interpolated_points2: ", interpolated_points2)
    with open("output.txt", "a") as f:  
        print("\n", file=f)

        
        print(interpolated_points2, file=f)
    return interpolated_points2

def mean(x, y):
    # Handle empty dataset
    if len(x)==0 or len(y)==0:
        print("No data points available.")
        mean = (None, None)  # Return None for both x and y if no data exists
    else:
        # Round the mean values to two decimal places
        mean = (round((sum(x) / len(x)), 2), round((sum(y) / len(y)), 2))

    return mean

def median(x, y):
    # Get the total number of points
    
    x.sort()
    y.sort()
    
    count = len(x)
    if count == 0:
        print("No data points available.")
        return None  # Return None if there are no rows

    # For even count, fetch the two middle rows and calculate the median
    if count % 2 == 0:
        medianlist =(x[(count//2)-1], y[(count//2)-1]), (x[count//2], y[count//2])
        median = [
            round((medianlist[0][0] + medianlist[1][0]) / 2, 2),  # Median for x_value
            round((medianlist[0][1] + medianlist[1][1]) / 2, 2)   # Median for y_value
        ]
    else:
        # For odd count, fetch the middle row
        result = (x[count // 2], y[count // 2])  # Get the middle element
        median = (round(result[0], 2), round(result[1], 2))  # Round the median values

    return median


def mode(x, y):
    x.sort()
    y.sort()
    y_count = 0
    x_count = 0
    x_id = None
    y_id = None
    temp_x_count = 0
    temp_y_count = 0
    for i in range(len(x)):
        temp_x_count+=1
        if i == len(x)-1 or x[i] != x[i+1]:
            if temp_x_count > x_count:
                x_count = temp_x_count
                x_id = x[i]
            elif temp_x_count == x_count:
                x_id = None
            temp_x_count = 0
    for i in range(len(y)):
        temp_y_count+=1
        if i == len(y)-1 or y[i] != y[i+1]:
            if temp_y_count > y_count:
                y_count = temp_y_count
                y_id = y[i]
            elif temp_y_count == y_count:
                y_id = None
            temp_y_count = 0
    
    result = (x_id, y_id)

    return result

