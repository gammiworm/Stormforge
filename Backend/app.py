import os
import matplotlib.pyplot as plt
import psycopg2
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

def fetch_x():
    try: 
        conn = psycopg2.connect(DATABASE_URL)

        cur = conn.cursor()
        cur.execute("SELECT x_value FROM datapoint;")
        xValue = cur.fetchall()
    except:
        print ("Error")
    
    return xValue

def fetch_y():
    try: 
        conn = psycopg2.connect(DATABASE_URL)

        cur = conn.cursor()
        cur.execute("SELECT y_value FROM datapoint;")
        yValue = cur.fetchall()
    except:
        print ("Error")
    
    return yValue


def main():
    x = []
    y = []
    
    xValue = fetch_x()
    yValue = fetch_y()
    size=len(xValue)
    
    for row in size:
        x[row]=xValue[row][0]
        y[row]=yValue[row][0]
    plt.scatter(x, y, color='red')

    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Scatter Plot Example")

    plt.show()



