import os
import discord
import random
from keep_alive import keep_alive
 
meme_list = ["https://www.reddit.com/r/linux_memes/comments/wcbkjg/linux_users_whenever_they_interact_with_windows/?utm_source=share&utm_medium=web2x&context=3", "https://i.redd.it/wbbjq9j3nrn61.jpg", "https://i.redd.it/rvenotrgq1x61.jpg", "https://www.reddit.com/r/linuxmemes/comments/ppi87t/haha/?utm_source=share&utm_medium=web2x&context=3", "https://www.reddit.com/r/linuxmemes/comments/qvurau/minecraft/?utm_source=share&utm_medium=web2x&context=3", "https://www.reddit.com/r/linuxmemes/comments/qg3nac/made_it_on_linux/?utm_source=share&utm_medium=web2x&context=3", "https://i.redd.it/aryo9p0vt4p71.png", "https://www.reddit.com/r/linuxmemes/comments/pmble6/can_you_do_that_on_macos_or_windows_no_only_on/?utm_source=share&utm_medium=web2x&context=3", "https://www.reddit.com/r/linuxmemes/comments/po8dm9/thats_basicly_all_oses_in_one_video/?utm_source=share&utm_medium=web2x&context=3", "https://i.redd.it/kpyi19jqiey71.jpg", "https://i.redd.it/qie4ekb7lvn81.png", "https://www.reddit.com/r/linuxmemes/comments/hwpmni/linux_gaming_recently/?utm_source=share&utm_medium=web2x&context=3", "https://i.redd.it/c4koha23q3f51.jpg", "https://i.redd.it/d015wdvlxqw71.png"]

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

  if message.content.lower().startswith("!2023"):
    await message.channel.send("Year of the Linux desktop!!!")

  if message.content.lower().startswith("!meme"):
    await message.channel.send(random.choice(meme_list))
  
  # Check for the !greet command
  if message.content.lower().startswith("!greet"):
    await message.channel.send("Hello! How are you today?")

  # Check for the !help command
  if message.content.lower().startswith("!help"):
    await message.channel.send("Here is a list of available commands: !greet, !help, !yesno Question, !poll Question: option1, option2... , !roll")

  
  # Check for the !yesno command
  if message.content.lower().startswith("!yesno"):
    # Split the message into a list containing the command and the rest of the message
    words = message.content.lower().split(maxsplit=1)

    # Check if the user provided a question
    if len(words) >= 2:
        # Create the poll message
        poll_message = "**POLL:** " + words[1] + "\n\n"
        poll_message += "1. Yes\n2. No\n"

        # Send the poll message to the channel
        poll_message = await message.channel.send(poll_message)
        # Add the thumbs up and thumbs down reactions to the message
        await poll_message.add_reaction("👍")
        await poll_message.add_reaction("👎")
    else:
        # If the user didn't provide a question, send an error message
        await message.channel.send("Please provide a question for the poll.")

  if message.content.lower().startswith("!poll"):
    # Split the message into a list containing the command and the rest of the message
    words = message.content.lower().split(maxsplit=1)

    # Check if the user provided a question for the poll
    if len(words) >= 2:
        # Split the rest of the message into a list containing the question and options
        parts = words[1].split(":")

        # Check if the user provided a question and at least one option
        if len(parts) >= 2:
            # Create the poll message
            poll_message = "**POLL:** " + parts[0] + "\n\n"

            # Split the options by the `,` character
            options = parts[1].split(",")

            # Add the options to the poll message
            for i, option in enumerate(options):
                poll_message += f"{i + 1}. {option.strip()}\n"
        else:
            # If the user didn't provide a question or any options, send an error message
            await message.channel.send("Please provide a question and at least one option for the poll.")
            return

        # Send the poll message to the channel
        poll_message = await message.channel.send(poll_message)
        # Add a reaction for each option in the poll
        for i in range(1, len(options) + 1):
            await poll_message.add_reaction(f"{i}:thumbsup:")
            await poll_message.add_reaction(f"{i}:thumbsdown:")
    else:
        # If the user didn't provide a question for the poll, send an error message
        await message.channel.send("Please provide a question for the poll.")
  if message.content.lower().startswith("!roll"):
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
