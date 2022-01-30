# ill create a seperate file for the JSON dump k

from aiohttp import web
import breads
import json


class _bread(web.Application):
    def __init__(self, app):
        self.app = app

    # /bread
    async def bread(self, response):
        """
        get bread 🥪
         - /bread?name=breadname

        get random bread 🍞
         - /bread?random=true
         - /bread/random
        
        put your own bread 🍴
         - /bread?put={"name":"bred","desc":"description","image":"image_url"}
        
        vote your favorite bread 😋
         -/bread/vote?name=breadname
        
        get the best breads(based on rating) 🏆
         -/bread/best
      
        get the worst breads 🤮
         -/bread/best?reverse=true
        """
        if "name" in response.query:
            # send bread by name
            bread = breads.get(name=response.query["name"])
            return web.json_response(bread)
        elif "random" in response.query and response.query["random"].lower() == "true":
            # send a random bread
            bread = breads.get()
            return web.json_response(bread)
        elif "put" in response.query:
          try:
            breadtoput = json.loads(response.query["put"])
            if "name" not in breadtoput or "desc" not in breadtoput:
              return web.Response(text=self.bread.__doc__+"[error] pls add all keys")
          except Exception:
            return web.Response(text=self.bread.__doc__+"[error] invalid json format") 
          name = breadtoput["name"]
          desc =breadtoput["desc"] 
          image =breadtoput["image"]
          # I rolled baguette twice, anyways, what should I do? <---
          #im testing put bread # ok
          # u can delete one ? one baguete
          # delete what? what?
          #u told u made 2 bagguetes 
          # I was going $bread and I got 2 baguettes, saying that it works
          #ah lol, nice
          # the api part is pretty much done ig
          # we just add more breads
          # ok
          # 
          # can I write to JSON file then push it to the db? 
          #have a python dict with "name" and "desc" and all the fields
          # then do putBread(name=json["name"]) and so on
          #or
          #or 
          #to put bread
          #
          #go to api
          #and do /bread?put={"name":"test","desc":"test","image":null,"rating":"0/10"} <= {"name": "not found :o"}
          #its added, it just says that
          #search for iter
          #/bread?name=name <= {"_id": 4, "name": "red bread", "desc": "i swear its not blood", "image": "https://bread-api-images.russiandev.repl.co/images/redBread/redBread.png", "rating": "2/10"}
          # I searched red bread
          
          #in your broswer or ur breadtoput 
          
          #i added a check so ppl cant add same breads again

          # how do you add bread?

          #  /bread?put={"name":"test","desc":"test","image":null,"rating":"0/10"} ???
          #yes
          # ima try it
          # if I do it in browser I get error 500, server broke itself
          #one min
          #it was added but error in response, try now
          # ok <= {"success": false, "error": "bread already exists"}
          # {"_id": 15, "name": "tes222t1", "desc": "te222st", "image": null, "rating": "2/10", "success": true}
          # real
          # where does this data go? just it go into the db or just one time use or sum

          ##################################################################################################################
          #                                                                                                                #
          # I gtg, ill be able to talk on discord mobile. Please update the gh repo with the new code if you get a chance. #
          #                                                                                                                #
          ##################################################################################################################
          
          re = breads.putBread(name,desc,image)
          return web.json_response(re)
        else:
            # if no params are specified, point to docs
            return web.Response(text=self.bread.__doc__)

    async def random(self, response):
        """
        get random bread 🍞
         - /bread/random
        """
        bread = breads.get()
        return web.json_response(bread)
      
    async def vote(self,response):
      """
      vote your favorite bread 😋
       -/bread/vote?name=breadname
      """
      if "name" in response.query:
        return web.json_response(breads.vote(response.query["name"]))
      else:
        return web.Response(text=self.vote.__doc__)
    
    async def best(self,response):
      """
      get the best breads(based on rating) 🏆
       -/bread/best
      
      get the worst breads 🤮
       -/bread/best?reverse=true
      """
      if "reverse" in response.query and response.query["reverse"].lower() == "true":
        return web.json_response(breads.leaderboard())
      return web.json_response(breads.leaderboard("-1"))
      



def setup(app):
    return _bread(app), {"bread": "/bread", "random": "/bread/random","vote":"/bread/vote","best":"/bread/best"}
