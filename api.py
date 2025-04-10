from flask import jsonify, request
from db_config import create_db_connection
from app import app

@app.errorhandler(404)
def not_found(error=None):
    message = {
        "status": 404,
        "message": "Not found: " + request.url,
    }
    response = jsonify(message)
    response.status_code = 404

    return response

def check_db():
    try:
        connection = create_db_connection()
        if connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SHOW TABLES")
            rows = cursor.fetchall()
            res = jsonify(rows)
            res.status_code = 200
            return res
        else:
            return jsonify({"message": "An error occurred"}), 500
    except Exception as e:
        print(e)
        return jsonify({"message": "An error occurred"}), 500
    finally:
        if connection and cursor:
            cursor.close()
            connection.close()