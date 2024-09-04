from flask import Blueprint, render_template

gaada_bp = Blueprint('gaada', __name__, url_prefix='/gaada')

@gaada_bp.route('/')
def home():
    return render_template('gaada.html')
