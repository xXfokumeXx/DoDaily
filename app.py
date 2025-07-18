import datetime
from flask import Flask, render_template, request


def create_app():
    app = Flask(__name__)
    habits = ["Test Task"]

    def date_range(start: datetime.date):
        dates = [start + datetime.timedelta(days=diff) for diff in range(-3,4)]
        return dates


    @app.route("/")
    def index():
        date_str = request.args.get("date")
        if date_str:
            selected_date = datetime.date.fromisoformat(date_str)
        else:
            selected_date = datetime.date.today()
        return render_template(
            "index.html",
            habits=habits,
            title="Do Daily - Home",
            date_range=date_range,
            selected_date=selected_date
        )

    

    @app.route("/add", methods=["GET", "POST"])
    def add_task():
        if request.method == "POST":
            habits.append(request.form.get("task"))
        return render_template("add_task.html", title="Do Daily - Add Habit")
    
    return app