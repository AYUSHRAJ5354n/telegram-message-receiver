import os
from pyrogram import Client, filters

api_id = 26107399
api_hash = "e10525d8ad0189f8bf7a82a32f538d12"
session_string = os.getenv("SESSION_STRING")

app = Client("my_session", api_id=api_id, api_hash=api_hash, session_string=session_string, in_memory=True)

@app.on_message(filters.private)
def handle_message(client, message):
    print(f"Received message from {message.from_user.id}: {message.text}")
    client.send_message(message.from_user.id, "Message received!")

app.run()
