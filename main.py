from caesar import rotate_string
from flask import Flask, request




app = Flask(__name__)

app.config['DEBUG'] = True



form = '''<!DOCTYPE html>



<html>

    <head>

		<style>

			form {{

				background-color: #eee;

				padding: 20px;

				margin: 0 auto;

				width: 540px;

				font: 16px sans-serif;

				border-radius: 10px;

			}}

			textarea {{

				margin: 10px 0;

				width: 540px;

				height: 120px;

			}}

		</style>



    </head>

    <body>

      <form action="/rotate" method="post">

	  <label for="rot">Rotate by:</label><br>

	  <input type="text" id="rot" name="rot" value="{0}" /><br>

	  <textarea id="text" name="text">{1}</textarea>

	  <input type="submit" value="sumbit" />

		

	  </form>

    </body>

</html>

'''
@app.route("/")

def index():

	return form.format("")


@app.route("/rotate", methods=["post"])
def rotate():

	text = request.form["text"]

	rot = int(request.form["rot"])

	final = encrypt(text, rot)

	return form.format(rot, final)

app.run()