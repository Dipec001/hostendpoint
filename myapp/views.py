from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime
import json

# Create your views here.
def get_info(request):
    # Get slack_name and track from the request's GET parameters
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')

    # Check if both slack_name and track are present and track is "backend"
    if slack_name and track == "backend":
        # Get the current day of the week
        current_day = datetime.now().strftime("%A")

        # Get the current UTC time within a +/-2 minute window
        utc_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

        # Construct the JSON response
        response = {
            "slack_name": slack_name,
            "current_day": current_day,
            "utc_time": utc_time,
            "track": track,
            "github_file_url": "https://github.com/Dipec001/hostendpoint/blob/master/myapp/views.py",
            "github_repo_url": "https://github.com/Dipec001/hostendpoint.git",
            "status_code": "200"
        }

        # Convert the dictionary to a JSON string with formatting
        formatted_response = json.dumps(response, indent=2)

        # Return the JSON string as a regular HttpResponse with JSON content type
        return HttpResponse(formatted_response, content_type='application/json')
    else:
        # Return an error JSON response for invalid parameters
        error_response = {
            "error": "Invalid parameters. Use format ?slack_name=example_name&track=backend"
        }
        return JsonResponse(error_response, status=400)
