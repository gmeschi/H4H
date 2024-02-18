#import googlemaps
import requests
import random

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
print({True: "Open Now!", False: "Closed!", None: "Unknown if Open or Closed!"} [openNow])
print("Rating: " + str(rating) + "/5")

names = [
    "Harmony Haven", "Serenity Springs", "Tranquil Terrace", "Unity Utopia", "Peaceful Pines",
    "Blissful Meadows", "Joyful Junction", "Pleasant Grove", "Calm Cove", "Serenity Sanctuary",
    "Happy Heights", "Cheerful Corner", "Contentment Court", "Friendly Fields", "Radiant Ridge",
    "Pleasantville", "Tranquility Trail", "Harmony Heights", "Joyous Junction", "Serenity Springs",
    "Unity Union", "Peaceful Park", "Cozy Corner", "Gratitude Grove", "Harmony Hill", "Cheerful Valley",
    "Blissful Boulevard", "Serene Shores", "Pleasant Place", "Tranquil Terrace", "Friendly Farmstead",
    "Joyful Jamboree", "Contentment Crossing", "Serenity Square", "Unity Village", "Peaceful Peninsula",
    "Calm Crossing", "Serene Slopes", "Happy Haven", "Cheerful Chateau", "Blissful Bay", "Pleasant Peninsula",
    "Harmony Harbor", "Tranquility Town", "Joyful Junction", "Serene Summit", "Unity Estate", "Peaceful Point",
    "Calm Cove", "Blissful Brook"
]

descriptions = [
    "A peaceful retreat where neighbors come together for community gardening.",
    "Rejuvenate your soul in this oasis with healing yoga sessions.",
    "Serenity meets adventure with scenic hiking trails at your doorstep.",
    "Celebrate diversity and cultural harmony through vibrant community events.",
    "Find solace in meditative forest walks beneath towering pine trees.",
    "Picnic on emerald grass and lose yourself in the starry skies of tranquility.",
    "Join in the laughter and connection of lively neighborhood gatherings.",
    "Bike through charming streets lined with blossoming trees.",
    "Embrace serenity with soothing beachcombing experiences by the calm sea.",
    "Discover inner peace through mindfulness retreats in a tranquil setting.",
    "Rise above with panoramic views and a community filled with joy.",
    "Brighten your day with friendly hellos and cheerful neighborhood walks.",
    "Experience contentment in every corner of this close-knit community.",
    "Play, laugh, and make memories in the welcoming embrace of friendly fields.",
    "Bask in the glow of community spirit atop a radiant ridge.",
    "Step into a picturesque world of charm and neighborly bliss.",
    "Journey through nature's beauty on serene trails that soothe the soul.",
    "Elevate your living experience in a harmonious hillside community.",
    "Where the joy of community meets the excitement of endless possibilities.",
    "Unite with neighbors in a shared vision of harmony and cooperation.",
    "Snuggle into the warmth of community and coziness on every corner.",
    "Cultivate gratitude in the heart of a lush grove filled with abundance.",
    "Take a leisurely stroll down blissful boulevards lined with laughter.",
    "Find peace along tranquil shores where waves whisper serenity.",
    "Discover the pleasure of belonging in a welcoming, pleasant place.",
    "Connect with nature and community in the heart of a friendly farmstead.",
    "Join the festivities and create memories in this joyful jamboree of community.",
    "Where paths converge, find contentment in the shared journey of community.",
    "Gather in serenity and harmony at the heart of this peaceful square.",
    "Embrace unity and diversity in a vibrant village buzzing with community spirit.",
    "Retreat to a tranquil peninsula where peace reigns supreme.",
    "Navigate life's journey with ease and tranquility at every calm crossing.",
    "Ascend to serenity on gentle slopes where peace is always within reach.",
    "Discover happiness and belonging in the comforting embrace of this haven.",
    "Elegant charm meets cheerful community spirit in this delightful chateau.",
    "Sail into blissful waters and embrace the serene beauty of the bay.",
    "Breathe in the fresh air and bask in the beauty of a pleasant peninsula.",
    "Dock your worries and find harmony in the sheltered embrace of the harbor.",
    "Wander through the quaint streets and discover the tranquility of town life.",
    "Reach new heights of peace and serenity atop the tranquil summit.",
    "Unite with fellow residents in a shared commitment to community and connection.",
    "Find your peaceful point of refuge where serenity meets the sea.",
    "Relax and recharge in the gentle embrace of this serene cove community.",
    "Follow the gentle flow of community and tranquility along the blissful brook.",
    "Breathe in the fresh mountain air and embrace the tranquility of terrace living.",
    "Share laughter and play in the wide-open spaces of friendly fields.",
    "Bask in the warmth of community and the radiant beauty of the ridge.",
    "Refresh your spirit in the natural springs of serenity and renewal.",
    "Create lasting memories and friendships in the haven of harmonious living.",
    "Where joy intersects with community, creating endless opportunities for connection.",
    "Find delight in the simple pleasures of life within the welcoming groves.",
    "Cast your worries away and sail into the tranquil waters of blissful bay."
]

locations = [
    "Los Angeles",
    "San Diego",
    "San Jose",
    "San Francisco",
    "Fresno",
    "Sacramento",
    "Long Beach",
    "Oakland",
    "Bakersfield",
    "Anaheim",
    "Santa Ana",
    "Riverside",
    "Stockton",
    "Irvine",
    "Chula Vista",
    "Fremont",
    "San Bernardino",
    "Modesto",
    "Fontana",
    "Oxnard",
    "Moreno Valley",
    "Huntington Beach",
    "Glendale",
    "Santa Clarita",
    "Garden Grove",
    "Oceanside",
    "Rancho Cucamonga",
    "Santa Rosa",
    "Ontario",
    "Elk Grove",
    "Corona",
    "Lancaster",
    "Palmdale",
    "Salinas",
    "Pomona",
    "Hayward",
    "Escondido",
    "Torrance",
    "Sunnyvale",
    "Orange",
    "Fullerton",
    "Pasadena",
    "Thousand Oaks",
    "Visalia",
    "Simi Valley",
    "Concord",
    "Roseville",
    "Victorville",
    "Santa Clara"
]

meeting_days = [
'TRW', 'MTW', 'MTW', 'TS', 'MTW', 'Su', 'Su', 'MT', 'Su', 'Su', 'MTW', 
'Su', 'Su', 'TWR', 'R', 'M', 'Su', 'MTW', 'M', 'Su', 'Su', 'MWF', 'Su', 
'Su', 'Su', 'W', 'Su', 'TWR', 'TR', 'W', 'MTW', 'Su', 'TR', 'W', 'R', 
'MT', 'Su', 'W', 'Su', 'F', 'M', 'Su', 'W', 'Su', 'Su', 'M', 'TR', 'MT', 
'Su', 'Su']

meeting_times = [
('09:30 AM', '10:30 AM'), ('02:00 PM', '04:00 PM'), ('11:30 AM', '02:30 PM'), 
('03:30 PM', '05:30 PM'), ('01:00 PM', '02:00 PM'), ('12:30 PM', '03:30 PM'), 
('05:30 PM', '08:00 PM'), ('12:00 PM', '01:30 PM'), ('11:00 AM', '01:00 PM'), 
('10:30 AM', '01:30 PM'), ('02:00 PM', '03:00 PM'), ('02:30 PM', '04:30 PM'), 
('12:00 PM', '01:00 PM'), ('11:30 AM', '01:00 PM'), ('03:00 PM', '06:00 PM'), 
('10:00 AM', '01:00 PM'), ('11:30 AM', '01:30 PM'), ('12:00 PM', '02:00 PM'), 
('01:00 PM', '03:00 PM'), ('12:30 PM', '03:30 PM'), ('11:30 AM', '01:30 PM'), 
('11:30 AM', '02:30 PM'), ('09:00 AM', '10:00 AM'), ('01:00 PM', '04:00 PM'), 
('12:30 PM', '02:00 PM'), ('12:30 PM', '02:30 PM'), ('02:30 PM', '05:30 PM'), 
('10:00 AM', '11:00 AM'), ('11:30 AM', '01:30 PM'), ('10:00 AM', '11:00 AM'), 
('12:30 PM', '03:30 PM'), ('11:00 AM', '02:00 PM'), ('01:00 PM', '03:00 PM'), 
('12:00 PM', '01:00 PM'), ('11:00 AM', '02:00 PM'), ('11:30 AM', '02:30 PM'), 
('01:00 PM', '03:00 PM'), ('12:00 PM', '01:30 PM'), ('12:30 PM', '03:00 PM'), 
('11:00 AM', '01:00 PM'), ('11:00 AM', '12:00 PM'), ('12:00 PM', '02:00 PM'), 
('10:30 AM', '01:30 PM'), ('11:00 AM', '01:30 PM'), ('11:30 AM', '01:30 PM'), 
('10:00 AM', '11:00 AM'), ('11:30 AM', '01:00 PM'), ('10:30 AM', '01:00 PM'), 
('01:00 PM', '04:00 PM'), ('11:30 AM', '01:30 PM')]

categories = ["volunteer", "social", "fitness"]

class communities:
  def __init__(self, cat):
    self.name = random.choice(names)
    self.description = random.choice(descriptions)
    self.num_members = random.randint(5, 100)
    self.category = cat
    self.locations = random.choice(locations)
    self.meeting_times = random.choice(meeting_times)

def getCommunities(category):
  community_dict = {}
  for i in range(0,5):
    #generate a community and add to dict if right category
    nCom = communities(category)
    community_dict[f'Community{i+1}'] = nCom
  return community_dict
      
def custom_serializer(obj):
    if isinstance(obj, communities):
        return {
            'name': obj.name,
            'description': obj.description,
            'num_members': obj.num_members,
            'category': obj.category,
            'locations': obj.locations,
            'meeting_times': obj.meeting_times
        }
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")


