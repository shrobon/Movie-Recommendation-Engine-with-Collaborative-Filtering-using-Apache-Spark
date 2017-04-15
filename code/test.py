from flask import Flask, render_template

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



app = Flask(__name__)

@app.route("/")
def hello():
	logger.info("Entered the hello method")
	return "Hello World !!"

if __name__ == "__main__":
	app.run(debug=True)
