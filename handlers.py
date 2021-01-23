import os
from starlette.applications import Starlette
from starlette.responses import FileResponse

async def avatarRequest(request):
	uid = request.path_params['id']

	if os.path.isfile("avatars/{}.png".format(uid)):
		return FileResponse("avatars/{}.png".format(uid))

	return FileResponse("avatars/-1.png")

async def homepage(request):
	return FileResponse("avatars/-1.png")
