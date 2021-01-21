import os, uvicorn, colors
from starlette.applications import Starlette
from starlette.responses import FileResponse
from starlette.routing import Route

async def avatarRequest(request):
	uid = request.path_params['id']

	if os.path.isfile("avatars/{}.png".format(uid)):
		return FileResponse("avatars/{}.png".format(uid))

	return FileResponse("avatars/-1.png")

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

app = Starlette(routes=[Route('/{id:int}', endpoint=avatarRequest, methods=['GET'])])

printConsole()

uvicorn.run(app, host="127.0.0.1", port=5000)
