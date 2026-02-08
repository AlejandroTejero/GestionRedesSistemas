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

