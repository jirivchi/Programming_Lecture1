# Proyecto final de Jonny 2022
from datetime import date
from datetime import datetime
from geopy.geocoders import Nominatim

# Locater class -------------------------------------------
locator = Nominatim (user_agent = "Final_Project")

# Transport class -----------------------------------------
class Transporte():
    destino = 'Internacional'
    distancia = 100
    pago = 'Tarjeta'
    collection = ' '
    delivery = ' '

    def choosetransport (self):
        sender = User()
        receiver = User()
        sender.filloutuser('Sender')
        receiver.filloutuser('Receiver')

    def calcroute (send):
        if User.dictroutecountry["Sender"] != User.dictroutecountry["Receiver"]:
            Transporte.destino = 'Internacional'
        else:
            Transporte.destino = 'Local'

        print(f'Package will be sent from {User.dictroutecity["Sender"]} ({User.dictroutecountry["Sender"]}) to {User.dictroutecity["Receiver"]} ({User.dictroutecountry["Receiver"]})')
        print(f'This shipping is \u001b[33m {Transporte.destino} \u001b[0m')



# Credir card class -------------------------------------------
class CreditCard():
    holder = "John"
    monthexpiry = date.today().month
    yearexpiry = date.today().year
    CVC = 111
    number = '1111111111111111'
    cardcompany =''

    def filloutcard (self):

        print('*------------------------ Credit card --------------------*')
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
        # Usa el Algoritmo de Luhn
        # Número de ejemplo: 49927398716
        # Se multiplican por 2 los dígitos que ocupan las posiciones pares empezando por el final:
        # (1×2) = 2, (8×2) = 16, (3×2) = 6, (2×2) = 4, (9×2) = 18
        # Se suman los dígitos que ocupan las posiciones impares con los dígitos de los productos obtenidos:
        # 6 + (2) + 7 + (1 + 6) + 9 + (6) + 7 + (4) + 9 + (1 + 8) + 4 = 70.
        # (1 + 6) es por la multiplicación de 8x2=16 y (1 + 8) es por la multiplicación de 9x2=18 del primer punto
        # Si el ressultado de esa suma es múltiplo de 10, el número es correcto: 70 % 10 = 0

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



# User class. ----------------------------------------------------------------+
class User():
    userfirstname = "John"
    userlastname = "Smith"
    useraddress = " "
    usercity = " "
    usercountry = " "
    dictroutecountry = {}
    dictroutecity = {}

    def filloutuser (self, side):

        print(f'*-------------------- {side} Data ---------------------------*')
        self.userfirstname = input(f' {side} firstname: ')
        self.userlastname = input(f' {side} lastname: ')
        self.useraddress = input (f' {side} address -street, number, floor-: ')
        self.usercity = input (f' {side} city: ')
        self.usercountry = input (f' {side} country: ')
        self.dictroutecountry [ side ] = self.usercountry
        self.dictroutecity [ side ]= self.usercity


user.filloutsender()
user.filloutreceiver()


# Package class --------------------------------------------------------------
class Package():

    width = 0
    height = 0
    length = 0
    volume = 0
    type = ''

    def filloutpack (self):
        print ('*--------------------- Package------------------*')
        self.length = int ( input ('Package length in cm: '))
        self.width = int ( input ('Package width in cm: '))
        self.height = int ( input ('Package height in cm: '))
        self.volume = self.height * self.width * self.length

        if self.volume < 8000:
            self.type = 'Small'
        elif self.volume < 125000:
            self.type = 'Medium'
        else:
            self.type = 'Large'

        print(f'\u001b[33m Your package is {self.type}-sized \u001b[0m')


#--------------- Code --------------------------------------------------------
location = geolocator.geocode ('Seville')
print (location)

miTransporte = Transporte ()
miCard = CreditCard ()
miPackage = Package()
#miTransporte.destino = input ('Teclee \u001b[33m I \u001b[0m para destino internacional o \u001b[33m N \u001b[0m para destino nacional: ')

miTransporte.choosetransport()
miTransporte.calcroute()
miPackage.filloutpack()
miCard.filloutcard()
miCard.company()

# Comprobamos que la tarjeta está bien
miCard.validate()
miCard.testexpiry()
