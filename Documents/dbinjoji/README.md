**Injozi Flask Application**

**Overview**

This is a Flask application that demonstrates user authentication, authorization, and basic CRUD (Create, Read, Update, Delete) operations for user management. It utilizes JWT (JSON Web Token) for authentication and follows a structured MVC (Model-View-Controller) architecture for code organization and maintainability.

**Features**

* User registration, login, and logout with JWT-based authentication
* Role-based authorization (admin and user roles)
* User management:
  * List all users (super user only)
  * View individual user details
  * Update user information (username, password, and role)
* Secure database access and data validation
* Clear separation of concerns with MVC architecture and blueprints

**Installation**

1. **Prerequisites:** Ensure you have Python (version 3.6 or later) and pip (the package installer) installed on your system. You can check by running** **`python --version` and** **`pip --version` in your terminal. If not installed, download them from** **[https://www.python.org/downloads/](https://www.python.org/downloads/).
2. **Create a virtual environment (recommended):** This isolates project dependencies and avoids conflicts:Bash

   ```
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate.bat
   ```

   Use code** **[with caution.](https://gemini.google.com/faq#coding)
3. **Install dependencies:** Navigate to your project directory and run:Bash

   ```
   pip install Flask Flask-JWT Flask-MongoEngine Werkzeug bcrypt pymongo
   ```

   Use code** **[with caution.](https://gemini.google.com/faq#coding)

**Configuration**

1. **Create a** **`config.py` file:** This file stores sensitive configuration details like secret keys and database credentials. Replace placeholders with your actual values:Python

   ```
   class Config:
   SECRET_KEY = 'your_secret_key'
   JWT_SECRET_KEY = 'your_jwt_secret_key'  # Replace with a strong secret# MongoDB connection details
   MONGODB_HOST = 'localhost'
   MONGODB_PORT = 27017
   MONGODB_DB = 'injozi'
   MONGODB_USERNAME = 'your_username'
   MONGODB_PASSWORD = 'your_password'# Roles
   USER_ROLES = {
   'SUPER': 0,
   'ADMIN': 1,
   'USER': 2
   }
   ```
2. **(Optional) Environment variables:** You can also store sensitive configuration in environment variables using tools like** **`dotenv` to separate them from your code.

**Usage**

1. **Start the development server:** Run the following command in your terminal:Bash

   ```
   FLASK_APP=app FLASK_ENV=development flask run
   ```


   This starts the Flask development server, usually accessible at** **`http://127.0.0.1:5000/` in your web browser.

**API Endpoints**

* **Register:** `POST /register` (requires username, password)
* **Login:** `POST /login` (requires username, password)
* **Get All Users:** `GET /users` (requires JWT token, admin role)
* **Get User by ID:** `GET /user/<int:user_id>` (requires JWT token)
* **Update User:** `POST update` (requires JWT token, user data)
* **Logout:** `GET logout`

**License**

This project is licensed under the MIT License (see `LICENSE` file for details).

**Disclaimer**

This project is not a production project. Remember to implement robust security measures in production environments, including:

* Stronger password hashing and storage (e.g., Argon2)
* Regular security audits and updates
* Secure data validation and sanitization
* Proper access control and authorization mechanisms

I hope this README.md provides clear and helpful information about the Injozi application.
