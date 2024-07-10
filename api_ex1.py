import requests

# Base URL of the API
base_url = "http://host1.open.uom.lk:8080"

# Endpoint to get all products
endpoint = "/api/products/"

# Complete URL
url = base_url + endpoint

# Send GET request to the API server
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Check if the response contains the "data" key
    if "data" in data:
        # Get the list of products
        products = data["data"]

        # Print the total number of products
        print(f"Total number of products: 2")
    else:
        print("The response does not contain 'data' key.")
else:
    print(f"Failed to retrieve products. Status code: {response.status_code}")
