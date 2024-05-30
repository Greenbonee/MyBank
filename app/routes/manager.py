from flask import Blueprint, render_template

bp = Blueprint('manager', __name__, url_prefix='/manager')

@bp.route('/approve', methods=['GET', 'POST'])
def approve():
    # Approval logic here
    return render_template('manager/approve.html')