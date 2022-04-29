def becalumn():
	print ("Datos para solicitud de becas de estudio")

	hermanos = int ( input ("Número de hermanos que conviven contigo en la familia: "))
	print (f'Hermanos convivientes contigo: {hermanos} hermanos' )

	distancia = int ( input ("Distancia de tu domicilio al centro de estudios: "))
	print ("Vives a Km del centro: : " + str (distancia) + ' km')

	salario = int ( input ("Salario bruto anual de la famila completa: "))
	print ( "El salario familiar es de: " + str (salario) + ' Euros')

	asignaturas = ( "griego", "arameo", "sumerio", "guanche") #tupla -> no puedo añadir mas una vez que está creada

	if hermanos > 1 and distancia > 40 and salario/(hermanos + 1) < 10000:
		print ("Tienes derecho a beca")
	else:
		print ("No tienes derecho a beca")

	print ("")

	print ("Elige asignaturas optativas")
	print ("Puedes elegir entre Griego, Arameo, Sumerio, Guanche")
	eleccion = input ( "Escribe tu elección: ")

	if eleccion.lower() in asignaturas:  #python es sensible a matusculas y minusculas.
		print ("Has elegido correctamente " + eleccion.upper())
	else:
		print ("La asignatura que has elegido no está entre las opcionales")


#################validar email juan###########################

def emailjuan():
	print ('Prueba para saber si una dirección de correo es correcta')

	tudir = input ('Escriba su dirección de correo: ')

	punto= False
	cuentarroba = 0

	for i in tudir:
		if i == ('@'):
			cuentarroba += 1
		# por si ha puesto más de una @
		# y solo busca el punto una vez que ya ha visto una @
		# porque los de antes no le interesan
		if cuentarroba == 1 and i == ('.'):
			punto = True

	if cuentarroba == 1 and punto:
		print ('La dirección es correcta')
	else:
		print ('La dirección es incorrecta')

#emailjuan()

#-------------------------------------------------------------------------------

print ('Prueba para saber si una dirección de correo es correcta')

incorrecto = True

while incorrecto:

    punto = False
    cuentarroba = 0

    tudir = input('Escriba su dirección de correo: ')

    for i in tudir:

        if i == ('@'):
          cuentarroba += 1

        # por si ha puesto más de una @
        # y solo busca el punto una vez que ya ha visto una @
        # porque los de antes no le interesan

        if cuentarroba == 1 and i == ('.'):
            punto = True

    if cuentarroba == 1 and punto:
        print ('La dirección es correcta')
        incorrecto = False
    else:
        print ('La dirección es incorrecta. Por favor, vuelve a introducirla.')

