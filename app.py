from flask import Flask, render_template, request
from flask_migrate import Migrate
from sqlalchemy import desc

from src.Tasks.Task_update import update
from src.Tasks.models import Tasks

from config import SECRET_KEY, DATABASE_URL
from database import db

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

db.init_app(app)
migrate = Migrate(app, db)


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html', title='MindWriter')

@app.route("/tasks", methods=['POST', 'GET'])
def get_tasks():
    if request.method == 'POST':
        form = request.form
        update(form)
        all_tasks = Tasks.query.order_by(desc(Tasks.id)).all()

    elif request.method == 'GET':
        all_tasks = Tasks.query.order_by(desc(Tasks.id)).all()

    return render_template(
        'tasks.html',
        title='Tasks',
        tasks=all_tasks
    )

if __name__ == '__main__':
    app.run(debug=True)