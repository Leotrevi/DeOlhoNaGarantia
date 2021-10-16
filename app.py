from flask import Flask, render_template
app = Flask('__name__')

@app.route('/')  #quando acessar o site e colocar a barra no final vai retornar um template em html o index.html
def index():
    return render_template('index.html')