import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('ODA1NTU0NjA4NzA5NTY2NTE1.YBclMQ.Uy5ZfKDvoS4hSb8G1oVcuDRktQY')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Video Games and General!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return


    responses = [
        'Hello there.',
        'Whats up!',
        'Hi, how are you.',
        'Yo'
    ]

    jokes = [
        'why did the chicken cross the road? because the cross walk was broken.',
        'why dont pirates know they alphabet? because they always get lost at c'
    ]

    if message.content == '!pizza':
        response = 'https://www.google.com/maps/search/pizza+hut+near+me/'
        await message.channel.send(response)

    if message.content == '!hi':
        response = random.choice(responses)
        await message.channel.send(response)

    if message.content == '!joke':
        response = random.choice(jokes)
        await message.channel.send(response)

    if message.content == '!commands':
        response = '!hi - no need to explain \n!joke - for a joke\n!pizza - for directions to the nearest pizza hut'
        await message.channel.send(response)


client.run('ODA1NTU0NjA4NzA5NTY2NTE1.YBclMQ.Uy5ZfKDvoS4hSb8G1oVcuDRktQY')
