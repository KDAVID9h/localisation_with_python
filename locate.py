import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium

# trouver le pays du numero
num = "+228********"
lenum = phonenumbers.parse(num)
locat = geocoder.description_for_number(lenum, "tg")
print(locat)

# Trouver l'operateur mobile
operat = phonenumbers.parse(num)
print(carrier.name_for_number(operat, "tg"))

# Trouver la longitude et la latitude
cle = "6a286c5f58234b00a0f2da5ad2af3ae5"
coord = OpenCageGeocode(cle)
requete = str(locat)
reponse = coord.geocode(requete)

latit = reponse[0]["geometry"]["lat"]
longi = reponse[0]["geometry"]["lng"]
print("Latitude = ",latit,"\nLongitude = ",longi)

#print(reponse)

#Creation de map
monMap = folium.Map(locat=[latit, longi], zoom_start=12)
folium.Marker([latit, longi], popup=locat).add_to(monMap)
monMap.save("map.html")