from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
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

    cgpa = round(sum(sem_gpas) / num_sems, 2) if num_sems > 0 else 0.0

    return render_template(
        'result.html',
        cgpa=cgpa,
        sem_gpas=sem_gpas,
        num_sems=num_sems
    )

if __name__ == "__main__":
    app.run(debug=True)