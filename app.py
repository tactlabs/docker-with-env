from flask import Flask
# from redis import Redis
import os

app = Flask(__name__)

PORT = os.environ["PY_PORT"]

@app.route('/')
def hello():
    result_dict={
        "city1":"Montreal", 
        "city2":"Qubec"
    }
    return result_dict

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = PORT)
