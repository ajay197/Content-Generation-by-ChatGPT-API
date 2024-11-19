# Content-Generation-by-ChatGPT-API

# 1. Generative AI Text Generation with OpenAI API

This project demonstrates using the OpenAI API to generate text responses based on a user-provided prompt. The example included generates a short essay on "Generative AI" using the `gpt-3.5-turbo` model.

## Prerequisites

- **Python 3.10+**
- **OpenAI API Key**: Obtain an API key from [OpenAI](https://platform.openai.com/signup/).

## Setup

1. **Install OpenAI's Python package**:
   ```bash
   pip install openai
   ```

2. **Store your API key**:
   Save your API key in a separate file named `apikey.py` with the following format:
   ```python
   apikey = "your_openai_api_key"
   ```

## Usage

1. **Run the Script**:
   ```python
   python text_generation.py
   ```

2. **Output**:
   The script prints the generated response to the console.

## Code Overview

- The script loads the API key from an external file (`apikey.py`) and sets it as an environment variable.
- It defines a prompt and makes a chat completion request to the OpenAI API, returning and printing the generated response.

## Text Models with pricing

| Model                 | Pricing (Input Tokens)         | Batch API Pricing (Input Tokens) | Cached Input Tokens | Pricing (Output Tokens)       | Batch API Pricing (Output Tokens) | Training Tokens       |
|-----------------------|--------------------------------|----------------------------------|---------------------|-------------------------------|------------------------------------|------------------------|
| **gpt-4o-2024-08-06** | $3.750 / 1M tokens            | $1.875 / 1M tokens              | $1.875 / 1M tokens  | $15.000 / 1M tokens           | $7.500 / 1M tokens               | $25.000 / 1M tokens   |
| **gpt-4o-mini-2024-07-18** | $0.300 / 1M tokens        | $0.150 / 1M tokens              | $0.150 / 1M tokens  | $1.200 / 1M tokens            | $0.600 / 1M tokens               | $3.000 / 1M tokens    |
| **gpt-3.5-turbo**     | $3.000 / 1M tokens            | $1.500 / 1M tokens              | N/A                 | $6.000 / 1M tokens            | $3.000 / 1M tokens               | $8.000 / 1M tokens    |
| **davinci-002**       | $12.000 / 1M tokens           | $6.000 / 1M tokens              | N/A                 | $12.000 / 1M tokens           | $6.000 / 1M tokens               | $6.000 / 1M tokens    |
| **babbage-002**       | $1.600 / 1M tokens            | $0.800 / 1M tokens              | N/A                 | $1.600 / 1M tokens            | $0.800 / 1M tokens               | $0.400 / 1M tokens    |

