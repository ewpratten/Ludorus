file = ""

db = {}

def read():
	global db
	global file
	with open(file, "r") as f:
		db = eval(f.read())
		print(f"{len(db['data'])} users")
		f.close()

def write():
	global db
	global file
	with open(file, "w") as f:
		f.writelines(str(db).replace("'",'"'))
		f.close()

def getUser(user):
	for entry in db["data"]:
		if entry["name"] == user:
			print(entry)
			return entry
	return None

def insert(data):
	global db
	db["data"].append(data)

def marketAdd(item):
	global db
	db["market"].append(item)

def marketFind(name, id=None):
	global db
	if id:
		for i,listing in enumerate(db["market"]):
			if listing["id"] == id:
				return (listing, i)
	else:
		for i,listing in enumerate(db["market"]):
			if listing["name"] == name:
				return (listing, i)
	return None

def subListing(index):
	global db
	db["market"][index]["quantity"] -= 1

def subcoins(username,coins):
	global db
	for i,user in enumerate(db["data"]):
		if user["name"] == username:
			db["data"][i]["coins"] -= coins
			return

def addcoins(username,coins):
	global db
	for i,user in enumerate(db["data"]):
		if user["name"] == username:
			db["data"][i]["coins"] += coins
			return