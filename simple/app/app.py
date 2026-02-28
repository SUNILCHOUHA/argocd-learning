from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h1>🚀 Flask App Running in Kubernetes</h1>
    <p><b>Hostname:</b> {socket.gethostname()}</p>
    <p><b>Version (SHA):</b> {os.getenv("VERSION", "Not Set")}</p>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
