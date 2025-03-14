from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from config import connection_pool

@csrf_exempt
def handleCRUD(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f"Received data: {data}")

            operation = data.get("operation")  # e.g., "create", "read", "update", "delete"
            metadata = data.get("metadata", {})

            changes = metadata.get("changes")

            # Process CRUD based on operation
            if operation == "create":
                # Handle creation logic
                x = changes.get("x")
                y = changes.get("y")
                try:
                    conn = connection_pool.getconn()
                    if conn:
                        print("connected")
                    cur = conn.cursor()
                    cur.execute("INSERT INTO datapoint (x_value, y_value) VALUES (%s, %s);", (x, y))
                    conn.commit()
                    cur.close()
                    connection_pool.putconn(conn)
                    print("Data point inserted successfully")
                    return JsonResponse({"success": True, "message": "Successfully inserted point"})
                except Exception as e:
                    print(f"Creation Error: {e}")
                    return JsonResponse({"error": "Insert Error"}, status=500)
            elif operation == "read":
                # Handle read logic
                pass
            elif operation == "update":
                # Handle update logic
                id = changes.get("id")
                x = changes.get("x")
                y = changes.get("y")
                try:
                    conn = connection_pool.getconn()
                    if conn:
                        print("connected")
                    cur = conn.cursor()
                    cur.execute("UPDATE datapoint SET x_value = %s, y_value = %s WHERE id = %s;", (x, y, id))
                    conn.commit()
                    cur.close()
                    connection_pool.putconn(conn)
                    print("Data point updated successfully")
                    return JsonResponse({"success": True, "message": "Successfully updated point"})
                except Exception as e:
                    print(f"Update Error: {e}")
                    return JsonResponse({"error": "Update Error"}, status=500)
            elif operation == "delete":
                # Handle delete logic
                id = changes.get("id")
                try:
                    conn = connection_pool.getconn()
                    if conn:
                        print("connected")
                    cur = conn.cursor()
                    cur.execute("DELETE FROM datapoint WHERE id = %s;", (id,))
                    conn.commit()
                    cur.close()
                    connection_pool.putconn(conn)
                    print("Data point deleted successfully")
                    return JsonResponse({"success": True, "message": "Successfully deleted point"})
                except Exception as e:
                    print(f"Delete Error: {e}")
                    return JsonResponse({"error": "Delete Error"}, status=500)
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({"error": "Invalid request"}, status=400)
    return JsonResponse({"error": "Invalid method"}, status=405)

@csrf_exempt
def get_data_points(request):
    if request.method == "GET":
        try:
            conn = connection_pool.getconn()
            if conn:
                print("connected")
            cur = conn.cursor()
            cur.execute("SELECT x_value, y_value FROM datapoint")
            data_points = cur.fetchall()
            cur.close()
            connection_pool.putconn(conn)
            return JsonResponse([{"x_value": x, "y_value": y} for x, y in data_points], safe=False)
        except Exception as e:
            print(f"Error fetching data points: {e}")
            return JsonResponse({"error": "Error fetching data points"}, status=500)
    return JsonResponse({"error": "Invalid method"}, status=405)
