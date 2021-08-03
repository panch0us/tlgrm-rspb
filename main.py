import telegram, my_token
TOKEN = my_token.my_token
bot = telegram.Bot(token=TOKEN)
print(bot.get_me())
