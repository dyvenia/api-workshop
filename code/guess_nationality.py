# Importing requests
import requests


# URL of the API
# Predict nationality based on a name API
url = "https://api.nationalize.io/"

# Setting parameters
print("-" * 80)
name = input("Hi, please type your name: ").strip().lower()
params = {"name": name}

# Making GET request to the API and storing the response object
response = requests.get(url, params)

# Notice how I use response.json() method to convert
# The json response to a python dictionary
dict_response = response.json()

# Printing raw response
print()
print("Raw response:")
print(dict_response)
print()

# Now I can work with the raw response and extract data from it
# I will extract the key information and display it necely
country_id = dict_response.get("country")[0].get("country_id")
probability = dict_response.get("country")[0].get("probability")

# Using another API to get full name of the country given its country id
url = f"https://restcountries.com/v2/alpha/{country_id}"
response = requests.get(url)
dict_response = response.json()
country_name = dict_response.get("name")

# Printing well formatted information
print()
print("Transformed and formatted information:")
print(
    f"Mmmm {name.title()}... I am {probability:.0%} sure that you are from {country_name}"
)
