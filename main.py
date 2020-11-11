'''
Author: Deeshan Sharma
Date Created: October 20, 2020
Purpose: Multi purpose Bot for Discord to serve all the functionality offered by MEE6 and YAGPDB Bots (will be expanding more further).
'''

import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.all()

# Enter your token in the same directory in 'token.env' file
load_dotenv('token.env')
TOKEN = os.getenv('DISCORD_TOKEN')

# Give your bot your own prefix here
bot = commands.Bot(command_prefix='RED ', intents=intents)

# Add your custom greeting messages in the list
greetings = ['Welcome', 'Hello and welcome', 'Hello there.! How you doing..?']

# On bot starting successfully
@bot.event
async def on_ready():
    print(f"Ready {bot.user.name}")

# Welcome Message to new members
@bot.event
async def on_member_join(member):
    embed = discord.Embed(title=f"Welcome to {member.guild.name}..!", color=random.randint(0, 0xffffff) , description=f"{random.choice(greetings)} \n\n Member #{member.guild.member_count}")
    embed.set_thumbnail(url=f"{member.avatar_url}")
    dm = f'Hello and welcome to {member.guild.mention}..! Please go through these simple rules here <#767386813114351636> and make sure you follow them. Have Fun and enjoy full on..!' # Change with your channel id
    msg = f'Hello {member.mention}... How you doing..?'
    channel = bot.get_channel(767307155317325848) # Change with your channel id
    await channel.send(msg, embed=embed)
    await member.send(dm)

# Leaving Log for the server members
@bot.event
async def on_member_remove(member):
    msg = f'{member.mention} left the server'
    channel = bot.get_channel(768746759278297089) # Change with your channel id
    await channel.send(msg)

# Kick command
@bot.command(name='kick', help='Command to Kick a Member can be used by Admin only.')
@commands.has_guild_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason='Not Specified'):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} has been kicked from the Server.')

# Kick command error handling
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CommandError):
        await ctx.send(error)

# Ban command
@bot.command(name='ban', help='Command to Ban a Member can be useed by Admin only.')
@commands.has_guild_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *, reason='Not Specified'):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been banned from the Server.')

# Ban command error handling
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.CommandError):
        await ctx.send(error)

# Message cleaning command
@bot.command(name='clean', help='Used to clear the messages of a particular channel (max 100) can be used by Moderators')
# @commands.has_permissions(manage_messsage=True)
async def clean(ctx, number):
    number = int(number)
    msgs = await ctx.channel.history(limit=number).flatten()
    await ctx.channel.delete_messages(msgs)
    await ctx.send(f'Deleted {number} messages.', delete_after=3)

bot.run(TOKEN)