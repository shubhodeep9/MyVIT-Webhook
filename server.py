from sanic import Sanic
from sanic.response import json
import json as js
import os

app = Sanic()

@app.route("/payload", methods=["POST", ])
async def test(request):
	ref = js.loads(request.form['payload'][0])['ref']
	if (ref == "refs/heads/prod"):
		os.chdir("/home/shubhodeep9/go/src/go-MyVIT")
		import subprocess
		subprocess.call(["git","checkout","prod"])
		subprocess.call(["git","pull"])
	return json({"hello": ref})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)