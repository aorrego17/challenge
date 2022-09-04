# FROM comando para descargar imagenes
FROM python:latest
RUN mkdir -p /home/userappmeli && HOME=/home/userappmeli && chmod -R 0755 /home/userappmeli && addgroup -S -g 10101 userappmeli && adduser -S -D -s /sbin/nologin -h /home/userappmeli -G userappmeli userappmeli
WORKDIR /home/userappmeli
COPY /bin /cert /lib .env /app.py requirements.txt ./
RUN pip3 install -r requirements.txt
WORKDIR /home/userappmeli/api_agente
EXPOSE 3000
CMD ["python3", "app.py"]