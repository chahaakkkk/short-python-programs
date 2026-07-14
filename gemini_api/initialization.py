from google import genai

client=genai.Client()

prompt=input("enter your prompt")

response=client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=prompt
)

print("------------------gemini response--------------------")
print(response.text)
