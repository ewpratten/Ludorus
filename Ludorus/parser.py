import re

def parseMSG(message):
	parsed_message = {
		"message":"",
		"tags":"",
		"type":"",
		"raw":message,
		"channel":"",
		"username":""
	}
	
	data = re.match( r'@(.*);user-type.*:(.*)!(.*)@.*.tmi.twitch.tv (.*) .* :(.*)', message, re.M|re.I)
	parsed_message["channel"] = data.group(3)
	parsed_message["tags"] = data.group(1)
	parsed_message["username"] = data.group(2)
	parsed_message["message"] = data.group(5).strip()
	parsed_message["type"] = data.group(4)
	
	
	return parsed_message

def parseJOIN(message):
	parsed = {
		"user":"",
		"channel":""
	}
	
	data = re.match( r':(.*)!.*JOIN (.*)', message, re.M|re.I)
	parsed["user"] = data.group(1)
	parsed["channel"] = data.group(2)
	
	return parsed