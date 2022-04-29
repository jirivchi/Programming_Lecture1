# --------------- Proyecto final de Jonny - Wagner 2022 -------------------------*

#LIBRARIES FROM EACH CLASS
from transportclass import Transporte
from packageclass import Package
from priceclass import Price
from creditcardclass import CreditCard
from userclass import User


#--------------------------------------- Code --------------------------------------------------------
print ('*-------------------------------------------------------------------------*')
print('*------------------------------ \033[1;33m RivEx \033[0m ----------------------------------*')
print('*---------------------- All shipping services ----------------------------*')
print('*-------------------------------------------------------------------------*')
print('')
print('')

sender =User()
receiver = User()
miTransporte = Transporte ()
miPackage = Package()
miPrice = Price ()
miCard = CreditCard()

while True:

    while True:
        sender.filloutuser('Sender')
        receiver.filloutuser('Receiver')
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
            print('Sorry. The price of your shipping is higher than your card limit')
            print('So, operation canceled')
            break

        else:
            miTransporte.assigntracknumber()
            print(f'Your track number is {miTransporte.tracknumber}')

    else:

        print('You will pay in our offices.')

