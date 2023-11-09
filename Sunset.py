import telebot
from mcrcon import MCRcon

# Replace these with your actual details
BOT_TOKEN = '6712031118:AAFFMr_4a3gIZZGdtIaAleNup-p3_jWNr00'
MINECRAFT_SERVER_IP = 'mc1112195.fmcs.cloud'
MINECRAFT_RCON_PORT = 25575  # Default RCON port
MINECRAFT_RCON_PASSWORD = '953424'

# Initialize the bot
bot = telebot.TeleBot(BOT_TOKEN)

# Function to set Minecraft server to day
def set_minecraft_to_day():
    with MCRcon(MINECRAFT_SERVER_IP, MINECRAFT_RCON_PASSWORD, MINECRAFT_RCON_PORT) as mcr:
        resp = mcr.command("/time set day")
        return resp

# Handler for "Good morning" message
@bot.message_handler(func=lambda message: message.text.lower() == 'good morning')
def handle_good_morning(message):
    try:
        response = set_minecraft_to_day()
        bot.reply_to(message, f"The day has been set on your Minecraft server. Server response: {response}")
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {e}")

# Polling for messages
bot.polling()
