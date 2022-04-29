# Credit card class -------------------------
from datetime import date
from datetime import datetime

# Credit card class
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

        print(f'{self.cardcompany} card number {self.number} {response}')


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
