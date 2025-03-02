from config import connection_pool

def fetch_x():
    try:
        conn = connection_pool.getconn()
        if conn:
            print("connected")
        cur = conn.cursor()
        cur.execute("SELECT x_value FROM datapoint;")
        xValue = cur.fetchall()
        cur.close()
        connection_pool.putconn(conn)
    except:
        print("fetch x Error")
    return xValue

def fetch_y():
    try:
        conn = connection_pool.getconn()
        if conn:
            print("connected")
        cur = conn.cursor()
        cur.execute("SELECT y_value FROM datapoint;")
        yValue = cur.fetchall()
        cur.close()
        connection_pool.putconn(conn)
    except:
        print("fetch y Error")
    return yValue

def mean():
    try:
        conn = connection_pool.getconn()
        if conn:
            print("connected")
        cur = conn.cursor()
        cur.execute("SELECT AVG(x_value), AVG(y_value) FROM datapoint;")
        mean = cur.fetchone()
        cur.close()
        connection_pool.putconn(conn)
    except:
        print("Mean Error")
    return mean

def median():
    try:
        conn = connection_pool.getconn()
        if conn:
            print("connected")
        cur = conn.cursor()
        cur.execute("SELECT COUNT(id) FROM datapoint;")
        count = cur.fetchone()[0]
        if count % 2 == 0:
            cur.execute("SELECT x_value, y_value FROM datapoint WHERE id = %s OR id = %s ORDER BY id;", (count//2, (count+1)//2,))
            medianlist = cur.fetchall()
            median = [(medianlist[0][0] + medianlist[1][0])/2, (medianlist[0][1] + medianlist[1][1])/2]
        else:
            cur.execute("SELECT x_value, y_value FROM datapoint WHERE id = %s;", ((count+1)//2,))
            median = cur.fetchone()
        cur.close()
        connection_pool.putconn(conn)
    except:
        print("median Error")
    return median

def mode():
    try:
        conn = connection_pool.getconn()
        if conn:
            print("connected")
        cur = conn.cursor()
        cur.execute("SELECT x_value, y_value, COUNT(x_value) FROM datapoint GROUP BY x_value, y_value ORDER BY COUNT(x_value) DESC LIMIT 1;")
        mode = cur.fetchone()
        cur.close()
        connection_pool.putconn(conn)
    except:
        print("mode Error")
    return mode