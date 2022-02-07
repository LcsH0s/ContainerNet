#!/usr/bin/env python
# encoding: utf-8

TEST_TOKEN = "OTM5OTc0NzE4MDk2ODE4MTc2.YgAprA.k2qt8S6UPH_snFEfGnxbS60TeVQ"

from time import time
import discord
import os


from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option

# Events handling
bot = commands.Bot(command_prefix=commands.when_mentioned_or(
    '!'), activity=discord.Game(name="w/ your little sister"), status=discord.Status.do_not_disturb, intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)

lp_tracker = LolTracker()
lp_tracker.track()


@bot.event
async def on_ready():
    print("\n<Connection Established>\n<Logged in as {0}>\n".format(bot.user))


# Command handling


@slash.slash(
    name="ctf",
    description="Displays upcomming CTFs",
    guild_ids=[858410822590136342]
)
async def ctf(ctx: SlashContext):
    events = getEvents()
    embed = discord.Embed()
    embed.title = "🚩 Upcoming CTF! 🚩"

    name_field_value = ""
    date_field_value = ""
    for i in range(5):
        name_field_value += '{0} - [{1}](https://ctftime.org/event/{2})\n'.format(
            i+1, events[i][1], events[i][0])
        date_field_value += ' {}\n'.format(events[i][2])
    embed.add_field(name='Name', value=name_field_value, inline=True)
    embed.add_field(name='Date', value=date_field_value)
    await ctx.send(embed=embed)


@slash.slash(
    name="elo_graph",
    description="N/A",
    guild_ids=[858410822590136342],
    options=[create_option(
        name='username',
        description='Player username',
        option_type=3,
        required=True,
        choices=[create_choice(name=username, value=username)
                 for username in lp_tracker.get_tracking_name_list()],
    )
    ]
)
async def elo_graph(ctx: SlashContext, username: str):
    tracking_name_list = lp_tracker.get_tracking_name_list()
    if not username in tracking_name_list:
        return await ctx.send('Please enter a valid username from the namesTrackedList')
    else:
        lp_tracker.get_lp_graph(username)
        file = discord.File(
            "/app/logs/figures/{}_lpgraph.png".format(username.replace(' ', '_')), filename="graph.png")
        embed = discord.Embed()
        embed.set_image(url="attachment://graph.png")
        await ctx.send(file=file, embed=embed)


@slash.slash(
    name="elo_add",
    description="N/A",
    guild_ids=[858410822590136342],
    options=[create_option(
        name='username',
        description='Player username',
        option_type=3,
        required=True,
        choices=[create_choice(name=username, value=username)
                 for username in lp_tracker.get_tracking_name_list()],
    )
    ]
)
async def elo_add(ctx, *username):
    global trackingNameList
    username = str(' '.join(username)).lower()
    if not lp_tracker.get_tracking_name_list().__contains__(username):
        lp_tracker.get_tracking_name_list().append(username)
        await ctx.send('Username added to tracking list!')
    else:
        await ctx.send('Username already in tracking list!')


@slash.slash(
    name="elo_ls",
    description="N/A",
    guild_ids=[858410822590136342],
)
async def elo_ls(ctx):
    global trackingNameList
    output = ""
    for name in lp_tracker.get_tracking_name_list():
        output += "{}\n".format(name)
    await ctx.send('Username list : \n' + output)

if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(__file__), 'botToken.token'), 'r') as f:
        DISCORD_TOKEN = f.read()
        f.close()

    bot.run(TEST_TOKEN)