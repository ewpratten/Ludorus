# Ludorus

## Setup
The following steps are required:

 - Create a folder at `.env/config` and add a file to it called `config.json`

### The config file
Inside `.env/config/config.json`, we will define all streaming-related info.
```json
{
    "stream_key":"<Your_Stream_Key>",
    "username":"ludorusgame",
    "oauth":{
        "TMI":"<TMI_Key>",
        "client":"<client_key>"
    }
}
```

The stream key should have been emailed to anybody authorized to stream to the main `ludorusgame` channel. Anyone else should use their own creds. All other data can be gotten from [Twitch OAUTH](https://twitchapps.com/tmi/). **Make sure to log in with the `ludorusgame` account. Not your own!**
