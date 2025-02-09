from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route("/")
def home():
    pod_name = socket.gethostname()  # Get the pod hostname
    pod_ip = os.popen("hostname -I").read().strip()  # Get the pod IP address
    return jsonify({"message": f"Hello from Backend App running in pod: {pod_name} with IP: {pod_ip}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
