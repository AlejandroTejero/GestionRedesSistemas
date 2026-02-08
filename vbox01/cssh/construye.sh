#!/bin/bash

USERNAME=alexteje
IMAGE_NAME="${USERNAME}/cssh"
docker build -t $IMAGE_NAME context/

