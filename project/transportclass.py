import certifi
import ssl
import geopy.geocoders
from datetime import datetime
from geopy.geocoders import Nominatim
from geopy import distance
from geopy.distance import geodesic
ctx = ssl._create_unverified_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx




from userclass import User

# Transport class
class Transporte():
    destino = 'Internacional'
    distancia = 100
    pago = 'Tarjeta'
    collection = ' '
    delivery = ' '
    way = ' '
    tracknumber = ''

    def choosetransport (self):

        print('*------------------------\u001b[33m Shipping \u001b[0m------------------------------*')
        print(f'You can choose wether your package will be collected at home -Cost 15€-')
        self.collection =  input( 'Type \u001b[33mY \u001b[0m or \u001b[33mN \u001b[0m:  ')

        if self.collection.upper() == 'Y':
            print('Collection at home')
            Transporte.collection = 'Y'

    def calcroute (self):

        if User.dictroutecountry["Sender"] != User.dictroutecountry["Receiver"]:
            Transporte.destino = 'International'
        else:
            Transporte.destino = 'Local'

        locator = Nominatim(user_agent='Master')

        City1 = User.dictroutecity["Sender"]
        City2 = User.dictroutecity["Receiver"]

        coord1 = locator.geocode(City1)
        coord2 = locator.geocode(City2)
        loc1 = ((coord1.latitude, coord1.longitude))
        loc2 = ((coord2.latitude, coord2.longitude))

        Transporte.distancia = int((distance.distance(loc1, loc2).km))
        print (f'Distancia: {Transporte.distancia} Km' )

        print(f'Package will be sent from {User.dictroutecity["Sender"]} ({User.dictroutecountry["Sender"]}) to {User.dictroutecity["Receiver"]} ({User.dictroutecountry["Receiver"]})')

        if Transporte.destino == 'Local' and Transporte.distancia > 1500:
            print('Even though shipping is national, it will be considered as international in view of the distance')
            Transporte.destino = 'International'


        if self.destino == 'International':
            print('You can choose to ship either by flight -delivery in 24 hours- or by surface -between 48 and 72 hours-')
            imethod = input ('Type \u001b[31m F \u001b[0m if you want send it by flight or \u001b[31m S \u001b[0m by truck or train: ')
        else:
            imethod = 'S'

        if imethod.upper() == 'F':
            Transporte.way = 'flight'
        elif imethod.upper() == 'S':
            Transporte.way = 'surface'
        else:
            print('You have not type properly, so we will send your package by surface')
            Transporte.way = 'surface'


        print (f'You chose to send your package by \u001b[33m {self.way} \u001b[0m')


    def assigntracknumber(self):

        # Tracknumber is a string of date and time just when payment is made
        now = datetime.now()
        self.tracknumber = now.strftime('%Y' '%m' '%d' '%H' '%M' '%S')

