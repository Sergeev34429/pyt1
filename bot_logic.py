import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password
def gen_coiny():
    coin = random.randint(0,1)
    if coin == 0:
        return "Орёл.."
    else:
        return "Решка.."
def gen_emoji():
    emo = random.randint(0,4)
    if emo == 0:
        return "☠️"
    elif emo == 1:
        return "💖"
    elif emo == 2:
        return "🗿"
    elif emo == 3:
        return "🤓"
    else:
        return "🤪🚽"
    
    