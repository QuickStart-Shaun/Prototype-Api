from fastapi import FastAPI
import openai
import os
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseSettings


def create_prompt(list_qa: list) -> str:
    start_sequence = "You are a professional business plan writer and have been given the following answered questions:"
    end_sequence = "From the above answered questions, write a great executive summary of a business plan"

    prompt = start_sequence + "\n"
    for qa in list_qa:
        prompt = prompt + "question: " + qa["question"] + "\n"
        prompt = prompt + "answer: " + qa["answer"] + "\n"
    prompt = prompt + end_sequence
    return prompt


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
def test_return(prompt: str, Prompt2: str):
    return {"test": prompt + Prompt2}


@app.get("/generate_business_plan")
async def generate_text(Q1: str, Q2: str):
    list_qa = [
        {"question": "What do you sell", "answer": Q1},
        {"question": "Who are your customers", "answer": Q2},
    ]

    # Set up OpenAI API request parameters
    model_engine = "text-davinci-002"
    temperature = 0.5
    max_tokens = 1024

    # Make request to OpenAI API
    print("hitting open ai")
    response = openai.Completion.create(
        engine=model_engine,
        prompt=create_prompt(list_qa),
        max_tokens=max_tokens,
        temperature=temperature,
    )
    # Return generated text
    return response.choices[0].text


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


if __name__ == "__main__":
    list_qa = [
        {"question": "did this work", "answer": "yup it did"},
        {"question": "did this work", "answer": "yup it did"},
        {"question": "did this work", "answer": "yup it did"},
    ]
    prompt = create_prompt(list_qa)
    print(prompt)
