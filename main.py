import requests, json
import discord
from keep_alive import keep_alive

token = "TOKEN"
client = discord.Client()

@client.event
async def on_ready():
  await       client.change_presence(activity=discord.Game('Weather Forecast ☁️')) 


def get_weather(city):
    try:
        base_url = "http://api.weatherapi.com/v1/current.json?key=WEATHERAPI_KEY"
        complete_url = base_url + "&q=" + city
        response =  requests.get(complete_url) 
        result = response.json()

        city = result['location']['name']
        country = result['location']['country']
        time = result['location']['localtime']
        wcond = result['current']['condition']['text']
        celcius = result['current']['temp_c']
        fahrenheit = result['current']['temp_f']
        fclike = result['current']['feelslike_c']
        fflike = result['current']['feelslike_f']

        embed=discord.Embed(title=f"{city}"'Weather', description=f"{country}", color=0x14aaeb)
        embed.add_field(name="Temprature C° 🌡️", value=f"{celcius}", inline=True)
        embed.add_field(name="Temprature F° 🌡️", value=f"{fahrenheit}", inline=True)
        embed.add_field(name="Wind Condition 🌬️", value=f"{wcond}", inline=False)
        embed.add_field(name="Feels Like F°", value=f"{fflike}", inline=True)
        embed.add_field(name="Feels Like C°", value=f"{fclike}", inline=True)
        embed.set_footer(text='Time 🕧: 'f"{time}")

        return embed
    except:
        embed=discord.Embed(title="No response", color=0x14aaeb)
        embed.add_field(name="Error", value="Oops! Please enter a city name", inline=True)
        return embed

@client.event
async def on_message(message):
    if message.content.lower().startswith("!w"):
            city = message.content[slice(11, len(message.content))].lower()
            result = get_weather(city)
            await message.channel.send(embed=result)

print("Bot has started running")

keep_alive()
client.run(token)
