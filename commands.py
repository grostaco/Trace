import discord
from discord.ext import commands

client = commands.Bot(command_prefix='t!')
client.remove_command('help')


def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()


@client.event
async def on_ready():
    print('Bot is ready')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command()
async def help(ctx):
    embed = discord.Embed(title="Trace's available commands",
                          description='',
                          colour=discord.Color.blue()
                          )

    #embed.set_author(name=client.user.name, icon_url='https://discordpy.readthedocs.io/en/latest/_images/snake.png')
    embed.set_footer(text='Hope this helps!', icon_url='https://pbs.twimg.com/media/DcEu95UWAAIvoWP.png')
    embed.set_image(url='https://pbs.twimg.com/media/DcEu9_wW0AAE2VK.png')
    embed.set_thumbnail(url='https://pbs.twimg.com/media/DcEu9_bXcAAQ-Cv.png')

    embed.add_field(name="Find source  :face_with_raised_eyebrow: ", value="t!source <picture>")
    embed.add_field(name="Top 5 source found!  :pencil: ", value="t!top", inline=False)

    await ctx.send(embed=embed)

@client.command()
async def announce(ctx, channel: discord.TextChannel, *, msg):
    await ctx.send('Success!')
    await channel.send(f'{msg}')


@client.command()
async def add(ctx):
    if ctx.author.bot:
        return
    for a in ctx.attachments:
        for i in ['3g2','3gp','amv','asf','avi','drc','f4a','f4b','f4p','f4v','flv','gif','gifv','m2ts','m2v','m4p','m4v','mkv','mng','mov','mp2','mp4','mpe','mpeg','mpg','mpv','mts','mxf','nsv','ogg','ogv','qt','rm','rmvb','roq','svi','ts','vob','webm','wmv','yuv']:
            if a.filename[-len(i)-1:]==f'.{i}':
                # add to database/directory after converting into histogram?
                return

@client.command()
async def source(ctx):
    if ctx.author.bot:
        return
    for a in ctx.attachments:
        for i in ['jpg', 'png', 'jpeg']:
            if a.filename[-len(i)-1:]==f'.{i}':
                # compare histogram?
                return


client.run(token)


