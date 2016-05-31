from flask import *

app = Flask(__name__, static_folder = '/template')

@app.route('/admin', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == ['admin'] or request.form['password'] == 'admin':
            return render_template('admin.html')
        else:
            return redirect(url_for('login'))
    return render_template('index.html')

if __name__=='__main__':

    app.run(port = 80, host = '0.0.0.0', debug = True)
