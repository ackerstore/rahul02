import threading
from api import app
from bot import start_bot

def run_api():
    app.run(host="0.0.0.0", port=8080)

threading.Thread(target=run_api).start()

start_bot()
