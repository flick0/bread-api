from aiohttp import web
import os
import importlib


class main(web.Application):
    def __init__(self, app):
        self.app = app

    def start(self):
        handles, cogs, routes = self.loadAllHandles()
        print(f"loaded cogs:")
        print(cogs, "\n")
        print(f"loaded handles:")
        print(handles, "\n")
        print("routes")
        print(routes, "\n")
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
                self.app.router.add_get(f"/{handle}", getattr(_cogs[cog][0], handle))
                _routes.append(f"/{handle}")
        return handles, _cogs, _routes


if __name__ == "__main__":
    app = web.Application()
    main(app).start()
