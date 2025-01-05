import os
from pyrogram import Client, filters

api_id = 26107399
api_hash = "e10525d8ad0189f8bf7a82a32f538d12"
session_string = "BAGOXgcAqb25_WY0LAXWL_OYTrzMpBm9MF9aa-L_ITj5d_PXsuZAaLrtbvCL3t_B9Lye7P9Xlw4B_k0NHnIV97MR9-rBPmFreUMbjzrfiPn-81PMEJt_YvCFJ7iUNTlk3AmCVzAF3NuakVBVc-pcLFbOwWowNA1RGWsNd9R5hV6xRj0Or5gkal5SjM_QcWpJAYu71eh0-WYPYn3Y1ZkwwKdjUwoGG7oAUauzJbdowcCufhgcQftdQChy9Yuw-1rzihJxnes1D29uWEkTB5VKx3D7PnjY4EgelJ8ODbpb4ChcyzIjkqyFtNltAoS0KYA0o4qjn2zX9hYXF6gy2-w8JmwAAAABMC-_yAA"

app = Client(session_string, api_id=api_id, api_hash=api_hash)

@app.on_message(filters.private)
def handle_message(client, message):
    print(f"Received message from {message.from_user.id}: {message.text}")
    client.send_message(message.from_user.id, "Message received!")

app.run()
