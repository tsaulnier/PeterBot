import discord
import responses
import config
    
currentIndex = 0

async def send_message(message, user_message, channel, is_private):
    try:
        response = responses.get_response(user_message, channel, currentIndex)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)
        
def run_discord_bot():
    TOKEN = config.token
    
    # client
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        print(f'{username} said: "{user_message}" ({channel})')
        
        await send_message(message, user_message, channel, is_private=False)
        
        
        # private DM functionality
        # if user_message[0] == '':
        #     user_message = user_message[1:]
        #     await send_message(message, user_message, channel, is_private=True)
        # else:
        #     await send_message(message, user_message, channel, is_private=False)
        
    client.run(TOKEN)
    
    # client.close()