# FROM comando para descargar imagenes
FROM ubuntu:jammy-20220815
RUN apk --no-cache add ca-certificates
RUN mkdir -p /home/userappmeli && HOME=/home/userappmeli && chmod -R 0755 /home/userappmeli && addgroup -S -g 10101 userappmeli && adduser -S -D -s /sbin/nologin -h /home/userappmeli -G userappmeli userappmeli
WORKDIR /home/userappmeli
COPY api_agente/ .
WORKDIR /home/userappmeli/api_agente
CMD ["./install.sh"]