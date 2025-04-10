# 🐍 Flask + MySQL Starter Kit — CRUD REST API

A beginner-friendly starter project to build a CRUD REST API using **Python**, **Flask**, and **MySQL** with `mysql-connector-python`. Perfect for learning backend fundamentals with relational databases.

---

## 🚀 Features

- Simple Flask project structure
- REST API for basic CRUD operations
- MySQL integration using `mysql-connector-python`
- Environment variable support using `python-dotenv`
- CORS support for frontend integration
- Easy to extend and deploy

---

## 🛠️ Tech Stack

- Python 3.8+
- Flask
- MySQL
- `mysql-connector-python`
- `python-dotenv`
- `flask-cors`

---

## 📦 Installation

### 1. Clone the repo

```bash
git clone https://github.com/Gnutyud/python-mysql-starter-kit.git
cd python-mysql-starter-kit
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

Create a .env file in the root directory and add your database config:
```env
FLASK_PORT=8080
FLASK_DEBUG="true"
MYSQL_DATABASE_HOST="localhost"
MYSQL_DATABASE_DB=""
MYSQL_DATABASE_USER=""
MYSQL_DATABASE_PASSWORD=""
MYSQL_DATABASE_PORT=3306
```

## ▶️ Running the app

```bash
flask run
# OR
python app.py
```

By default the API will be available at:
http://127.0.0.1:5000/
