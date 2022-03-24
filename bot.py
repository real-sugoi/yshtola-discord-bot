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

    if message.content == 'ping!':
        response = 'pong!'
        await message.channel.send(response)

    if 'addle' in message.content:
        response = 'Nice Addle Koneko!'
        await message.channel.send(response)

    if message.content == '!mommy':
        big_url = url + '/posts/random.json?tags=y%27shtola_rhul'


        j = requests.get(big_url).json()

        response = j["file_url"]

        await message.channel.send(response)

    if message.content == '!megamommy':
        big_url = url + '/posts/random.json?tags=y%27shtola_rhul+club3+&z=5'


        j = requests.get(big_url).json()

        response = j["file_url"]

        await message.channel.send(response)

    if message.content == '!mommycount':
        counts_url = url + '/counts/posts.json?tags=y%27shtola_rhul'
        j_counts = requests.get(counts_url).json()
        count = j_counts["counts"]["posts"]

        response = "There are " + str(count) + " Y'shtola posts on Danbooru"
        await message.channel.send(response)

client.run(TOKEN)




