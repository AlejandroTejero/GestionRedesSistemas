# MEMORIA PRÁCTICA 1:

## Práctica 1.1. Directorios de las prácticas

1.  Crea el directorio en home:

``` bash
pandoc -s -c pandoc.css test_markdown.md -o test_markdown_css.html
```

2.  Creo un symlink a la carpeta con:

``` bash
ln -s <ruta_origen> <ruta_destino>
ln -s ~/lagrs ~/Escritorio
```

3.  Ponle permisos rwx:

``` bash
chmod 700 ~/largs
```

4.  Crea el directorio:

``` bash
mkdir ~/largs/practica01
```

5.  Crea el fichero:

``` bash
touch ~/largs/practica01.md
```

6.  Crea un directorio images:

``` bash
mkdir ~/largs/images
```

## Práctica 1.2. Uso básico de vi

1.  Crea fichero ejemplo.md con vim:

``` bash
vim ~/largs/practica01/ejemplo.md
```

2.  Pulsamos a o i para modo escritura, esc para salir del modo y
    escribimos :wq para cerrar y guardar o :q! para salir sin
    guardar.

## Práctica 1.3. Uso de un editor sin gráficos

1.3.1. De momento me quedaré con el editor de texto "vim", ya que
por foros dicen que es un básico y que es tan usado que en
cualquier sistema Unix viene de forma predeterminada. Aunque al
comienzo parece un poco difícil creo que una vez consigas
dominarla tiene un gran potencial.

1.3.2 Algunos atajos imprescindibles: a: Pasar de modo orden a
modo insertar R: Pasar de modo orden a modo reemplazar Esc:
Volver al modo orden x: Eliminar un carácter :wq : Guardar el
fichero y salir :q! : Salir sin guardar el fichero

Luego existen otras órdenes interesantes: :r nombre: Lee el
fichero con ese nombre :w nombre: Escribe el fichero ctrl r:
Rehacer lo último desecho u: Deshace el último cambio

## Práctica 1.4. Markdown

1.  Preparamos el documento con:

``` bash
touch <direccion/nombre_archivo.md>
touch ~/lagrs/practica01/test_markdown.md
```

2.  Para abrir el documento escribiremos:

``` bash
vi <direccion/nombre_archivo.md>
vi ~/lagrs/practica01/test_markdown.md
```

3.  Una vez abierto podremos escribir en formato markdown,
    ejemplo en el md.

4.  Primero debemos crear el scrip en el home, con el nombre de
    clean_md.sh, para limpiar el fichero con pandoc pondremos:

``` bash
<direccion_clean/clean_md.sh> <Direccion Archivo/nombre_archivo>
~/clean_md.sh ~/lagrs/practica01/test_markdown.md
```

- Tanto clean como test_markdown tienen que tener la direccion
  delante si no se encuentran en el mismo sitio, el .sh debe
  estar en el home. En este caso el terminal esta en el home asi
  que solo ponemos la direccion de test_markdown

![**Ejemplo comando clean_md.sh**](images/clean_md.png)

Esto pasará el archivo de markdown a markdown, colocando y
limpiando el texto escrito.

5.  Para generar una versión html del .md pondremos:

``` bash
pandoc -s -c <direccion_pandoc_css> <direccion_archivo> -o <direccion_y_nombre.html>
pandoc -s -c pandoc.css test_markdown.md -o test_markdown_css.html
```

- El primer md sera el nombre de nuestro archivo mientras que el
  siguiente será el nombre del nuevo archivo html. En este caso
  tenemos el css de pandoc en el archivo llamado pandoc.css, por
  lo que no es el css base. Ahora el terminal está en la carpeta
  home, asi que ponemos la dirección del archivo pandoc, del
  archivo test_markdown y donde quieres que se guarde el html.

![**Ejemplo de pandoc**](images/pandoc.png)

![**css de pandoc**](https://gsyc.urjc.es/~mortuno/pandoc.css)
![**css de killercup**](https://gsyc.urjc.es/~mortuno/md.css)

Arriba a la izq tenemos el *css de pandoc*, y a la derecha el
*css de killercup*.

Si queremos usar la css de killercup deberiamos crear un
killercup.css con ese codigo y cambiar el comando a:

``` bash
pandoc -s -c <direccion_killercup_css> <direccion_archivo> -o <direccion_y_nombre.html>
pandoc -s -c killercup.css test_markdown.md -o test_markdown_css.html
```

## Práctica 1.5. Gestión de contraseñas

1.  Cifrado con gpg Creo un txt con:

``` bash
touch <Direccion y nombre arhivo.txt>
touch ~/lagrs/PruebaGpg.txt
```

E introduzco las contraseñas dentro. Ahora ciframos con:

``` bash
gpg -c PruebaGpg.txt
```

Una vez cifrado el txt lo podemos descrifrar con:

``` bash
gpg PruebaGpg.txt.gpg
```

![**PruebaGpg**](images/PruebaGpg.png)

2.  Cifrado con LibreOffice

Abriremos un archivo de escritura, escribiremos nuestra
contraseña y al guardar le daremos a añadir cifrado.

![**PruebaOffice**](images/PruebaOffice.png)

3.  Cifrado con KeePassX

Al crear el archivo te pedira que crees la contraseña de entrada,
una vez creada puedes guardar tus contraseñas. Cada vez que
quieras inciar el archivo tendras que meter esta contraseña
inicial.

![**PruebaKPX**](images/PruebaKPX.png)

## Práctica 1.6. Secret Sharing

Para crear una contraseña con sss de 6 trozos, de forma que con
juntar 4 de esos trozos sirva para recomponerla hemos de hacer lo
siguiente:

``` bash
sss-split -t 4 -n 6
```

Indica que con 4 de esos 6 trozos es suficiente. Después nos
pedira que introduzcamos la contraseña y nos dará 6 fragmentos.

![**Ejemplo ssss**](images/ssss-split.png)

Para restaurar la contraeña hemos de introducir:

``` bash
sss-combine -t 4
```

Nos pedirá que introduzcamos 4 fragmentos de los 6 anteriores, no
hace falta que sean en orden. Ejemplo:

![**Ejemplo restauración ssss**](images/ssss-combine.png)

## Práctica 1.7. Vagrant

1.  Primero debemos crear el project directory:

``` bash
mkdir ~/lagrs/vbox01
```

2.  Iniciaremos la app virtualbox con:

``` bash
virtualbox
```

- Debemos cambiar el directorio por **/var/tmp/alexteje**, aqui
  se guardara la maquina virtual. Es un sitio de guardado
  temporal, ya que la maquina virtual ocupa mucho espacio.

3.  Para crear una maquina virtual de ubuntu 24.04 pondremos (en
    ~/lagrs/vbox01):

``` bash
vagrant init bento/ubuntu-24.04
```

- Este comando crea un vagrantfile, que contiene los detalles de
  la creacion de la maquina. Aqui es donde puedes cambiar el
  nombre de la maquina entre otras cosas.
- Esto solo se hace una vez, es para crear la maquina virtual de
  inicio, si ya la creaste en otro momento solo tienes que
  levatarla con up y meterte con ssh
- Tardara un poco en crearse, pero una vez se haya creado la
  maquina virtual debemos levantarla

4.  Para ello ponemos:

``` bash
vagrant up
```

5.  Despues entraremos a la maquina virtual con:

``` bash
vagrant ssh
```

6.  Ya estaras dentro de la maquina **vagrant@vagrant**, dentro
    tienes acceso a la carpeta vagrant:

``` bash
cd vagrant
```

- Esta carpeta es **MUY IMPORTANTE** ya que esta conectada con el
  home de tu usario (home/alexteje) y todo lo que guardes en esta
  carpeta se guardara en tu home. Desde tu usario normal tambien
  podras editar estos proyectos de forma que se guardara en la
  maquina virtual. Esto se hace por si se borra la maquina
  virtual poder seguir teniendo las cosas guardadas.

- Todos estos comandos debemos hacerlos en el project directory,
  en ese caso en vbox01, es decir, cd lagrs/vbox01. Sino no se
  estaria levantando la maquina virtual correcta. Cada maquina
  tiene su propia carpeta/project directory.

7.  Para cambiar el nombre de la maquina a **vagratn@vbox01**
    deberemos añadir en el fichero vagrantfile:

``` bash
vi vagrantfile
config.vm.hostname = "vbox01"
config.vm.define vbox01
```

8.  Para apagar la maquina virtual iremos al terminal del project
    directory (~/lagrs/vbox01), podemos apagarla, dormirla o
    eliminarla:

``` bash
vagrant halt
vagrant suspend
vagrant destroy
```

## Practica 1.8. Usuarios y Grupos

1.  Primero debemos iniciar la maquina virtual, nos meteremos en
    ~/lagrs/vbox01 y ejecutaremos levataremos la maquina virtual
    con **vagrant up**, despues accederemos con **vagrant ssh**.

2.  Para crear un nuevo usuario debemos poner:

``` bash
sudo adduser alexteje
```

3.  Abriremos sesion con el nuevo usuario con unos de estos
    comandos:

``` bash
su alexteje
```

4.  Como el usuario no tiene privilegios e intentamos ejecutar
    sudo apt update por ejemplo, nos pedira una contraseña pero
    al introducirla el proceso fallara
5.  Para poder ejecutar comandos sudo debemos volver al usario
    principal y darle privilegios:

``` bash
su usuario_princial
sudo usermod -aG sudo alexteje
```

6.  Volvemos a la sesion creada con **su alexteje** y ahora si
    podremos ejecutar sudo apt update
7.  Crearemos dos grupos con nombres cualquiera y meteremos el
    usuario en estos grupos con:

``` bash
sudo groupadd nombregrupo
groups alexteje
```

8.  La orden **newgrp** cambia el grupo primario temporalmente
    por el que elijas. Si ejecutamos:

``` bash
newgrp grupo1
```

Podremos comprobarlo con el comando **id**.

9.  Para salir de la sesion ejecutaremos **exit**

## Practica 1.9. Ssh sin contraseñas

- En esta parte configuraremos la cuenta de laboratorio para
  poder entrar desde cualquier otra sin necesidad de escribir
  contraseñas.

-Primero ejecutaremos el comando:

``` bash
ssh-keygen
```

Esto nos generara una clave publica/privada que la guardara en el
archivo /.ssh/id_ed25519 (Se puede abrir y ver la contraseña)

- Al ejecutar ese comando nos deja cifrar la contraseña aleatoria
  con un contraseña nuestra (passphrase) que podremos o no crear.
  Al seguir creara una identificacion que se guardara en
  ./ssh/id_ed25519.pub
- Al seguir saldra un dibujo aleatorio que nos indica que ya ha
  la contraseña ha sido creada correctamente, si deseamos en
  algun momento crear otra diferente habria que seguir estos
  pasos y al llegar al dibujo se creara otro distinto.
- Para acceder a los archivos anteriores es conveniente acceder
  con uno de estos dos comandos:

``` bash
view nombre_archivo
cat nombre_archivo
```

View para evitar modificar sin querer y cat para que salga por
terminal.

- Todo esto es para crear la clave publica/privada, solo hay que
  hacerlo una vez.

- **Acceder sin contraseña**: Para poder acceder a otro ordenador
  sin contraseña debemos añadir esta contraseña que acabamos de
  crear (/.ssh/id_ed25519.pub) en el .ssh/authorized_keys del
  ordenador al que queremos acceder.

- Ahora necesitamos dar permisos. Mas concretamente estos:

1.  Dueño : Permisos 700
2.  Ssh : Permisos 700
3.  Ficheros de ssh: Permisos 600
4.  Ademas necesitaremos que los ficheros pertenezcan al usuario
    y tengan como grupo el usuario

- Para poder ver los permisos tenemos estos comandos: Comandos de
  los archivos de la carpeta ssh, una vez que estamos en ese
  directorio:

``` bash
ls -l
```

Si no estamos en el directorio ssh:

``` bash
ls -l .ssh
```

Permisos de la carpeta ssh, necestiamos estar en home
(Escritorio, lagrs,Musica... ):

``` bash
ls -ld .sshls -l .ssh
```

![**Observacion de permisos**](images/Permisos.png)

## Practica 1.10. Ssh sin contraseñas

- Para configurar la maquina para acceder sin contraseña debemos
  añadir el /.ssh/id_ed25519.pub en el /.ssh/authorized_keys de
  la maquina virtual.

- Para probar los ficheros tar, he creado con touch un archivo
  llamado Prueba.md y he escrito dentro de el.

- Para comprimirlo a .tar debemos

``` bash
tar -cvf <NombreTar.tar> <Direccion y nombre del archivo a comprimir> 
tar -cvf Prueba_tar.tar Prueba.md
```

- Con view podras obrservar el nombre del archivo y su interior
  el contenido
- Para descomprimir usaremos

``` bash
tar -tf <NombreArchivoTar.tar>
tar -tf archivo.tar
```

## Practica 1.10bis. Provisionamineto del box

-En esta practica craremos el provisionamineto de la maquina
virtual para poder cceder desde cualquier maquina de la
universidad. Para ello deberemos realizar estos pasos al iniciar
el box desde una maquina diferente:

1.  Iniciar virtualbox y eliminar la vbox01
2.  Levantar una nueva maquina con vafrant up

**Recordatorio**: Si queremos editar el Vagrantfile e actualizar
la maquina debemos realizar:

``` bash
vagrant destroy
vagrant up
vagrant ssh
```

- Para realizar el provisionamineto haremos lo siguiente:

![**VagrantFile**](images/Vagrantfile.png)

- Añadimos el usuario de esta forma (adduser) ya que le crea el
  directorio personal (con useradd hay que añadir las lineas
  comentadas).
- Gecos se refiere a informacion extra del usuario como su
  oficina... de momento no nos interesa. El disbled password nos
  permite crearlo sin pedir la contraseña inicial para crearlo,
  la contraseña del usuario habra que introducirla cuando se
  inicie. Y por ultimo el echo chpassw sirve para establecer la
  contraseña del usuario.
- El directorio ssh del usuario no estara crearlo, asi que
  debemos crearlo y añadirle el authorized_key. deontro hay que
  añadir la clave con:

``` bash
scp ~/.ssh/authorized_keys usuario@ip_de_maquina_virtual:~/.ssh/
cp  ~/.ssh/authorized_keys usuario@ip_de_maquina_virtual:~/.ssh/
cp solo funciona en el mismo sistema, scp para copiar de un sist a otro (pc-vbox01)
```

- Ademas de esto, para poder acceder sin contraseña debemos darle
  permisos al usuario con chown y chgrp a los directorios
  creados.

## Practica 1.11. Scp

1.  Accederemos al directorio tmp de mi maquina y crearemos un
    archivo de prueba para enviarlo con scp a otra maquina, de
    esta forma:

``` bash
cd /tmp
touch <nombre_fichero>
scp Prueba_scp.md alexteje@f-l3109-pc03.aulas.eif.urjc.es:/tmp
scp <nombre_fichero> <usuario>@<ip_del_vecino>:/tmp
```

- Al hacer scp por primera vez con un vecino nos saldra un
  mensaje de que se guarda la claves de ese host en
  /.ssh/known_hosts
- Si entramos al puesto vecino con ssh podremos ver el archivo en
  /tmp

2.  Creamos el directorio en /tmp del vecino con nuestro nombre
    de usuario, creamos algunos ficheros y lo mandamos a nuestro
    puesto habitual:

``` bash
ssh alexteje@<ip_vecina>
mkdir alexteje
cd alexteje
touch <archivo.md>
cd .. (cd /tmp) --> Para situarnos en /tmp/
scp -r alexteje alexteje@f-l3109-pc07.aulas.eif.urjc.es:/tmp
```

- el -r sera neccesario para copiar un directorio, antes como era
  un solo fichero (Prueba_scp.md) no era neccesario

3.  **Importante (ip vbox01)**: Para copiar ficheros y archivos
    necesitamos saber la direccion ip de la maquina virtual, si
    realizamos:

``` bash
ip a
```

Saldran los datos de la maquina, buscando en eth0 encontramos la
dirrecion mas concretamente donde pone inet (inet 10.0.2.15/24),
asi que pondremos 10.0.2.15

- Para copiar el fichero haremos

``` bash
scp <nombre_del_archivo> vagrant@10.0.2.15:/tmp
```

4.  Y para copiar el fichero haremos

``` bash
scp -r <nombre_del_directorio> vagrant@10.0.2.15:/tmp
```

**Error a saber:**

- Estos comandos aunque parezca que lo mandan al usuario creado
  en vagrant, no es asi. Lo que hacen es guardarlo en el mismo pc
  desde donde estas ejcutando el comando (localhost).

``` bash
scp <nombre_del_archivo> alexteje@localhost:/tmp
scp -r <nombre_del_directorio> alexteje@localhost:/tmp
```

## Practica 1.12. Split

1.  Descargamos unas fotos y las guardamos en el directorio fotos

``` bash
mkdir fotos
```

2.  Calculamos y guardamos los hash de todas las fotos

``` hash
cd fotos
sha256sum * > hashes_almacenados.txt
```

- Esto creara los hashes de sha-256 de cada foto y los metera en
  un txt llamado hashes_almacenados

3.  Comprimimos el directorio donde estas las imagenes

``` bash
tar -czvf fotos_comprimidas.tgz fotos/
tar -czvf mi_directorio.tgz mi_directorio/
```

- Siendo fotos_comprimidas el nombre del nuevo fichero creado
  (compresion de fotos) y fotos/, el fichero original que hemos
  comprimido

4.  Trocearemos el fichero en ficheros mas pequeños de por
    ejemplo 1 MB

``` bash
split -b 1M fotos_comprimidas.tgz trozos_fotos_comprimidas_
split -b 1M mi_directorio.tgz parte_ 
```

- Donde parte_ se refiere al nombre que recibiran los trozos del
  archivo, en este caso los trozos en los que se divide el
  directorio fotos_comprimidas, se llamaran
  trozos_fotos_comprimidas_aa, trozos_fotos_comprimidas_ab...

5.  Para copiar los trozos al directorio /tmp de vbox01 debemos:

``` bash
scp trozos_fotos_comprimidas_* vagrant@10.0.2.15:/tmp
```

- Con el \* hacemos que se envien todos los archivos que tengan
  el nombre trozos_fotos_comprimidas_...

6.  Para recomponer los trozos en vbox01 debemos:

``` bash
vagrant up
vagrant ssh
cd /tmp
cat trozos_fotos_comprimidas_* > fotos_reconstruidas.tgz
```

- Con el cat anterior crearemos un fichero tar llamado
  fotos_reconstruidas

- Para extraer los ficheros del fichero anterior, debemos:

``` bash
tar -xzvf fotos_reconstruidas.tgz
```

7.  Para calcular los hashes de los ficheros y comprobar que son
    identicos a los originales, deberemos en /tmp de vbox01 sacar
    las fotos de fotos_recostruidas a una carpeta llamada fotos y
    comprobarlos:

``` bash
cd /tmp/fotos
sha256sum * > hashes_extraidos.txt
```

- Extraemos los hashes en un fichero, y comprobamos

``` bash
diff hashes_almacenados.txt hashes_extraidos.txt
```

- Si no existen diferencias el comando diff no mostrara nada, en
  caso contrario mostrara las diferencias entre los hashes

## Practica 1.13. Rsync

1.  El primer paso sera el envio de un directorio local a una
    maquina remota, para ello he hecho:

``` bash
mkdir Prueba_rsync
touch Archivo_prueba.md
vi Archivo_prueba.md --> Para añadir contenido
rsync -avz Prueba_rsync alexteje@f-l3109-pc07.aulas.eif.urjc.es:~/Escritorio
rsync -avz /directorio_local usuario@maquina_remota:/directorio_remoto --> Comando ejecutado
```

- De esta manera estoy enviando el fichero Prueba_rsync al
  escritorio de la maquina virtual. Si en el comando pongo
  PRueba_rsync/, esto hace que se envien los contenidos de dentro
  del fichero sueltos

2.  Para hacerlo al contrario, es decir, de la maquina virtual a
    la maquina virtual haremos esto pero desde la **maquina
    local**:

``` bash
rsync -avz alexteje@f-l3109-pc07.aulas.eif.urjc.es:~/Escritorio/Prueba_rsync ~/Desktop
rsync -avz usuario_remoto@ip_remota:/ruta/directorio_remoto /ruta/destino_local
```

- De esta forma conseguimos copiar el direcotrio entero en la
  maquina local. Aqui al igual que antes, si solo queremos los
  contenidos del fichero y no el fichero haremos
  /ruta/directorio_remoto/, importante el / del final.

3.  Consulta la pagina del manual, elige tres opciones y
    comprueba que se comportan como deben.

- Si ejecutamos man rsync veremos todas las opciones de rsync.
- **Delete**: (Elimina archivos en el destino que no están en el
  origen)

``` bash
rsync -avz --delete /ruta/directorio_local usuario_remoto@ip_remota:/ruta/destino_remoto
```

- **Exlude**: (Excluye archivo del envio)

``` bash
rsync -avz --exclude 'archivo_o_directorio_a_excluir' /ruta/directorio_local usuario_remoto@ip_remota:/ruta/destino_remoto
```

- **Progress**: (Para ver el progreso de la sincronizacion)

``` bash
rsync -avz --progress /ruta/directorio_local usuario_remoto@ip_remota:/ruta/destino_remoto
```

## Practica 1.14. FreeFileSync

- Para esta practica crearemos ambas carpetas en el ordenador
  local o el ordenador virutal, da igual ya que el usuario es el
  mismo en ambos, y podemos acceder desde uno u otro:

``` bash
~/simula_labo/lagrs
~/simula_casa/lagrs
```

- De forma que las sincronizaremos ambas y cuando estemos en los
  laboratorios trabajaremos en la carpeta simula_lab, y cuando
  estemos en el ordenador local trabajaremos en el directorio
  simula_casa. Asi tendriamos siempre todo actualizado.
- Tendriamos que darle una sincronizacion en modo espejo, para
  poder actualizar de un lado a otro.
- En este caso he creado una prueba en simula_labo y al darle a
  sincronizar ocurre lo siguiente:

![**Sincronizacion FreeFileSync**](images/Sincro_ffs.png)

- Simula casa tiene la direcion del pc de casa y simula labo la
  direccion de un pc, auqnue podrian tener la misma direccion del
  un solo pc, hay que el usuario es el mismo.

## Practica 1.15. Conflicto con FreeFileSync

- Un conflito se genera cuando editas el mismo archivo en dos
  dsipositivos sin haberlo sin cronizado antes.
- Un **ejemplo** es: Si el archivo base se llama P1, en un
  ordenador tu has añadido algo se convierte en P1 + x y si lo
  haces en el otro seria P1 + y, de forma que FreeFileSync no
  sabe cual es el adecuado y te genera este conflicto
- La unica forma de resolverlo en guardando uno de los dos con su
  contenido, por lo que estas perdiendo la informacion o de x o
  de y. No es una buena forma de usar FreeFileSync.
- Por eso es conveniente sincronizar cada vez que cambias de
  dispositivo.

## Practica 1.16. Sincronización real de tu cuenta

- Despues de descargar FreeFileSync he sincronizado las carpetas
  lagrs creadas.
- Mi dispositvo personal esta conectado a traves de:

``` bash
ssh alexteje@f-l3109-pc07.aulas.eif.urjc.es
```

## Practica 1.17. Localizacion de procesos

1.  Para comparar los nombres de estos programas lo que haremos
    sera guardar los nombres en un fichero, luego abrire una app
    (gedit), volvere a guardar los nombres en otro fichero y los
    comparare.

``` bash
ps -ef > procesos_antes.txt
gedit
ps -ef > procesos_despues.txt
diff procesos_antes.txt procesos_despues.txt
```

- De esta forma si han ocurrido cambios, diff nos los mostrara.
  Donde no hayan ocurrido cambios no mostrara nada.

## Practica 1.18. Invocacion de la shell

1.  El bashrc se ejecuta solamente en las shells interactivas que
    no son de login.

- Cuando tu inicias una terminal se esta ejecutando al bshrc.
- Cuando una shell es de login, como su <usuario>, se esta
  ejecutando el bash_profile perteneciente a ese usuario.

2.  Abriremos el bashrc (en este caso he probado en el ordenador
    local) y añadiremos una traza, de forma que si lo hemos hecho
    correctamente cada vez que abramos una terminal deberia
    ejecutarse ese comando. Haremos lo siguiente:

``` bash
vi ~/.bashrc
echo "¡Bienvenido al terminal remoto, alexteje!"
source ~/.bashrc --> Es neccesario actualizar, a veces no funciona, probamos cambiando de terminal
```

- Una vez añadido y guardado, abrimos una nueva terminal y vemos
  que:

![**echo_bashrc**](images/echo_bashrc.png)

3.  De primeras en las cuentas de laboratorio no existe el
    bash_profile, por lo que deberemos crearlo con:

``` bash
vi ~/.bash_profile
```

- una vez creado haremos que bash_profile llame a bashrc
  añadiendo estas lineas de codigo en bash_profile:

``` bash
if [ -f ~/.bashrc ]; then
    . ~/.bashrc
fi
```

4.  Cuando entramos a un usuario mediante **su <usuario>** se
    ejecuta una shell de login ya que esta pidiendo la contraseña
    del usuario en cuestion, de forma que pasa a ejecutarse el
    bash_profile de dicho usuario.

5.  Para añadir alias en el bashrc se haria de esta manera:

``` bash
alias c='clear'
source ~/.bashrc --> Si no funciona cambio de terminal
```

- Como tenemos redireccionado el bash_profile de laboratorio al
  bashrc, los alias debemos ponerlos en bashrc.
- En caso de que no este redireccionado y tengamos alias en los
  dos bash (rc y profile), funcionaria ambos alias

## Practica 1.19. Instalacion de Docker

- Para realizar la instalacion de Docker debemos realizar los
  siguiente pasos para ver que actualizaciones hay disponibles y
  descargarlas:

``` bash
apt update
apt upgrade -y
apt install docker.io
```

- Para comprobar que la instalacion es correcta lanzaremos el
  hola mundo.
- Para ello debemos crear un grupo docker e introducir el usuario
  que creamos en su momento (alexte).Para ello haremos lo
  siguiente:

``` bash
sudo add group docker
groups
sudo adduser alexteje docker
su alexteje
groups
--- Lanzamos holamundo
docker run debian echo "Hola mundo"
```

- Quiza al lanzar el docker run debian echo necesite la
  instalacion, esto solo pasa cuando se hace por primera vez,
  luego ya se ejecuta sin problema alguno.

## Practica 1.20. Uso basico de imagenes

1.  Para crear un contenedor interactivo sin nombre del tipo
    ubuntu 24.04 debemos hacer el siguiente comando **desde el
    usuario creado (su alexteje)**:

``` bash
docker run -it ubuntu
```

- Alguna ordenes que podemos ejecutar es lc,echo "Texto"...
- Alguna de las ordenes que no podemos ejecutar son

2.  Para crear un contendor con el nombre alexc01 debemos
    ejecutar lo siguiente:

``` bash
docker run -it --name NOMBRE_DOCKER ubuntu
docker run -it --name alexc01 ubuntu 
```

- Si quisieramos que cambiar el nombre del hostname seria:

``` bash
docker run -it --name NOMBRE_DOCKER -h NOMBRE_HOSTNAME ubuntu
```

3.  Las ordenes para listar los contenedores y las imagenes son:

``` bash
docker ps      --> Contenedores interactivos (activos)
docker ps -a   --> Contenedores (incluye los detenidos)
docker images  --> Imagenes
docker rm <x>  --> Elimina el contedor x (x = --name x)
docker stop <x>--> Pausa el contenedor x (x = --name x)
```

![**Ejemplo de docker ps-a y rm**](images/dockerrm.png)

- Al realizar estos comandos veremos los detalles de los
  contenedores o de las imagenes (status,name,port...)

4.  Para pausar el contenedor ejecutaremos:

``` bash
exit 
Ctrl + dD
```

- Para ver los contenedores e imagenes detenidas usaremos el
  segundo y tercer comando del punto 3.

5.  Para comprobar que el sistema de ficheros del contenedor no
    es persistente hare dos pruebas:

- **Creaccion, suspense del contenedor y conexion**

``` bash
docker run -it --name alexc01 -h alejandro ubuntu
ls
touch prueba.md
exit
dokcer ps -a 
docker start alexc01
docker attach alexc01
```

- En este caso el contenedor no ha sido borraod, sino apagado y
  vuelto a encender, por lo que el archivo persiste.

- **Creacion, eliminacion y creacion**

``` bash
docker run -it --name alexc01 -h alejandro ubuntu
ls
touch prueba.md
exit
dokcer ps -a
docker rm alexc01
docker ps -a
docker run -it --name alexc01 -h alejandro ubuntu
```

- Ahora el contenido del contedor si se ha eliminado.

## Practica 1.21. Creacion de una imagen de un contenedor

1.  Primero crearemos una cuenta en docker hub para poder subir
    nuestras imagenes ademas de poder coger otras que sean
    publicas.
2.  **Prepararemos la imagen** alexteje/banner para ello haremos
    lo siguiente dentro de vbo01:

``` bash
mkdir context
```

- Y dentro de context haremos

``` bash
vi Dockerfile
vi entrypoint.sh
```

- Rellenaremos estos dos ultimos archivos con el siguiente
  contenido:

``` bash
DOCKERFILE
FROM ubuntu:24.04
RUN apt update && apt upgrade -y && apt install -y sysvbanner
COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
```

``` bash
ENTRYPOINT.SH
#!/bin/bash
banner bienvenido
banner a
banner $HOSTNAME
```

- **Datos importantes**: El dockerfile se suele tocar menos que
  el entrypoint. En el dockerfile hay que poner si necesitamos
  instalar algun paquete(sysvbanner) mientras que en el
  entrypoint pondremos lo "comandos" que ejecutara la shell. **lo
  haremos en vbox01, asi que podremos acceder desde /vagrant en
  la maquina virtual**.

3.  Una vez tenemos preparada la imagen necesitamos **lanzar el
    contenedor**. Primero conprobaremos que el entrypoint
    funciona haciendo:

``` bash
./entrypoint.sh ---> En el fichero al que pertenezca
```

docker

- Para lanzar el contenedor haremos en /vagrant (Ya que ahi se
  situa el directorio context):

``` bash
docker build -t alexteje/banner context 
docker run -it --name contenedorP21 -h hostP21 alexteje/banner
docker run -it --name NombreContenedor -h NombreHost NombreImagen
```

- Deberiamos ver por pantalla que se ejecuta lo que teniamos en
  el entrypoint.sh.
- **RECORDAR** que si modificas el entrypoint debes borrar el
  contenedor de la imagen y crearlo de nuevo.

``` bash
docker ps -a
docker rm NombreContendor
docker build -t alexteje/banner context
docker run -it --name contenedorP21 -h hostP21 alexteje/banner
```

4.  Para una vez lanzada la imagen no solo muestr ele banner sino
    tambien abra una shell, debemos cambiar el entrypoint, para
    ello añadiremos esto:

``` bash
#!/bin/bash
banner bienvenido
banner a
banner $HOSTNAME
/bin/bash
```

5.  Al modificiar el entrypoint debemos borrar el contenedor y
    volver a lanzarlo como he expecificado al final del apartado
    3.

``` bash
docker ps -a
docker rm 
docker build -t alexteje/banner context
docker run -it --name contenedorP21 -h hostP21 alexteje/banner
```

- Al ejecutar esto se emitira el banner y seguira una shell con
  el nombre:

``` bash
root@hostP21
```

6.  Para subir el contenedor a docker hub debemos hacer:

``` bash
docker login
docker push alexteje/banner
```

- Al hacer el login nos pedira el usuario y contraseña de docker
  hub, se introduce y se hace un push para subir la imagen.

## Pracitca 1.22 Creacion de una imagen personalizada

1.  Para que el paquete cal este instalado en cada maquina
    virtual que iniciemos debemos añadirlo en el provisionamineto
    (Vagrantfile).

``` bash
apt-get install -y ncal
```

2.  Crearemos las carpetas y archivos necesarios en la carpeta
    vbox01 y en /vagrant de la maquina virtual, ya que estan
    conectados.

``` bash
~/lagrs/vbox01/cal
~/lagrs/vbox01/cal/construye.sh
~/lagrs/vbox01/cal/lanza_jpercal01.sh
~/lagrs/vbox01/cal/lanza_jpercal02.sh
~/lagrs/vbox01/cal/context
~/lagrs/vbox01/cal/context/Dockerfile
~/lagrs/vbox01/cal/context/entrypoint.sh
```

- Asi debe quedar en vbox01, recuerda que los directorios se
  crean con mkdir NombreDirecotrio, y los ficheros con touch
  Nombre.md o vi Nombre.sh

3.  Ahora rellenaremos los ficheros, especificaciones:

- construye.sh ---\> Script para construir la imagen alexteje/cal

- lanza_alexcal01.sh ---\> Script para lanzar el contendor
  alexcal01

- lanza_alexcal02.sh ---\> Script para lanzar el contendor
  alexcal02

- Dockerfile ---\> Especificaciones de la imagen y paquetes a
  instalar

- entrypoint.sh ---\> Comandos que ejecutara la shell

- Para ejecutar el script debemos dar permisos de escritura a
  todos los scripts:

``` bash
chmod +x NombreScript.sh
```

- Una vez dado permisos debemos ejecutar de la siguiente manera:

``` bash
cd /vagrant/cal
./construye.sh
./lanza_alexcal01.sh
./lanza_alexcal02.sh ---> De momento hace lo mismo que el 01
```

-Cada contenedor se lanza desde su carpeta en vagrant, en este
caso **TODO** desde cd /vagrant/cal.

- **CONTENIDO DE LOS SCRIPTS:**

1.  construye.sh

``` bash
#!/bin/bash
# Define tu login aquí
LOGIN=alexteje

# Construir la imagen con el nombre de usuario y nombre de imagen
docker build -t "$LOGIN/cal" context
#Prueba: #!/bin/bash
docker build -t tulogin/cal ~/lagrs/vbox01/cal/context
```

2.  lanza_alexcal0X.sh

``` bash
#!/bin/bash
docker run -it -h alexcal01 --name alexcal01 --rm \
alexteje/cal
```

3.  Dockerfile

``` bash
FROM ubuntu:24.04
RUN apt update && apt upgrade -y && apt install -y ncal
COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
```

4.  entrypoint.sh

``` bash
#!/bin/bash
#Esto ejecuta el calendario
cal
```

## Practica 1.23. Montaje Bind

1. El nombre de la imagen a crear sera:

``` bash
alexteje/bind 
```

2.  Creamos la carpeta remoto dentro de vbox01, y dentro
    crearemos los siguientes ficheros:

``` bash
~/lagrs/vbox01/bind/construye.sh
~/lagrs/vbox01/bind/lanza_alexbind01.sh
~/lagrs/vbox01/bind/context/Dockerfile
~/lagrs/vbox01/bind/context/entrypoint.sh
```
3. **Preparacion de la imagen:**

- Debemos añadir al Dockerfile la instalacion del editor de texto
vim, asi como el sysvbanner para la traza de prueba de funcionamiento 
que he puesto. Para que el contenedor ejecute una shell debemos añadir
en el entrypoint:
``` bash
su alexteje
/bin/bash
```
- Por ultimo para que el contenedor monte el directorio /tmp/test de vbox01 
en el directorio /tmp/test del contenedor debemos crear el directorio test/
desde la shell que nos ejecute el contendor, creando dentro un archivo que se 
vera en el vbox01 si añadimos esta linea en el lanza_alexbind01.sh
``` bash
-v /tmp/test:/tmp/test \
```
- Esto hara que el directorio tmp del contenedor se vuelque tambien en el
directorio tmp de vbox01.

4. Una vez rellenados todos los ficheros debemos darle permisos de ejecucion a
los .sh
``` bash
chmod +x fichero.sh
```

5. Ejecucion del contenedor:
``` bash
su alexteje
cd
cd /vagrant/bind
./construye.sh
docker images --> Comprobacion de la creacion de la imagen 
./lanza_alexbind01.sh
---> Lanza nueva shell
cd 
cd /tmp
mkdir test
touch hola_jperez
---> Añades contenido a hola_jperez
exit, exit.. hasta llegar a usuario vagrant
cat /tmp/test/hola_jperez 
```
- Si todo ha ido correctamente se deberia pintar por pantalla el contenido del 
fichero hola_jperez


- **Permisos usuarios individuales:**

- Una que te salgas del terminal creado por el contenedor, los permisos del fichero
creado seran solo de lectura, si tu ejecutas: ls -l, saldra esto:
``` bash
-rw-r--r-- 1 root root 13 Dec  5 12:26 hola
```

- Para poder darle permisos a tu cuenta para poder escribir debermos hacer desde
alexteje@vbox01:/tmp/test$:
``` bash
sudo chown alexteje:alexteje /tmp/test/hola
ls -l
total 4
-rw-r--r-- 1 alexteje alexteje 13 Dec  5 12:26 hola
```
- De forma que desde el usuario alexteje podremos escribir y veremos tanto en el
contenedor como en el usuario el contenido actualizado

- Ademas de que el fichero y el contenido es persistente, una vez que cierras 
el contenedor y vuelves a abrir seguira ahi. Sin embargo, si apagas la maquina
virtual el directorio test permanecera pero el fichero hola_jperez se habra 
borrado, debido a que el directorio /tmp es un directorio temporal.

- Si otro usuario no puede editarlo, como en este caso ahora pertenece al usuario
alexteje, el usuario vagrant no podria. Bastaria con escribir:
``` bash
sudo chown vagrant:vagrant /tmp/test/hola
```

- **Permisos para todos los usuarios:**
- Para que todos los usuarios puedar editar este fichero desde su /tmp, deremos ir a
uno de ellos y ejecutar: 
``` bash
sudo chmod o+w /tmp/test/hola
```
- De este forma cualquiera podra editar el contenido del archivo, y desde todos se
podra ver el contenipdo actualizado


- **Contenido de los ficheros:**

1. construye.sh
```bash
#!/bin/bash
# Define tu login aquí
LOGIN=alexteje

# Construir la imagen con el nombre de usuario y nombre de imagen
docker build -t "$LOGIN/bind" context
```

2. lanza_alexbind0X.sh
```bash
#!/bin/bash
docker run -it -h alexbind01 --name alexbind01 --rm \
-v /tmp/test:/tmp/test \
alexteje/bind
```

3. Dockerfile
```bash
FROM ubuntu:24.04
RUN apt update && apt upgrade -y && apt install -y vim sysvbanner
COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
```

4. entrypoint.sh
```bash
#!/bin/bash
#Traza de funcionamiento
banner funciona

#Ejecutar la shell
su alexteje
/bin/bash
```


## Practica 1.24. Conectividad entre contenedores

1.  El nombre de la imagen que crearemos mas adelante sera:

``` bash
alexteje/remoto
```

2.  Creamos la carpeta remoto dentro de vbox01, y dentro
    crearemos los siguientes ficheros:

``` bash
~/lagrs/vbox01/remoto/construye.sh
~/lagrs/vbox01/remoto/lanza_alexremoto01.sh
~/lagrs/vbox01/remoto/lanza_alexremoto02.sh
~/lagrs/vbox01/remoto/context/Dockerfile
~/lagrs/vbox01/remoto/context/entrypoint.sh
```

3.  **Preparacion de la imagen:**

- Para que el contenedor ejecute el demonio servidor ssh, debemos
  añadirlo a la instalacion en el Dockerfile (openssh-server).
- Para poder relaizar el ifconfig y el ping debemos instalarlo
  tambien (net-tools)
- Tambien he añadido el paquete inetutils-ping, aunque no seria
  neccesario ya que el propio sistema tiene la posibilidad de
  realizar pings sin la instalacion de este paquete.

4.  El contenedor tendra un usuario con privilegios, por lo que
    debemos añadirlo al Dockerfile para que se cree al lanzar el
    contenedor

5.  **Contenido de todos los ficheros:**

- Una vez rellenados todos los ficheros debemos darle permisos a
  los ficheros .sh

``` bash
chmod +x fichero.sh
```

6.  Abrimos dos terminales ejecutando vbox01 (vagrant up, vagrant
    ssh) y lanzamos los dos contenedores (lanza_alexremoto@.sh),
    haremos ifconfig en ambos y miraremos la direccion ip de
    ambos. La direccion ip se encuentra en el apartado inte de
    172.17.0.2 eth0.

7.  Pasos a seguir:

``` bash
cd
cd /vagrant/remoto
./construye.sh
docker images --> Para comprobar que se ha creado la imagen
./lanza_alexremoto01.sh 
- Se iniciara un terminal
ifconfig
```

En otro terminal de vbox01 haremos:

``` bash
cd
cd /vagrant/remoto
./construye.sh
docker images
./lanza_alexremoto02.sh
ping <Direccion inet eth0 del otro terminal vbox01>
Ctrl+C
```

- Una vez acabado el envio de paquetes comprobamos que se han
  enviado y ejecutamos:

``` bash
sudo netstat -tupan
```

- Explicacion de las siglas: -t: Muestra las conexiones TCP. -u:
  Muestra las conexiones UDP. -p: Muestra el proceso y su ID
  (PID) asociado con cada conexión. -a: Muestra todos los sockets
  activos, incluidas las conexiones en espera (listening) y las
  conexiones establecidas. -n: Muestra las direcciones y puertos
  de forma numérica (sin resolver nombres de host o de
  servicios).

- Para ejecutar el comando anterior nos pedira una contraseña que
  sera la creada en el Dockerfile junto al usuario

- Este comando nos ayuda a identificar conexiones activas y ver
  que procesos se estan escuchando y en que puertos especificos

![**Ejemplo netstat -tupan**](images/netstat.png)

8.  Para acceder a otro pc desde esta terminal, deberemos mirar
    el inet (eth0) del pc al que queremos acceder y ejecutar:

``` bash
ssh alexteje@inet
```

- La contraseña que nos pedira sera la creada en el Dockerfile,
  al crear y dar privelegios al usuario

- **Contenido de los archivos**

1.  construye.sh

``` bash
#!/bin/bash
# Define tu login aquí
LOGIN=alexteje

# Construir la imagen con el nombre de usuario y nombre de imagen
docker build -t "$LOGIN/remoto" context
```

2.  lanza_alexremoto0X.sh

``` bash
#!/bin/bash
docker run -it -h alexremoto01 --name alexremoto01 --rm \
alexteje/remoto
```

3.  Dockerfile

``` bash
FROM ubuntu:24.04
#Instalaciones
RUN apt update && apt upgrade -y && apt install -y sudo net-tools inetutils-ping openssh-server sysvbanner
RUN service ssh start

#Creacion usuario
RUN useradd -rm -d /home/alexteje -s /bin/bash -u 1001 alexteje -g root -G sudo 
RUN echo 'alexteje:Alejandro' | chpasswd

COPY entrypoint.sh /
EXPOSE 22
ENTRYPOINT ["/entrypoint.sh"]
```

4.  entrypoint.sh

``` bash
#!/bin/bash
/usr/sbin/sshd

banner funciona

su alexteje
/bin/bash
```

- **Importante conocer:**
- El usuario se crea, se le da permisos y se le asigna contraseña
  en el Dockerfile
- Los paquetes a instalar tambien se añaden en el Dockerfile
- El lanzamiento de la terminal una vez lanzado la imagen se pone
  en el entrypoint con

``` bash
/bin/bash
```

## Practica 1.25. Sshfs

- En el directorio tmp de la maquina virtual crearemos una
  carpeta que se llamara labo, basicamente:

``` bash
cd /tmp
mkdir labo
```

- Con el comando que ejecutaremos a continuacion lo que estamos
  haciendo sera copiar todo el contenido del pc que
  seleccionemos, de forma que si editamos en la maquina virtual
  tambien se editara en el pc original, y viceversa.
``` bash
sshfs alexteje@f-l3103-pc03: /tmp/labo
```

- Si sale un error de que el comando not found, se debe a que no 
tenemos instalado el paquete de sshfs:
```bash
sudo apt update && sudo apt install -y sshfs
```

- Siendo alexteje el usuario del pc original, y /tmp/labo la
  direccion donde se copiara todo el contenido.

**Comandos de eliminacion:**
**MUCHO CUIDADO PQ SE BORRA EL CONTENIDO DEL ORDENADOR ORIGINAL:**
- Para eliminar la carpeta montada debemos primero desmontar y 
ya luego eliminar:
```bash
fusermount -u /tmp/labo
sudo rm -r labo (No se si funcionara sin sudo)
``` 

## Practica 1.26. Contenedor con sshfs

1.  El nombre de la imagen que crearemos mas adelante sera:
``` bash
alexteje/cssh
```

2.  Creamos la carpeta remoto dentro de vbox01, y dentro
    crearemos los siguientes ficheros:
``` bash
~/lagrs/vbox01/cssh/construye.sh
~/lagrs/vbox01/cssh/lanza_alexcssh01.sh
~/lagrs/vbox01/cssg/context/Dockerfile
~/lagrs/vbox01/cssh/context/entrypoint.sh
```

3. Una vez rellenados todos los ficheros debemos darle permisos de ejecucion a
los .sh
``` bash
chmod +x fichero.sh
```

4. **Importante:** Debemos crear las dos carpetas a sincronizar con sshfs con mkdir.
- Una en el ordenador local, donde meteremos algo de cotenido:
```bash
cd /tmp
mkdir Prueba_sshfs
vi Prueba1
vi Prueba2
```
- Y otra en el **tmp del contendor**, es decir, ejecutaremos el construye y el lanza.
```bash 
cd /vagrant/cssh
./construye.sh
./lanza_alexcssh01.sh
cd /tmp
mkdir Prueba_sshfs_contenedor
```
- Una vez estemos en la shell que nos lanza el entrypoint haremos:
```bash
cd /tmp
mkdir Prueba_sshfs
```

5. Para comprobar que sshfs esta descargado en la maquina virtual ejecutaremos:
```bash
sshfs -V
```
6. Ejecuccion del contenedor:
```bash
---> Creas carpetas en local y en contenedor
cd /vagrant/cssh
./construye.sh
./lanza_alexcssh01.sh
sshfs alexteje@f-l3109-pc05:/Direcion_Carpeta_Local /Direccion_Carpeta_Contenedor
ls -l /Direcion_Carpeta_Local
--> Si salen los archivos aqui es que ha ido correctamente
touch /Direccion_Carpeta_Contenedor/testfile 
--> Te vas al pc05 y ves si se te ha creado el archivo testfile, si es que si,
todo correcto
```
7. Para hacer lo mismo pero desde el usuario creado en el Dockerfile debemos 
tener la carpeta con archivos en el ordendor remoto.
```bash
cd /tmp
mkdir Prueba_sshfs
vi Prueba1
vi Prueba2
```
- Y tambien debemos crear la carpeta en el /tmp del usuario iniciado desde la 
shell del contenedor:
```bash
```bash 
cd /vagrant/cssh
./construye.sh
./lanza_alexcssh01.sh
su alexteje
cd /tmp
mkdir Prueba_sshfs_alexteje
```
- Luego ejecutaremos:
```bash
sshfs alexteje@f-l3109-pc08:/Direcion_Carpeta_Local /Direccion_Carpeta_Contenedor --> Comando general
sshfs alexteje@f-l3109-pc08:/tmp/Prueba_sshfs /tmp/Prueba_sshfs_alexteje 
ls -l /tmp/Prueba_sshfs_alexteje 
--> Deberan salir los archivos del directorio /tmp/Prueba_sshfs del pc08
touch /tmp/Prueba_sshfs_alexteje/TESTFILE2
--> Si miras con ls en /tmp/Prueba_sshfs deberia aparecer TESTFILE2, como un archivo mas.
```

- **Solucion de posibles errores:**

- Si nos dice **permission denegated** sera por lo los permisos de la carperta,
haces id en alexteje o en root para ver que a grupos pertenece y ejecutas:
```bash
id ---> Para ver los grupos (pertenece al grupo root debido al Dockerfile)
sudo chown alexteje:root /tmp/Virtual_contenedor/
```
- Si ocurre algun error esta bien comprobar que ssh funciona (no sshfs) conectandose
a una maquina y viendo si salta algun error o funciona correctamente


- **Contenido de los archivos:**
1. construye.sh:
```bash
#!/bin/bash

USERNAME=alexteje
IMAGE_NAME="${USERNAME}/cssh"
docker build -t $IMAGE_NAME context/
```

2. lanza_alexcssh01.sh:
```bash
#!/bin/bash

CONTAINER_NAME="alexcssh01"
HOSTNAME="alexcssh01"
IMAGE_NAME="alexteje/cssh"

docker run -it --rm --name $CONTAINER_NAME \
    --hostname $HOSTNAME \
    --privileged \
    --device /dev/fuse \
    --cap-add SYS_ADMIN \
    --security-opt apparmor:unconfined \
    $IMAGE_NAME
```

3. Dockerfile:
```bash
FROM ubuntu:20.04

# Configuración del idioma
ENV LANG es_ES.UTF-8
ENV LANGUAGE es_ES:es
ENV LC_ALL es_ES.UTF-8
RUN apt-get update && apt-get install -y locales && \
    locale-gen es_ES.UTF-8 && \
    update-locale LANG=es_ES.UTF-8

# Instalación de sshfs y otras herramientas
RUN apt-get install -y sshfs sudo vim openssh-server

# Creación del usuario
ARG USERNAME=alexteje
RUN useradd -m -s /bin/bash $USERNAME && \
    echo "$USERNAME:$USERNAME" | chpasswd && \
    usermod -aG sudo $USERNAME

# Configuración del SSH
RUN mkdir /var/run/sshd
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
```

4. entrypoint.sh
```bash
#!/bin/bash

# Iniciar el servicio SSH
service ssh start

# Mensaje de bienvenida
echo "Contenedor configurado con éxito. Usuario: $USERNAME"

# Mantener el contenedor activo
/bin/bash
```

## Practica 1.27. Contenedor con fichero hosts

1.  El nombre de la imagen que crearemos mas adelante sera:
``` bash
alexteje/chosts
```

2.  Creamos la carpeta remoto dentro de vbox01, y dentro
    crearemos los siguientes ficheros:
``` bash
~/lagrs/vbox01/chosts/construye.sh
~/lagrs/vbox01/chosts/lanza_alexchosts01.sh
~/lagrs/vbox01/chosts/lanza_alexchosts02.sh
~/lagrs/vbox01/chosts/context/Doackerfile
~/lagrs/vbox01/chosts/context/entrypoint.sh
```

3.  Para que los contenedores conozcan las direcciones ip de las
    d maquinas del laboratorio crearemos el fichero delta_hosts,
    en el cual introduciremos las direcciones ip encontradas en
    el fichero /etc/hosts, de esta forma
``` bash
view /etc/hosts touch
touch ~/lagrs/vbox01/chosts/context/delta_hosts
---> Copiar las direcciones que consideremos
```

- Contenido de delta_hosts:
``` bash
212.128.254.52  Maquina8
212.128.254.53  Maquina9
212.128.254.54  Maquina10
```

4.  Para que este fichero aparezca en el /tmp/ de la imagen
    debemos añadirlo al Dockerfile como:
``` bash
COPY delta_hosts /tmp/delta_hosts
```

5.  Debemos hacer que cada vez que se inicie la imagen, se
    **añadan** estas entradas al /etc/hosts del contenedor. Para
    ello debemos añadir esto en el entrypoint:
``` bash
cat /tmp/delta_hosts >> /etc/hosts
```
- **Recordatorio importante:** En docker no es posible borrar ni reemplazar el fichero
/etc/hosts de una imagen, pero sí puedes modificarlo añadiendo entradas

6. Para poder hacer ifconfig, ping  y ssh debemos instalar los paquetes neccesarios, 
los cuales los añadiremos en el Dockerfile:
```bash
RUN apt update && apt upgrade -y && apt install -y sudo net-tools inetutils-ping openssh-server sysvbanner
```

7.  Importante la creacion de todos los archivos correctamente y
    **darles permisos neccesarios**, en este caso solo debemos
    dar permisos a los .sh, para poder ejecutar.

``` bash
chmod +x archivo.sh
```

8.  Pasos a seguir para la ejecucion del ping de un contenedor a
    un pc del laboratorio:

``` bash
cd
cd /vagrant/chosts
./construye
./lanza_alexchosts01.sh
---> Se abrira nuevo terminal
ls -a
cd /tmp/
ls
cat delta_hosts
ping <NombreAsigandoEnDeltaHosts>
```

9.  Pasos a seguir para entrar por ssh desde un contenedor a un
    ordenador del laboratorio:

- Desde el terminal que se abre al ejecutar el script
  lanza_alexchosts.sh

``` bash
ssh alexteje@Maquina8
```

- Te pedira confirmar el fingerprint con yes (Primera vez que
  inicies sesion en esa maquina), y la contraseña de la
  respectiva maquina, en este caso de la cuenta de linux del
  laboratorio.

- **Contenido de los archivos: **

1. Construye.sh
``` bash
LOGIN=alexteje

# Construir la imagen con el nombre de usuario y nombre de imagen
docker build -t "$LOGIN/chosts" context
```

2. Lanza_alexchosts0X.sh
``` bash
#!/bin/bash
docker run -it -h alexchosts01 --name alexchosts01 --rm \
alexteje/chosts
```

3. DockerFile
``` bash
FROM ubuntu:24.04
#Instalaciones
RUN apt update && apt upgrade -y && apt install -y sudo net-tools inetutils-ping openssh-server sysvbanner
RUN service ssh start

#Creacion usuario
RUN useradd -rm -d /home/alexteje -s /bin/bash -u 1001 alexteje -g root -G sudo
RUN echo 'alexteje:Alejandro' | chpasswd

COPY delta_hosts /tmp/delta_hosts

COPY entrypoint.sh /
EXPOSE 22
ENTRYPOINT ["/entrypoint.sh"]
```
4. entrypoint.sh
``` bash
#!/bin/bash
/usr/sbin/sshd

#Traza de funcionamiento
banner funciona

#Aparecera en el tmp de la imagen
cat /tmp/delta_hosts >> /etc/hosts

#Lanzar terminal 
su alexteje
/bin/bash
```

5. Delta_hosts
``` bash
212.128.254.52  Maquina8
212.128.254.53  Maquina9
212.128.254.54  Maquina10
```
