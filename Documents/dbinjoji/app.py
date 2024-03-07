from flask import Flask
from flask_jwt_extended import JWTManager
from views import auth_bp

app = Flask(__name__)
app.secret_key = 'super_secret_key'
jwt = JWTManager(app)

app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(debug=True)
