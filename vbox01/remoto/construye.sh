#!/bin/bash
# Define tu login aquí
LOGIN=alexteje

# Construir la imagen con el nombre de usuario y nombre de imagen
docker build -t "$LOGIN/remoto" context
