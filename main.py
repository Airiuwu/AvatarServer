import os, uvicorn
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import FileResponse

async def avatarRequest(request):
	uid = request.path_params['id']

	if os.path.isfile("avatars/{}.png".format(uid)):
		return FileResponse("avatars/{}.png".format(uid))

	return FileResponse("avatars/-1.png")

async def homepage(request):
	return FileResponse("avatars/-1.png")

app = Starlette(routes=[
    Route('/', endpoint=homepage, methods=['GET']),
    Route('/{id:int}', endpoint=avatarRequest, methods=['GET'])
])

uvicorn.run(app, host="127.0.0.1", port=5000)
