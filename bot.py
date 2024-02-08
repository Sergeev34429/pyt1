from bot_logic import gen_pass, gen_coiny, gen_emoji
import discord

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("сквазимабзабза")
    elif message.content.startswith('кто ты'):
        await message.channel.send("я Кубо-шлёпа (его он создал..)")
    elif message.content.startswith('!пароль'):
        await message.channel.send(gen_pass(7))
    elif message.content.startswith('!игра'):
        await message.channel.send(gen_coiny())
    elif message.content.startswith('?игра'):
        await message.channel.send(gen_emoji())
    elif  message.content.startswith('$heh123456'):
        if len(message.content) > 4:
            count_heh = int(message.content[4:])
        else:
            count_heh = 5
        await message.channel.send("he" * count_heh)
    else:
        await message.channel.send(message.content)

client.run("MTIwMjYyNzk4MzA0NzkyMTY4NQ.GOoCwV.8LwVLzd5HKBohLZIaJDRF47hSUcaREzHAd1GCI")