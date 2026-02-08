import subprocess  # Ejecuta comandos del sistema

def obtener_procesos():
    result = subprocess.run(['top', '-b', '-n', '1'], stdout=subprocess.PIPE, text=True)
    return result.stdout


def obtener_usuario_info(usuario):
    # Obtiene el UID y los grupos del usuario, omitiendo errores de usuarios no válidos.
    try:
        # Ejecuto el comando (id -u) con run
        result_uid = subprocess.run(
            ['id', '-u', usuario],
            # Capturo salida estandar del terminal
            stdout=subprocess.PIPE,
            # Redirigir errores de `id` a /dev/null
            stderr=subprocess.DEVNULL,
            text=True
        )
        uid = result_uid.stdout.strip()
        # Ejecuto el comando (id -Gn) con run
        result_grupos = subprocess.run(
            ['id', '-Gn', usuario],
            # Capturo salida estandar del terminal
            stdout=subprocess.PIPE,
            # Redirigir errores de `id` a /dev/null
            stderr=subprocess.DEVNULL,
            text=True
        )
        grupos = result_grupos.stdout.strip()

        return uid, grupos
    except Exception:
        return None, None


def filtrar_procesos(salida_top, usuario=None, umbral_cpu=0):
    # Explicacion funcion: Filtrado de la salida de top para incluir solo los procesos con %CPU > 0,

    # Lista donde metere los procesos correctos, es decir con % > 0.
    salida_filtrada = []
    titulos_encontrados = False

    for linea in salida_top.splitlines():
        # Detectar y saltar la línea de encabezados
        if not titulos_encontrados and 'PID' in linea and '%CPU' in linea:
            titulos_encontrados = True #Si titulos encontrados, saltar siguiente linea
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
            continue # Ignorar líneas mal mostradas

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
        try:
            # Escribir el contenido en el fichero.
            with open(archivo_salida, 'w') as f:
                f.write('\n'.join(output) + '\n')
        except IOError as e:
            print(f"Error al escribir en el archivo: {e}")
    # Si no se usa opcion -o, pintar en el terminal 
    else:
        print('\n'.join(output))

