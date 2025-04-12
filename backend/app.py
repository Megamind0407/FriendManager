from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(
    __name__,
    static_folder=os.path.join("..", "frontend", "dist"),
    static_url_path=""
)

# Uncomment if you want to allow CORS (not usually needed when frontend is served by Flask)
# CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///friends.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Serve React frontend
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_react(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, "index.html")

# Import and register API routes
import routes

with app.app_context():
    db.create_all()

# Only for local development
if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
