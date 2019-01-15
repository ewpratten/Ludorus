# Interface for twitch chat
import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import time

import parser as parser
import os
from pathlib import Path
home = str(Path.home())

callback = None

def setCallback(func):
	global callback
	callback = func

def on_message(ws, message):
	global callback
	# deal with pingpong
	if message == "PING :tmi.twitch.tv":
		sw.send("PONG :tmi.twitch.tv")
	
	if "Error logging in" in message:
		os._exit()
	
	# check if the message is from the server
	if message[0] != "@":
		try:
			data = parser.parseJOIN(message)
			print(f"{data['user']} joined {data['channel']}")
			ws.send(callback({"action":"join","user":data["user"]}))
		except:
			print(f"TWITCH: {message}")
	else:
		try:
			data = parser.parseMSG(message)
			ws.send(callback({"action":"message","data":data}))
			# cmd = data["message"].split(" ")[0]
			# if cmd in mods.list:
			# 	response = mods.list[cmd](data)
			# 	if response == 0:
			# 		ws.send("PRIVMSG #retrylife k")
			# 	elif response == 1:
			# 		ws.send("PRIVMSG #retrylife e")
			# 	else:
			# 		ws.send(f"PRIVMSG #retrylife {response}")
			# print(f"{data['username']}: {data['message']}")
		except:
			print(f"MSG: {message}")

def on_error(ws, error):
	print(f"ERROR: {error}")

def on_close(ws):
	print("Closed.")

def on_open(ws):
	global token
	global username
	global channel
	print("Connecting")
	
	ws.send(f"PASS {token}")
	ws.send(f"NICK {username}")
	ws.send(f"JOIN #{channel}")
	
	ws.send("CAP REQ :twitch.tv/membership")
	ws.send("CAP REQ :twitch.tv/tags twitch.tv/commands")
	
	# send ready message
	ws.send("PRIVMSG #retrylife :Ludorus bot is online")
	

## Start Bot ##

username  = "retrylife"
channel   = "retrylife"

with open(home + "/.shiver_login", "r") as f:
	data = f.read().split("\n")
	client_id = data[0]
	token = data[1]
	f.close()

# websocket.enableTrace(True)
ws = websocket.WebSocketApp("wss://irc-ws.chat.twitch.tv/irc", on_message = on_message, on_error = on_error, on_close = on_close)
ws.on_open = on_open
# ws.run_forever()