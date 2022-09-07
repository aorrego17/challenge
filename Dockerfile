FROM ubuntu:20.04
RUN apt-get update
RUN apt-get install python3 wget net-tools python3-pip -y
WORKDIR /appmeli
COPY . /appmeli
RUN pip3 install -r requirements.txt
EXPOSE 3000
CMD ["python3", "./challenge/app.py"]
ENTRYPOINT ["curl", "-k", "--request", "POST", "https://127.0.0.1:3000/add"]