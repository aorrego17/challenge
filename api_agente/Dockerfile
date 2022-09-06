# FROM comando para descargar imagenes
FROM python:buster
RUN mkdir -p /home/userappmeli && HOME=/home/userappmeli
WORKDIR /home/userappmeli
RUN python3 -m venv userappmeli
COPY cert/ userappmeli/cert/
COPY .env userappmeli/.env
COPY app.py userappmeli/app.py
COPY requirements.txt userappmeli/requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 3000
CMD ["python3", "app.py","&&","curl -k --request POST https://127.0.0.1:3000/add"]
