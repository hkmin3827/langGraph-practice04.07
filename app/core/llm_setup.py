from google import genai
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

import os
load_dotenv()

client = genai.Client()


model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=0
)

# response = client.models.generate_content(
#     model="gemini-3-flash-preview", contents="랭체인과 랭그래프 관계 설명해줘"
# )
# print(response.text)