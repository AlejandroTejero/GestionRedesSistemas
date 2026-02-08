FROM ubuntu:24.04
RUN apt update && apt upgrade -y && apt install -y sysvbanner
COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
