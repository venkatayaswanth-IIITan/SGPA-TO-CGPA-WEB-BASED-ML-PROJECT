from flask import Flask, render_template, request
import joblib
import os
import numpy as np

# AWS Elastic Beanstalk requires the WSGI callable to be named 'application'
application = Flask(__name__)

# ── Load trained ML model once at startup ──
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")
model = joblib.load(MODEL_PATH)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/calculate', methods=['POST'])
def calculate():
    num_sems = int(request.form.get('num_sems', 0))
    sem_gpas = []

    for i in range(1, num_sems + 1):
        val = request.form.get(f'sem{i}', 0)
        try:
            gpa = float(val)
        except ValueError:
            gpa = 0.0
        sem_gpas.append(round(gpa, 2))

    # ── ML Prediction (model trained on exactly 4 SGPAs) ──
    use_ml = (num_sems == 4)
    if use_ml:
        features = np.array([sem_gpas])
        cgpa = round(float(model.predict(features)[0]), 2)
        method = "ml"
    else:
        # Fallback: simple average for other semester counts
        cgpa = round(sum(sem_gpas) / num_sems, 2) if num_sems > 0 else 0.0
        method = "average"

    return render_template(
        'result.html',
        cgpa=cgpa,
        sem_gpas=sem_gpas,
        num_sems=num_sems,
        method=method
    )

# This block only runs locally; EB uses gunicorn to serve the app
if __name__ == "__main__":
    application.run(debug=True)
