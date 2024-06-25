from flask import Flask, render_template

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/home_servidor')
def home_servidor():
    return render_template('home_servidor.html')

if __name__ == '__main__':
    app.run(debug=True)
