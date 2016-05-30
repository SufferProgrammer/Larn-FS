from flask import *

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('index.html')

if __name__=='__main__':

    app.run(port = 80, host = '0.0.0.0', debug = True)
