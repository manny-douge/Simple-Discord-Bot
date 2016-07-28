import discord
import asyncio
import random
import requests

if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')

leaguedict={
     }

bot = discord.Client()


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "my summoner name is " in message.content.lower():
        name = message.author.name.lower()
        lolname=message.content.lower()[20:]
        leaguedict[name]=lolname

    if "league id" in message.content.lower():
        name=message.author.name.lower()
        summoner=leaguedict[name]
        r=requests.get('https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/'+summoner+'?api_key=RGAPI-0E9F7F62-AE11-44E6-8ECE-D76945CB4EB0')
        requestJSON=r.json()
        id=(requestJSON[summoner]['id'])
        await bot.send_message(message.channel, 'Your summoner ID is '+str(id), tts=False)



    if '!casual' in message.content.lower():
        await bot.send_message(message.channel,
                               "http://i1.kym-cdn.com/entries/icons/original/000/013/017/casual.jpg", tts=False)
    if '!troll' in message.content.lower():
        await bot.send_message(message.channel, "http://puu.sh/k0Hki.jpg",
                               tts=False)
    if 'hey' in message.content.lower():
        mentioned=message.mentions
        if not mentioned:
            return None
        await bot.send_message(message.channel,"https://openclipart.org/image/2400px/svg_to_png/65653/Display-17-Digital-Hello.png",
                               tts=False)
        for x in range(len(mentioned)):
            await bot.send_message(message.channel, 'Hey %s' %(mentioned[x].name), tts=True)
            x += 1
bot.run('token')