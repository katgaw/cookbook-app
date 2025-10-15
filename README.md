# Diet Recipe Generator 🍽️

A simple FastAPI application that generates personalized dinner recipes based on dietary preferences (Vegetarian/Vegan) using GPT-4.

## Features

- 🌱 Support for Vegetarian and Vegan diets
- 🤖 Powered by OpenAI GPT-4
- 🎨 Beautiful, modern web interface
- ⚡ Fast and simple to use
- 🔒 Secure - API key only used for individual requests

## Prerequisites

- Python 3.8+
- OpenAI API Key (get one at https://platform.openai.com/api-keys)

## Installation

1. Clone or navigate to the project directory:
```bash
cd cookbook-app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the FastAPI server:
```bash
uvicorn main:app --reload
```

The application will be available at: **http://localhost:8000**

## Usage

1. Open your browser and go to http://localhost:8000
2. Enter your OpenAI API Key in the provided field
3. Select your diet preference (Vegetarian or Vegan)
4. Click "Generate Recipe"
5. Wait a few seconds for GPT-4 to generate your personalized dinner recipe!

## API Endpoints

### `GET /`
Returns the main web interface

### `POST /api/recipe`
Generate a recipe based on diet preference

**Request Body:**
```json
{
  "diet_type": "vegetarian",  // or "vegan"
  "api_key": "your-openai-api-key"
}
```

**Response:**
```json
{
  "recipe": "Recipe details...",
  "diet_type": "vegetarian"
}
```

### `GET /health`
Health check endpoint

## Security Note

Your API key is sent directly to OpenAI and is not stored by this application. Each request uses the API key you provide.

## Tech Stack

- **Backend**: FastAPI
- **LLM**: OpenAI GPT-4
- **Frontend**: HTML, CSS, JavaScript (vanilla)
- **Server**: Uvicorn

## Troubleshooting

- **Invalid API Key**: Make sure your OpenAI API key is correct and has GPT-4 access
- **Rate Limiting**: If you get rate limit errors, wait a moment before trying again
- **Connection Issues**: Ensure you have an active internet connection

## License

MIT License - Feel free to modify and use as needed!

