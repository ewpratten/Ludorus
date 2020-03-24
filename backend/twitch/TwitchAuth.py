from json import load

# Twitch authentication data


class TwitchAuth(object):
    tmi: str
    client_key: str
    username: str

    def __init__(self):

        # Load the JSON config from the user
        j = load(open(".env/config/config.json", "r"))
        self.tmi = j["oauth"]["TMI"]
        self.client_key = j["oauth"]["client"]
        self.username = j["username"]

        # Ensure there is data from the user
        assert self.tmi is not ""
        assert self.client_key is not ""
        assert self.username is not ""


# Define a getter for a global auth instance
_globalAuth = TwitchAuth()
def getAuth() -> TwitchAuth: return _globalAuth
