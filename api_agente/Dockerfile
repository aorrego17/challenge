# FROM comando para descargar imagenes
FROM ubuntu:latest
RUN mkdir -p /home/userappmeli && HOME=/home/userappmeli
WORKDIR /home/userappmeli
COPY bin/ bin/
COPY cert/ cert/
COPY lib/ lib/
COPY .env .
COPY app.py .
COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN source bin/activate
EXPOSE 3000
CMD ["python3", "app.py"]