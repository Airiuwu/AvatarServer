import os, uvicorn, colors
from starlette.applications import Starlette
from starlette.responses import FileResponse
from starlette.routing import Route

avatarFolder = "avatars"

async def homepage(request):
	return FileResponse("{}/-1.png".format(avatarFolder))

async def avatarRequest(request):
	uid = request.path_params['id']

	if os.path.isfile("{}/{}.png".format(avatarFolder, uid)):
		return FileResponse("{}/{}.png".format(avatarFolder, uid))

	return FileResponse("{}/-1.png".format(avatarFolder))

def printConsole():
	os.system('cls' if os.name=='nt' else 'clear')
	print("{}										 ".format(colors.ENDC))	  
	print("{}  █████╗ ██╗   ██╗ █████╗ ████████╗ █████╗ ██████╗     ███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗".format(colors.RED))
	print("{} ██╔══██╗██║   ██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗    ██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗".format(colors.LIGHT_RED))
	print("{} ███████║██║   ██║███████║   ██║   ███████║██████╔╝    ███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝".format(colors.RED))
	print("{} ██╔══██║╚██╗ ██╔╝██╔══██║   ██║   ██╔══██║██╔══██╗    ╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗".format(colors.LIGHT_RED))
	print("{} ██║  ██║ ╚████╔╝ ██║  ██║   ██║   ██║  ██║██║  ██║    ███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║".format(colors.RED))
	print("{} ╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝    ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝".format(colors.LIGHT_RED))	
	print("											   {}".format(colors.ENDC))

app = Starlette(routes=[
	Route('/', endpoint=homepage, methods=['GET']),
	Route('/{id:int}', endpoint=avatarRequest, methods=['GET'])
])

printConsole()

uvicorn.run(app, host="127.0.0.1", port=5000)
