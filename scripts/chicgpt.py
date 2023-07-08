import json
import openai

from config import api_key

# Set up your OpenAI API credentials
openai.api_key = api_key


def get_advice(user_input, conversation):
    # Define the initial messages for the conversation if it's empty
    if len(conversation) == 0:
        initial_message = {
            'role': 'system',
            'content': 'You are an assistant that provides fun fashion advice.'
        }
        conversation.append(initial_message)

        with open('my_wardrobe.json', 'r') as json_file:
            wardrobe_data = json.load(json_file)
            wardrobe_json = json.dumps(wardrobe_data)

            print(wardrobe_json)

        wardrobe_message = {
            'role': 'system',
            'content': 'This is the contents of my wardrobe: ' + wardrobe_json
        }
        conversation.append(wardrobe_message)

    # Define the user's question
    user_question = f"{user_input}"

    user_message = {'role': 'user', 'content': user_question}

    # Add the user message to the conversation
    conversation.append(user_message)

    # Convert the conversation to a list of message objects
    messages = [{'role': message['role'], 'content': message['content']} for message in conversation]

    # Make the API call to generate a response
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
        max_tokens=500,
        temperature=1,
        n=1
    )

    # Get the generated response from the API
    generated_text = response.choices[0].message['content']

    # Print the generated response
    return generated_text
