from flask import session
from flask import Flask, redirect, url_for, render_template, request
from flask_login import LoginManager,login_required
import pymysql
# import MySQLdb.cursors

# db connection
hostname = 'localhost'
user = 'root'
password = ''

db = pymysql.connections.Connection(
    db='elearnApp',
    host=hostname,
    user=user,
    password=password
)

cursor = db.cursor()

app = Flask(__name__, template_folder="templates", static_folder="static")

# login configuration
app.secret_key = b'4e78a5cddb098e0a6924a8939abfaab6cd26e61f64acd238ea4fdbca4ddda53d'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'elearnApp'
 
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/practice')
def workspace():
    return render_template('workspace.html')

@app.route('/',methods = ['GET', 'POST'])
def index():
    if 'username' in session:
        msg = "welcome " + session['username']
        return render_template('index.html',msg=msg)
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(index)

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/register',methods = ['GET','POST'])
def register():
    msg = 'Nothing entered'
    # msg = "User id and credentials donot Match!!"
    if request.method == 'POST' and 'username' in request.form and 'passcode' in request.form:
        name = request.form['username']
        passcode = request.form['passcode']
        context = {'name':name,'passcode':passcode}
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("INSERT INTO user_details VALUES(%s,%s,%s)", (name,passcode,1))
        # return redirect(url_for('index'))
    return render_template('register.html',msg = msg)
if __name__ == "__main__":
    app.run(debug=True)