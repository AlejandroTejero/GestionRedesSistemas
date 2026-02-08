#!/usr/bin/env python3

# Nombre: Alejandro
# Apellidos: Tejero de la Morena
# Login: alexteje

from optparse import OptionParser # Añadido para poder poner opciones al programa
import subprocess  # Ejecuta comandos externos o de python

# Explicacion del programa:
# Se encarga de mostrar el contenido del comando top -n 1 por pantalla pero solo los procesos que tengan + 0% uso CPU,
# tiene en especial que he añadido opciones que modifican la salida (-u, -t y -o)


def obtener_procesos():
    # Explicacion funcion: Ejecuccion del comando (batch= sin interfaz interactiva) 

    # Redirijo con stdout a pytohn para filtrarlo luego, y que sea una cadena de texto 
    result = subprocess.run(['top', '-b', '-n', '1'], stdout=subprocess.PIPE, text=True)
    return result.stdout

def obtener_usuario_info(usuario):
    # Explicacion funcion: Obtencion del UID (id -u) y de los grupos del usuario (id -Gn)
    
    try:
        # Obtener UID del usuario (Cuarta columna)
        result_uid = subprocess.run(['id', '-u', usuario], stdout=subprocess.PIPE, text=True)
        # Elimino titulo de UID
        uid = result_uid.stdout.strip()

        # Obtener nombres de grupos (5 columna)
        result_grupos = subprocess.run(['id', '-Gn', usuario], stdout=subprocess.PIPE, text=True)
        # Elimino titulo de grupos
        grupos = result_grupos.stdout.strip()

        return uid, grupos

    except Exception as e:
        return None, None

def filtrar_procesos(salida_top, usuario=None, umbral_cpu=0):
    # Explicacion funcion: Filtrado de la salida de top para incluir solo los procesos con %CPU > 0,

    # Lista donde metere los procesos correctos, es decir con % > 0.
    salida_filtrada = []
    titulos_encontrados = False # Saltar titulos del comando original 

    for linea in salida_top.splitlines():
        # Detectar y saltar la línea de encabezados
        if not titulos_encontrados and 'PID' in linea and '%CPU' in linea:
            titulos_encontrados = True  #Si titulos encontrados, saltar siguiente linea
            continue

        # Ignorar líneas primeras, con informacion no importante, al inicio de top -n 1
        if not titulos_encontrados or not linea.strip():
            continue

        # Parte importante, Filtrar procesos con %CPU > 0
        try:
            # Guardo los valores de las columnas en variables
            columnas = linea.split()
            pid = columnas[0]
            propietario = columnas[1]
            cpu = float(columnas[8].replace(',', '.')) # Quito puntos, dejo comas en numeros decimales
            comando = ' '.join(columnas[11:]) # En caso de que el nombre del proceso tenga espacios

            if cpu > umbral_cpu and (usuario is None or usuario == propietario):
                # Obtener información del usuario propietario
                uid, grupos = obtener_usuario_info(propietario)
                if uid and grupos:
                    # Guardo lista correcta para mostrarse en lista salida_filtrada.
                    salida_filtrada.append((comando, pid, propietario, uid, grupos, cpu))
        except (ValueError, IndexError):
            continue    # Ignorar líneas mal mostradas

    return salida_filtrada

def imprimir_procesos(procesos, archivo_salida=None):
    # Explicacion funcion: Imprimo resultado con el orden pedido, ademas alineo los resultados para que quede bien

    # Orden: Nombre Proceso, PID, Usuario, UID usuario, Grupos, Porcentaje CPU.
    output = [] # Lista para el output
    for comando, pid, usuario, uid, grupos, cpu in procesos:
        # Pintamos la salida con espacios definidos, para que no se junten por si son grandes nombres.
        # Anchos fijos para que siempre salgan alineados los valores
        linea = "{:<20} {:<10} {:<10} {:<10} {:<30} {:>6.2f}".format(
            comando, pid, usuario, uid, grupos, cpu
        )
        # Si el contenido esta bien lo guardo para la opcion -o
        output.append(linea)
    if archivo_salida:
        # Escribir el contenido en el fichero.
        with open(archivo_salida, 'w') as f:
            f.write('\n'.join(output) + '\n')
    else:
        # Si no se usa opcion -o, pintar en el terminal 
        print('\n'.join(output))

def main():
    # Configuracion de las opciones
    parser = OptionParser()

    # Opcion 1: Filtrar por nombre
    parser.add_option("-u", "--user", dest="user", help="Filtrar procesos por usuario")
   
   # Opcion 2: Filtrar por valor CPU
    parser.add_option("-t", "--threshold", dest="threshold", type="float", default=0,
                      help="Mostrar procesos con %CPU mayor al umbral especificado")
   
    # Opcion 3: Guardar salida
    parser.add_option("-o", "--output", dest="output", help="Guardar salida en un archivo")

    # Leer opciones
    (options, args) = parser.parse_args()

    # Obtener y filtrar procesos
    salida_top = obtener_procesos()
    procesos = filtrar_procesos(salida_top, usuario=options.user, umbral_cpu=options.threshold)

    # Por si acaso no hay procesos con % > 0 de cpu, aunque siempre suelen existir
    if procesos:
        imprimir_procesos(procesos, archivo_salida=options.output)
    else:
        print("No se encontraron procesos con %CPU > 0.")

if __name__ == '__main__':
    main()
