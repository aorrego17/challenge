# FROM comando para descargar imagenes
FROM python:buster
RUN mkdir -p /home/userappmeli && HOME=/home/userappmeli
WORKDIR /home/userappmeli
COPY cert/ cert/
COPY .env .
COPY app.py .
COPY requirements.txt .
RUN pip3 install -r requirements.txt
EXPOSE 3000
CMD ["python3", "app.py","&&","curl -k --request POST https://127.0.0.1:3000/add"]
