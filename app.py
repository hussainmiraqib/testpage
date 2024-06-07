from flask import Flask, render_template, request, flash
from werkzeug.security import check_password_hash
import os  # Add this import statement

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necessary for flashing messages

# Example user data for demonstration
users = {
    'testuser': check_password_hash('testpassword', 'pbkdf2:sha256:150000$xyz')
}

@app.route("/")
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']

    if username in users and check_password_hash(users[username], password):
        flash('Login successful!', 'success')
        # Redirect to a logged-in user page (implement later)
        return render_template('login.html')  # Placeholder for now
    else:
        flash('Invalid username or password.', 'error')
        return render_template('login.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
