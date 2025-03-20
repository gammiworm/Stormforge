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
        result = cur.fetchone()

        # Handle empty dataset
        if result is None or result[0] is None or result[1] is None:
            print("No data points available.")
            mean = (None, None)  # Return None for both x and y if no data exists
        else:
            # Round the mean values to two decimal places
            mean = (round(result[0], 2), round(result[1], 2))

        cur.close()
        connection_pool.putconn(conn)
        return mean

    except Exception as e:
        print(f"Mean Error: {e}")
        if conn:
            connection_pool.putconn(conn)  # Ensure connection is returned to the pool
        return (None, None)  # Return None in case of an error

def median():
    try:
        conn = connection_pool.getconn()
        if conn:
            print("connected")
        cur = conn.cursor()

        # Get the total count of rows
        cur.execute("SELECT COUNT(*) FROM datapoint;")
        count = cur.fetchone()[0]

        if count == 0:
            print("No data points available.")
            return None  # Return None if there are no rows

        # For even count, fetch the two middle rows and calculate the median
        if count % 2 == 0:
            cur.execute("""
                SELECT x_value, y_value 
                FROM datapoint 
                ORDER BY id 
                LIMIT 2 OFFSET %s;
            """, ((count // 2) - 1,))
            medianlist = cur.fetchall()
            median = [
                round((medianlist[0][0] + medianlist[1][0]) / 2, 2),  # Median for x_value
                round((medianlist[0][1] + medianlist[1][1]) / 2, 2)   # Median for y_value
            ]
        else:
            # For odd count, fetch the middle row
            cur.execute("""
                SELECT x_value, y_value 
                FROM datapoint 
                ORDER BY id 
                LIMIT 1 OFFSET %s;
            """, (count // 2,))
            result = cur.fetchone()
            median = (round(result[0], 2), round(result[1], 2))  # Round the median values

        cur.close()
        connection_pool.putconn(conn)
        return median

    except Exception as e:
        print(f"Median Error: {e}")
        return None

def mode():
    try:
        conn = connection_pool.getconn()
        if conn:
            print("connected")
        cur = conn.cursor()

        # Query to find the mode of x_value and y_value pairs
        cur.execute("""
            SELECT x_value, y_value, COUNT(*)
            FROM datapoint
            GROUP BY x_value, y_value
            ORDER BY COUNT(*) DESC
            LIMIT 1;
        """)
        result = cur.fetchone()

        # Check if there are no repeats (i.e., count is 1)
        if result and result[2] == 1:
            mode = None  # No mode exists
        else:
            mode = result[:2]  # Return x_value and y_value

        cur.close()
        connection_pool.putconn(conn)
        return mode

    except Exception as e:
        print(f"Mode Error: {e}")
        return None