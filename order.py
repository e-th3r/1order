from app import db
from app.models import User

app = Flask(__name__)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}