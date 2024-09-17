from flask import Blueprint, render_template

hehe_bp = Blueprint('hehe', __name__, url_prefix='/hehe/')

@hehe_bp.route('/')
def maps():
    return render_template('maps2.html')
