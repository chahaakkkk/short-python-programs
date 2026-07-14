from google import genai
from google.genai import types

client=genai.Client()

prompt = input("enter the prompt: ")

response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=prompt,
    config=types.GenerateContentConfig(
        system_instruction="give explanation in 50 words or less",
        temperature=2
    )
)

print("----------------gemini response-----------------------")
print(response.text)