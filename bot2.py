import discord, random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command(description='На случай, если ты захочешь свести счеты каким-нибудь другим способом11222')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def heads_or_tails(ctx):
    result=['Орёл','Решка']
    await ctx.send(random.choice(result)) 

@bot.command()
async def cube(ctx):
    result=['однёрка','двойка','тройка','четвёрка','пятёрка','шестёрка']
    await ctx.send(random.choice(result)) 

@bot.command()
async def password(ctx, lenn: int):
    pass1= "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(lenn):
        password += pass1[random.randint(0,len(pass1))] 
    await ctx.send(password)

bot.run("MTIwMjYyNzk4MzA0NzkyMTY4NQ.GOoCwV.8LwVLzd5HKBohLZIaJDRF47hSUcaREzHAd1GCI") 
