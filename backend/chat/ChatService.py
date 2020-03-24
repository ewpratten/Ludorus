from twitchio.ext import commands
from ..twitch.TwitchAuth import TwitchAuth, getAuth


class ChatService(commands.Bot):

    auth: TwitchAuth

    def __init__(self):
        self.auth = getAuth()
