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


b.run(token)

#NOT COMPLETED YET, DO NOT REPOST WITHOUT CONSENS
