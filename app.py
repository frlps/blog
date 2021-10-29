from flask import Flask, render_template
import os
import datetime
import sqlite3
from flask_sqlalchemy import SQLAlchemy

#Já deve ter criado o arquivo databbase.db
project_dir = os.path.dirname(os.path.abspath(__file__))
print('Inicializando a partir do caminho: '+project_dir)

#Monta caminho para banco de dados com sqlite
database_file = "sqlite:///{}".format(os.path.join(project_dir,"database.db"))

app = Flask(__name__)
app.config['SECRET_KEY']='admin123'
app.config['SQLALCHEMY_DATABASE_URI']=database_file
db = SQLAlchemy(app)

#Criando a classe para o bd
class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(300), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__app__':
    app.run(debug=True, host='0.0.0.0') #0.0.0.0 resolve em todos os ambientes
    # Rodando debug mode True o flask identifica sozinho 
    # alterações no código e 'restarta' a aplicação