
import discord
from os import environ


from discord.activity import create_activity
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option

TEST_TOKEN = environ['BOT_TOKEN']

# Events handling
bot = commands.Bot(command_prefix=commands.when_mentioned_or(
    '!'), activity=discord.Game(name="w/ your little sister"), status=discord.Status.do_not_disturb, intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)


@bot.event
async def on_ready():
    print("\n<Connection Established>\n<Logged in as {0}>\n".format(bot.user))


# Command handling

@slash.slash(
    name="ctf",
    description="Displays upcomming CTFs",
    guild_ids=[858410822590136342]
)
async def ping(ctx: SlashContext):
    ctx.send("pong")

if (__name__ == '__main__'):
    bot.run(TEST_TOKEN)
