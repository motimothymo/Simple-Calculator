from flask import Flask, render_template, redirect, session
import redis

#Init Flask
app = Flask(__name__)


if __name__ == "__main__":
    app.run(debug=True)

#Blueprints
from .calculator import calc_blueprint

app.register_blueprint(calc_blueprint)
app.logger.info(app.url_map)

#Lobby
@app.route("/")
def index():
    return redirect ("/api/prime/3")