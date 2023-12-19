from flask import Flask, render_template, request, redirect, url_for
from todo_app.data.session_items import get_items, add_item

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        title = request.form['add-items']
        add_item(title)
        # Redirect to the index page to avoid form resubmission on page refresh
        return redirect(url_for('index'))

    # If it's a GET request or after processing the POST request, render the index page
    to_do_items = get_items()
    return render_template('index.html', to_do_items=to_do_items)

#@app.route('/form', methods = ['POST', 'GET'])
#def form():
    #title = request.form['add-items']
    #add_item(title)

if __name__ == '__main__':
    app.run(debug=True)


