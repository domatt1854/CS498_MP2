from flask import Flask, request

app = Flask(__name__)

seed = 0

@app.route("/", methods=['GET', 'POST'])
def num():
    global seed
    
    if request.method == 'POST':
        json_data = request.get_json()
        num = json_data.get('num')
        seed = num
        return "Successfully updated seed to {}".format(num)
    elif request.method == 'GET':
        return str(seed)