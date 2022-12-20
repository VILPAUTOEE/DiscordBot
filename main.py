import os
import discord
import random
from keep_alive import keep_alive
import restart

prefix = "?"
allowed_channels = ["bot-test", "botti-koodaus🔒"]

swear = ["Voi helv*tti sun kanssa", "Ei jum*lauta", "P*ska", "P*rkele", "Ei s*atana", "V*ttu Jari", "Hista v*ttu", "Ei v*ttu s*atana k*si p*rkele", "Mä p*nen sun mutsii", "Haista v*ttu", "Haista vesa v*ttu"]

other_swear = ["F*ck you", "Oh sh*t", "Bloody h*ll mate", "Sch*iße", "You son of a b*tch", "A*shole", "F*cking bastard", "B*tch", "F*cking c*nt", "D*ckhead", "I f*ck your mom"]
 
meme_list = ["https://www.reddit.com/r/linux_memes/comments/wcbkjg/linux_users_whenever_they_interact_with_windows/?utm_source=share&utm_medium=web2x&context=3", "https://i.redd.it/wbbjq9j3nrn61.jpg", "https://i.redd.it/rvenotrgq1x61.jpg", "https://www.reddit.com/r/linuxmemes/comments/ppi87t/haha/?utm_source=share&utm_medium=web2x&context=3", "https://www.reddit.com/r/linuxmemes/comments/qvurau/minecraft/?utm_source=share&utm_medium=web2x&context=3", "https://www.reddit.com/r/linuxmemes/comments/qg3nac/made_it_on_linux/?utm_source=share&utm_medium=web2x&context=3", "https://i.redd.it/aryo9p0vt4p71.png", "https://www.reddit.com/r/linuxmemes/comments/pmble6/can_you_do_that_on_macos_or_windows_no_only_on/?utm_source=share&utm_medium=web2x&context=3", "https://www.reddit.com/r/linuxmemes/comments/po8dm9/thats_basicly_all_oses_in_one_video/?utm_source=share&utm_medium=web2x&context=3", "https://i.redd.it/kpyi19jqiey71.jpg", "https://i.redd.it/qie4ekb7lvn81.png", "https://www.reddit.com/r/linuxmemes/comments/hwpmni/linux_gaming_recently/?utm_source=share&utm_medium=web2x&context=3", "https://i.redd.it/c4koha23q3f51.jpg", "https://i.redd.it/d015wdvlxqw71.png"]

intents = discord.Intents().all()
client = discord.Client(intents=intents);

@client.event
async def on_ready():
  print(f'{client.user} is now running!')
  await client.change_presence(activity=discord.Game(prefix + "help"))

@client.event
async def on_message(message):
  username = str(message.author).split('#')[0]
  channel = str(message.channel.name)
  msg = message.content.lower()
  if message.author == client.user:
    return
    
  # Check if the message contains the word "hello"
  if channel in allowed_channels:
    if "hello" in msg or "hi" in msg:
      await message.channel.send("Hi " + username + "!")
      return
      
    # Check if the message contains the word "bye"
    elif "bye" in msg:
      await message.channel.send("Goodbye " + username + "!")
      return
      
    elif "linux" in msg:
      await message.channel.send("""I’d just like to interject for a moment. What you’re refering to as Linux, is in fact, GNU/Linux, or as I’ve recently taken to calling it, GNU plus Linux. Linux is not an operating system unto itself, but rather another free component of a fully functioning GNU system made useful by the GNU corelibs, shell utilities and vital system components comprising a full OS as defined by POSIX.

Many computer users run a modified version of the GNU system every day, without realizing it. Through a peculiar turn of events, the version of GNU which is widely used today is often called Linux, and many of its users are not aware that it is basically the GNU system, developed by the GNU Project.

There really is a Linux, and these people are using it, but it is just a part of the system they use. Linux is the kernel: the program in the system that allocates the machine’s resources to the other programs that you run. The kernel is an essential part of an operating system, but useless by itself; it can only function in the context of a complete operating system. Linux is normally used in combination with the GNU operating system: the whole system is basically GNU with Linux added, or GNU/Linux. All the so-called Linux distributions are really distributions of GNU/Linux!""")
      return
      
    elif msg.startswith(prefix + "2023"):
      await message.channel.send("Year of the Linux desktop!!!")

    elif msg.startswith(prefix + "kirosana"):
      await message.channel.send(random.choice(swear))
    elif msg.startswith(prefix + "swear"):
      await message.channel.send(random.choice(other_swear))
    elif msg.startswith(prefix + "meme"):
      await message.channel.send(random.choice(meme_list))
    
    # Check for the !greet command
    elif msg.startswith(prefix + "greet"):
      await message.channel.send("Hello! How are you today?")
  
    # Check for the !help command
    elif msg.startswith(prefix + "help"):
      await message.channel.send("Here is a list of available commands: " + prefix + "greet, " + prefix + "help, " + prefix + "swear, " + prefix + "kirosana, " + prefix + "2023, " + prefix + "meme, " + prefix + "yesno Question, " + prefix + "poll Question: option1, option2... , " + prefix + "roll and optionally a number.")
  
    
    # Check for the !yesno command
    elif msg.startswith(prefix + "yesno"):
      # Split the message into a list containing the command and the rest of the message
      words = msg.split(maxsplit=1)
  
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
  
    elif msg.startswith(prefix + "poll"):
      # Split the message into a list containing the command and the rest of the message
      words = msg.split(maxsplit=1)
  
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
    elif msg.startswith(prefix + "roll"):
      # Split the message into a list of words
      words = msg.split()
  
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

    else:
      return
      

keep_alive()

try:
  TOKEN = os.environ.get("DISCORD_BOT_SECRET")
  client.run(TOKEN)
except discord.errors.HTTPException:
  os.system("kill 1")
  restart()
  print("restarting")
  client.run(TOKEN)
