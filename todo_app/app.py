from flask import Flask, render_template, request, redirect, url_for
from todo_app.helpers.trello_items import get_items, add_item, toggle_list
from todo_app.helpers.view_class import ViewModel
import os
import requests

from todo_app.flask_config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    @app.route('/', methods = ['GET'])
    def index():
        cards = get_items()
        item_view_model = ViewModel(cards)
        return render_template('index.html', view_model=item_view_model)
    

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
    
    return app



