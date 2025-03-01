import os
import matplotlib.pyplot as plt
import psycopg2
import numpy as np
from psycopg2 import pool
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()
# Get the database URL from the environment variables
DATABASE_URL = os.getenv("DATABASE_URL")
# Create a connection pool
connection_pool = pool.SimpleConnectionPool(1, 10, dsn=DATABASE_URL, sslmode='require')
# Check if the connection pool was created successfully
if(connection_pool):
    print("Connection Pool created successfully")


#Select all x values from the dataset
#return a list of tuples of x values in the form x[row number][0]
def fetch_x():
    try: 
        conn = connection_pool.getconn()

        if (conn):
            print("connected")

        cur = conn.cursor()
        cur.execute("SELECT x_value FROM datapoint;")
        xValue = cur.fetchall()
        cur.close()
        connection_pool.putconn(conn)
    except:
        print ("fetch x Error")
    
    return xValue

#Select all y values from the dataset
#return a list of tuples of y values in the form y[row number][0]
def fetch_y():
    try: 
        conn = connection_pool.getconn()

        if (conn):
            print("connected")

        cur = conn.cursor()
        cur.execute("SELECT y_value FROM datapoint;")
        yValue = cur.fetchall()
        cur.close()
        connection_pool.putconn(conn)
    except:
        print ("fetch y Error")
    
    return yValue

#Insert a new point into the dataset
#return a string indicating the point was successfully inserted
def insert_point(x, y):
    try: 
        conn = connection_pool.getconn()
        
        if (conn):
            print("connected")
        
        cur = conn.cursor()
        cur.execute("INSERT INTO datapoint (x_value, y_value) VALUES (%s, %s);", (x, y))
        conn.commit()
        cur.close()
        connection_pool.putconn(conn)
    except:
        print ("insert Error")
        
    return "successfully inserted point"

#Update a point in the dataset
#return a string indicating the point was successfully updated
def update_point(id, x, y):
    try: 
        conn = connection_pool.getconn()

        if (conn):
            print("connected")

        cur = conn.cursor()
        cur.execute("UPDATE datapoint SET x_value = %s, y_value = %s WHERE id = %s;", (x, y, id))
        conn.commit()
        cur.close()
        connection_pool.putconn(conn)
    except:
        print ("update Error")
    
    return "successfully updated point " + id

#Delete a point from the dataset
#return a string indicating the point was successfully deleted
def delete_point(id):
    try: 
        conn = connection_pool.getconn()
    
        if(conn):
            print("connected")
            
        cur = conn.cursor()
        cur.execute("DELETE FROM datapoint WHERE id = %s;", (id,))
        conn.commit()
        cur.close()
        connection_pool.putconn(conn)
    except:
        print ("delete Error")
    
    return "successfully deleted point " + id


#Returns means as a list of size 1 with x and y called mean
def mean():
    try: 
        conn = connection_pool.getconn()
        
        if (conn):
            print("connected")
        
        cur = conn.cursor()
        cur.execute("SELECT AVG(x_value), AVG(y_value) FROM datapoint;")
        mean = cur.fetchone()
        cur.close()
        connection_pool.putconn(conn)
    except:
        print ("Mean Error")
        
    return mean

#returns the median as a list of size 1 with x and y called median
def median():
    try: 
        conn = connection_pool.getconn()
        
        if (conn):
            print("connected")
        
        cur = conn.cursor()
        ## if the num of rows N is odd, then fetch ((N+1)/2)th row
        ## if N is even, then fetch Nth & (N+1)th rows and calculate their average
        cur.execute("SELECT COUNT(id) FROM datapoint;")
        count = cur.fetchone()[0]
        
        if(count % 2 == 0):
            cur.execute("SELECT x_value, y_value FROM datapoint WHERE id = %s OR id = %s ORDER BY id;", (count//2, (count+1)//2,))
            medianlist = cur.fetchall()
            median = [(medianlist[0][0] + medianlist[1][0])/2, (medianlist[0][1] + medianlist[1][1])/2]
        else:
            cur.execute("SELECT x_value, y_value FROM datapoint WHERE id = %s;", ((count+1)//2,))
            median = cur.fetchone()
        
        cur.close()
        connection_pool.putconn(conn)
    except:
        print ("median Error")
        
    return median

def mode():
    try: 
        conn = connection_pool.getconn()
        
        if (conn):
            print("connected")
        
        cur = conn.cursor()
        cur.execute("SELECT x_value, y_value, COUNT(x_value) FROM datapoint GROUP BY x_value, y_value ORDER BY COUNT(x_value) DESC LIMIT 1;")
        mode = cur.fetchone()
        cur.close()
        connection_pool.putconn(conn)
    except:
        print ("mode Error")   
        
    return mode

def best_fit():
    try: 
        conn = connection_pool.getconn()
    
        if (conn):
            print("connected")   
            
        cur = conn.cursor()
        cur.execute("SELECT COUNT(id) FROM datapoint;")
        count = cur.fetchone()[0]
        
        cur.execute("SELECT x_value, y_value FROM datapoint;")
        points = cur.fetchall()
        
        bestfit = []
        means = mean()
        for i in range(count):
            bestfit[i] = [points[0][i]- means[0], points[1][i]- means[1]] ## list of differences between the point and the mean
        

        m = (count*sum[3] - sum[0]*sum[1]) / (count*sum[2] - sum[0]*sum[0])
        b = (sum[1] - m*sum[0]) / count
        
        cur.close()
        connection_pool.putconn(conn)
    except:
        print ("best fit line Error")
        
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
    plt.plot(x, y)

    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Plot Example")

    plt.show()


main()