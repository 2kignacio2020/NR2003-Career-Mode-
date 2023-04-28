# Importamos la librería para trabajar con archivos
import os

# Definimos la función que agrupa los equipos y pilotos y asigna la reputación
def generar_lista(nombre_archivo):
    
    # Abrimos el archivo
    with open(nombre_archivo, 'r') as archivo:
        # Leemos todas las líneas del archivo
        lineas = archivo.readlines()
        
        # Creamos un diccionario para almacenar los equipos y pilotos
        equipos_pilotos = {}
        
        # Recorremos cada línea del archivo
        for linea in lineas:
            # Separamos la línea en las diferentes partes (equipo, piloto, número de coches)
            partes = linea.strip().split(',')
            
            # Si el equipo ya existe en el diccionario, agregamos el piloto y el número de coches
            if partes[0] in equipos_pilotos:
                equipos_pilotos[partes[0]]['pilotos'].append(partes[1])
                equipos_pilotos[partes[0]]['coches'] += int(partes[2])
            # Si el equipo no existe, creamos una nueva entrada en el diccionario
            else:
                equipos_pilotos[partes[0]] = {'pilotos': [partes[1]], 'coches': int(partes[2])}
        
        # Creamos una lista con los equipos y pilotos, y les asignamos la reputación basada en el número de coches
        lista_final = []
        for equipo, datos in equipos_pilotos.items():
            reputacion = datos['coches'] * 100
            for piloto in datos['pilotos']:
                lista_final.append({'equipo': equipo, 'piloto': piloto, 'reputacion': reputacion})
    
    # Retornamos la lista final ordenada por equipo y piloto
    return sorted(lista_final, key=lambda x: (x['equipo'], x['piloto']))

# Pedimos al usuario que ingrese el nombre del archivo
nombre_archivo = input("Ingrese el nombre del archivo: ")

# Verificamos si el archivo existe
if os.path.exists(nombre_archivo):
    # Si existe, generamos la lista
    lista_final = generar_lista(nombre_archivo)
    # Imprimimos la lista final
    for item in lista_final:
        print(item)
else:
    # Si no existe, mostramos un mensaje de error
    print("El archivo no existe.")
