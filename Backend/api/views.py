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
                except Exception as e:
                    print(f"Creation Error: {e}")
                    return JsonResponse({"error": "Insert Error"}, status=500)
                return JsonResponse({"success": True, "message": "Successfully inserted point"})
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
                except Exception as e:
                    print(f"Update Error: {e}")
                    return JsonResponse({"error": "Update Error"}, status=500)
                return JsonResponse({"success": True, "message": "Successfully updated point"})
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
                except Exception as e:
                    print(f"Delete Error: {e}")
                    return JsonResponse({"error": "Delete Error"}, status=500)
                return JsonResponse({"success": True, "message": "Successfully deleted point"})
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({"error": "Invalid request"}, status=400)
    return JsonResponse({"error": "Invalid method"}, status=405)
