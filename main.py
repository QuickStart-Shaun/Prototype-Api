from fastapi import FastAPI
import openai
import os
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseSettings

origins = [
    "https://shauns-stellar-site-4dbb3e.webflow.io",
]


class Settings(BaseSettings):
    test: str = "default"


settings = Settings()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# Set up OpenAI API credentials
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.get("/")
def index():
    return {"test": "working"}


@app.get("/test")
def test_return(prompt: str):
    return {"test": prompt}


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
