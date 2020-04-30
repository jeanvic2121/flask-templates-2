from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    usuarios = [
        ['joao', 'joao@gmail.com'],
        ['jose', 'jose@gmail.com'],
        ['Maria', 'maria@gmail.com']
    ] 
    return render_template(
        'index.html',
        titulo = 'Index',
        usuarios = usuarios
        )

if __name__ == '__main__':     
    app.run()