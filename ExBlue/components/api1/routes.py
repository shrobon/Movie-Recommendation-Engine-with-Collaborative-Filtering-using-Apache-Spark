from flask import Blueprint
mod = Blueprint('firstapi',__name__)

@mod.route('/weather')
def weather_handler():
	return "<h1>You are using the Weather API</h1>"


