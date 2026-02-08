## Práctica 3.2. FHS

1. Primero creo 3 archivos en tenxto plano con diferentes frases, importante que tenga letras como la ñ para ver como cambia la codificacion.
2. Para comprobar la codificacion de los ficheros ejecuto:
```bash 
file <nombre_archivo.txt>
```
- El resultado de este comando es siempre el mismo:
```bash
TextoX.txt: Unicode text, UTF-8 text
```
3. Para ver la codificacion empleada en mi maquina ejecutamos:
```bash 
locale
```
 Y buscamos donde ponga LANG, en este caso sale: LANG=es_ES.UTF-8

4. Convertimos los ficheros a una codificacion distinta con:
```bash
cp TextoX TextoXcod
recode <codificacion actual>..<codificacion deseada> <TextoXcod>
recode utf-8..cp1252 Texto1cod
``` 

- En este caso he creado los siguientes archivos:
```bash
Texto1cod.cp1252.txt
Texto2cod.latin1.txt
Texto3cod.utf16.txt
```
- Se puede observar como cambian algunos caracteres como las tildes, o las ñ.
Como dato los caracteres que suelen cambiar suelen ser: ",',-,_ ...


## Práctica 3.3. Cron

- Esta practica la hare desde mi sistema operativo ya que cron es uno de los demonios que se inicia con el ordenador. 
- Para ver si cron esta funcionando ejecutare este comando, para ver si se abre la tabla, si cron no esta instalado saltara un warning
```bash
crontab -e
```

1. Para ejecutar cada minuto necesitamos 5 asteriscos, que perteneceran a los campos de m,h,dayofmonth,month y dow.
- Abriremos la tabla con el comando anterior (crontab -e) y ahi meteremos la siguiente linea:
```bash 
* * * * * touch /tmp/test_cron_alejandro
```
- Mas alante se comentara esta linea ya que es simplemente para comprobar si funcion cron, por eso lo creamos en el tmp. Una vez que veamos en el tmp que se ha creado el archivo comentamos la linea.

- Para que el fichero que crearemos en el siguiente punto se actualice cada minuto debemos añadir esta linea
```bash 
* * * * * ~/Desktop/lagrs/practica03/escribe_log
```

2. Ahora debemos crear el scrip escribe_log (sin extension) con:
```bash 
touch escribe_log
```
- Modificaremos el scrip donde añadiremos lo siguiente: 
```bash 
#!/bin/bash

echo "probando cron - $(date)" >> ~/Desktop/lagrs/log.txt
```
- Esto hara que se cada vez que se ejecute de mande esa linea al final del fichero log.txt, y la primera vez que se ejecute se creara dicho fichero.

- Para que escribe_log se pueda ejecutar debemos darle permisos con:
```bash
chmod +x escribe_log
```

- He comentado el contenido de contab -e para que no se llene el archivo log.txt. Para ver si la tarea estaba funcionando:
```bash
tail -f ~/Desktop/lagrs/log.txt
```

3. Para cambiar la periodicidad de la tarea abriremos crontab -e y debajo de la linea comentada de ejecuccion cada minuto añadimos esto:
```bash
0 9 * * 1-5 ~/Desktop/lagrs/practica03/escribe_log
```
- Significado: Ejecuta a las 9 horas, de cual dia del mes, de lunes-viernes (1-5).
- Minuto,hora,dia del mes (dos dias),dias semana













