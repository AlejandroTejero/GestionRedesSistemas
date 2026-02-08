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

