import json
from flask import Flask, render_template, request, jsonify

from scripts.chicgpt import get_advice

app = Flask(__name__)

conversation = []


@app.route('/')
def index():
    global conversation
    conversation.clear()
    return render_template('index.html')


@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json['user_input']

    global conversation  # Access the conversation variable

    # Process user input and generate a response using your chatbot logic
    response = get_advice(user_input, conversation)
    formatted_message = response.replace('\n', '<br>')

    # Add the user input and chatbot response to the conversation
    conversation.append({'role': 'user', 'content': user_input})
    conversation.append({'role': 'assistant', 'content': response})

    return formatted_message


@app.route('/wardrobe')
def show_json():
    with open('my_wardrobe.json') as json_file:
        data = json.load(json_file)
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
