from flask import Flask, request

#importing Blueprint
from flask import Blueprint
main = Blueprint('main', __name__)

import json 
from engine import RecommendationEngine

#importing logging
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@main.route("/<int:user_id>/ratings/top/<int:count>",methods=["GET"])
def top_ratings(user_id,count):
	logger.debug("User %s TOP ratings requested",user_id)
	top_ratings = recommendation_engine.get_top_ratings(user_id,count)
	return json.dumps(top_ratings)



@main.route("/<int:user_id>/ratings",methods=["POST"])
def add_ratings(user_id):
	#These ratings will be obtained from the user
	ratings_list = request.form.keys()[0].strip().split("\n")
	ratings_list = map(lambda x: x.split(","),ratings_list)

	#creating engine parsable format for the new ratings (user_id,movie_id,rating)
	ratings = map(lambda x: (user_id,int(x[0]),float(x[1])),ratings_list)

	#adding the newly obtained user ratings to our recommendation engine
	recommendation_engine.add_ratings(ratings)

	return json.dumps(ratings)


def create_app(spark_context,dataset_path):
	global recommendation_engine

	recommendation_engine = RecommendationEngine(spark_context,dataset_path)
	app = Flask(__name__)
	app.register_blueprint(main)
	return app








