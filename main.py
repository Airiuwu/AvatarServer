import os, uvicorn, colors
from starlette.applications import Starlette
from starlette.responses import FileResponse
from starlette.routing import Route

async def avatarRequest(request):
	uid = request.path_params['id']

	if os.path.isfile("avatars/{}.png".format(uid)):
		return FileResponse("avatars/{}.png".format(uid))

	return FileResponse("avatars/-1.png")

app = Starlette(routes=[Route('/{id:int}', endpoint=avatarRequest, methods=['GET'])])

colors.printConsole()

uvicorn.run(app, host="127.0.0.1", port=5000)
