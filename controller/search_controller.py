import json
import requests


def search(query):
    filter_type = ["api", "document"]
    url = "http{server}/similarity_search"
    payload = json.dumps({
        "query": query,
        "filter_type": filter_type
    })

    headers = {
        'Content-Type': 'application/json'
    }

    # Send the request
    response = requests.request("POST", url, headers=headers, data=payload)

    # Print response for debugging

    # Initialize context list
    context_list = []

    # Check if the response status is OK
    if response.status_code == 200:
        # Parse JSON response
        response_data = response.json()
        searched_results = response_data.get("searched_results", [])

        # Process each story
        for story in searched_results:
            context = [chunk['content'] for chunk in story['chunks']]
            context.append(f"هذه القصة تم نشرها في تاريخ {str(story['published_at'])}")
            merged_string = " ".join(context)
            context_list.append(merged_string)

    return context_list
