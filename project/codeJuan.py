# --------------- Proyecto final de Jonny 2022 -------------------------*
import certifi
import ssl
import geopy.geocoders
from datetime import date
from datetime import datetime
from geopy.geocoders import Nominatim
from geopy import distance
from geopy.distance import geodesic

ctx = ssl._create_unverified_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx


# Transport class -----------------------------------------

class Transporte():
    destino = 'Internacional'
    distancia = 100
    pago = 'Tarjeta'
    collection = ' '
    delivery = ' '
    way = ' '
    tracknumber = ''

    def choosetransport (self):

        sender = User()
        receiver = User()
        sender.filloutuser('Sender')
        receiver.filloutuser('Receiver')

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


# User class. ----------------------------------------------------------------+
class User():
    userfirstname = "John"
    userlastname = "Smith"
    useraddress = " "
    usercity = " "
    usercountry = " "
    dictroutecountry = {}
    dictroutecity = {}

    def filloutuser (self,side):

        print(f'*--------------------\u001b[33m {side} Data \u001b[0m---------------------------*')
        self.userfirstname = input(f'{side} firstname: ')
        self.userlastname = input(f'{side} lastname: ')
        self.useraddress = input (f'{side} address -street, number, floor-: ')
        self.usercity = input (f'{side} city: ')
        self.usercountry = input (f'{side} country: ')
        self.dictroutecountry [ side ] = self.usercountry
        self.dictroutecity [ side ]= self.usercity


# Package class --------------------------------------------------------------
class Package():

    width = 0
    height = 0
    length = 0
    volume = 0
    weight = 0
    type = ''
    strweight = ' '

    def filloutpack (self):
        print (   print(f'*--------------------\u001b[33m Package \u001b[0m---------------------------*'))
        self.length = int ( input ('Package length in cm: '))
        self.width = int ( input ('Package width in cm: '))
        self.height = int ( input ('Package height in cm: '))
        self.weight = float (input('Weight of the package in Kg: '))
        self.volume = self.height * self.width * self.length

        if self.volume < 8000:
            self.type = 'Small'
        elif self.volume < 125000:
            self.type = 'Medium'
        else:
            self.type = 'Large'

        if self.weight <= 2.000:
            self.strweight = 'light'
        elif self.weight <= 5.000:
            self.strweight = 'semi'
        else:
            self.strweight = 'heavy'


        print (f'\u001b[93mEl envío {Transporte.destino} será de un paquete de tamaño {self.type} {self.strweight}-weighted vía {Transporte.way} a {Transporte.distancia} Km\u001b[0m')



# Price class --------------------------------------------------**
class Price():

    basicprice = 5
    dicttipo = {"International": 1.5, "Local" : 1}
    dictmethod = {"flight": 2, "surface": 1}
    dictweight = {"light" : 1, "semi" : 1.5, "heavy": 2}
    dictsize = {"Small": 1, "Medium": 1.5, "Large": 2}
    totalprice = 0

    # El cálculo se hace a partir de una base mínima -5- multiplicada por 1, 1.5 o 2 en función del tipo de envío, la distancia,
    # el medio utilizado y el tamaño y peso del paquete. En el caso de la distancia, los Km se dividen por 1100 y se multiplican por 1.5

    def CalcPrice (self, viaje, dist, metodo, vol, peso):

        self.totalprice = round ( self.basicprice * self.dicttipo [viaje] * (dist * 1.5 / 1100) * self.dictmethod [metodo] * self.dictsize [vol] * self.dictweight[peso], 2 )

        if Transporte.collection == 'Y':
           self.totalprice += 15
           print('Collection at home -15€-')

        print (f'\u001b[33mTotal price for your shipping: {self.totalprice} €\u001b[0m')



# Credir card class -------------------------
class CreditCard():
    holder = "John"
    monthexpiry = date.today().month
    yearexpiry = date.today().year
    CVC = 111
    number = '1111111111111111'
    cardcompany =''
    limite = 0

    def filloutcard (self):

        print('*------------------------\u001b[33m Credit card \u001b[0m--------------------*')
        self.holder = input ('Credit card holder: ')

        while True:  # Lo repite hasta que lo escriba bien
            self.number = input ('Card number: ')
            if 13 < len(self.number) < 19:
                break
            else:
                print("\u001b[33m Check Card number once again. It must be between 13 and 19 digits long.\u001b[0m")

        while True: # Lo repite hasta que ponga un mes válido
            self.monthexpiry = input ('Expiration month: ')
            if 0 < int(self.monthexpiry ) < 13:
                break
        self.yearexpiry = input ('Expiration year: ')
        self.limite = int(input('Credit limit: '))
        self.CVC = input('Type the secret number: ')


    def company(self):

        if str(self.number).startswith('4'):
            self.cardcompany = 'Visa Card'
        elif str(self.number).startswith(('50', '67', '58', '63',)):
            self.cardcompany = 'Maestro Card'
        elif str(self.number).startswith('5'):
            self.cardcompany = 'Master Card'
        elif str(self.number).startswith('37'):
            self.cardcompany = 'American Express Card'
        else:
            self.cardcompany = 'Not recognized company'



    def validate(self):
        """
        Usa el Algoritmo de Luhn
        Número de ejemplo: 49927398716
        Se multiplican por 2 los dígitos que ocupan las posiciones pares empezando por el final:
        (1×2) = 2, (8×2) = 16, (3×2) = 6, (2×2) = 4, (9×2) = 18
        Se suman los dígitos que ocupan las posiciones impares con los dígitos de los productos obtenidos:
        6 + (2) + 7 + (1 + 6) + 9 + (6) + 7 + (4) + 9 + (1 + 8) + 4 = 70.
        (1 + 6) es por la multiplicación de 8x2=16 y (1 + 8) es por la multiplicación de 9x2=18 del primer punto
        Si el ressultado de esa suma es múltiplo de 10, el número es correcto: 70 % 10 = 0
        """

        # inicializa variable para la suma
        sum_ = 0

        # pone el número al revés para contar mejor
        crd_no = self.number [::-1]

        # los impares (con resto = 1) son en realidad los pares ya que la lista comienza con el 0
        for i in range(len(crd_no)):
            if i % 2 == 1:
                double_it = int(crd_no[i]) * 2
                if len(str(double_it)) == 2:
                    sum_ += sum([eval(i) for i in str(double_it)])
                else:
                    sum_ += double_it
            else:
                sum_ += int(crd_no[i])

        if sum_ % 10 == 0:
            response = "válida"
        else:
            response = '\u001b[33m no válida \u001b[0m'

        print(f'{miCard.cardcompany} card number {miCard.number} {response}')


    def testexpiry(self):
        if len(self.monthexpiry) == 1:
            self.monthexpiry = '0' + self.monthexpiry

        date_time_str = '20' + self.yearexpiry + '-' + self.monthexpiry + '-' + '01' + ' 00:00:00'
        today = date.today()

        fechaexp = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')

        faltandias = (fechaexp.date() - today).days

        if faltandias <= 0:
            print( '\u001b[33m Expired card. Type a new card. \u001b[0m')
        else:
            print ( 'Card in use')

'''
    def cardbalance(self):

       self.limite -= Price.totalprice

       if self.limite < 0:
            print( 'Operation denied' )

'''

#--------------------------------------- Code --------------------------------------------------------
print ('*-------------------------------------------------------------------------*')
print('*------------------------------ \033[1;33m RivEx \033[0m ----------------------------------*')
print('*---------------------- All shipping services ----------------------------*')
print('*-------------------------------------------------------------------------*')
print('')
print('')

miTransporte = Transporte ()
miPackage = Package()
miPrice = Price ()
miCard = CreditCard()

while True:

    while True:
        miTransporte.choosetransport()
        miTransporte.calcroute()
        miPackage.filloutpack()
        miPrice.CalcPrice(miTransporte.destino, miTransporte.distancia, miTransporte.way, miPackage.type, miPackage.strweight)

        ok = input('Are all the data correct? -\u001b[33mY\u001b[0m or \u001b[33mN\u001b[0m-: ')
        if ok.upper() == 'Y':
            break

    Cash_Card = input('Will you pay with \u001b[33mC\u001b[0mard or in Cas\u001b[33mH\u001b[0m: ')

    if Cash_Card.upper() == 'C':

        miCard = CreditCard()
        miCard.filloutcard()
        miCard.company()
        miCard.validate()
        miCard.testexpiry()

        miCard.limite -= miPrice.totalprice
        print(f'El límite tras el pago será de {miCard.limite}')

        if miCard.limite < 0:
            print('Sorry. The price of ypur shipping is higher than your card limit')
            print('So, operation canceled')
            break

        else:
            miTransporte.assigntracknumber()
            print(f'Your track number is {miTransporte.tracknumber}')

    else:

        print('You will pay in our offices.')

