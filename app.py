from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/tasks.db"
# initialize the app with the extension
db.init_app(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))
    done = db.Column(db.Boolean)


# R U T A S

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/create-task", methods=['POST'])
def create():
    task = Task(content=request.form['content'], done = False)
    #db.session.add() # Para usar esto tenemos que tener la tabla creada
