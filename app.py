from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/home_servidor')
def home_servidor():
    return render_template('home_servidor.html', current_url=request.path)

@app.route('/home_cliente')
def home_cliente():
    dropdown_options = ['Option 1', 'Option 2', 'Option 3']
    dropdown_services = ['Servico 1', 'Servico 2', 'Servico 3', 'Service 4', 'Service 5']
    return render_template('home_cliente.html', current_url=request.path, 
                           dropdown_options=dropdown_options, dropdown_services=dropdown_services)

@app.route('/contratar')
def ontratar():
    return render_template('contratar.html', current_url=request.path)

@app.route('/agenda')
def agenda():
    return render_template('agenda.html', current_url=request.path)

if __name__ == '__main__':
    app.run(debug=True)
