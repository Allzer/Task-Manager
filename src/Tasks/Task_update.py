from database import db
from src.Tasks.models import Tasks


def update(form):
    t = Tasks(
        title=form["title"],
        description=form["description"],
        date=form["date"],
        importance=form["importance"]
    )

    db.session.add(t)
    db.session.commit()
    print("Изменения внесены")
