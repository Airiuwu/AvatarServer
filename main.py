import uvicorn, utils, handlers
from starlette.applications import Starlette
from starlette.routing import Route

app = Starlette(routes=[Route('/', endpoint=handlers.homepage, methods=['GET']),Route('/{id:int}', endpoint=handlers.avatarRequest, methods=['GET'])])

utils.printConsole()

uvicorn.run(app, host="127.0.0.1", port=5000)
