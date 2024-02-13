from flask import Flask, render_template, request, redirect, url_for
from todo_app.data.session_items import get_items, add_item

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/', methods = ['GET'])
def index():
    to_do_items = get_items()
    return render_template('index.html', to_do_items=to_do_items)

@app.route('/', methods=['POST'])
def new_item():
    title = request.form['add-items']
    add_item(title)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)


