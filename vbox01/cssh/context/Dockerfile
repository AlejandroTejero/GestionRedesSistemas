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

