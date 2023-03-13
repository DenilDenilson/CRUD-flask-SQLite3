from flask import Flask, render_template, request, redirect, url_for
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
    tasks = Task.query.all()
    return render_template('index.html', tasks = tasks) # la variable tasks puede llamarse como gustes

@app.route("/create-task", methods=['POST'])
def create():
    task = Task(content=request.form['content'], done = False)
    db.session.add(task) # Para usar esto tenemos que tener la tabla creada
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/done/<id>")
def done(id):
    task = Task.query.filter_by(id=int(id)).first()
    task.done = not(task.done)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/delete/<id>")
def delete(id):
    Task.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(url_for('home'))

