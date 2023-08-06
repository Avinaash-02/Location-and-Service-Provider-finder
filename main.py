import phonenumbers
import opencage
import folium
from myphone import numbers

from phonenumbers import geocoder

pepnumber=phonenumbers.parse(numbers,"CH")
location=geocoder.description_for_number(pepnumber,"en")
print(location)
from phonenumbers import carrier
service_number=phonenumbers.parse(numbers,"RO")
print(carrier.name_for_number(service_number,"en"))

from opencage.geocoder import OpenCageGeocode
key='3a03ee88d0984c6f94c9761c480632ca'

geocoder=OpenCageGeocode(key)
query=str(location)
results=geocoder.geocode(query)
print(results)
lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']
print(lat,lng)
myMap=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(myMap)

myMap.save("mylocation.html")
