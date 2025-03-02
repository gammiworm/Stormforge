from django.http import JsonResponse
import json

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
                pass
            elif operation == "read":
                # Handle read logic
                pass
            elif operation == "update":
                # Handle update logic
                pass
            elif operation == "delete":
                # Handle delete logic
                pass
            else:
                return JsonResponse({"error": "Invalid operation"}, status=400)

            return JsonResponse({"success": True, "operation": operation})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)