from flask import Flask
# from redis import Redis
import os

app = Flask(__name__)

PORT = os.environ["PY_PORT"]

@app.route('/')
def hello():
    return 'Montreal'

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = PORT, debug = True)
