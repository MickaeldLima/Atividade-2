from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') # essa é a primeira tela que vai aparecer (raiz)
def inicio():
    return render_template("inicio.html");

@app.route('/produto1') 
def produto1():
    return render_template("produto1.html");

@app.route('/produto2') 
def produto2():
    return render_template("produto2.html");

@app.route('/produto3') 
def produto3():
    return render_template("produto3.html");

@app.route('/produto4') 
def produto4():
    return render_template("produto4.html");