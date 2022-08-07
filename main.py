import  phonenumbers
from myphone import number
import opencage,folium


from phonenumbers import geocoder,carrier

pepnumber=phonenumbers.parse(number)

location=geocoder.description_for_number(pepnumber,"en")
print("This Number is located in"+location+".")

service=phonenumbers.parse(number)
print("The service is "+carrier.name_for_number(service,"en"))


from opencage.geocoder import OpenCageGeocode

key='cf92bbf0a8da4ab8bcf519238aa70205'

geocoder=OpenCageGeocode(key)

query=str(location)

results=geocoder.geocode(query)

lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']

print(lat,lng)

mymap=folium.Map(location=[lat,lng],zoom_start=9)

folium.Marker([lat,lng],popup=location).add_to(mymap)

mymap.save("Mylocation.html")


