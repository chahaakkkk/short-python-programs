from google import genai
from google.genai import types

client=genai.Client()

ground_tools = types.GoogleSearch()

response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents = "which team won the most matchs in fifa world cup 2026 till date",
    config= types.GenerateContentConfig(
        tools=[ground_tools])
    )
print(response.text)