from flask import Flask, render_template, request

from scripts.chicgpt import get_advice

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        item = request.form.get('item')
        json_file = request.files['json_file']
        message = get_advice(user_input, item, json_file)
        formatted_message = message.replace('\n', '<br>')
        return render_template('result.html', message=formatted_message)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
