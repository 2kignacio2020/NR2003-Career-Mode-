import random

# Creamos una lista vacía para almacenar los equipos
equipos = []

# Pedimos el nombre del usuario
nombre = input("Hola, ¿cómo te llamas? ")

# Pedimos los equipos, números y reputación al usuario
while True:
    # Pedimos los datos del equipo
    equipo = input("Ingresa el nombre del equipo o escribe 'Estoy harto' para salir: ")
    
    # Si el usuario escribe 'Estoy harto', salimos del ciclo
    if equipo == "Estoy harto":
        break
    
    numero_coches = int(input("Ingresa el número de coches del equipo: "))
    reputacion = int(input("Ingresa la reputación del equipo (entre 1 y 100): "))
    
    # Agregamos los datos del equipo a la lista
    equipos.append({'equipo': equipo, 'coches': numero_coches, 'reputacion': reputacion})

# Generamos 3 ofertas aleatorias a partir de los equipos ingresados
ofertas = []
for i in range(3):
    # Seleccionamos un equipo aleatorio de la lista
    equipo = random.choice(equipos)
    
    # Calculamos el precio base de la oferta
    precio_base = equipo['coches'] * 500
    
    # Aplicamos un descuento aleatorio entre el 10% y el 20%
    descuento = random.randint(10, 20) / 100
    precio_oferta = precio_base * (1 - descuento)
    
    # Agregamos la oferta a la lista
    ofertas.append({'equipo': equipo['equipo'], 'precio_base': precio_base, 'descuento': descuento, 'precio_oferta': precio_oferta})

# Mostramos las ofertas generadas
print("Estas son las ofertas que hemos generado para ti, {}:".format(nombre))
for oferta in ofertas:
    print("Oferta para el equipo {}: precio base ${}, descuento del {}% (ahorro de ${}), precio de oferta ${}".format(oferta['equipo'], oferta['precio_base'], oferta['descuento']*100, oferta['precio_base']*oferta['descuento'], oferta['precio_oferta']))

