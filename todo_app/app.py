from flask import Flask, render_template
from todo_app.data.session_items import get_items, add_item

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    to_do_items = get_items()
    return render_template('index.html', to_do_items = to_do_items)
