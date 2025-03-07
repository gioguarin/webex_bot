import os

from webex_bot.commands.echo import EchoCommand
from webex_bot.webex_bot import WebexBot

# Create a Bot Object
bot = WebexBot(teams_bot_token=os.getenv("MDc5YzNlNzEtMjNmNy00YjgwLTgzMTItN2Y3ZDdkYjIxZmI3ZDNlNmQyOTItOWVl_PF84_a3749315-ae09-4a52-806c-2c3222fa7c2c"),
               approved_rooms=['151a31b0-9895-11ec-baa3-df6b8f84527f'],
               bot_name="Mimir",
               include_demo_commands=True)

# Add new commands for the bot to listen out for.
bot.add_command(EchoCommand())

# Call `run` for the bot to wait for incoming messages.
bot.run()
