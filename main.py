import os
import discord
import random
from keep_alive import keep_alive
 

intents = discord.Intents().all()
client = discord.Client(intents=intents);

@client.event
async def on_ready():
    print(f'{client.user} is now running!')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  # Check if the message contains the word "hello"
  if "hello" in message.content.lower():
    await message.channel.send("Hi there!")

  # Check if the message contains the word "bye"
  if "bye" in message.content.lower():
    await message.channel.send("Goodbye!")

    
  # Check if the message starts with the command "/roll"
  if message.content.lower().startswith("/roll"):
    # Split the message into a list of words
    words = message.content.lower().split()

    # Set the default upper bound to 6
    upper_bound = 6

    # Check if there is a second word in the list
    if len(words) >= 2:
      # Check if the second word is a valid integer
      if words[1].isdigit():
        # Convert the second word to an integer and use it as the upper bound
        upper_bound = int(words[1])

    # Generate a random number between 1 and the upper bound
    roll = random.randint(1, upper_bound)
    await message.channel.send(f"You rolled a {roll}!")
  
keep_alive()
my_secret = os.environ['DISCORD_BOT_SECRET']
client.run(my_secret)
