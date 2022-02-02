import discord
from discord.ext import commands, tasks
from discord import client, Embed

token = 'OTMyMjA3MTQwMzUxOTMwMzkw.YePnjQ.D9M_VQC9t6c**********'

print("Applicazione avviata")

b = commands.Bot(command_prefix="!")
b.remove_command("help")


# https://python.plainenglish.io/how-to-change-discord-bot-status-with-discord-py-39219c8fceea for more on status!
@b.event
async def on_ready():
    await b.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='!help for commands'))


# "A Bit Of error handling for perms, argument and not found commands"
@b.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('Un permesso specifico è richiesto per eseguire questo comando')
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title='**Missing Argument!**', color=discord.Color.red())
        embed.add_field(name="Argomento mancante!", value='Digita !help per  maggiori informazioni', inline=False)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title='**Comando non trovato!**', color=discord.Color.red())
        embed.add_field(name='**Command Not Found**', value='!help per la lista di comandi', inline=False)
        await ctx.send(embed=embed)


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


@b.command(name='scan_database')
async def scan_database(ctx, *, arg):
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


@b.command(name='urlscan')
async def urlscan(ctx, *, url):
    headers = {'API-Key': '***********************', 'Content-Type': 'application/json'}
    data = {"url": url, "visibility": "public"}
    res = requests.post('https://urlscan.io/api/v1/scan/', headers=headers, data=json.dumps(data)).json()
    risultato = res['result']
    embed = discord.Embed(title='**Analisi del link richiesto: **', color=discord.Color.green())
    embed.add_field(name='**Link scansionato** :', value=str(url), inline=False)
    embed.add_field(name='**Link della scansione con urlscan.io**: ', value=risultato, inline=False)
    embed.add_field(name='Crediti: ',
                    value='Scansione effettuata su https://urlscan.io utilizzando le API messe a disposizione dal '
                          'sito. Programma realizzato interamente da DiStRuTtOrE_Tm#6449 ( '
                          'ID=586202654087184384)', inline=False)
    await ctx.send(embed=embed)


@b.command(name='help')
async def help(ctx):
    embed = discord.Embed(title='Aiuto e Crediti', color=discord.Color.red())
    embed.add_field(name='**Lista Comandi**', value='Lista dei comandi del bot!', inline=False)
    embed.add_field(name='!check [Es: !check youtube.com]', value='Esegue una scansione su '
                                                                'https://www.ipqualityscore.com tramite le API '
                                                                'reperibili qui: '
                                                                'https://www.ipqualityscore.com/documentation'
                                                                '/malicious-url-scanner-api/overview. Per utilizzare '
                                                                'questo comando è necessario inserire il **dominio** '
                                                                'del '
                                                                'sito da scansionare. Tutti i risultati e lo '
                                                                'strumento utilizzato '
                                                                'appartengono ad https://www.ipqualityscore.com',
                    inline=False)
    embed.add_field(name='!urlscan [Es: !urlscan https://urlscan.io]', value="Esegue una scansione su "
                                                                             "https://urlscan.io usando le API "
                                                                             "reperibili qui: "
                                                                             "https://urlscan.io/docs/api/. Per "
                                                                             "utilizzare questo comando è necessario "
                                                                             "inserire l'**url** del sito. Tutti i "
                                                                             "risultati e lo strumento utilizzato "
                                                                             "appartengono a https://urlscan.io",
                    inline=False)
    embed.add_field(name='**Crediti:**', value='API di https://www.ipqualityscore.com e https://urlscan.io', inline=False)
    embed.add_field(name='GitHub con il codice del bot: ', value='https://github.com/Lamer-Inc/random-stuff/blob/main'
                                                                 '/anti-scam-bot.py', inline=False)
    embed.add_field(name='Creatore del bot: ', value='DiStRuTtOrE_Tm#6449 (ID=586202654087184384). Non replicare '
                                                     'senza autorizzazione. Le API utilizzate appartengono ai '
                                                     'rispettivi siti. Ogni uso è a puro fine informativo.',
                    inline=False)
    embed.add_field(name='Per finire...', value="Questo progetto nasce con l'idea di rendere Discord un po' più "
                                                "sicuro. Ogni risultato è puramente informativo e le scansioni sono "
                                                "effettuate dai rispettivi siti. DiStRuTtOrE_Tm#6449 non si assume "
                                                "alcuna responsabilità per un utilizzo sbagliato del bot. Bot a solo "
                                                "fine informativo, senza scopo di lucro.", inline=False)
    embed.add_field(name='Differenza fra dominio e url: ', value='https://www.sistrix.it/chiedi-a-sistrix/ottimizzazione-onpage/qual-e-la-differenza-tra-url-dominio-sottodominio-nome-host-ecc/', inline=False)
    await ctx.send(embed=embed)


b.run(token)

#NOT COMPLETED YET, DO NOT REPOST WITHOUT CONSENS

#https://urlscan.io
#https://www.ipqualityscore.com

#ALL API USED ARE OF THE RESPECTIVE OWNERS. DO NOT USE WITHOUT CONSENS
