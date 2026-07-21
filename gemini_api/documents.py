from google import genai
import httpx
from google.genai import types

client=genai.Client()

document_url= "https://cdnbbsr.s3waas.gov.in/s301894d6f048493d2cacde3c579c315a3/uploads/2026/04/202604271907903947.pdf"
document=httpx.get(document_url).content

pdf=types.Part.from_bytes(
    data=document,
    mime_type="application/pdf"
)


response=client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=[pdf,"summarize this pdf in 100 words"]
)
print(response.text)