# FROM comando para descargar imagenes
FROM python:buster
RUN pip install --upgrade pip
RUN adduser -D userappmeli
USER userappmeli
WORKDIR /home/userappmeli
COPY cert/ cert/
COPY bin/ bin/
COPY lib/ lib/
COPY .env .
COPY app.py .
COPY --chown=userappmeli:userappmeli requirements.txt requirements.txt
RUN pip install --user -r requirements.txt
ENV PATH="/home/userappmeli/.local/bin:${PATH}"
COPY --chown=userappmeli:userappmeli . .
EXPOSE 3000
CMD ["python3", "app.py","&&","curl -k --request POST https://127.0.0.1:3000/add"]
