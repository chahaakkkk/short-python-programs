from google import genai
from google.genai import types
import httpx,io

client=genai.Client()

doclink="https://arunodayauniversity.ac.in/wp-content/uploads/2025/01/Research-Methodology-Methods-and-Techniques-Kothari.pdf"
doc=io.BytesIO(httpx.get(doclink).content)

pdf=client.files.upload(
    file=doc,
    config={
    "mime_type" : "application/pdf"
    }
)

response=client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=[pdf,"summarize this pdf in 100 words"]
)

print(response.text)