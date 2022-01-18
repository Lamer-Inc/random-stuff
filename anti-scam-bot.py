import discord
from discord.ext import commands, tasks
from discord import client, Embed

token = 'OTMyMjA3MTQwMzUxOTMwMzkw.YePnjQ.D9M_VQC9t6c**********'

print("Applicazione avviata")

b = commands.Bot(command_prefix="!")


@b.command(name='report')
async def report(ctx, *, url):
    channel_to_scan = await b.fetch_channel(932337902078292050)
    await channel_to_scan.send(str(ctx.message.author) + ' reported the following url: ' + url)


owner_id = 586202654087184384

scam_link = []


@b.command(name='add_link')
async def add_link(ctx, *, arg):
    if ctx.author.id == owner_id:

        if arg in scam_link:
            await ctx.send('Link have been previously reported')
        else:
            scam_link.append(arg)
            channel_with_reported_link = await b.fetch_channel(930511461187452998)
            await channel_with_reported_link.send(arg)
    else:
        await ctx.send('You cannot use this command, contact the bot owner')


@b.command(name='scan')
async def scan(ctx, *, arg):
    if arg in scam_link:
        await ctx.send('Link is in ours scam link database, please pay attention!')
    else:
        await ctx.send('Link is not in the scam link database, but still could be dangerous. Do a VirusTotal scam '
                       'before using it')


#Comando per scansionare link direttamente tramite il bot su Discord. Riferirsi a ipqualityscore per qualsiasi informazione o utilizzo. Per funzionare, necessita di un'API registrata.
@b.command(name='check')
async def check(ctx, *, arg):
    link = 'https://ipqualityscore.com/api/json/url/******************/'
    link_to_scan = str(arg)
    json_url = link + link_to_scan
    result = requests.get(json_url).json()
    stato = result['message']
    unsafe = result['unsafe']
    #ip = result['ip_address']
    spam = result['spamming']
    pishing = result['phishing']
    suspect = result['suspicious']
    adult = result['adult']
    risk = result['risk_score']
    embed = discord.Embed(title='**Analisi del link richiesto: **', color=discord.Color.green())
    embed.add_field(name='**Link scansionato** :', value=str(arg), inline=False)
    embed.add_field(name='Stato della richiesta: ', value=stato, inline=False)
    embed.add_field(name='**È pericoloso**? (True/False)', value=unsafe, inline=False)
    embed.add_field(name='Spam link(True/False): ', value=spam, inline=False)
    embed.add_field(name='Phishing link(True/False): ', value=pishing, inline=False)
    embed.add_field(name='Link Sospetto(True/False): ', value=suspect, inline=False)
    embed.add_field(name='Link a sito per adulti(True/False): ', value=adult, inline=False)
    embed.add_field(name='Livello di rischio: ', value=risk, inline=False)
    embed.add_field(name='**Crediti**: ', value='Programma realizzato interamente da DiStRuTtOrE_Tm#6449 ('
                                                'ID=586202654087184384) usando le fantastiche api di '
                                                'https://www.ipqualityscore.com', inline=False)
    await ctx.send(embed=embed)


b.run(token)

#NOT COMPLETED YET, DO NOT REPOST WITHOUT CONSENS
