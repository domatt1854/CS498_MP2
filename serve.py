from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def num():
    if request.method == 'POST':
        command = ["python3", "stress_cpu.py"]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return "Ran Process."
        
    elif request.method == 'GET':
        return socket.gethostname()

app.run(host='0.0.0.0')