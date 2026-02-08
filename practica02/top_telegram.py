#!/usr/bin/env python3

import telepot # Biblioteca para interactuar con telegram 
from telepot.loop import MessageLoop # Permite manejar entradas de mensajes continuas
import os # Para interactuar con el sistemas op

# Añado modulos necesarios para el programa. El PYTONPATH esta en el bashrc
from alexteje_top import obtener_procesos, filtrar_procesos, imprimir_procesos
from alexteje_verificaciones import verificar_pythonpath, verificar_modulos
from alexteje_excepciones import PYTHONPATHError, ModuleMissingError

def leer_token():
    # Explicacion funcion: Lee el token del archivo token.txt
    try:
        with open("token.txt", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError("El archivo token.txt no existe. Por favor, crea uno con el token de tu bot.")
    except Exception as e:
        raise Exception(f"Error al leer el archivo token.txt: {e}")

def ejecutar_mi_top(opciones=""):
    # Explicacion funcion:  Ejecuta las funciones necesarias de los módulos para simular mi_top03.py
    
    try:
        # Procesar las opciones en formato: opciones_split = ["-u", "alex", "-t", "10"].
        opciones_split = opciones.split()
        usuario = None
        umbral_cpu = 0

        for i, opt in enumerate(opciones_split):
            # Si la opcion añadida es -u
            if opt == "-u" and i + 1 < len(opciones_split):
                usuario = opciones_split[i + 1]
            # Si la opcion es -t
            elif opt == "-t" and i + 1 < len(opciones_split):
                try:
                    umbral_cpu = float(opciones_split[i + 1])
                # Control de error por si la opcion -t no le sigue un valor numerico
                except ValueError:
                    return "Error: La opción -t requiere un valor numérico."
            elif opt in ["-h", "--help"]:
                return "Uso: mi_top [opciones]\n\nOpciones:\n  -u <usuario>   Filtra los procesos por usuario.\n  -t <umbral>    Muestra procesos con %CPU mayor que el umbral.\n  -h, --help     Muestra este mensaje de ayuda."

        # Obtener y filtrar procesos llamando a los modulos directamente
        salida_top = obtener_procesos()
        procesos_filtrados = filtrar_procesos(salida_top, usuario, umbral_cpu)

        # Imprimir salida con anchos fijos para que siempre salgan alineados los valores
        salida = []
        for proceso in procesos_filtrados:
            salida.append(
                "{:<20} {:<10} {:<10} {:<10} {:<30} {:>6.2f}".format(
                    proceso[0], proceso[1], proceso[2], proceso[3], proceso[4], proceso[5]
                )
            )
        # Si no hay procesos con % > 0
        return "\n".join(salida) if salida else "No se encontraron procesos que coincidan con los criterios."

    except Exception as e:
        return f"Error al intentar ejecutar mi_top03.py: {e}"

def dividir_mensaje(mensaje, tamano_max=4096):
    # Explicacion funcion: Divido el mensaje en partes más pequeñas (tamaño max = 4096)
    return [mensaje[i:i+tamano_max] for i in range(0, len(mensaje), tamano_max)]

def handle(msg):
    # Explicacion funcion: Maneja los mensajes entrantes del bot

    # RECORDATORIO: Chat y from son diccionarios llenos de varias claves, cada clave con su valor
    chat_id = msg["chat"]["id"]  # Obtienes clave ID del dicc chat 
    # Como text no es un dicc, obtengo directamente su valor
    texto = msg.get("text", "").strip().lower() # Obtienes Texto del mensaje, o mensaje vacio si no hay mensajes

    if texto.startswith("mi_top") or texto.startswith("top"):
        # Extraer opciones si las hay
        opciones = texto.split(maxsplit=1)[1] if len(texto.split()) > 1 else ""
        respuesta = ejecutar_mi_top(opciones)
    else:
        respuesta = "Ejecute mi_top o top, con alguna de estas opciones '-u', '-t', '-h'."

    # Dividir el mensaje si excede el tamaño máximo permitido
    mensajes = dividir_mensaje(respuesta)
    for mensaje in mensajes:
        bot.sendMessage(chat_id, mensaje)

def main():
    """Inicia el bot."""
    try:
        # Verificar entorno
        verificar_pythonpath()
        verificar_modulos("alexteje")

        # Leer token y configurar bot
        token = leer_token()
        
        # Crear el bot
        global bot
        bot = telepot.Bot(token)

        # Iniciar el bucle de manejo de mensajes a traves de threads
        MessageLoop(bot, handle).run_as_thread()

        while True:
            pass  # Mantener el programa corriendo

    # Control de excepciones
    except PYTHONPATHError as e:
        pass
    except ModuleMissingError as e:
        pass
    except Exception as e:
        pass

if __name__ == "__main__":
    main()
