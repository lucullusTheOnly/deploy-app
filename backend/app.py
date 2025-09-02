from flask import Flask, request, render_template_string

app = Flask(__name__)
from flask_cors import CORS
CORS(app)  # allows all origins

@app.route("/deploy", methods=["POST"])
def deploy():
    description = request.form.get("description")
    environment = request.form.get("environment")
    replicas = request.form.get("replicas")

    return render_template_string("""
    <div class='alert alert-success'>
        ✅ Deploy triggered!<br>
        Description: {{ description }}<br>
        Environment: {{ environment }}<br>
        Replicas: {{ replicas }}
    </div>
    """, description=description, environment=environment, replicas=replicas)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
