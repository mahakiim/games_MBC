from flask import Flask, render_template
import os

app = Flask(__name__)
from Controller import about, home, maps

#testing mas

app.register_blueprint(home.home_bp)
app.register_blueprint(about.about_bp)
app.register_blueprint(maps.maps_bp)

if __name__ == '__main__':
    app.run(debug=True)
