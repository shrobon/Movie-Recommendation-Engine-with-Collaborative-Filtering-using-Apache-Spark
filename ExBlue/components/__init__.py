from flask import Flask 

app = Flask(__name__)

from api1.routes import mod
from api2.routes import mod 


# Now registering both the API's
app.register_blueprint(api1.routes.mod,url_prefix="/api1")
app.register_blueprint(api2.routes.mod,url_prefix="/api2")
