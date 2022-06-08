# Weather Discord Bot ☁️
This is a Weather bot for Discord that displays temperature in °F/°C, wind conditions and time 


## Install Directly on a local computer

- Create a [Bot account](https://discordpy.readthedocs.io/en/stable/discord.html) and invite the Bot to a Discord server

- Add `main.py` and `keep_alive.py` to a new repository on [Replit](https://replit.com/)

- Replace `TOKEN` with the Discord Bot token

- The Weather API key can be generated at [Weather API](https://www.weatherapi.com/) and pasted into <WEATHERAPI_KEY>

`http://api.weatherapi.com/v1/current.json?key=WEATHERAPI_KEY`

## Replit

Run the following in the bash shell:

`pip install discord`

`pip install requests`

- Then run `main.py`, this should generate a URL `https://Weather.winniiew.repl.co/` that can then be used in [UptimeRobot](https://uptimerobot.com/) to host the Discord bot.

### Uptime Robot
1. Click `+ Add New Monitor`
2. Select `HTTP(s)` under `Monitor Types`
3. Paste the generated URL
4. Change the monitoring interval to 5 minutes

<p align="center">
<img width="600" alt="weather1" src="https://user-images.githubusercontent.com/86391366/172726371-ea576e58-081e-4443-9953-ec14bfd0a102.png">
<p>

## Invite Bot to join Server
https://discord.com/api/oauth2/authorize?client_id=984035152281862145&permissions=259845990464&scope=bot
  
## Commands

`!w COUNTRY, CITY`
 
 **Example**
  
`!w France, Paris`

`!w STATE, CITY`
 
**Example**
  
`!w California, San Francisco`
