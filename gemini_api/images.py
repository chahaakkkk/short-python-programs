from google import genai
from google.genai import types
from PIL import Image

client=genai.Client()

imgaes=Image.open("img/img1.jpg")

response=client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=[imgaes,"describe the image"],
    config=types.GenerateContentConfig(
        system_instruction="explain in 20 words , be funny"
    )
)

print("------------------gemini response--------------------")
print(response.text)
