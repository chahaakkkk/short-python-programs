from google import genai

client=genai.Client()
chat=client.chats.create(model="gemini-3.1-flash-lite")
prompt=input("User: ")
while prompt!="endchat":
    response=chat.send_message(prompt)
    #print("ai: ",response.text)
    prompt=input("User: ")

for message in chat.get_history():
    print(message.parts[0].text)

