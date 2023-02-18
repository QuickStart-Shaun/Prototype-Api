from fastapi import FastAPI
import openai
import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    test: str = "default"


settings = Settings()
app = FastAPI()

# Set up OpenAI API credentials
openai.api_key = os.getenv("OPENAI_API_KEY")

print("OPENAI_API_KEY =", os.getenv("OPENAI_API_KEY"))
print(settings.test)


@app.get("/")
def index():
    return {"test": "working"}


@app.get("/generate_text")
async def generate_text(prompt: str):
    # Set up OpenAI API request parameters
    model_engine = "text-davinci-002"
    temperature = 0.5
    max_tokens = 1024

    # Make request to OpenAI API
    print("hitting open ai")
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
    )

    # Return generated text
    return response.choices[0].text
