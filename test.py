import os
import asyncio
import sys
from concurrent.futures import ThreadPoolExecutor

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

async def ainput(prompt: str = ""):
    with ThreadPoolExecutor(1, "AsyncInput", lambda x: print(x, end="", flush=True), (prompt,)) as executor:
        return (await asyncio.get_event_loop().run_in_executor(
            executor, sys.stdin.readline
        )).rstrip()

async def main():
    while True:
        name = await ainput("Input: ")
        print("Your Input: {}!".format(name))
        print(client.guilds)
        for guild in client.guilds:
            if guild.name == "3207":
                # print(guild.me.guild_permissions)
                for channel in guild.channels:
                    if channel.name == "general":
                        invitelink = await channel.create_invite(max_uses=1,unique=True)
                        print(invitelink)

                        await channel.send(name)

                        print(channel)
                        messages = await channel.history(limit=10).flatten()
                        for message in messages:
                            print(str(message.author) + ": "+ message.content)

@client.event
async def on_message(message):
    if (str(message.guild) == "3207"):
        print("Message Channel" + str(message.channel))
        print(str(message.author) + ": " + str(message.content))

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.loop.create_task(main())
client.run(TOKEN)
