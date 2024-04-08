from flask import Flask, render_template

app = Flask(__name__)
conn = psyc


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route('/auth/login', methods=['POST'])
def login():
    return render_template('auth/auth.login.html')


@app.route('/auth/register', methods=['POST'])
def register():
    return render_template('auth/auth.signup.html')


if __name__ == '__main__':
    app.run()
