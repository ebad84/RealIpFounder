from flask import Flask, render_template, request
from time import ctime,sleep,time
from json import dumps

app = Flask(__name__)


try:
        data = eval(open("ips.json","r").read())
except:
        data = {}




@app.route("/")
def index():
        return render_template('index.html')
@app.route("/addip/<ip>")
def add_ip(ip):
        file = open("ips.json","w")
        print(ip,"\n")
        data[str(ctime())+" | "+str(time())] = ip
        file.write(dumps(data,indent=4))
        file.close()
        return ""

if __name__ == '__main__':
        app.run(port=1234)

