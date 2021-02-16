import os
from quart import Quart, send_file

app = Quart(__name__)

@app.route("/")
async def homepage():
	return await send_file("avatars/-1.png")

@app.route("/<int:uid>")
async def avatarRequest(uid):
	if os.path.exists(f"avatars/{uid}.png"):
		return await send_file(f"avatars/{uid}.png")

	return await send_file("avatars/-1.png")

app.run()
