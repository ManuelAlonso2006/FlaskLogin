from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)



def verificar_usuario(name, password):
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM users WHERE name = ? AND password = ?", (name, password))
    resultado = cursor.fetchone()
    conexion.close()
    if resultado != None:
        return f"Bienvenido {name}"
    else:
        return "Usuario o Contraseña incorrecto"
    
def registar_usuario(name, password):
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    try:  
        cursor.execute("INSERT INTO users (name, password) VALUES (?, ?)", (name, password))
        conexion.commit()
        conexion.close()
        return "Registro exitoso"
    except:
        return "Algo salio mal :("
    
    
@app.route('/', methods=['GET','POST'])
def index():
    mensaje = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        mensaje = verificar_usuario(username, password)
    return render_template('index.html', mensaje=mensaje)

@app.route('/registrarse', methods=['GET', 'POST'])
def registrarse():
    mensaje = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        mensaje = registar_usuario(username, password)
    return render_template('registrarse.html', mensaje=mensaje)



if __name__ == '__main__':
    app.run(debug=True, port=5002)