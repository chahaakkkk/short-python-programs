from google import genai
from google.genai import types

client = genai.Client()

print("chat starts here , write 'fuck you' to exit")

prompt = input("enter the prompt: ")

chat=[]

while prompt != "fuck you":
    chat.append("User: " + prompt)
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=chat,
        config=types.GenerateContentConfig(
            system_instruction="respond in 10 words or less",
            temperature=1
        )
    )
    print("gemini :",response.text)
    chat.append("gemini: "+ response.text)
    prompt=input("User: ")
