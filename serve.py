from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def num():
    if request.method == 'POST':
        command = ["python", "stress_cpu.py"]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return "Output: {}\nError: {}".format(stdout, stderr)
        
    elif request.method == 'GET':
        return socket.gethostname()

app.run(host='0.0.0.0')