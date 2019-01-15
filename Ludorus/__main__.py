print("Starting...")

import chat_interface as chat
import commands as commands
import time


def newMSG(data):
	if data["action"] == "join":
		return f"PRIVMSG #{chat.channel} :{commands.login(data)}"
	cmd = data["data"]["message"].split(" ")[0].strip()
	if cmd in commands.command_mapping:
		response = commands.command_mapping[cmd](data['data'])
		return f"PRIVMSG #{chat.channel} :{response}"
	return ""


# connect to chat
chat.setCallback(newMSG)
chat.ws.run_forever()

commands.db.write()
print("Wrote to db")


# Startup
## check for files
### create missing files
## connect to twitch chat
## check stream health
# allow interaction through the console as god
