from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from openai import OpenAI
import httpx
import os
from typing import Literal

app = FastAPI(title="Diet Recipe App")


class RecipeRequest(BaseModel):
    diet_type: Literal["vegetarian", "vegan"]
    api_key: str


class RecipeResponse(BaseModel):
    recipe: str
    diet_type: str


@app.post("/api/recipe", response_model=RecipeResponse)
async def get_recipe(request: RecipeRequest):
    """
    Generate a dinner recipe based on diet preference using GPT-4
    """
    if not request.api_key:
        raise HTTPException(status_code=400, detail="OpenAI API key is required")
    
    # Create prompt based on diet type
    prompt = f"""Generate a simple and delicious {request.diet_type} dinner recipe. 
    Include:
    - Recipe name
    - Cooking time
    - Ingredients list
    - Step-by-step instructions
    
    Keep it simple and practical for home cooking."""
    
    # Use context manager to properly handle httpx client lifecycle
    try:
        with httpx.Client(timeout=60.0) as http_client:
            # Create OpenAI client with the provided API key and custom httpx client
            # This avoids proxy-related issues in serverless environments
            client = OpenAI(api_key=request.api_key, http_client=http_client)
            
            # Call OpenAI API
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful chef assistant that provides simple, practical recipes."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=800,
                temperature=0.7
            )
            
            recipe = response.choices[0].message.content
            
            return RecipeResponse(
                recipe=recipe,
                diet_type=request.diet_type
            )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating recipe: {str(e)}")


@app.get("/", response_class=HTMLResponse)
async def read_root():
    """
    Serve the main HTML page
    """
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Diet Recipe Generator</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 20px;
            }
            
            .container {
                background: white;
                border-radius: 20px;
                box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
                padding: 40px;
                max-width: 800px;
                width: 100%;
            }
            
            h1 {
                color: #333;
                text-align: center;
                margin-bottom: 10px;
                font-size: 2.5em;
            }
            
            .subtitle {
                text-align: center;
                color: #666;
                margin-bottom: 30px;
                font-size: 1.1em;
            }
            
            .form-group {
                margin-bottom: 25px;
            }
            
            label {
                display: block;
                margin-bottom: 10px;
                color: #333;
                font-weight: 600;
                font-size: 1.1em;
            }
            
            input[type="text"],
            input[type="password"],
            select {
                width: 100%;
                padding: 15px;
                border: 2px solid #e0e0e0;
                border-radius: 10px;
                font-size: 1em;
                transition: border-color 0.3s;
            }
            
            input[type="text"]:focus,
            input[type="password"]:focus,
            select:focus {
                outline: none;
                border-color: #667eea;
            }
            
            .diet-options {
                display: flex;
                gap: 15px;
                margin-top: 10px;
            }
            
            .diet-option {
                flex: 1;
                padding: 20px;
                border: 2px solid #e0e0e0;
                border-radius: 10px;
                text-align: center;
                cursor: pointer;
                transition: all 0.3s;
                background: white;
            }
            
            .diet-option:hover {
                border-color: #667eea;
                transform: translateY(-2px);
            }
            
            .diet-option.selected {
                border-color: #667eea;
                background: #f0f4ff;
            }
            
            .diet-option input[type="radio"] {
                display: none;
            }
            
            .diet-icon {
                font-size: 2em;
                margin-bottom: 10px;
            }
            
            button {
                width: 100%;
                padding: 18px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                border: none;
                border-radius: 10px;
                font-size: 1.2em;
                font-weight: 600;
                cursor: pointer;
                transition: transform 0.2s, box-shadow 0.2s;
            }
            
            button:hover {
                transform: translateY(-2px);
                box-shadow: 0 10px 20px rgba(102, 126, 234, 0.4);
            }
            
            button:active {
                transform: translateY(0);
            }
            
            button:disabled {
                opacity: 0.6;
                cursor: not-allowed;
            }
            
            .loading {
                display: none;
                text-align: center;
                margin-top: 20px;
            }
            
            .loading.active {
                display: block;
            }
            
            .spinner {
                border: 4px solid #f3f3f3;
                border-top: 4px solid #667eea;
                border-radius: 50%;
                width: 50px;
                height: 50px;
                animation: spin 1s linear infinite;
                margin: 0 auto 15px;
            }
            
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
            
            .result {
                display: none;
                margin-top: 30px;
                padding: 25px;
                background: #f9fafb;
                border-radius: 10px;
                border-left: 4px solid #667eea;
            }
            
            .result.active {
                display: block;
                animation: slideIn 0.5s ease-out;
            }
            
            @keyframes slideIn {
                from {
                    opacity: 0;
                    transform: translateY(20px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
            
            .result h2 {
                color: #667eea;
                margin-bottom: 15px;
            }
            
            .recipe-content {
                white-space: pre-wrap;
                line-height: 1.8;
                color: #333;
            }
            
            .error {
                display: none;
                margin-top: 20px;
                padding: 15px;
                background: #fee;
                border-left: 4px solid #f44;
                border-radius: 5px;
                color: #c00;
            }
            
            .error.active {
                display: block;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🍽️ Diet Recipe Generator</h1>
            <p class="subtitle">Get personalized dinner recipes based on your dietary preferences</p>
            
            <form id="recipeForm">
                <div class="form-group">
                    <label for="apiKey">OpenAI API Key</label>
                    <input 
                        type="password" 
                        id="apiKey" 
                        name="apiKey" 
                        placeholder="sk-..." 
                        required
                    >
                </div>
                
                <div class="form-group">
                    <label>Select Your Diet Preference</label>
                    <div class="diet-options">
                        <label class="diet-option" id="vegetarian-option">
                            <input type="radio" name="dietType" value="vegetarian" required>
                            <div class="diet-icon">🥗</div>
                            <div>Vegetarian</div>
                        </label>
                        <label class="diet-option" id="vegan-option">
                            <input type="radio" name="dietType" value="vegan" required>
                            <div class="diet-icon">🌱</div>
                            <div>Vegan</div>
                        </label>
                    </div>
                </div>
                
                <button type="submit">Generate Recipe</button>
            </form>
            
            <div class="loading" id="loading">
                <div class="spinner"></div>
                <p>Generating your delicious recipe...</p>
            </div>
            
            <div class="error" id="error"></div>
            
            <div class="result" id="result">
                <h2>Your Recipe</h2>
                <div class="recipe-content" id="recipeContent"></div>
            </div>
        </div>
        
        <script>
            // Handle diet option selection styling
            document.querySelectorAll('.diet-option').forEach(option => {
                option.addEventListener('click', function() {
                    document.querySelectorAll('.diet-option').forEach(opt => {
                        opt.classList.remove('selected');
                    });
                    this.classList.add('selected');
                });
            });
            
            // Handle form submission
            document.getElementById('recipeForm').addEventListener('submit', async (e) => {
                e.preventDefault();
                
                const apiKey = document.getElementById('apiKey').value;
                const dietType = document.querySelector('input[name="dietType"]:checked')?.value;
                
                if (!dietType) {
                    showError('Please select a diet preference');
                    return;
                }
                
                // Show loading, hide result and error
                document.getElementById('loading').classList.add('active');
                document.getElementById('result').classList.remove('active');
                document.getElementById('error').classList.remove('active');
                document.querySelector('button[type="submit"]').disabled = true;
                
                try {
                    const response = await fetch('/api/recipe', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({
                            diet_type: dietType,
                            api_key: apiKey
                        })
                    });
                    
                    const data = await response.json();
                    
                    if (!response.ok) {
                        throw new Error(data.detail || 'Failed to generate recipe');
                    }
                    
                    // Show result
                    document.getElementById('recipeContent').textContent = data.recipe;
                    document.getElementById('result').classList.add('active');
                    
                } catch (error) {
                    showError(error.message);
                } finally {
                    document.getElementById('loading').classList.remove('active');
                    document.querySelector('button[type="submit"]').disabled = false;
                }
            });
            
            function showError(message) {
                const errorDiv = document.getElementById('error');
                errorDiv.textContent = message;
                errorDiv.classList.add('active');
            }
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

