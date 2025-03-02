from django.shortcuts import render
from django.http import JsonResponse
import json
from config import connection_pool


def handleCRUD(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            operation = data.get("operation")  # e.g., "create", "read", "update", "delete"
            metadata = data.get("metadata", {})

            user_id = metadata.get("userId")
            timestamp = metadata.get("timestamp")
            dataset_id = metadata.get("datasetId")
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
                except Exception as e:
                    print(f"Delete Error: {e}")
                    return JsonResponse({"error": "Delete Error"}, status=500)
                return JsonResponse({"success": True, "message": "Successfully deleted point"})
            else:
                return JsonResponse({"error": "Invalid operation"}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)
