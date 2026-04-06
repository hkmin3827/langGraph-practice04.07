from google import genai
from dotenv import load_dotenv

import os
load_dotenv()

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="랭체인과 랭그래프 관계 설명해줘"
)
print(response.text)