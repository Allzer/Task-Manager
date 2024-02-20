from flask import Flask, render_template, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import SECRET_KEY, DATABASE_URL

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html', title='MindWriter')

@app.route("/tasks")
def get_tasks():
    return render_template('tasks.html', title='Tasks')

if __name__ == '__main__':
    app.run(debug=True)