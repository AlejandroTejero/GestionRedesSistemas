FROM ubuntu:24.04
RUN apt update && apt upgrade -y && apt install -y ncal
COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

