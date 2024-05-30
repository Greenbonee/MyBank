from flask import Blueprint, render_template

bp = Blueprint('customer', __name__, url_prefix='/customer')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    # Registration logic here
    return render_template('customer/register.html')