# Imports modules
import discord
from discord.utils import get
import random
import os
import re
from webserver import keep_alive
from discord.ext import commands


# Gets the token environment variable
TOKEN = os.environ.get("token")
# Enables the client with the prefixes "!woof" and !meow"
client = commands.Bot(command_prefix=("!woof ", "!meow "))

# Tells me the bot is ready
@client.event
async def on_ready():
    print("Bot is ready")
    await client.change_presence(
        status=discord.Status.online, activity=discord.Game("!woof _help/!meow _help")
    )


# Flips a coin
@client.command()
async def flipacoin(ctx):
    randomnumber = random.randint(1, 2)
    rn2 = random.randint(1, 2)
    if randomnumber == 1 and rn2 == 1:
        await ctx.send(f"The coin says heads, woof!")
    elif randomnumber == 1 and rn2 == 2:
        await ctx.send(f"The coin says heads, meow!")
    elif randomnumber == 2 and rn2 == 1:
        await ctx.send(f"The coin says tails, woof!")
    else:
        await ctx.send(f"The coin says tails, meow!")


# Simulates a magic 8ball
@client.command(aliases=["8ball"])
async def _8ball(ctx, *, question):
    answers = [
        "Not a chance, meow.",
        "Not a chance, woof.",
        "Of course, woof!",
        "Of course, meow!",
        "Definitely, woof!",
        "Definitely, meow!",
        "Definitely not, woof.",
        "Definitely not, meow.",
        "Why wouldn't that happen, woof!",
        "Why wouldn't that happen, meow!",
        "Nope, woof.",
        "Nope, meow.",
        "Yup, woof!",
        "Yup, meow!",
    ]
    await ctx.send(random.choice(answers))


# Tells you the commands
@client.command()
async def _help(ctx):
    embed = discord.Embed(title="Commands", colour=discord.Colour.red())
    embed.set_image(
        url="https://pbs.twimg.com/profile_images/1262300939614068737/DKw5Fmbn_400x400.jpg"
    )
    embed.add_field(
        name="!woof 8ball (question)/!meow 8ball (question)",
        value="Simulates a magic 8ball",
        inline=False,
    )
    embed.add_field(
        name="!woof flipacoin/!meow flipacoin", value="Flips a coin", inline=False
    )
    embed.add_field(
        name="!woof ispretty (user)/!meow ispretty (user)",
        value="Says (user) is pretty",
        inline=False,
    )
    embed.add_field(
        name="!woof isugly (user)/!meow isugly (user)",
        value="Says (user) is ugly",
        inline=False,
    )
    embed.add_field(
        name="!woof isgay (user)/!meow isgay (user)",
        value="Says (user) is gay",
        inline=False,
    )
    embed.add_field(
        name="!woof feedback (your feedback)/!meow feedback (your feedback)",
        value="Emails the developer of this bot your feedback!",
        inline=False,
    )
    await ctx.send(embed=embed)


# Calls someone pretty
@client.command()
async def ispretty(ctx, member: discord.Member):
    gin = get(ctx.guild.members, name="Gin")
    if member == gin:
        mow = random.randint(1, 2)
        if mow == 1:
            await ctx.send("Oh, you think so? Thanks, woof!")
        else:
            await ctx.send("Oh, you think so? Thanks, meow!")
    else:
        await ctx.send(
            f"{ctx.message.author.mention} thinks {member.mention} is pretty!"
        )


# Calls someone ugly
@client.command()
async def isugly(ctx, member: discord.Member):
    gin = get(ctx.guild.members, name="Gin")
    if member == gin:
        mow = random.randint(1, 2)
        if mow == 1:
            await ctx.send("That's rude, woof.")
        else:
            await ctx.send("That's rude, meow.")
    else:
        await ctx.send(f"{ctx.message.author.mention} thinks {member.mention} is ugly!")


# Lets you know how to send me feedback
@client.command()
async def feedback(ctx):
    mow = random.randint(1, 2)
    if mow == 1:
        await ctx.send(
            "Email me (donkeyride0728@gmail.com) to send your feedback, woof!"
        )
    else:
        await ctx.send(
            "Email me (donkeyride0728@gmail.com) to send your feedback, meow!"
        )


# Kicks someone if the command user has permissions to use the command
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    if reason != None:
        await ctx.send(
            f"{member.mention} has been kicked, woof! Here's the reason, meow: {reason}"
        )
    else:
        await ctx.send(
            f"{member.mention} has been kicked, woof! Here's the reason, meow: No reason specified"
        )


# Bans someone if the command user has permissions to use the command
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    mow = random.randint(1, 2)
    await member.ban(reason=reason)
    if reason != None:
        if mow == 1:
            await ctx.send(f'{member.mention} has been banned for: "{reason}", woof!')
    else:
        await ctx.send(f'{member.mention} has been banned for: "{reason}", meow!')


# Calls someone gay
@client.command()
async def isgay(ctx, member: discord.Member):
    await ctx.send(f"{ctx.message.author.mention} thinks {member.mention} is gay!")


# The code below is just error handling
@_8ball.error
async def _8ballerror(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            "Oh no, there's a command error, woof! Next time, make sure you enter the question, meow!"
        )


@isgay.error
async def isgayerror(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            "Oh no, there's a command error, woof! Next time, make sure to mention somebody, meow!"
        )


@ispretty.error
async def isprettyerror(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            "Oh no, there's a command error, woof! Next time, make sure to mention somebody, meow!"
        )


@isugly.error
async def isuglyerror(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            "Oh no, there's a command error, woof! Next time, make sure to mention somebody, meow!"
        )


@kick.error
async def kick_error(ctx, error):
    mow = random.randint(1, 2)
    if isinstance(error, commands.MissingPermissions):
        if mow == 1:
            await ctx.send("You don't have permissions to do that, woof!")
        else:
            await ctx.send("You don't have permissions to do that, meow!")


@ban.error
async def ban_error(ctx, error):
    mow = random.randint(1, 2)
    if isinstance(error, commands.MissingPermissions):
        if mow == 1:
            await ctx.send("You don't have permissions to do that, woof!")
        else:
            await ctx.send("You don't have permissions to do that, meow!")


# If someone says a certain message, it will react with a heart.
@client.event
async def on_message(message):
    emoji = client.get_emoji(882008386663772231)
    if (
        re.match("sara", message.content.lower())
        or re.match("chidouin", message.content.lower())
        or re.match("joe", message.content.lower())
        or re.match("tazuna", message.content.lower())
    ):
        await message.add_reaction(emoji)
    await client.process_commands(message)


# More error handling
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(
            "Oh no, there's a command error, woof! That command doesn't exist, meow."
        )


# Keeps the bot online
keep_alive()

# Runs the bot
client.run(TOKEN)
