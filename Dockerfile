FROM ubuntu:20.04
RUN ln -snf /usr/share/zoneinfo/$CONTAINER_TIMEZONE /etc/localtime && echo $CONTAINER_TIMEZONE > /etc/timezone

# Install dependencies:
RUN apt-get update && apt-get install -y tzdata

RUN apt-get update && apt-get install -y python3.9 python3.9-dev python3-pip
ARG DEBIAN_FRONTEND=noninteractive
WORKDIR /appmeli
COPY . /appmeli
RUN pip3 install -r requirements.txt
EXPOSE 4000
CMD ["python3", "challenge/app.py"]