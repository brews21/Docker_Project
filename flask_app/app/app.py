from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def index():
    return jsonify(
        {
            "app": "flask-docker-example",
            "status": "ok",
            "message": "Flask is running in Docker.",
        }
    )


@app.get("/health")
def health():
    return jsonify({"status": "healthy"})
