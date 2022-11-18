# Importing requests
import requests


# URL of the API
# Star Wars information API
url = "https://swapi.dev/api/planets/3/?format=json"

# Making GET request to the API and storing the response object
response = requests.get(url)

# Displaying all attributes of the response object
for attr, value in response.__dict__.items():
    if not attr.startswith("__"):
        # Printing
        print(f"attribute '{attr}':  {value}")
        print()
