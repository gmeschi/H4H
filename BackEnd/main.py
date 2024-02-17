import googlemaps
import requests

#gmaps = googlemaps.Client(key = 'AIzaSyA5L1utCSQOnj7d-MKRU8kLUopQ3DUVE38')

#reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

#print(reverse_geocode_result)

def get_place_info(address, api_key):
# Base URL
  base_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"

# Parameters in a dictionary
  
  params = {
   "input": address,
   "inputtype": "textquery",
   "fields": "formatted_address,name,business_status,opening_hours",
   "key": api_key,
  }

# Send request and capture response
  response = requests.get(base_url, params=params)

# Check if the request was successful
  if response.status_code == 200:
    return response.json()
  else:
    return None
  
api_key = "AIzaSyA5L1utCSQOnj7d-MKRU8kLUopQ3DUVE38"
address = input("Give a Description of the location you would like to visit: \n")
place_info = get_place_info(address, api_key)

if place_info is not None:
  print(place_info)
else:
  print("Failed to get a response from Google Places API")