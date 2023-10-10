from flask import Flask, request, render_template as rt
from socket import gethostname
from yaml import load, dump
import os

app = Flask(__name__)
app.secret_key = os.urandom(16)
        
def generate_flag():
    with open(r'web\flag.txt', 'w') as f:
        f.write("NC{{{}}}".format(os.urandom(16).hex()))

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        yml = load(request.data)
        with open('subs.yml', 'a+') as y:
            dump(yml, y)

        return 'You subscribed successfully with: ' + str(yml)

    return rt('index.html')

if __name__ == '__main__':
    generate_flag()
    if 'liveconsole' not in gethostname():
        app.run(debug=False, host='0.0.0.0', port=80)
