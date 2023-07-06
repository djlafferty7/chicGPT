from flask import Flask, render_template

from config import secret_key
from scripts.forms import MyForm
from scripts.chicgpt import get_advice

app = Flask(__name__)
app.secret_key = secret_key

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        user_input = form.user_input.data
        item = form.item.data
        json_file = form.json_file.data
        message = get_advice(user_input, item, json_file)
        formatted_message = message.replace('\n', '<br>')
        return render_template('result.html', message=formatted_message)
    else:
        return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
