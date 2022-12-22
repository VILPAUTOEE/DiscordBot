import os
from replit import db
import discord
from discord.ext import commands
import restart
from keep_alive import keep_alive
import random
from datetime import datetime as dt
import requests
import html
import datetime
from lists import swear, other_swear, meme_list, scores
from copyPasta import rmsmsg
import json

# List of JSON files to read
json_files = ['scores.json', 'swear.json', 'other_swear.json', 'meme_list.json']

# Initialize empty dictionaries to store the data from each file
scores = []
swear = []
other_swear = []
meme_list = []

# Loop through the list of JSON files
for json_file in json_files:
  
  # Open the JSON file
  with open(json_file, 'r') as f:
    
    # Load the data from the file and store it in the appropriate dictionary
    if json_file == 'scores.json':
      
      scores = json.load(f)
      f.close()
      
    elif json_file == 'swear.json':
      
      swear = json.load(f)
      f.close()
      
    elif json_file == 'other_swear.json':
      
      other_swear = json.load(f)
      f.close()
      
    elif json_file == 'meme_list.json':
      
      meme_list = json.load(f)
      f.close()


print(scores)
print(swear)
print(other_swear)
print(meme_list)

random.seed(dt.now().timestamp())


#bot = discord.Bot()
bot = commands.Bot()

servers = [1005731721079165008, 1054778571882770453] #server id
trivia_data = {}

@bot.event
async def on_ready():
  
  print(f'{bot.user} is now running!')
  await bot.change_presence(activity=discord.Game("/help"))


@bot.slash_command(guild_ids=servers, name="2023", description="Tell's what 2023 will come")
async def yearOfTheLinux(ctx):
  
  embed = discord.Embed(
    title="2023",
    description="Year of the Linux desktop",
    color=discord.Colour.blurple(),
    )
  
  embed.set_image(url="https://i.imgur.com/Okbs2oG.jpg")
  await ctx.respond("", embed=embed)


@bot.slash_command(guild_ids=servers, name="kirosana", description="Swears in Finnish")
async def swear123(ctx):
  
  await ctx.respond(random.choice(swear))


@bot.slash_command(guild_ids=servers, name="swear", description="Swears")
async def other_swear123(ctx):
  
  await ctx.respond(random.choice(other_swear))


@bot.slash_command(guild_ids=servers, name="meme", description="Random meme")
async def meme(ctx):
  
  meme = random.choice(meme_list)
  
  if meme.endswith(".jpg") or meme.endswith(".png"):
    
    embed = discord.Embed(
      title="Meme",
      description="Randomly chochen meme",
      color=discord.Colour.blurple(),
      )
    embed.set_image(url=meme)
    await ctx.respond("", embed=embed)
    
  else:
    
    await ctx.respond(meme)

  
@bot.slash_command(guild_ids=servers, name="greet", description="Greets you")
async def greet(ctx):
  
  await ctx.respond("Hello! How are you?")


@bot.slash_command(guild_ids=servers, name="help", description="Shows a list of all commands")
async def help(ctx):
  
  embed = discord.Embed(
    title="Here is a list of available commands:",
    description="/help\n/greet\n/swear\n/kirosana\n/2023\n/meme\n/yesno Question\n/poll Question: option1, option2... \n/roll and optionally a number\n/trivia\n/answer\n/leaderboard\n/weather city, country example. /weather Laukaa, FI",
    color=discord.Colour.blurple(),
    )
  
  embed.set_image(url="https://helperbyte.com/files/questions/42bc13f6-08df-827a-92b5-8390e3cc2c24.png")
  await ctx.respond("Help", embed=embed)


@bot.slash_command(guild_ids=servers, name='roll', description='Roll a die')
async def roll(ctx, dice_sides: int=6):
  
  roll = random.randint(1, dice_sides)
  embed = discord.Embed(title=f"You rolled a {roll}!", color=discord.Colour.blurple())
  await ctx.respond(embed=embed)


@bot.slash_command(guild_ids=servers, name='poll', description='Create a poll')
async def poll(ctx, question: str, options: str):
  
  numbers_to_words = {
    0: '0️⃣',
    1: '1️⃣',
    2: '2️⃣',
    3: '3️⃣',
    4: '4️⃣',
    5: '5️⃣',
    6: '6️⃣',
    7: '7️⃣',
    8: '8️⃣',
    9: '9️⃣',
    10: '🔟'
  } 
  # Split the message into a list containing the question and options

  # Check if the user provided a question and at least one option
  if len(options) >= 2:
    
    # Create the poll message
    poll_message = question + "\n"

    # Split the options by the `,` character
    options = options.split(",")

    for i, option in enumerate(options):
      
      poll_message += f"{i + 1}. {option.strip()}\n"
      
  else:
    
    # If the user didn't provide a question or any options, send an error message
    embed = discord.Embed(title="Error", description="Please provide a question and at least one option for the poll.", color=discord.Colour.red())
    await ctx.respond(embed=embed)
    return

  # Create the embed message
  embed = discord.Embed(title="POLL", description=poll_message, color=discord.Colour.blurple())
  # Send the embed message to the channel
  poll_message2 = await ctx.send("", embed=embed)
  await ctx.respond("‎ ")
  # Add a reaction for each option in the poll
  
  for i in range(1, len(options) + 1):
    
    await poll_message2.add_reaction(str(numbers_to_words[i]))
      

@bot.slash_command(guild_ids=servers, name='yesno', description='Create a yes/no poll')
async def yesno(ctx, *, question: str):
  
  # Create the poll message
  poll_message1 = question
  poll_message = "1. Yes\n2. No\n"

  # Create the embed message
  embed = discord.Embed(title=poll_message1, description=poll_message, color=discord.Color.blurple())
  # Send the embed message to the channel
  poll_message2 = await ctx.send("", embed=embed)
  await ctx.respond("‎ ")
  # Add the thumbs up and thumbs down reactions to the message
  await poll_message2.add_reaction("👍")
  await poll_message2.add_reaction("👎")


@bot.slash_command(guild_ids=servers, name="trivia", description="Gives you a trivia question to answer")
async def trivia(ctx):
  
  # Use the Open Trivia DB API to get a random trivia question
  r = requests.get("https://opentdb.com/api.php?amount=1&type=multiple")
  data = r.json()
  
  if "results" in data:
    
    # Extract the question, correct answer, and incorrect answers from the API response
    question = html.unescape(data["results"][0]["question"])
    correct_answer = html.unescape(data["results"][0]["correct_answer"])
    incorrect_answers = html.unescape(data["results"][0]["incorrect_answers"])
    # Shuffle the list of answers so the correct answer isn't always the last one
    answers = incorrect_answers + [correct_answer]
    random.shuffle(answers)
    # Save the question, correct answer, and answers in the trivia_data dictionary
    trivia_data["question"] = question
    trivia_data["correct_answer"] = correct_answer
    trivia_data["answers"] = answers
  
    # Create a list of numbered choices for the user to choose from
    choices = html.unescape("\n".join(["{}. {}".format(i+1, a) for i, a in enumerate(answers)]))
    # Create an embed object
    embed = discord.Embed(title="Trivia", color=discord.Colour.blurple())
    # Add the question as a field in the embed object
    embed.add_field(name="Question", value=question, inline=False)
    # Add the list of numbered choices as a field in the embed object
    embed.add_field(name="Choices", value=choices, inline=False)
    # Send the embed message
    await ctx.respond(embed=embed)

    
@bot.slash_command(guild_ids=servers, name="answer", description="Submits your answer to the current trivia question")
async def answer(ctx, *, answer):
  
  # Check if there is a current trivia question
  
  if "question" in trivia_data:
    
    # Extract the correct answer and list of answers from the trivia_data dictionary
    correct_answer = trivia_data["correct_answer"]
    answers = trivia_data["answers"]
    
    try:
      
      # Convert the user's response to an integer and use it to get the corresponding answer from the list
      response = int(answer)
      selected_answer = answers[response - 1]
      # Check if the selected answer is correct
      
      if selected_answer == correct_answer:
        
        # Create the embed message for a correct answer
        embed = discord.Embed(title="Correct!", color=discord.Colour.green())
        embed.add_field(name="Answer", value=correct_answer)
        await ctx.respond(embed=embed)
        
        trivia_data.clear()
        user_id = ctx.author.id
        for entry in scores:
          
          if entry[0] == user_id:
            
            # Update the score for the user
            entry[1] += 1
            break
            
        else:
          
          # The user_id was not found in the list, so add a new entry
          scores.append([user_id, 1])
      
        # Serialize the scores dictionary to a JSON string
        # scores_json = json.dumps(scores)
        # Write the JSON string to the scores.json file
          
        with open('scores.json', 'w') as f:
          
          json.dump(scores, f)
            
        f.close()
        
      else:
        
        # Create the embed message for an incorrect answer
        embed = discord.Embed(title="Incorrect", color=discord.Colour.red())
        embed.add_field(name="Correct Answer", value=correct_answer)
        await ctx.respond(embed=embed)
        trivia_data.clear()
        
    except ValueError:
      
      # The user's response could not be converted to an integer
      embed = discord.Embed(title="Invalid Input", color=discord.Colour.orange())
      embed.add_field(name="Error", value="Please select a valid option by typing the number corresponding to your answer.")
      await ctx.respond(embed=embed)
      
  else:
    
    # There is no current trivia question
    embed = discord.Embed(title="Error", description="There is no current trivia question. Use the `/trivia` command to start a new game.", color=discord.Colour.red())
    
    await ctx.respond("", embed=embed)


@bot.slash_command(guild_ids=servers, name="leaderboard", description="Displays the top 10 users with the highest scores")
async def leaderboard(ctx):
  
  # Read the scores from the scores.json file
  with open('scores.json', 'r') as f:
    
    scores = json.load(f)

  # Get a list of (user_id, score) tuples sorted by score in descending order
  sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
  # Get the top 10 scores
  top_scores = sorted_scores[:10]
  # Build the leaderboard message
  leaderboard_message = ""
  
  for i, (user_id, score) in enumerate(top_scores):
    
    # Get the user's name
    user = await bot.fetch_user(user_id)
    user_name = user.name if user else "Unknown User"
    # Add the user's score to the leaderboard message
    leaderboard_message += "**{}**. {}: {}\n".format(i+1, user_name, score)
    
  # Create the embed object
  embed = discord.Embed(title="Top 10 Leaderboard", color=discord.Colour.blurple())
  # Send the embed message
  embed.add_field(name='Leaderboard', value=leaderboard_message)
  await ctx.respond(embed=embed)


@bot.slash_command(guild_ids=servers, name='weather', description='Get the weather for a location')
async def weather(ctx, city, country):
  
  # Make a request to the OpenWeatherMap API to get the weather data for the specified location
  api_key = '886c6e82d2c262ff807565a47a15cd66'
  url = f'https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}'
  r = requests.get(url)
  data = r.json()
  # Check if the API returned an error
  
  if data['cod'] != 200:
    await ctx.respond(f'Error: {data["message"]}')
    return
    
  # Extract the weather data from the API response
  temperature = data['main']['temp'] - 273.15
  weather_description = data['weather'][0]['description']
  humidity = data['main']['humidity']
  wind_speed = data['wind']['speed']
  sunrise_timestamp = data['sys']['sunrise']
  sunrise = datetime.datetime.fromtimestamp(sunrise_timestamp).strftime('%H.%M')
  sunset_timestamp = data['sys']['sunset']
  sunset = datetime.datetime.fromtimestamp(sunset_timestamp).strftime('%H.%M')
  # Send the weather data to the user
  embed = discord.Embed(title='Weather Report', description=city + ", " + country, color=discord.Colour.blurple())
  embed.add_field(name='Temperature', value=f'{temperature:.1f}°C')
  embed.add_field(name='Weather', value=weather_description)
  embed.add_field(name='Humidity', value=f'{humidity}%')
  embed.add_field(name='Wind Speed', value=f'{wind_speed} m/s')
  embed.add_field(name='Sunrise', value=sunrise)
  embed.add_field(name='Sunset', value=sunset)
  # Send the embed to the user
  await ctx.respond(embed=embed)


keep_alive()


try:
  
  TOKEN = os.environ.get("DISCORD_BOT_SECRET")
  bot.run(TOKEN)
  
except discord.errors.HTTPException:
  
  os.system("kill 1")
  restart()
  print("restarting")
  bot.run(TOKEN)
