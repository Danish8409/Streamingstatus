import discord, os, keep_alive, asyncio, datetime, pytz, random

from discord.ext import tasks, commands

client = commands.Bot(command_prefix=':', self_bot=True)


@client.event
async def ch_pr():
  await client.wait_until_ready()

  statuses = os.getenv("STATUS")

  while not client.is_closed():

    status = random.choice(statuses)

    await client.change_presence(activity=discord.Streaming(name=status, url="https://www.twitch.tv/Scoooolzs"))

    await asyncio.sleep(os.getenv("STATUS_DELAY"))

client.loop.create_task(ch_pr())



keep_alive.keep_alive()
client.run(os.getenv("TOKEN"), bot=False)
