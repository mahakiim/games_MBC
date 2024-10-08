from flask import Flask, render_template
import os

app = Flask(__name__)
from controller import about, home, maps, gaada, hehe

#testing mas

app.register_blueprint(home.home_bp)
app.register_blueprint(about.about_bp)
app.register_blueprint(maps.maps_bp)
app.register_blueprint(gaada.gaada_bp)
app.register_blueprint(hehe.hehe_bp)

@app.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
