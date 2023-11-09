# Minecraft Server Day Setter Telegram Bot

This Python script creates a Telegram bot that listens for the message "Good morning" and sets the time to day on a Minecraft server hosted on server.pro.

## Features

- Listens for "Good morning" message on Telegram
- Sets the Minecraft server time to day

## Requirements

- Python 3.6 or higher
- `python-telegram-bot` package
- `mcrcon` package
- Access to your Minecraft server with RCON enabled

## Setup

1. Install the required Python packages using pip:

```bash
pip install python-telegram-bot mcrcon

Usage

Send "Good morning" to your Telegram bot, and it will set the time to day on your Minecraft server.
Disclaimer

Make sure you have the proper permissions to interact with the Minecraft server.


**IMPORTANT:**
- Replace `YOUR_BOT_TOKEN`, `your_minecraft_server_ip`, `your_rcon_port`, and `your_rcon_password` with your actual bot token and Minecraft server details.
- Ensure that your Minecraft server has RCON enabled and is accessible from the location you run this script.
- This script and guide assume a basic level of familiarity with Python programming, using the command line, and managing Minecraft servers.
- Always check with the server administrator or hosting provider to ensure you're allowed to interact with the server programmatically.

This script is a basic example and does not include error handling, logging, or advanced features. It should be used as a starting point and customized according to your needs and the server's requirements.



