# bot.py
import os
import requests
import discord
from dotenv import load_dotenv
import json

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
url = 'https://danbooru.donmai.us'
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'ping!': #test
        response = 'pong!'
        await message.channel.send(response)

    if 'addle' in message.content:
        response = 'Nice Addle Koneko!' #pepelaugh
        await message.channel.send(response)

    if message.content == '!mommy': #gets an image of y'shtola
        big_url = url + '/posts/random.json?tags=y%27shtola_rhul'


        j = requests.get(big_url).json()

        response = j["file_url"]

        await message.channel.send(response)

    if message.content == '!megamommy': #gets an image of y'shtola drawn by club3
        big_url = url + '/posts/random.json?tags=y%27shtola_rhul+club3+&z=5'


        j = requests.get(big_url).json()

        response = j["file_url"]

        await message.channel.send(response)

    if message.content == '!mommycount': #returns the number of y'shtola posts on danbooru
        counts_url = url + '/counts/posts.json?tags=y%27shtola_rhul'
        j_counts = requests.get(counts_url).json()
        count = j_counts["counts"]["posts"]

        response = "There are " + str(count) + " Y'shtola posts on Danbooru"
        await message.channel.send(response)

    if message.content.startswith("!getpost"): #gets a post with the indicated tags ( up to 2 tags, format: !getpost tag tag )

        inter_url = url + "/posts/random.json"


        inter_url = inter_url + "?tags="
        x = message.content.split(" ")


        for tag in x:
            if tag != '!getpost':
                inter_url = inter_url + tag + "+"

        j = requests.get(inter_url).json()


        if len(x) > 3:
            response = "Can only use up to 2 tags"
        else:
            response = j["file_url"]

        await message.channel.send(response)






client.run(TOKEN)




