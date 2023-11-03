from geopy.geocoders import Nominatim
import sys

def geolocaliser_numero(numero):
    geolocator = Nominatim(user_agent="geolocalisation_app")
    location = geolocator.geocode(numero)

    if location is not None:
        latitude = location.latitude
        longitude = location.longitude
        return f"Latitude : {latitude}, Longitude : {longitude}"
    else:
        return "Adresse non trouvée."

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Utilisation : python geolocalisation.py numéro_de_téléphone")
        sys.exit(1)

    numero = sys.argv[1]
    resultat = geolocaliser_numero(numero)
    print(resultat)