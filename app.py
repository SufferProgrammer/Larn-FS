from flask import *
from sqlalchemy.orm import sessionmaker
from models import *
import sqlite3 as Db
import os

eng = create_engine('sqlite:///management/database/database.db', echo = True)
app = Flask(__name__, static_folder = 'static')


@app.route('/admin', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = str(request.form['username'])
        passwd = str(request.form['password'])

        sess = sessionmaker (bind=eng)
        inputData = sess()
        Qu = inputData.query(User).filter(User.user.in_([uname]), User.passwd.in_([passwd]))
        res = Qu.first()
        if res:
            session['logged_in']=True
            return render_template('admin.html')
        else:
            flash ("somethink error")
    return render_template('login.html')

@app.route('/')
def index():
   con = Db.connect("management/database/database.db")
   con.row_factory = Db.Row
   
   cur = con.cursor()
   cur.execute("select * from post")
   
   rows = cur.fetchall();
   return render_template("index.html",rows = rows)

@app.route('/post', methods = ['GET', 'POST'])
def post():
    if request.method == 'POST':
        title = request.form['title']
        cont = request.form['content']
        date = request.form['pdate']
                
        db = Db.connect('management/database/database.db')
        db.row_factory = Db.Row
        
        if title == null and cont == null and date == null:

            error = "Don't leave blank form"
            return render_template('post.html', error=error)
        else:
            
            ex = db.cursor()
            ex.execute("INSERT INTO post(title, content, p_date) VALUES (?, ?, ?)" (title, cont, date))
            ex.commit()
            ex.close()
            flash("success create post")
        return redirect(url_for('index'))
    return render_template('post.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__=='__main__':
    app.secret_key = os.urandom(12)
    app.run(port = 80, host = '0.0.0.0', debug = True)
