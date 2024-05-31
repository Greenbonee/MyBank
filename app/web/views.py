from flask import render_template, redirect, url_for, flash,  request, session
from . import bp

# General

users = {
    'admin': {'password': 'password123', 'name': 'Admin User', 'dob': '1990-01-01', 'email': 'admin@example.com', 'phone': '1234567890', 'address': '123 Admin St'}
}

@bp.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('web.login'))

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            session['username'] = username
            return redirect(url_for('web.home'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html')

@bp.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('web.login'))

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        name = request.form['name']
        dob = request.form['dob']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        
        if username in users:
            flash('Username already exists', 'danger')
        else:
            users[username] = {'password': password, 'name': name, 'dob': dob, 'email': email, 'phone': phone, 'address': address}
            return redirect(url_for('web.registration_success'))
    return render_template('register.html')

@bp.route('/registration_success')
def registration_success():
    return render_template('success.html')



# Admin Routes

@bp.route('/backup', methods=['GET', 'POST'])
def backup():
    # Backup logic here
    return render_template('admin/backup.html')


# Manager Routes

@bp.route('/approve', methods=['GET', 'POST'])
def approve():
    # Approval logic here
    return render_template('manager/approve.html')

# Customer Routes

@bp.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    # Withdraw logic here
    return render_template('customer/withdraw.html')