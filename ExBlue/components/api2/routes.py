from flask import Blueprint

mod = Blueprint('secondapi',__name__)

@mod.route('/time')
def time_handler():
	return "<h1>You are using the time API</h1>"