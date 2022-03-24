# bot.py
import os
import requests
import discord
from dotenv import load_dotenv
import json
import base64

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

    if message.content == '!help':  # help command

        response = "!help - you just used this command \n!mommy - gets an image of y'shtola from danbooru \n!megamommy - gets an image of y'shtola from danbooru drawn by club3 \n!mommycount - lists the number of y'shtola posts on danbooru \n!danbooru - gets an image from danbooru with the specified tags up to 2 in the following format: !danbooru tag tag \n!e621 - gets an image from e621 with the specified tags (can do more than 2) in the following format: !e621 tag tag\n!b64 - base64 decoder \n \nTroubleshoot - if the bot doesn't send an image then it likely came across image that requires a login to view. I will not be fixing this"
        await message.channel.send(response)

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

    if message.content.startswith("!danbooru"): #gets a post with the indicated tags ( up to 2 tags, format: !danbooru tag tag )

        inter_url = url + "/posts/random.json"


        inter_url = inter_url + "?tags="
        x = message.content.split(" ")


        for tag in x:
            if tag != '!danbooru':
                inter_url = inter_url + tag + "+"

        j = requests.get(inter_url).json()


        if len(x) > 3:
            response = "Can only use up to 2 tags"
        else:
            response = j["file_url"]

        await message.channel.send(response)

    if message.content.startswith("!b64"): #b64 decoder
        encoded = message.content.split(" ")
        buildResponse = ""
        for b64String in encoded[1:]:
            buildResponse += str(base64.b64decode(b64String))
            buildResponse = buildResponse[2:len(buildResponse)-1]
        await message.channel.send(buildResponse)
        

    if message.content.startswith("!e621"): #gets a post with the indicated tags from e621 ( format: !e621 tag tag... )
        headers = {"User-Agent": "Y'shtola Lewd Bot"} #replace this if your bot name is different
        inter_url = 'https://e621.net/posts/random.json'


        inter_url = inter_url + "?tags="
        x = message.content.split(" ")


        for tag in x:
            if tag != '!e621':
                inter_url = inter_url + tag + "+"

        j = requests.get(inter_url, headers=headers).json()



        response = j["post"]["file"]["url"]


        await message.channel.send(response)








client.run(TOKEN)




