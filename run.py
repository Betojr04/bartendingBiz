from app import db
from flask_migrate import Migrate

migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return {"db": db}
