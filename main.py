import os, random
from quart import Quart, send_file

app, defaultAvatars = Quart(__name__), ["-1", "-2", "-3", "-4", "-5"]

@app.route("/")
async def homepage():
	return await send_file("avatars/{}.png".format(random.choice(defaultAvatars)))

@app.route("/<int:uid>")
async def avatarRequest(uid):
	if os.path.exists(f"avatars/{uid}.png"):
		return await send_file(f"avatars/{uid}.png")

	return await send_file("avatars/-1.png")

app.run()
