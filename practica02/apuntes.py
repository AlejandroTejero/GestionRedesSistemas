#!/usr/bin/env python3
import telepot
import telepot.namedtuple
import time
from telepot.loop import MessageLoop

TOKEN = "7449152748:AAFaQnSAT5rCVCJvfJJxTMT8a7jgUA_Kc88"
bot = telepot.Bot(TOKEN)

def handle(msg):
    
    chat_id = msg["chat"]["id"]
    texto = msg["text"]
    
    print("Recibiendo mensaje:")
    print(msg)
    
    respuesta = "Me has dicho " + texto
    bot.sendMessage(chat_id, respuesta)

    return

def main():
    
    MessageLoop(bot, handle).run_as_thread()
    print("Escuchando...")
       
    while 1:
        time.sleep(10)
    return

if __name__ == "__main__":
    main()
