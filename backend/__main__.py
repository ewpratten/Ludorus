from .twitch.TwitchAuth import getAuth
from .logger import log

# Perform pre-start checks
log("Main", "Performing pre-start checks")
log("Main", "Checking for an auth config")

try:
    getAuth()
except AssertionError as e:
    log("Main", "Encountered malfourmed config")
    print(e)
    exit(1)
    
