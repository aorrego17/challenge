# FROM comando para descargar imagenes 
FROM python:3.8.2-alpine
LABEL maintainer="challengemeli@meli.com"
# RUN comando de Dockerfile para ejecutar dentro del contenedor
RUN apk --no-cache add ca-certificates
RUN mkdir -p /home/userappmeli && HOME=/home/userappmeli && chmod -R 0755 /home/userappmeli && addgroup -S -g 10101 userappmeli && adduser -S -D -s /sbin/nologin -h /home/userappmeli -G userappmeli userappmeli

WORKDIR /home/userappmeli
COPY api_agente/ .
RUN 