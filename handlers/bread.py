# ill create a seperate file for the JSON dump k

from aiohttp import web
import breads


class _bread(web.Application):
    def __init__(self, app):
        self.app = app

    # /bread
    async def bread(self, response):
        """
        get bread 😋
         - /bread?name=breadname

        get random bread 🍞
         - /bread?random=true
         - /bread/random
        """
        if "name" in response.query:
            # send bread by name
            bread = breads.get(name=response.query["name"])
            return web.json_response(bread)
        elif "random" in response.query and response.query["random"].lower() == "true":
            # send a random bread
            bread = breads.get()
            return web.json_response(bread)
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


def setup(app):
    return _bread(app), {"bread": "/bread", "random": "/bread/random"}
