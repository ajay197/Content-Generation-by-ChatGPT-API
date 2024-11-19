from openai import OpenAI  # Import the OpenAI module to use its API.
from apikey import apikey  # Import the API key from a separate file for secure storage.
import os                  # Import the 'os' module to manage environment variables.
from PIL import Image      # Import the Image module from PIL (Pillow) to handle image display and saving.
import requests            # Import the 'requests' module to handle HTTP requests.
from io import BytesIO     # Import BytesIO to handle byte data in memory.

# Set the 'OPENAI_API_KEY' environment variable to the value of 'apikey'.
# This ensures that the OpenAI client can securely access the API key.
os.environ['OPENAI_API_KEY'] = apikey
OpenAI.api_key = apikey    # Set the API key directly in the OpenAI module.

# Initialize an OpenAI client.
client = OpenAI()

# Define the prompt for the image generation request.
prompt = "A cute puppy playing in the backyard, cartoon"

print("Generating Image...")

# Make an image generation request to the OpenAI API with the following parameters:
# - model: specify "dall-e-3" as the model to use for generating the image.
# - prompt: the prompt text describing the desired image.
# - size: specify the dimensions of the image (1024x1024 pixels).
# - n: specify the number of images to generate (1 image in this case).
response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    n=1,
)

# Print the raw response from the API for debugging or logging purposes.
print(response)

# Retrieve the URL of the generated image from the response data.
image_url = response.data[0].url

# Send a GET request to the image URL to retrieve the image content.
image = requests.get(image_url)

# Open the image using PIL by loading it from the retrieved byte data.
image = Image.open(BytesIO(image.content))

# Display the image in the default image viewer.
image.show()

# Save the image locally as "generated_image.png".
image.save("generated_image.png")
