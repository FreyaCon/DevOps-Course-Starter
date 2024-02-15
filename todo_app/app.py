from flask import Flask, render_template, request, redirect, url_for
from todo_app.helpers.trello_items import get_items, add_item, toggle_list
import os
import requests

from todo_app.flask_config import Config
from todo_app.helpers.list_id_helper import LIST_ID

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/', methods = ['GET'])
def index():
    cards = get_items()
    return render_template('index.html', to_do_items=cards, list_helper = LIST_ID)
   

@app.route('/', methods=['POST'])
def new_item():
    title = request.form['add-items']
    desc = request.form['add-desc']
    add_item(title, desc)
    return redirect(url_for('index'))

@app.route('/complete-item/<item_id>', methods=['GET'])
def change_list(item_id):
    toggle_list(item_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)


