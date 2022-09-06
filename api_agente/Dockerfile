# FROM comando para descargar imagenes
FROM ubuntu:latest as base
RUN apt-get update
RUN apt-get install python3 curl wget net-tools python3.10-venv -y
RUN mkdir -p /home/userappmeli && HOME=/home/userappmeli
WORKDIR /home/userappmeli
RUN python3 -m venv challengemeli
COPY cert/ challengemeli/cert/
COPY .env challengemeli/.env
COPY app.py challengemeli/app.py
COPY requirements.txt challengemeli/requirements.txt
RUN wget https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py
RUN pip3 install -r challengemeli/requirements.txt
EXPOSE 3000
CMD ["python3", "app.py","&&","curl -k --request POST https://127.0.0.1:3000/add"]
