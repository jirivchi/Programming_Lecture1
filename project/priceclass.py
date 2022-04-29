from transportclass import Transporte

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


