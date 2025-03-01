from flask import Flask, render_template, request, redirect, url_for
from config import db, SQLALCHEMY_DATABASE_URI
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Task Model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(10), default="Pending")  # Status: Pending / Done

# Create Database Tables
with app.app_context():
    db.create_all()

# Home Page - Show All Tasks
@app.route("/")
def index():
    tasks = Task.query.all()
    return render_template("index.html", tasks=tasks)

# Add New Task
@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title")
    if title:
        new_task = Task(title=title)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for("index"))

# Update Task Status
@app.route("/update/<int:task_id>")
def update_task(task_id):
    task = db.session.get(Task , task_id)
    
    if task:
        task.status = "Done" if task.status == "Pending" else "Pending"
        db.session.commit()
    return redirect(url_for("index"))

# Delete Task
@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
