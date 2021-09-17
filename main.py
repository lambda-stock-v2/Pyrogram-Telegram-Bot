from pyrogram import Client, filters
import asyncio
from time import time
import time
import os

app = Client(
    "<YOUR_SESSION_NAME>", bot_token="<YOUR_BOT_TOKEN"
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await client.send_message(message.chat.id, f"""**Welcome** @{message.from_user.username}.
**Group**: ```{message.chat.title}```
**Invite Link**:  ```t.me/{message.chat.username}```
**Your User ID**: ```{message.from_user.id}```

You can contact with me from PM if you need more help.
""")

#@app.on_message(filters.private)
#async def log(client, message):
#    await client.send_message('sgteammain', f"""
#A message was sent from private.:
#	
#{message.text}

#Sender: {message.from_user.id}
#""")

@app.on_message(filters.command("info"))
async def info(client, message):
    await client.edit_message_text(message.chat.id, f"""**User Info**
ID: ```{message.reply_to_message.from_user.id}```
Username: @{message.reply_to_message.from_user.username}
Name: {message.reply_to_message.from_user.first_name}
Surname: {message.reply_to_message.from_user.last_name}
Data Center: ```{message.reply_to_message.from_user.dc_id}```
""")

@app.on_message(filters.command("data"))
async def data(client, message):
    await client.send_message(message.chat.id, f"""```{message.from_user}```""")

@app.on_message(filters.command("send"))
async def send(client, message):
    await client.send_message(message.chat.id, f"""Data was successfully sent to terminal.""")
    print(message)

@app.on_message(filters.command("get_sticker_id"))
async def get_sticker_id(client, message):
	await client.send_message(message.chat.id, f"```{message.reply_to_message.sticker.file_id}```")

@app.on_message(filters.command("send_sticker"))
async def send_sticker(client, message):
    stickinput_withcmd = message.text
    stickinput = stickinput_withcmd.replace("/send_sticker ", "")
    await client.send_sticker(message.chat.id, f"{stickinput}")


app.run()
#asyncio.get_event_loop().run_until_complete(main())