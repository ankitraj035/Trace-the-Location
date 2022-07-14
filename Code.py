# Import module
from geopy.geocoders import Nominatim

# Initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")

# Assign Latitude & Longitude
Latitude = input("latitude :-")
Longitude = input("longitude :- ")

# Displaying Latitude and Longitude
print("Latitude: ", Latitude)
print("Longitude: ", Longitude)

# Get location with geocode
location = geolocator.geocode(Latitude+","+Longitude)

# Display location
print("\nLocation of the given Latitude and Longitude:")
print(location)
