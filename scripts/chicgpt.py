import json
import openai

from config import api_key

# Set up your OpenAI API credentials
openai.api_key = api_key


def get_advice(user_input, item, json_file):

    # Define the initial messages for the conversation
    initial_message = {
        'role': 'system',
        'content': 'You are an assistant that provides fun fashion advice.'
    }

    if json_file:
        # Read the file content
        file_content = json_file.read()

        wardrobe_data = json.loads(file_content)
        wardrobe_json = json.dumps(wardrobe_data)

        wardrobe_message = {
            'role': 'system',
            'content': wardrobe_json
        }
    else:
        wardrobe_message = {
            'role': 'system',
            'content': ''
        }

    # Define the user's question
    if item:
        user_question = f"I'm going to wear {item}. What else should I wear {user_input}"
    else:
        user_question = f"What should I wear {user_input}"

    user_message = {'role': 'user', 'content': user_question}

    # Create the conversation with the initial message and user question
    conversation = [initial_message, wardrobe_message, user_message]

    # Convert the conversation to a list of message objects
    messages = [{'role': message['role'], 'content': message['content']} for message in conversation]

    # Make the API call to generate a response
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
        max_tokens=300,
        temperature=1,
        n=1
    )

    # Get the generated response from the API
    generated_text = response.choices[0].message['content']

    # Print the generated response
    return generated_text
