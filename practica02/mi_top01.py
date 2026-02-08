#!/usr/bin/env python3

# Nombre: Alejandro
# Apellidos: Tejero de la Morena
# Login: alexteje

import subprocess # Ejecuta comandos externos o de python

# Explicacion del programa:
# Se encarga de mostrar el contenido del comando top -n 1 por pantalla pero solo los procesos que tengan + 0% uso CPU

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

def filtrar_procesos(salida_top):
    # Explicacion funcion: Filtrado de la salida de top para incluir solo los procesos con %CPU > 0,

    # Lista donde metere los procesos correctos, es decir con % > 0.
    salida_filtrada = []
    titulos_encontrados = False # Saltar titulos del comando original 

    for linea in salida_top.splitlines():
        # Detectar y saltar la línea de encabezados
        if not titulos_encontrados and 'PID' in linea and '%CPU' in linea:
            titulos_encontrados = True   #Si titulos encontrados, saltar siguiente linea 
            continue

        # Ignorar líneas primeras, con informacion no importante, al inicio de top -n 1
        if not titulos_encontrados or not linea.strip():
            continue

        # Parte importante, Filtrar procesos con %CPU > 0
        try:
            # Guardo los valores de las columnas en variables
            columnas = linea.split()
            pid = columnas[0]
            usuario = columnas[1]
            cpu = float(columnas[8].replace(',', '.')) # Quito puntos, dejo comas en numeros decimales
            comando = ' '.join(columnas[11:])  # En caso de que el nombre del proceso tenga espacios

            if cpu > 0.0:
                # Obtener información del usuario propietario
                uid, grupos = obtener_usuario_info(usuario)
                if uid and grupos:
                    # Guardo lista correcta para mostrarse en lista salida_filtrada.
                    salida_filtrada.append((comando, pid, usuario, uid, grupos, cpu))
        except (ValueError, IndexError):
            continue  # Ignorar líneas mal mostradas

    return salida_filtrada

def imprimir_procesos(procesos):
    # Explicacion funcion: Imprimo resultado con el orden pedido, ademas alineo los resultados para que quede bien
    # Orden: Nombre Proceso, PID, Usuario, UID usuario, Grupos, Porcentaje CPU.
    
    for comando, pid, usuario, uid, grupos, cpu in procesos:
        # Pintamos la salida con espacios definidos, para que no se junten por si son grandes nombres.
        # Anchos fijos para que siempre salgan alineados los valores
        print("{:<20} {:<10} {:<10} {:<10} {:<30} {:>6.2f}".format(
            comando, pid, usuario, uid, grupos, cpu
        ))

def main():
    # Ejecucion del programa entero.

    salida_top = obtener_procesos()
    procesos = filtrar_procesos(salida_top)

    # Por si acaso no hay procesos con % > 0 de cpu, aunque siempre suelen existir
    if procesos:
        imprimir_procesos(procesos)
    else:
        print("No se encontraron procesos con %CPU > 0.")

if __name__ == '__main__':
    main()

