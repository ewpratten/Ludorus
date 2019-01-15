import db as db
db.file = './db/main.json'
db.read()

def login(data):
	if not db.getUser(data["user"]):
		db.insert({"name":data["user"], "coins":100, "stores":{}, "inventory":{}})
		db.write()
		return f"{data['user']} has moved in. Welcome!"
	else:
		return ""

def getBalance(data):
	coins = db.getUser(data['username'])['coins']
	username = data['username']
	return f"{username} has {coins} coins"

def buy(data):
	item = data["message"].split(" ")[1]
	item_id = None
	if len(data["message"].split(" ")) > 2:
		item_id = data["message"].split(" ")[2]
	
	listing,index = db.marketFind(item,item_id)
	if listing["price"] > db.getUser(data["username"])["coins"]:
		return f"{data['username']} Cannot afford item"
	if listing['quantity'] != "unlimited":
		db.subListing(index)
	db.subcoins(data["username"], listing["price"])
	db.addcoins(listing["seller"], listing["price"])
	return f"{data['username']} bought {item} ({item_id})"

def cost(data):
	item = data["message"].split(" ")[1]
	print(f"Searching for {item}" )
	listing,_ = db.marketFind(item, None)
	if listing:
		return f"{data['username']} The price of {item} is {listing['price']} coins"

command_mapping = {
	"?balance":getBalance,
	"?cost":cost,
	"?buy":buy
}