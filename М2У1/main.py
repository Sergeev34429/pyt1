import discord, random, os, requests
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

@bot.command(description='На случай, если ты захочешь свести счеты каким-нибудь другим способом')
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

@bot.command()
async def mem(ctx):
    k = os.listdir('images')
    img_name = random.choice(k)
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)

def get_animal_image_url():    
    url = 'https://www.searchapi.io/api/v1/search?api_key=rMwjwJ7U4UrjqHnVkeFLmiDH&engine=google_images&q=animals'
    res = requests.get(url)
    data = res.json()
    img1 = data['images']
    img2 = img1[random.randint(0,99)]
    img_link = img2['original']
    return img_link['link']
    
@bot.command('animals')
async def animals(ctx):
    image_url = get_animal_image_url()
    await ctx.send(image_url)

bot.run("MTIwMjYyNzk4MzA0NzkyMTY4NQ.GOoCwV.8LwVLzd5HKBohLZIaJDRF47hSUcaREzHAd1GCI") 