from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
    try:
        conn = psycopg2.connect(
            host=os.environ['DB_HOST'],
            database=os.environ['DB_NAME'],
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASS']
        )
        return "PostgreSQL Connected!"
    except Exception as e:
        return f"error: {e}"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
