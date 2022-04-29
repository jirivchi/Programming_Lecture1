#####BUCLE FOR########
def buclefor():
    suma = 0
    anterior = 0
    previo = 1

    for i in range (15):
        suma = anterior + previo
        print (suma, end= " ")
        anterior = previo
        previo = suma

    print(' ')

    inicio=0
    mov=2
    for x in range(15):
        suc=inicio
        print(suc, end=' ')
        inicio=suc+mov

#######VALIDAR EMAIL################
def validateemail():
    email=input('escriba el email:')
    print(email)

    #split string
    separar=list(email)
    print(separar)
    #for loop to ir sobre las palabras
    letra='@'

    for split in separar:
        if split==letra:
            print('email valido')

        else:
            print('email no valido')


#validateemail()


####email mejorado: escribir el email hasta que este bien


##ejercicios pildoras

def ejercicio1():
    numero=True
    anterior=input('introduzca primer numero: ')
    while numero:
        posterior=input('introduzca siguiente numero: ')
        if anterior<posterior:
            anterior=posterior
        else:
            numero=False
    print('proceso finalizado')
#ejercicio1()


####Ejercicio2########

def ejercicio2():
    numero=True
    umbral=0
    sumatotal=0
    while numero:
        primero=int(input('introduzca siguiente numero: '))
        if umbral<primero:
            sumatotal+=primero
        else:
            numero=False
            print('proceso finalizado')
    print(sumatotal)

#ejercicio2()

#### versión mejorada de ejercicio 3 pero resta el último numero.
def ejercicio3():
    umbral=0
    sumatotals=0
    primeros=0
    while umbral<=primeros:
        primeros=int(input('introduzca siguiente numero: '))
        sumatotals += primeros
    print(sumatotals)

#ejercicio3()


























