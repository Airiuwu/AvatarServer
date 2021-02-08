import os, uvicorn
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import FileResponse

async def home(request):
	return FileResponse("avatars/-1.png")

async def avatarRequest(request):
	uid = request.path_params['id']

	if os.path.isfile(f"avatars/{uid}.png"):
		return FileResponse(f"avatars/{uid}.png")

	return FileResponse("avatars/-1.png")

app = Starlette(routes=[
    Route('/', endpoint=home, methods=['GET']),
    Route('/{id:int}', endpoint=avatarRequest, methods=['GET'])
])

uvicorn.run(app, host="127.0.0.1", port=5000)
