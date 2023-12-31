from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv(".env")

# Access the secret API key from the environment
api_key = os.getenv("API_KEY")