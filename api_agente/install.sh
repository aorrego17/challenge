pip3 install -r requirements.txt
source bin/activate
python3 app.py
sleep 3
curl -k --request POST https://127.0.0.1:3000/add
