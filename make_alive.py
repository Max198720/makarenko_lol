from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')
def home():
    return "Монитор активен"
def run():
  port = int(os.environ.get("PORT",4000))
  app.run(host='0.0.0.0', port=port)
def keep_aliv():
  t = Thread(target=run)
  t.start()
