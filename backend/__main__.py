from .twitch.TwitchAuth import getAuth
from .logger import log
from .chat import ChatService
import time

# Perform pre-start checks
log("Main", "Performing pre-start checks")
log("Main", "Checking for an auth config")

try:
    getAuth("AuthTester")
except AssertionError as e:
    log("Main", "Encountered malfourmed config")
    print(e)
    exit(1)
    
# Announce self to the world
chat:ChatService.ChatService = ChatService.getChat("Main")
ChatService.sendMSG("/me ChatService has started!")

# Busy loop
# while True:
#     time.sleep(1)


chat.run()