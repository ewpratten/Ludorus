from twitchio.ext import commands
from ..twitch.TwitchAuth import TwitchAuth, getAuth
from ..logger import log

class ChatService(commands.Bot):

    auth: TwitchAuth

    def __init__(self):

        # Get auth for this bot
        self.auth = getAuth("ChatService")

        # Init the bot controller
        super().__init__(irc_token=self.auth.tmi, client_id=self.auth.client_key,
                       nick=self.auth.username, prefix="!", initial_channels=[self.auth.username])



_globalChat: ChatService = ChatService()
def getChat(svc:str)->ChatService:
    log("ChatService", f"{svc} now has chat access")
    return _globalChat

def sendMSG(msg: str):
    # self._ws.send_privmsg(self.auth.username, msg)
    pass


@_globalChat.event
async def event_message(ctx):
    # Ignore messages from self
    if ctx.author.name.lower() == _globalChat.auth.username.lower():
        return
    
    # Log this event
    log("ChatService", f"RCV Message from (@{ctx.author.name}): {ctx.content}")
    
    