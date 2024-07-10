import requests

# Base URL of the API
base_url = "http://host1.open.uom.lk:8080"

# Endpoint to update a product
endpoint = "/api/products/85"  # Assuming the product ID is 85

# Complete URL
url = base_url + endpoint

# Product data with the updated brand
updated_product = {
    "productName": "Araliya Basmathi Rice",
    "description": "White Basmathi Rice imported from Pakistan. High-quality rice with extra fragrance. Organically grown.",
    "category": "Rice",
    "brand": "Araliya",  # Updated brand
    "expiredDate": "2023.05.04",
    "manufacturedDate": "2022.02.20",
    "batchNumber": 324567,
    "unitPrice": 1020,
    "quantity": 200,
    "createdDate": "2022.02.24"
}

# Send PUT request to the API server to update the product
response = requests.put(url, json=updated_product)

# Print the JSON response of the request
print(response.json())
