from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from bson import ObjectId

from models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form.get('role', 'USER')

        if not username or not password:
            return render_template('register.html', message='Username and password are required')

        if User.find_by_username(username):
            return render_template('register.html', message='Username already exists')

        User.create(username, password, role)
        return redirect(url_for('auth.login'))

    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            return render_template('login.html', message='Username and password are required')

        user = User.find_by_username(username)
        if not user or not check_password_hash(user["password"], password):
            return render_template('login.html', message='Invalid username or password')

        access_token = create_access_token(identity=username)
        return redirect(url_for('auth.dashboard', token=access_token))

    return render_template('login.html')

@auth_bp.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        username = request.form['username']
        new_password = request.form['new_password']

        if not username or not new_password:
            return render_template('reset_password.html', message='Username and new password are required')

        user = User.find_by_username(username)
        if not user:
            return render_template('reset_password.html', message='User not found')

        hashed_password = generate_password_hash(new_password)
        User.update(user["_id"], {"password": hashed_password})

        return redirect(url_for('auth.login'))

    return render_template('reset_password.html')

@auth_bp.route('/update', methods=['GET', 'POST'])
def update_user_by_id():
    if request.method == 'POST':
        user_id_str = request.form['user_id']

        if not user_id_str:
            return render_template('update_user.html', message='User ID is required')

        try:
            user_id = ObjectId(user_id_str)
            user = User.find_by_id(user_id)
        except:
            return render_template('update_user.html', message='Invalid user ID format')

        if not user:
            return render_template('update_user.html', message='User not found')

        update_data = {}
        if request.form['username'] and request.form['username'] != '':
            update_data["username"] = request.form['username']
        if request.form['new_password'] and request.form['new_password'] != '':
            hashed_password = generate_password_hash(request.form['new_password'])
            update_data["password"] = hashed_password
        if request.form['role'] and request.form['role'] != '':
            update_data["role"] = request.form['role']

        if update_data:
            User.update(user_id, update_data)
            return redirect(url_for('auth.login'))

    return render_template('update_user.html')

@auth_bp.route('/logout')
def logout():
    # You can implement any logout logic here, such as clearing JWT tokens or session data
    return redirect(url_for('auth.login'))

# Other routes and functions go here...
@auth_bp.route('/users', methods=['GET'])
def get_all_users():
    all_users = User.get_all()
    return render_template('all_users.html', all_users=all_users)

@auth_bp.route('/user', methods=['POST'])
def get_user_by_id():
    user_id = request.form.get('user_id')

    if not user_id:
        return jsonify({'message': 'User ID is required'}), 400

    user = User.find_by_id(ObjectId(user_id))
    if not user:
        return render_template('no_users.html')

    return render_template('user.html', user=user)

@auth_bp.route('/dashboard')
def dashboard():
    token = request.args.get('token')
    if token:
        # Extract user's role from JWT token claims
        # current_user = get_jwt_identity()
        return render_template('dashboard.html', token=token)  # , is_super=is_super
    else:
        return redirect(url_for('auth.login'))

@auth_bp.route('/admin')
def admin():
    token = request.args.get('token')
    if token:
        # Extract user's role from JWT token claims
        # current_user = get_jwt_identity()
        # Add authorization check (e.g., check if current_user['role'] == 'SUPER')
        # if current_user['role'] == 'SUPER':
        return render_template('admin.html', token=token)  # , is_super=is_super
        # else:
        #   return render_template('unauthorized.html'), 403  # Forbidden for non-super users
    else:
        return redirect(url_for('auth.login'))

