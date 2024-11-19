# Content-Generation-by-ChatGPT-API

# Generative AI Text/Image Generator

This project is a Python program that uses the OpenAI API to generate a short essay on a given topic, specifically on "Generative AI." The script connects to the OpenAI GPT-3.5 model, sends a prompt, and retrieves the generated content as a response. This project demonstrates the basics of setting up the OpenAI API and retrieving responses using Python.

## Prerequisites

Before running the program, ensure that you have:

- Python 3.7 or higher
- An API key for OpenAI, stored in a separate file for security (see **Setup** below)
- OpenAI Python SDK installed (`openai` package)

## Setup

1. **Install the OpenAI Python SDK**:  
   Run the following command in your terminal to install the OpenAI SDK:
   ```bash
   pip install openai

2. API Key Storage:

Create a file named apikey.py in the same directory as the main script.
Inside apikey.py, define a variable apikey and set it to your OpenAI API key:

apikey = "your_openai_api_key"

This helps keep your API key secure and separated from the main code.
3. Environment Variable Setup: The program uses the os library to set the API key as an environment variable, allowing the OpenAI SDK to access it securely.









Here’s a sample `README.md` file for the program:

```markdown
# Generative AI Essay Generator

This project is a Python program that uses the OpenAI API to generate a short essay on a given topic, specifically on "Generative AI." The script connects to the OpenAI GPT-3.5 model, sends a prompt, and retrieves the generated content as a response. This project demonstrates the basics of setting up the OpenAI API and retrieving responses using Python.

## Prerequisites

Before running the program, ensure that you have:

- Python 3.7 or higher
- An API key for OpenAI, stored in a separate file for security (see **Setup** below)
- OpenAI Python SDK installed (`openai` package)

## Setup

1. **Install the OpenAI Python SDK**:  
   Run the following command in your terminal to install the OpenAI SDK:
   ```bash
   pip install openai
   ```

2. **API Key Storage**:
   - Create a file named `apikey.py` in the same directory as the main script.
   - Inside `apikey.py`, define a variable `apikey` and set it to your OpenAI API key:
     ```python
     apikey = "your_openai_api_key"
     ```
   - This helps keep your API key secure and separated from the main code.

3. **Environment Variable Setup**:
   The program uses the `os` library to set the API key as an environment variable, allowing the OpenAI SDK to access it securely.

## Usage

1. **Run the Program**:
   Execute the script by running:
   ```bash
   python script_name.py
   ```
   Replace `script_name.py` with the actual name of your Python file.

2. **Output**:
   The program will output a generated response on the topic "Generative AI." This is printed in the console under the header `Message Content:`.

## Code Overview

- **Environment Variable**: `os.environ['OPENAI_API_KEY'] = apikey` securely sets the API key as an environment variable for use by the OpenAI client.
- **Client Initialization**: `client = OpenAI()` initializes a client instance to interact with the OpenAI API.
- **API Call (Chat Completion)**: `client.chat.completions.create(...)` sends the prompt to the GPT-3.5 model.
- **Output Retrieval**: `response.choices[0].message.content` extracts and displays the AI's response.

## Example Output

Upon running the script, you should see something similar to the following in your terminal:

```plaintext
Message Content:
Generative AI is a rapidly growing field in artificial intelligence...
```

## License

This project is open-source and available for modification and distribution under the MIT License.

## Contact

For any issues or inquiries, please feel free to open an issue in the repository.

```

This `README.md` provides setup instructions, code explanations, usage, and an example output to make it easy for others to understand and run the program.
