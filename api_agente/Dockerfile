# FROM comando para descargar imagenes
FROM python:3.9-slim-bullseye
RUN python3 -m venv /opt/venv
# Install dependencies:
COPY requirements.txt .
RUN . /opt/venv/bin/activate && pip install -r requirements.txt
# Run the application:
COPY app.py .
COPY cert/ .
EXPOSE 3000
CMD . /opt/venv/bin/activate && exec python app.py