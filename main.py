from aiohttp import web
import os
import importlib

# dad?
# mom
# son

class main(web.Application):
    def __init__(self, app):
        self.app = app


    async def index(self): # still nothing
      return web.FileResponse('./static/index.html')

    def start(self):
        handles, cogs, routes = self.loadAllHandles()
        print(f"loaded cogs:")
        print(cogs, "\n")
        print(f"loaded handles:")
        print(handles, "\n")
        print("routes")
        print(routes, "\n")
        self.index()
        web.run_app(self.app, port=8080)


    def loadAllHandles(self):
        global cogs
        _cogs = {}
        _routes = []
        for handle in os.listdir(r"./handlers"):
            if handle[-3:] == ".py":
                cog, handles = importlib.import_module(f"handlers.{handle[:-3]}").setup(self.app)
                _cogs[handle[:-3]] = [cog, handles]
        for cog in _cogs:
            for handle in _cogs[cog][1]:
                self.app.router.add_get(f"{_cogs[cog][1][handle]}", getattr(_cogs[cog][0], handle))
                _routes.append(f"{_cogs[cog][1][handle]}")
        return handles, _cogs, _routes
        # this is very advanced.
        # I'll work on writings random breds to a JSON file..




if __name__ == "__main__":
    app = web.Application()
    main(app).start()
