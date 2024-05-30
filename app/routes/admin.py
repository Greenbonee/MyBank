from flask import Blueprint, render_template

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/backup', methods=['GET', 'POST'])
def backup():
    # Backup logic here
    return render_template('admin/backup.html')