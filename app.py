from flask import *
from sqlalchemy.orm import sessionmaker
from models import *

eng = create_engine('sqlite:///management/database/database.db', echo = True)

app = Flask(__name__, static_folder = 'static')

@app.route('/admin', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        userData = 'admin'
        user = request.form['username']
        passwd = request.form['password']
        if user == userData or passwd == userData:
            return render_template('admin.html', user=userData)
    else:
        flash = 'username or password is wrong !!'
    return render_template('login.html')

@app.route('/')
def index():
    return render_template('index.html')

if __name__=='__main__':

    app.run(port = 80, host = '0.0.0.0', debug = True)
