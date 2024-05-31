from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'  

users = {
    'admin': {'password': 'password123', 'name': 'Admin User', 'dob': '1990-01-01', 'email': 'admin@example.com', 'phone': '1234567890', 'address': '123 Admin St'}
}

@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
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
            return redirect(url_for('registration_success'))
    return render_template('register.html')

@app.route('/registration_success')
def registration_success():
    return render_template('success.html')




if __name__ == '__main__':
    app.run(debug=True)
