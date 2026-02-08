#!/usr/bin/env python3

#Nombre: Alejandro
#Apellidos: Tejero de la Morena
#Login: alexteje


def ordenar_lista(lista):
    # Verificamos si el argumento es de tipo lista
    if not isinstance(lista, list):
        raise TypeError("El argumento debe ser una lista.")

    # Verificar que todos los elementos de la lista sean cadenas
    for elemento in lista:
        if not isinstance(elemento, str):
            raise Exception("MALLLLL, elementos deben ser cadenas")
            
            #OTRA FORMA de lanzar la excepcion
            #raise TypeError("Todos los elementos de la lista deben ser cadenas.")

    # Ordenar la lista por la longitud de las cadenas
    lista.sort(key=len)


# EJEMPLO 1:
lista = ["Alejandro", "Bisbal", "Camavinga", "Lewandoski"]

try:
    ordenar_lista(lista)
    print(lista)  # Imprime la lista ordenada por longitud
except Exception as e:
    print(f"Error: {e}")

