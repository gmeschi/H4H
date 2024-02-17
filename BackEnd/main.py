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
   "fields": "formatted_address,name,business_status,opening_hours,rating",
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
dict = get_place_info(address, api_key)

'''
if place_info is not None:
  print(place_info)
else:
  print("Failed to get a response from Google Places API")

dict = {'candidates': 
[{'business_status': 'OPERATIONAL', 
'formatted_address': '1000 Lafayette St C, Santa Clara, CA 95050, United States', 
'name': 'Hungry Hound', 
'opening_hours': {'open_now': True}, 
'photos': [{'height': 3072, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/116370847898776376364">Michael Xu</a>'], 
'photo_reference': 'ATplDJbjF3AMgKhWGA3ZUcImjKOmyIQ2pPL53mDlZACqzpgNPEIK5PyORSH8ai2QJenbxp-zsAXK4Wnqw86ZWMuSfo7oEHRxScvwIhaNqrgUSQiLTOpX_9V5KpViK2lKlqn2iWRQQ7DuTzxXrLI_TIjLGng6Cm9vJ59Fc89yG1D90Uss2ozb', 'width': 4080}], 
'rating': 4.4}], 'status': 'OK'}
'''

business_status = dict['candidates'][0]['business_status']
adress = dict['candidates'][0]['formatted_address']
name = dict['candidates'][0]['name']
openNow = dict['candidates'][0]['opening_hours']['open_now']
rating = dict['candidates'][0]['rating']

print("Business is " + business_status.lower() + ".")
print("Name: " + name)
print("Adress: " + adress)
print({True: "Open Now!", False: "Closed!"} [openNow])
print("Rating: " + str(rating) + "/5")


