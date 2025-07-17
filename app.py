
from flask import Flask, render_template, request


def create_app():
    app = Flask(__name__)
    habits = ["Test Task"]


    @app.route("/")
    def index():
        return render_template("index.html", habits=habits, title="Do Daily - Home")
    

    @app.route("/add", methods=["GET", "POST"])
    def add_task():
        if request.method == "POST":
            habits.append(request.form.get("task"))
        return render_template("add_task.html", title="Do Daily - Add Habit")
    
    return app