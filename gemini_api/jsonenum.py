from google import genai
from pydantic import BaseModel
from enum import Enum

class Difficulty(Enum):
    DIFFICULT = "When the chosen path is very difficult and requires a lot of effort."
    MODERATE = "When the chosen path is difficult but requires less effort than the difficult path."
    EASY = "When the path is simple to follow."

class Paths(BaseModel):
    pathname:str
    roadmap:list[str]
    skills:list[str]
    difficulity:Difficulty


client = genai.Client()

response  = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents="gived the carrer paths an engineeroing student can take in the first year also give its road map and skills he has to develop for each path",
    config={
        "response_mime_type":"application/json",
        "response_schema":list[Paths]    
        }
)
print(response.text)