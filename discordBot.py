import discord, logging, json
import random
import os
import requests
import json
import emoji

from discord.ext import commands


bot = commands.Bot(command_prefix='yo ')

greetings = ["Yoooooo, it's all good",
'dog, ',
"Sorry I'm late guys",
"What's big Bryan up to now? ",
'how is it going broes',
"That's baller",
'Let me live (when we play league) ',
'I’m a godddd',
'"let me live"',
'BAAAAAAAAAAAAA',
'dUmBAsS',
'BAAAAAAAAAAAAA',
'Yo I got a coupon for this',
'naw, this will be more v a l u e',
"What's up man?",
"i'd go gay for zac efron",
'brb doing calisthenics',
"that's CRAYYYZEEEE",
"wanna get boba"]

emojis = list(emoji.UNICODE_EMOJI)
token = os.getenv("ALAN_BOT_TOKEN")

print("Initializing Discord bot...")


@bot.event
async def on_ready():
    # Print to console when the bot first runs
    print(bot.user.name)
    print(bot.user.id)
    print("Connected.")


@bot.command(pass_context=True)
async def cat(ctx):
	cat_emojis = ["😹", "😻", "😿", "😽", "😺", "😼", "😾"]
	res = requests.get("https://api.thecatapi.com/v1/images/search")
	res_url = res.json()[0]['url']
	msg = res_url + ' ' + cat_emojis[random.randint(0, len(cat_emojis) - 1)]
	ch = ctx.message.channel
	await ch.send(msg)

@bot.command(pass_context=True)
async def hbd(ctx):
	leftdance = '<:dance1:766504081807376464>'
	rightdance = '<:dance2:766504487140851742>'
	msg = leftdance + 'HAPPY BIRTHDAY ALAN https://docs.google.com/presentation/d/1fxUqEyrbZ7HavY8rlUR3SiXHl1k0VajwwQqEzHuTojk/edit ' + rightdance
	ch = ctx.message.channel
	await ch.send(msg)
	await ctx.message.add_reaction("santa:9a77e13be0f62ffa5f508f3cf50912c2")


@bot.command(pass_context=True)
async def alan(ctx):
    name = ctx.message.author.nick 
    if name is None:
    	name = ctx.message.author

    msg = greetings[random.randint(0, len(greetings) - 1)] + ' ' + str(name) + '! ' + emojis[random.randint(0, len(emojis) - 1)]
    ch = ctx.message.channel
    await ch.send(msg)


@bot.command(pass_context=True)
async def purge(ctx, num):
    msgs = []
    number = int(num)
    await bot.send_message(ctx.message.channel, "Deleting " + str(number) + " messages from client side.")
    async for x in bot.logs_from(ctx.message.channel, limit=number):
        msgs.append(x)
    await bot.delete_messages(msgs)

bot.run(token)
