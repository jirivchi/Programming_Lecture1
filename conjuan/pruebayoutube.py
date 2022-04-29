import certifi
import ssl
import geopy.geocoders

from geopy.geocoders import Nominatim

ctx = ssl._create_unverified_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx

locator = Nominatim(scheme='https', user_agent="Test")
location = locator.reverse("48.86543,2.34996")

print(location.raw)