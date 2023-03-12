from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

# Instanciamos una base de datos
db = SQLAlchemy()

app = Flask(__name__)

# Indicamos cómo conectarse a la base de datos real
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database\\tasks.db"

# Inicializamos la base de datos
db.init_app(app)

# Creamos un modelo que será nuestra tabla
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))
    done = db.Column(db.Boolean)


with app.app_context():
    db.create_all()


# R U T A S

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/create-task", methods=['POST'])
def create():
    task = Task(content=request.form['content'], done = False)
    #db.session.add() # Para usar esto tenemos que tener la tabla creada

