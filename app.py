
from flask import Flask, render_template, request


def create_app():
    app = Flask(__name__)

    @app.route("/", methods=["GET", "POST"])
    def home():
        return render_template("base.html")
    
    return app