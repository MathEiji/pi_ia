import discord
import requests
 
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)
 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
 
@client.event
async def on_message(message):
    print("message-->", message)
    print("message content-->", message.content)
    print("message attachments-->", message.attachments)
    print("message id", message.author.id)
    a_id = message.author.id
    if a_id != 1100544229895327904:
   
        for x in message.attachments:
            print("attachment-->",x.url)
            d_url = requests.get(x.url)
            file_name = x.url.split('/')[-1]
            with open(file_name, "wb") as f:
                f.write(d_url.content)
 
    if message.author == client.user:
        return
 
    if message.content.startswith('oi'):
        await message.channel.send('Send it!')
 
    if message.content.startswith('drift'):
        await message.channel.send('Get sideways')
        await message.channel.send(file=discord.File('sideways.jpg'))
 

client.run('secret_key')