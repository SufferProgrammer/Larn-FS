from flask import *
from sqlalchemy.orm import sessionmaker
from models import *
import os

eng = create_engine('sqlite:///management/database/database.db', echo = True)

app = Flask(__name__, static_folder = 'static')

@app.route('/admin', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form['username']
        passwd = request.form['password']

        sess = sessionmaker (bind=eng)
        inputData = sess()
        Qu = inputData.query(User).filter(User.user.in_([uname]), User.password.in_([passwd]))
        res = Qu.first()
        if res:
            session['logged_in']=True
        else:
            flash ("somethink error")
    return render_template('login.html')

@app.route('/')
def index():
    return render_template('index.html')


if __name__=='__main__':
    app.secret_key = os.urandom(12)
    app.run(port = 80, host = '0.0.0.0', debug = True)
