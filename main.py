from flask_test import app

HOST = "0.0.0.0"
PORT = 4567

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=True)
