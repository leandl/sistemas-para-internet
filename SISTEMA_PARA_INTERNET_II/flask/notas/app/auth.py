from flask import Blueprint, url_for


auth = Blueprint('auth', __name__)

@auth.get('/login')
def login():
    return '<h1>Login</h1>'

@auth.get('/logout')
def logout():
    return '<h1>Logout</h1>'

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    return '<h1>Sign Up</h1>'

    