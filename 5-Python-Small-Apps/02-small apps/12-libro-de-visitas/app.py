from flask import Flask, render_template, request, redirect, url_for
import json
from datetime import datetime

app = Flask(__name__)

# Archivo JSON donde se almacenarán los mensajes
GUESTBOOK_FILE = "guestbook.json"


def load_messages():
    try:
        with open(GUESTBOOK_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_message(name, message, date):
    messages = load_messages()
    messages.append({"name": name, "message": message, "date": date})
    with open(GUESTBOOK_FILE, 'w') as file:
        json.dump(messages, file)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        save_message(name, message, date)
        return redirect(url_for('index'))

    messages = load_messages()
    return render_template('index.html', messages=messages)


if __name__ == '__main__':
    app.run(debug=True)
