# Importing requests
import requests


# URL of the API
# Facts about numbers API
url = "http://numbersapi.com/random/math"

# Making GET request to the API and storing the response object
response = requests.get(url)

# Using .text method to retrieve the text response we got
print(response.text)
