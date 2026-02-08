#!/usr/bin/env python3

import telepot # Biblioteca para interactuar con telegram 
from telepot.loop import MessageLoop # Permite manejar entradas de mensajes continuas 
import time 
import os # Para interactuar con el sitemas op
import sys # Incluye funciones de python

def leer_token():
    # Explicacion funcion: Lee el token desde el archivo token.txt en el directorio actual.

    archivo_token = "token.txt"
    # Si no existe:
    if not os.path.exists(archivo_token):
        print(f"Error: El archivo '{archivo_token}' no existe.", file=sys.stderr)
        sys.exit(1)  # Termina el programa con el código de error
    try:
    # Si si existe:
        with open(archivo_token, 'r') as f:
            return f.read().strip()  # Lee el token y elimina espacios o saltos de línea
    # Manejo de excepcion:
    except Exception as e:
        print(f"Error: No se pudo leer el archivo '{archivo_token}': {e}", file=sys.stderr)
        sys.exit(1) # Termina el programa con el código de error

def convertir_fecha_unix_a_legible(fecha_unix):
    # Explicacion funcion: Convierte una fecha Unix a un formato legible ajustado a la hora local del sistema.

    t = time.localtime(fecha_unix)  # Convierte la marca de tiempo a struct_time en la hora local
    # Formato que asegura que el año tenga 4 digitos, el mes 2...
    return "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(
        t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec
    )

def handle(msg):
    # Explicacion funcion: Maneja los mensajes recibidos en el bot.

    # RECORDATORIO: Chat y from son diccionarios llenos de varias claves, cada clave con su valor
    chat_id = msg["chat"]["id"]  # Obtienes clave ID del dicc chat 
    # Como text no es un dicc, obtengo directamente su valor
    texto = msg.get("text", "")  # Obtienes Texto del mensaje, o mensaje vacio si no hay mensajes
    nombre = msg["from"]["first_name"]  # Obtienes first_name de from
    id_usuario = msg["from"]["id"]  # ID del usuario
    tipo_chat = "privado" if msg["chat"]["type"] == "private" else "en grupo"  # Tipo de chat

    # Convertir fecha Unix a formato legible usando la hora local
    fecha_legible = convertir_fecha_unix_a_legible(msg["date"])

    # Crear frase legible para mostrar en terminal usando format
    frase = (
        "El usuario \"{nombre}\" (ID: {id_usuario}) envió un mensaje {tipo_chat} diciendo: \"{texto}\". "
        "Fecha del mensaje: {fecha}."
    ).format(
        # Asigno a cada parte de la frase su valor
        nombre=nombre,
        id_usuario=id_usuario,
        tipo_chat=tipo_chat,
        texto=texto,
        fecha=fecha_legible
    )

    print(frase)  # Mostrar frase en terminal

    # Responder al cliente en Telegram usando format
    respuesta_en_telegram = "Hola {nombre}, me has dicho: {texto}".format(nombre=nombre, texto=texto)
    bot.sendMessage(chat_id, respuesta_en_telegram)

def main():
    # Función principal del programa

    # Leer el token desde el archivo
    token = leer_token()

    # Crear el bot
    global bot
    bot = telepot.Bot(token)

    # Enviar un mensaje inicial al usuario
    id_usuario = "2030217618"
    bot.sendMessage(id_usuario, "Buenos dias Alejandro")

    # Iniciar el bucle de manejo de mensajes a traves de threads
    MessageLoop(bot, handle).run_as_thread()
    print("Escuchando mensajes...")

    # Mantener el programa en ejecución
    while True:
        time.sleep(10)

if __name__ == "__main__":
    main()

