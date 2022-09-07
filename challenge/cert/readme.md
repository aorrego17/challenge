**Crear los ssl/tls**

- openssl genrsa -out secret.pem

- openssl req -new -key secret.pem -out csr.pem

- openssl x509 -req -days 365 -in csr.pem -signkey secret.pem -out cert.pem

