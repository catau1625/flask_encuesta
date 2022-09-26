from unicodedata import name
from flask import Flask,session,request,redirect,render_template

app = Flask(__name__)
app.secret_key = 'SecretKey'

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/redirect',methods=['POST'])
def redirect():
    session['nombre'] = request.form['nombre']
    session['ciudad'] = request.form['ciudad']
    session['lenguaje'] = request.form['lenguaje']
    session['comentario'] = request.form['comentario']
    return render_template('user.html',name=session['nombre'],ciudad=session['ciudad'],lenguaje=session['lenguaje'],comentario=session['comentario'])

if __name__ == '__main__':
    app.run(debug=True)