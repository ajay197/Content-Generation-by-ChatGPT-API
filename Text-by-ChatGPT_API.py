from openai import OpenAI, api_key  # Import the OpenAI module and the api_key variable.
from apikey import apikey           # Import the API key from a separate file named 'apikey'.
import os                            # Import the 'os' module to manage environment variables.

# Set the 'OPENAI_API_KEY' environment variable to the value of 'apikey'.
# This allows OpenAI's API to use the provided key.
os.environ['OPENAI_API_KEY'] = apikey

# Assign the 'api_key' variable to 'OpenAI.api_key' to authenticate the API usage.
OpenAI.api_key = api_key

# Instantiate an OpenAI client.
client = OpenAI()

# Define the prompt to be used in the API call.
prompt = "Write a short essay on Generative AI"

# Make a chat completion request to the API with the following parameters:
# - model: specify "gpt-3.5-turbo" as the model to be used.
# - messages: a list of messages where "role" is "user" and "content" contains the prompt text.
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
)

# Print the message content returned by the API in the response object.
print("Message Content:")
print(response.choices[0].message.content)  # Access the first choice and print its content.
