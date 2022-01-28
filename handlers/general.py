from aiohttp import web


class general(web.Application):

    def __init__(self, app):
        self.app = app

    async def ping(self, request):
        re = {"success": True, "data": "pong!"}
        return web.json_response(re)


def setup(app):
    return general(app), ['ping']
