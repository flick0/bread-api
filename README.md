# <img alt=":O Bread" src="https://bread-api-images.russiandev.repl.co/images/icon.png" style="display:block;width:3%;margin-left:auto;margin-right:auto;"> Bread-API
![Generic badge](https://img.shields.io/badge/version-0.1.0-black.svg) \
A lightweight and simple API for bread.\
Inspiration: _<a href="https://github.com/Mr-Conos/Rock-API">Rock-API</a>_  by  _<a href="https://github.com/Mr-Conos">Mr-Conos</a>_ (OG Dev, go check out Rock-API)\
Made by:  _<a href="https://github.com/flicker211">flicker211<a>_  |  _<a href="https://github.com/russian-dev">russian-dev</a>_ \
Bread-API Discord: <a href="https://discord.gg/vCAtrFzMUE">.gg/vCAtrFzMUE</a>


## **UptimeRobot Statistics**
**API Status:**  \
![Generic badge](https://badgen.net/uptime-robot/status/m790509518-b946e5eb6c4de5cf141b2c00)
![Generic badge](https://badgen.net/uptime-robot/response/m790509518-b946e5eb6c4de5cf141b2c00) 


**API Image DB Status:** \
![Generic badge](https://badgen.net/uptime-robot/status/m790509611-6bd9a6ee25e3abedc2e1838f)
![Generic badge](https://badgen.net/uptime-robot/response/m790509611-6bd9a6ee25e3abedc2e1838f) 

	
	
---
### Notes:

- _<a href="https://bread-api.russiandev.repl.co/bread/random">`https://bread-api.russiandev.repl.co/bread/random`</a>_ if you want a random bread type. (Subject to change)
- _<a href="https://bread-api.russiandev.repl.co/bread?name=">`https://bread-api.russiandev.repl.co/bread?name=[BREAD]`</a>_ if you want a specific bread type. ^^^
- _<a href="https://bread-api.russiandev.repl.co/bread">`https://bread-api.russiandev.repl.co/bread`</a>_ if you want more details.

---
**Current official bread types** ***(10)***: \
_`white bread`_
_`rye bread`_
_`moldy bread`_
_`red bread`_
_`big bread`_
_`very big bread`_
_`humonous bread`_
_`collosol bread`_\
_`bread bread bread bread`_
_`baguette`_
_+ user-created_
# Discord.py get random bread command using bread-api:
```python
import json
from urllib.request import urlopen

@client.command()
async def bread(ctx):
    uri = "https://bread-api.russiandev.repl.co/bread/random"
    response = urlopen(uri)
    data = json.load(response)

    NAME = data['name']
    DESC = data['desc']
    IMAGE = data['image']
    RATING = data['rating']
    embed: discord.Embed = discord.Embed(title="Bread Info:", description="", color=discord.Color.dark_blue())
    embed.set_author(name="Bread-API")
    embed.set_thumbnail(url=IMAGE)
    embed.add_field(name="Name", value=NAME, inline=False)
    embed.add_field(name="Description", value=DESC, inline=False)
    embed.add_field(name="Rating", value=RATING, inline=False)
	
    await ctx.send(embed=embed)
    uri = ""
```
 
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
	
*Please create an Issue If you find any bugs*	


	
