from flask import Flask, send_from_directory
from dotenv import load_dotenv
import os
from flask_cors import CORS
import api

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Enable CORS for all routes
cors = CORS(app)

@app.route("/")
def hello():
    return "Hello world!"

@app.route("/checkdb")
def checkdb():
    return api.check_db()

if __name__ == "__main__":
    port = int(os.getenv("FLASK_PORT", 5000)) # Default port is 5000 if not set in .env
    debug = os.getenv("FLASK_DEBUG", "False").lower() == "true"
    app.run(host="0.0.0.0", port=port, debug=debug)