# MVP Discord Bot

_**MVP: The only Bot you need..!**_

A Multi-Purpose Bot designed with the vision of having all the required functions and capabilities performed by many other Bots such as MEE6, YAGPDB, etc. So, you only need a single Bot on your Server.

## Objective

The main objective of this bot is to reduce the no of bots required in the server to perform various tasks, so you require only this single multi-purpose bot. Hence the name justifies MVP (Most Valuable Player).

## Features

- Custom Welcome Message
  - On Server
  - Personal Message
- Members Leaving Log on to a Channel
- Basic Moderation Commands
  - Mute
  - Kick
  - Ban

### Features that will be introduced in the near future

- Leveling and Rank System
- Issue resolving Ticket System
- More moderation commands
  - Warn
- Auto-Moderation System with some rules
  - Spamming
  - Invite Links
  - Link Sharing
  - Mass Mention
  - Many More
- Reaction Roles
- Announcement Sharing
- Server Updates such as
  - Warnings
  - Kicks
  - Bans
  - Other Updates

### Not sure about these

- Music
- Games

# Installation & Requirement

- Clone the repo
  - Using HTTPS

      `git clone https://github.com/DeeshanSharma/MVP-Discord-Bot.git`

  - Using SSH

      `git clone git@github.com:DeeshanSharma/MVP-Discord-Bot.git`

- Setup your Virtual Environment 🔵

    `python -m venv .venv`

- Activate your Virtual Environment ⭐
  - Windows (CMD)

      `.venv/Scripts/activate.bat`

  - Linux/macOS

      `source .venv/bin/activate`

- Install using requirements.txt 🟢

    `pip install -r requirements.txt`

OR

- Discord Module

    `pip install discord.py`

- Dotenv Module

    `pip install python-dotenv`

# Usage ⭐

1. Give Bot Administrator Permission
1. Create a file token.env
1. Enter your token as-

    `DISCORD_TOKEN = <your_token>`

1. Replace Channel IDs & Role IDs in the [main.py](main.py) file with your own Server's Channel IDs & Role IDs
1. You can change the Bot Prefix in the [main.py](main.py) to your own custom prefix 🔵

# Future Plans

A full-fledged website for the Bot where the users can manage the Bot in their own Server similar to the other Bots and this code will be in the backend.

# Terminology

⭐ - Very Important

🟢 - Recommended

🔵 - Optional
