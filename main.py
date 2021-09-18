from os import path
from random import randint as randomNumber
from quart import Quart, send_file

app = Quart(__name__)

@app.route("/")
async def homepage():
	return await send_file(f"avatars/-{randomNumber(1, 5)}.png")

@app.route("/<int:uid>")
async def avatarRequest(uid):
	if path.exists(f"avatars/{uid}.png"):
		return await send_file(f"avatars/{uid}.png")

	return await send_file(f"avatars/-{randomNumber(1, 5)}.png")

app.run()
