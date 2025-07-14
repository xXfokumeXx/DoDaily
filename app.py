
from flask import Flask, render_template


def create_app():
    app = Flask(__name__)


    @app.route("/")
    def index():
        return render_template("index.html", title="Do Daily - Home")
    

    @app.route("/add", methods=["GET", "POST"])
    def add_habit():
        return render_template("add_habbit.html", title="Do Daily - Add Habit")
    
    return app