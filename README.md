# bread-api 
![Generic badge](https://img.shields.io/badge/Release-soon™-purple.svg) ![Generic badge](https://img.shields.io/badge/Version-null-black.svg) \
A lightweight and simple API for bread.\
Fork of _<a href="https://github.com/Mr-Conos/Rock-API">Rock-API</a>_  by  _<a href="https://github.com/Mr-Conos">Mr-Conos</a>_ (OG Dev, go check out Rock-API)\
Made by:  _<a href="https://github.com/flicker211">flicker211<a>_  |  _<a href="https://github.com/russian-dev">russian-dev</a>_ 

\
**API Status (UptimeRobot):** \
![Generic badge](https://badgen.net/uptime-robot/status/m790509518-b946e5eb6c4de5cf141b2c00)
![Generic badge](https://badgen.net/uptime-robot/response/m790509518-b946e5eb6c4de5cf141b2c00) \
![Generic badge](https://badgen.net/uptime-robot/day/m790509518-b946e5eb6c4de5cf141b2c00)
![Generic badge](https://badgen.net/uptime-robot/week/m790509518-b946e5eb6c4de5cf141b2c00)
![Generic badge](https://badgen.net/uptime-robot/month/m790509518-b946e5eb6c4de5cf141b2c00)

	
	
---
### Notes:

- ``https://bread-api.russiandev.repl.co/bread/random`` if you want a random bread type. (Subject to change, this is a place holder)
- ``https://bread-api.russiandev.repl.co/bread/[breadName]`` if you want a specific bread type. ^^^
- It's formatted as a JSON.

---
Current bread types (9):
`whiteBread`
`ryeBread`
`moldyBread`
`redBread`
`bigBread`
`verybigBread`
`humonousBread`
`collosolBread`
`breadception`
# Discord.py command using bread-api:
```python
import json
from urllib.request import urlopen
from discord.ext import commands

@client.command()
async def bread(ctx):
    uri = "https://bread-api.russiandev.repl.co/bread/random"
    response = urlopen(uri)
    data = json.load(response)

    NAME = data['name']
    DESC = data['desc']
    IMAGE = data['image']
    RATING = data['rating']
    embed: discord.Embed = discord.Embed(title="Rock Info:", description="", color=discord.Color.dark_blue())
    embed.set_author(name="Rock-API")
    embed.set_thumbnail(url=IMAGE)
    embed.add_field(name="Name", value=NAME, inline=False)
    embed.add_field(name="Description", value=DESC, inline=False)
    embed.add_field(name="Rating", value=RATING, inline=False)
	
    await ctx.send(embed=embed)
    uri = ""
```

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
	
*Please create an Issue If you find any bugs*
	

<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="100" height="20" role="img" aria-label="Release: soon™"><title>Release: soon™</title><linearGradient id="s" x2="0" y2="100%"><stop offset="0" stop-color="#bbb" stop-opacity=".1"/><stop offset="1" stop-opacity=".1"/></linearGradient><clipPath id="r"><rect width="100" height="20" rx="3" fill="#fff"/></clipPath><g clip-path="url(#r)"><rect width="53" height="20" fill="#555"/><rect x="53" width="47" height="20" fill="purple"/><rect width="100" height="20" fill="url(#s)"/></g><g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" text-rendering="geometricPrecision" font-size="110"><text aria-hidden="true" x="275" y="150" fill="#010101" fill-opacity=".3" transform="scale(.1)" textLength="430">Release</text><text x="275" y="140" transform="scale(.1)" fill="#fff" textLength="430">Release</text><text aria-hidden="true" x="755" y="150" fill="#010101" fill-opacity=".3" transform="scale(.1)" textLength="370">soon™</text><text x="755" y="140" transform="scale(.1)" fill="#fff" textLength="370">soon™</text></g></svg>

