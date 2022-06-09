import phonenumbers
from phonenumbers import geocoder,carrier
from opencage.geocoder import OpenCageGeocode
import folium
from colorama import Fore


number = input("[!] Please Enter a Number ~> ")
user_number = phonenumbers.parse(number)
location = geocoder.description_for_number(user_number, 'fa')
print(location)

simcard_service = phonenumbers.parse(number)
print(carrier.name_for_number(simcard_service, 'en'))

    
key = '98ea9581ca504450ae5e6528fc1c2fa9'

geocoder = OpenCageGeocode(key)
query = str(location)

result = geocoder.geocode(query)
# print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print(lat,lng)

my_map = folium.Map(location=[lng,lat], zoom_start=10)
folium.Marker([lng,lat],popup=location).add_to(my_map)

my_map.save("location.html")

# print(Fore.RED+"APP Closed!"+Fore.RESET)