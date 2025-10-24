from flask import Flask, request, render_template_string
import logging

app = Flask(__name__)
from flask_cors import CORS
#CORS(app)  # allows all origins
CORS(app, supports_credentials=True)
logging.basicConfig(level=logging.INFO)

@app.route("/build", methods=["POST"])
def build():
    description = request.form.get("description")
    environment = request.form.get("environment")
    replicas = request.form.get("replicas")
    data = request.json()
    data["status"] = "ok"
    app.logger.info(str(data))
    return data

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
