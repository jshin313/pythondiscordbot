import os
import asyncio
import sys
from concurrent.futures import ThreadPoolExecutor
import sys

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
            print(guild.name)
            # if guild.name == "taewonnies":
            # if guild.name == "The Temple Homies":
            if guild.name == "Test Server for my Bots":
                # print(guild.me.guild_permissions)
                for channel in guild.channels:
                    # if channel.name == "general":
                    if channel.name == "f-a-c-k":
                        # invitelink = await channel.create_invite(max_uses=1,unique=True)
                        # print(invitelink)

                        # while True:
                        #     name = "<@!746617651475775518>"*59
                        #     message = await channel.send(name)
                        #     await asyncio.sleep(3)

                        # while (True):
                        # message = await channel.send("<@!499930480217554944>")
                        message = await channel.send("<@!270999459784032257> Yo.")
                        await asyncio.sleep(3)
                        birthday = """
```
              (        (
             ( )      ( )          (
      (       Y        Y          ( )
     ( )     |"|      |"|          Y
      Y      | |      | |         |"|
     |"|     | |.-----| |---.___  | |
     | |  .--| |,~~~~~| |~~~,,,,'-| |
     | |-,,~~'-'___   '-'       ~~| |._
    .| |~       // ___            '-',,'.
   /,'-'     <_// // _  __             ~,\\
  / ;     ,-,     \\\\_> <<_' ____________;_)
  | ;    {(_)} _,      ._>>`'-._          |
  | ;     '-'\_\/>              '-._      |
  |\ ~,,,      _\__            ,,,,,'-.   |
  | '-._ ~~,,,            ,,,~~ __.-'~ |  |
  |     '-.__ ~~~~~~~~~~~~ __.-'       |__|
  |\         `'----------'`           _|
  | '=._                         __.=' |
  :     '=.__               __.='      |
   \         `'==========='`          .'
    '-._                         __.-'
        '-.__               __.-'
             `'-----------'`

------------------------------------------------
HAPPY BIRTHDAY!
```
"""

                        # birthday = """```
                      # █▄█ ▄▀▄ █▀▄ █▀▄ █▄█
                      # █▀█ █▀█ █▀▀ █▀▀ ░█
                      # 🄱 🄸 🅁 🅃 🄷 🄳 🄰 🅈

                        #        )\\
                        #       (__)
                        #        /\\
                        #       [[]]
                        #    @@@[[]]@@@
                     # @@@@@@@@@[[]]@@@@@@@@@
                 # @@@@@@@      [[]]      @@@@@@@
             # @@@@@@@@@        [[]]        @@@@@@@@@
            # @@@@@@@           [[]]           @@@@@@@
            # !@@@@@@@@@                    @@@@@@@@@!
            # !    @@@@@@@                @@@@@@@    !
            # !        @@@@@@@@@@@@@@@@@@@@@@        !
            # !              @@@@@@@@@@@             !
            # !             ______________           !
            # !             HAPPY BIRTHDAY           !
            # !             --------------           !
            # !!!!!!!                          !!!!!!!
                 # !!!!!!!                !!!!!!!
                     # !!!!!!!!!!!!!!!!!!!!!!!
# ```
# """
                        message = await channel.send(birthday)
                        await asyncio.sleep(3)
                        # message = await channel.send("Now let's speed things up a bit.")
                        # await asyncio.sleep(10)

                        # for j in range(100):
                        #     msg = ""
                        #     for i in range(300):
                        #         counter += 1
                        #         msg += str(counter) +  '\n'
                        #         if (counter >= 6969):
                        #             message = await channel.send(msg)
                        #             await asyncio.sleep(1)

                        #             # message = await channel.send("")
                        #             # await asyncio.sleep(7)
                        #             sys.exit()

                        #     message = await channel.send(msg)
                        #     await asyncio.sleep(1)
                        #     # await message.delete()

                        print(channel)

                        # messages = await channel.history(limit=10).flatten()
                        # for message in messages:
                        #     print(str(message.author) + ": "+ message.content)

@client.event
async def on_message(message):
    # if (str(message.guild) == "3207"):
    print("Message Channel" + str(message.channel))
    print(str(message.author) + ": " + str(message.content))

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.loop.create_task(main())
client.run(TOKEN)
