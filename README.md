## Python-Blog-Posts-Project
A simple web application built with Flask (Python) that allows users to write blog posts, register/login, and ask & answer questions

Features
- Create, edit, and delete blog posts
- Register and log in users
- Ask and answer questions (Q&A section)

⚙️Tech Stack
- Flask
- SQLite
- HTML, CSS, Jinja2 Templates

General
- Simple UI built with HTML & CSS
- Secure password hashing using Werkzeug
- To create forms flask-wtf
- SQLite database with SQLAlchemy ORM

🗂️ Project Structure
- Flask-Blog/
- ├── app/
- │   ├── __init__.py
- │   ├── models.py
- │   ├── routes.py          
- │   ├── forms.py
- │   └── templates/
- │       ├── base.html
- │       ├── index.html
- │       ├── post.html
- │       ├── create.html
- │       ├── edit.html
- │       ├── login.html
- │       ├── register.html
- │       ├── questions.html
- ├── app.py
- ├── requirements.txt

🧠 How It Works
- Users register and log in to their accounts.
- They can create blog posts from their dashboard.
- In the Q&A section, users can ask questions

Installation & Setup

- Create a virtual environment:
- python -m venv venv
- source venv/bin/activate   # For macOS/Linux
- venv\Scripts\activate      # For Windows
- Install dependencies:
- pip install -r requirements.txt
- Run the app: python run.py
 -Visit in browser: http://127.0.0.1:5000
