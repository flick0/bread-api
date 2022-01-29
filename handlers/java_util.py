from aiohttp import web
import json


class java_util(web.Application):
    def __init__(self, app):
        self.app = app

    async def convertHashmapJson(self, request):
        """
        to convert json to hashmap:
         - /convertHashapJson?json={"your":"json"}

        to convert hashmap to json
         - /convertHashapJson?hashmap={your=hashmap}
        """
        if "hashmap" in request.query:
            rs_json = {}
            hashmap = request.query["hashmap"].replace("{", "").replace("}", "").replace(", ", ",")
            for pair in hashmap.split(","):
                key, value = pair.split("=")
                rs_json[key] = value
            return web.json_response(rs_json)
        elif "json" in request.query:
            rs_json = json.loads(request.query["json"])
            hashmap = "{"
            for key in rs_json:
                hashmap += f"{key}={rs_json[key]},"
            hashmap = hashmap[:-1] + "}"
            return web.Response(text=hashmap)
        else:
            return web.Response(text=self.convertHashmapJson.__doc__)


def setup(app):
    return java_util(app), {"convertHashmapJson": "/convertHashmapJson"}
