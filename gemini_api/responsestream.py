from google import genai

client=genai.Client()

prompt=input("enter your prompt")

response=client.models.generate_content_stream(
    model="gemini-3.1-flash-lite",
    contents=prompt
)

for chunk in response:
    print(chunk.text ,end="----------------------------\n")
