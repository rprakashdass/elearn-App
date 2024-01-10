from flask import Flask, render_template, request
from flask_login import LoginManager

app = Flask(__name__, template_folder="templates", static_folder="static")
login_manager = LoginManager()
login_manager.init_app(app)
app.secret_key = b'4e78a5cddb098e0a6924a8939abfaab6cd26e61f64acd238ea4fdbca4ddda53d'

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        userdata = request.form
        return render_template('index.html', user=userdata)
    # return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('login.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')

if __name__ == "__main__":
    app.run(debug=True)