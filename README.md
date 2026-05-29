# 🎓✨ SGPA to CGPA — Web-Based ML Project on AWS Elastic Beanstalk ☁️🚀

> 📚 A fully functional, beautifully designed **CGPA Predictor** web application built using **Python Flask** 🐍 + **Machine Learning (Linear Regression)** 🤖 and deployed live to **AWS Elastic Beanstalk** ☁️.
>
> 🌈 Features include:
>
> * 🤖 ML-powered CGPA prediction (Linear Regression)
> * 🎨 4 switchable UI themes
> * 📅 Dynamic semester selection (1–8 semesters)
> * 📊 Animated CGPA results with progress bars
> * 🏆 Grade classification badges
> * 🎉 Confetti celebration effects
> * 📤 Share button with live URL
> * ☁️ Deployed to AWS Elastic Beanstalk
>
> 👨‍💻 Beginner-friendly + easy to understand for viewers.

---

# 🌐 Live Project URL

👉 [http://cgpa-calculator-env.eba-mkrp46vf.ap-south-1.elasticbeanstalk.com](http://cgpa-calculator-env.eba-mkrp46vf.ap-south-1.elasticbeanstalk.com/)

---

# 📋 Table of Contents

1. 📖 About the Project
2. 🤖 ML Model Details
3. ✨ Features
4. 🛠️ Technology Stack
5. 📐 How CGPA is Predicted
6. 📁 Project Structure
7. 🎨 UI Themes
8. 💻 Local Development Setup
9. 🧠 Train the ML Model
10. ☁️ AWS Elastic Beanstalk Deployment
11. 📋 All Commands Reference
12. 🐛 Errors & Fixes
13. 💰 AWS Cost Estimate
14. 👤 Project Info
15. 📄 License

---

# 📖 About the Project

This project was built as a practical web application 🖥️ to help students **predict their CGPA (Cumulative Grade Point Average)** across semesters using **Machine Learning** 🤖.

🎓 Most universities in India use a **10-point GPA scale**, and this predictor fully supports that system.

## 🚀 Project Evolution

| Phase | Description |
|-------|-------------|
| v1 | Simple marks calculator (3 subjects) |
| v2 | CGPA Calculator using arithmetic average |
| v3 ✅ | **ML-powered CGPA Predictor using Linear Regression** |

The v3 upgrade integrated:

✅ Linear Regression model trained on real student data  
✅ `train_model.py` — standalone training script  
✅ `Student_Performance1.csv` — training dataset  
✅ `model.pkl` — saved model loaded at Flask startup  
✅ ML badge shown on result page when model is used  
✅ Fallback average for non-4-semester inputs  
✅ Fixed scikit-learn version pinning for AWS compatibility  

---

# 🤖 ML Model Details

| 📌 Property        | 📄 Value                        |
| ------------------ | ------------------------------- |
| 🧠 Algorithm       | Linear Regression               |
| 📚 Training Data   | Student_Performance1.csv (20 rows) |
| 🎯 Features (X)    | SGPA1, SGPA2, SGPA3, SGPA4      |
| 🎯 Target (y)      | CGPA                            |
| 📊 Train/Test Split| 80% / 20%                       |
| 📈 R² Score        | 1.0000 (near-perfect fit)       |
| 🔧 Library         | scikit-learn 1.7.0              |
| 💾 Saved Format    | joblib pickle (`model.pkl`)     |

## 📊 Sample Training Data

| SGPA1 | SGPA2 | SGPA3 | SGPA4 | CGPA |
|-------|-------|-------|-------|------|
| 7.48  | 7.78  | 7.83  | 7.17  | 7.57 |
| 8.10  | 8.30  | 8.20  | 8.50  | 8.28 |
| 9.10  | 9.00  | 9.20  | 9.30  | 9.15 |
| 6.80  | 7.00  | 7.20  | 7.30  | 7.08 |
| ...   | ...   | ...   | ...   | ...  |

## 🔮 Prediction Logic

```python
# When user selects exactly 4 semesters → ML model predicts
features = np.array([[sgpa1, sgpa2, sgpa3, sgpa4]])
cgpa = model.predict(features)[0]

# For other semester counts → arithmetic average (fallback)
cgpa = sum(sem_gpas) / num_sems
```

---

# ✨ Features

| 🌟 Feature               | 📄 Description                                                   |
| ------------------------ | ---------------------------------------------------------------- |
| 🤖 ML Prediction         | Linear Regression model predicts CGPA from 4 SGPAs              |
| 🎨 4 UI Themes           | Cosmic Purple 🟣, Ocean Blue 🔵, Sunset Glow 🟠, Forest Green 🟢 |
| 📅 Semester Selector     | Select 1–8 semesters dynamically                                 |
| 📊 CGPA Prediction       | ML model for 4 sems, average fallback for others                 |
| 🏆 Grade Classification  | Automatically assigns grade based on CGPA                        |
| 📈 Progress Bar          | Animated performance bar                                         |
| 🎉 Confetti Effect       | Celebration animation when CGPA ≥ 6.0                           |
| 📊 Semester Breakdown    | Displays GPA of each semester with mini bars                     |
| 📤 Share / Copy          | Share results with live URL using Web Share API                  |
| 🌊 Animated Background   | Moving gradient effects                                          |
| ✨ Floating Particles     | 18 animated particles in background                              |
| 🔄 Ripple Effect         | Button click ripple animation                                    |
| 🧠 Theme Memory          | Saves selected theme using localStorage                          |
| 📱 Responsive Design     | Mobile + Tablet + Desktop support                                |

---

# 🛠️ Technology Stack

## 🐍 Backend Technologies

| ⚙️ Technology   | 📌 Version         | 📄 Description                      |
| --------------- | ------------------ | ----------------------------------- |
| 🐍 Python       | 3.13.3             | Core programming language           |
| 🌶️ Flask       | 3.1.0              | Lightweight Python web framework    |
| 🧩 Jinja2       | Bundled with Flask | Dynamic HTML templating engine      |
| 🚀 Gunicorn     | 22.0.0             | Production-grade WSGI server        |
| 🤖 scikit-learn | 1.7.0              | Linear Regression ML model          |
| 🔢 NumPy        | 2.3.0              | Numerical arrays for ML input       |
| 🐼 Pandas       | 2.2.3              | CSV data loading and preprocessing  |
| 💾 Joblib       | 1.4.2              | Model serialization (save/load pkl) |

## 🖥️ Frontend Technologies

| 💻 Technology        | 📄 Description                      |
| -------------------- | ----------------------------------- |
| 🌐 HTML5             | Structure of the web pages          |
| 🎨 Vanilla CSS       | Styling + animations + themes       |
| ⚡ JavaScript (ES6+) | Dynamic UI interactions             |
| 🔤 Google Fonts      | Modern typography using Outfit font |

## ☁️ Cloud Infrastructure

| ☁️ Service                | 📄 Description                       |
| ------------------------- | ------------------------------------ |
| ☁️ AWS Elastic Beanstalk  | Manages deployment + infrastructure  |
| 🖥️ Amazon EC2            | Runs Flask app + Gunicorn            |
| 📦 Amazon S3              | Stores deployment ZIP files          |
| 🌐 Elastic Load Balancer  | Distributes incoming traffic         |
| 🔁 Nginx                  | Reverse proxy server                 |
| 🔐 AWS IAM                | User permissions + access management |
| 📊 CloudWatch             | Monitoring + alarms                  |

## 🧰 Developer Tools

| 🛠️ Tool   | 📄 Description                  |
| ---------- | ------------------------------- |
| ☁️ AWS CLI | Configure AWS locally           |
| 🚀 EB CLI  | Deploy/manage Elastic Beanstalk |
| 📦 pip     | Install Python packages         |
| 🐙 Git     | Version control + GitHub push   |

---

# 📐 How CGPA is Predicted

## 🤖 When ML Model is Used (4 Semesters)

```python
# application.py / app.py
model = joblib.load("model.pkl")   # loaded once at startup

features = np.array([[sgpa1, sgpa2, sgpa3, sgpa4]])
cgpa = round(float(model.predict(features)[0]), 2)
```

The result page shows a **🤖 ML Predicted** badge.

## 🧮 When Average is Used (1, 2, 3, 5–8 Semesters)

```python
cgpa = round(sum(sem_gpas) / num_sems, 2)
```

## 🏆 Grade Classification Logic

```javascript
if      (cgpa >= 9.0) → Grade O  — Outstanding
else if (cgpa >= 8.0) → Grade A+ — Excellent
else if (cgpa >= 7.0) → Grade A  — Very Good
else if (cgpa >= 6.0) → Grade B+ — Good
else if (cgpa >= 5.0) → Grade B  — Average
else                  → Below Average
```

---

# 📁 Project Structure

```text
cal project/
│
├── application.py           ← AWS EB entry point (with ML model)
├── app.py                   ← Local dev entry point (with ML model)
├── train_model.py           ← Train & save model.pkl
├── Student_Performance1.csv ← Training dataset (20 rows)
├── model.pkl                ← Saved ML model (not in git)
├── requirements.txt         ← Python dependencies (ML + Flask)
├── Procfile                 ← Gunicorn startup command
├── .ebignore                ← Excludes train_model.py from EB deploy
├── .gitignore               ← Excludes model.pkl from git
├── .ebextensions/
│   └── python.config        ← EB WSGI + static files config
├── .elasticbeanstalk/
│   └── config.yml           ← EB app/env/region config
└── templates/
    ├── index.html           ← Input form (semester selector)
    └── result.html          ← Result page (ML badge + share URL)
```

## 📄 File Explanations

| 📁 File                    | 📄 Purpose                                      |
| -------------------------- | ----------------------------------------------- |
| 🐍 application.py          | AWS Elastic Beanstalk WSGI entry point          |
| 🧪 app.py                  | Local Flask development server                  |
| 🤖 train_model.py          | Train LinearRegression and save model.pkl       |
| 📊 Student_Performance1.csv| 20-row dataset: SGPA1–4 → CGPA                  |
| 💾 model.pkl               | Trained model binary (generated locally)        |
| 📦 requirements.txt        | All Python dependencies with pinned versions    |
| 🚀 Procfile                | `gunicorn --bind :8000 --workers 3 application:application` |
| 🚫 .ebignore               | Excludes training scripts from AWS bundle       |
| ⚙️ python.config           | EB WSGIPath + static files configuration        |
| 🌐 index.html              | Main input form page                            |
| 📊 result.html             | Result display with ML badge + share feature    |

---

# 🎨 UI Themes

All themes use CSS variables and are stored in browser localStorage 🧠.

| 🎨 Theme         | 🌈 Colors       |
| ---------------- | --------------- |
| 🟣 Cosmic Purple | Purple + Indigo |
| 🔵 Ocean Blue    | Navy + Cyan     |
| 🟠 Sunset Glow   | Red + Orange    |
| 🟢 Forest Green  | Emerald + Mint  |

---

# 💻 Local Development Setup

## ✅ Prerequisites

* 🐍 Python 3.10+
* 📦 pip package manager

## 🚀 Step-by-Step Setup

```powershell
# Step 1: Open project folder
cd "c:\Users\pesal\Music\ML folder\cal project"

# Step 2: Create virtual environment
python -m venv venv
venv\Scripts\activate

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Train the ML model (generates model.pkl)
python train_model.py

# Step 5: Run the app
python app.py
```

## 🌐 Open Browser

```text
http://127.0.0.1:5000
```

---

# 🧠 Train the ML Model

The ML model is NOT stored in GitHub (binary file). You must generate it locally before running or deploying.

```powershell
python train_model.py
```

This script will:

✅ Load `Student_Performance1.csv`  
✅ Train a Linear Regression model  
✅ Print R² score and coefficients  
✅ Save `model.pkl` in the project root  
✅ Save `model_evaluation.png` (actual vs predicted plot)  

### Output Example

```text
Model trained successfully!
Coefficients: {'SGPA1': 0.2217, 'SGPA2': 0.2694, 'SGPA3': 0.2627, 'SGPA4': 0.2486}
Intercept: -0.0224

-- Evaluation on Test Set --
  MSE  : 0.0000
  RMSE : 0.0021
  R2   : 1.0000

Sample prediction for [7.48, 7.78, 7.83, 7.9]: CGPA = 7.75
[OK] Model saved to: model.pkl
```

> ⚠️ You must run `train_model.py` before deploying to AWS, so `model.pkl` is present in the project folder for the EB deployment bundle.

---

# ☁️ Deploy to AWS Elastic Beanstalk

> 🚀 Direct deployment from local machine to AWS.

---

## 🛠️ Step 1 — Install AWS CLI & EB CLI

```powershell
pip install awscli
pip install awsebcli

aws --version
eb --version
```

---

## 🔐 Step 2 — Create IAM User

1️⃣ Open AWS IAM Console  
2️⃣ Create user → `cgpa-deployer`  
3️⃣ Attach `AdministratorAccess`  
4️⃣ Create Access Keys  
5️⃣ Copy Access Key + Secret Key  

⚠️ Secret Key appears only once.

---

## ⚙️ Step 3 — Configure AWS Credentials

```powershell
aws configure
```

Enter:

```text
AWS Access Key ID
AWS Secret Access Key
Region → ap-south-1
Output format → json
```

Verify:

```powershell
aws sts get-caller-identity
```

---

## 🚀 Step 4 — Initialize Elastic Beanstalk

```powershell
eb init -p python-3.12 cgpa-calculator --region ap-south-1
```

---

## ☁️ Step 5 — Train Model & Deploy

```powershell
# Generate model.pkl first (IMPORTANT!)
python train_model.py

# Create environment and deploy
eb create cgpa-calculator-env --instance-type t3.micro
```

### 🔄 What Happens Automatically?

✅ ZIP project files (including model.pkl)  
✅ Upload to Amazon S3  
✅ Launch EC2 instance  
✅ Install dependencies from requirements.txt  
✅ Load model.pkl via joblib  
✅ Start Gunicorn on port 8000  
✅ Configure Load Balancer  
✅ Generate live URL  

⏳ Takes around 3–5 minutes.

---

## 🌐 Step 6 — Open Live App

```powershell
eb open
```

---

## 🔄 Redeploy After Code Changes

```powershell
# If you updated model or dataset, retrain first
python train_model.py

# Then deploy
eb deploy
```

---

# 📋 All Commands Reference

## ☁️ AWS CLI Commands

```powershell
aws configure
aws sts get-caller-identity
aws s3 ls
```

## 🚀 EB CLI Commands

```powershell
eb init -p python-3.12 cgpa-calculator --region ap-south-1
eb create cgpa-calculator-env --instance-type t3.micro
eb deploy
eb open
eb status
eb logs
eb logs --all
eb health
eb ssh
eb config
eb list
eb terminate cgpa-calculator-env
```

## 🐙 Git Commands

```powershell
git add .
git commit -m "your message"
git push origin main
```

---

# 🐛 Errors Encountered & Fixes

## ❌ Error 1 — `aws` Command Not Found

```text
aws : The term 'aws' is not recognized
```

**Cause:** AWS CLI not installed.  
**Fix:**
```powershell
pip install awscli
```

---

## ❌ Error 2 — Internal Server Error (500)

**Cause:** Old Jinja2 formatting syntax issue.

```html
<!-- Broken -->
{{ "%.1f"|format(avg) }}

<!-- Fixed -->
{{ cgpa }}
```

---

## ❌ Error 3 — 502 Bad Gateway (Port Mismatch)

**Cause:** Nginx expected port 8000 but Gunicorn was running on 8080.

```text
# Wrong
web: gunicorn --bind :8080 --workers 3 application:application

# Fixed
web: gunicorn --bind :8000 --workers 3 application:application
```

---

## ❌ Error 4 — EB Could Not Find Flask App

**Cause:** Elastic Beanstalk requires file `application.py` with object named `application`.

```python
# Correct
application = Flask(__name__)
```

---

## ❌ Error 5 — 502 Bad Gateway (sklearn Version Mismatch)

**Cause:** `model.pkl` was saved with scikit-learn `1.7.0` locally, but `requirements.txt` specified `1.5.2` on the server.

```text
InconsistentVersionWarning: Trying to unpickle estimator LinearRegression 
from version 1.7.0 when using version 1.5.2.
```

**Fix:** Pin `requirements.txt` to match your exact local version:

```text
scikit-learn==1.7.0
numpy==2.3.0
```

> ✅ Rule: Always match the scikit-learn and numpy versions in `requirements.txt` to the versions you used to run `train_model.py`.

---

## ❌ Error 6 — Git Push Rejected

```text
! [rejected] main -> main (fetch first)
```

**Cause:** Remote GitHub had newer commits than local.  
**Fix:**
```powershell
git pull origin main --rebase
git push origin main
```

---

# 💰 AWS Cost Estimate

| ☁️ Resource          | 🆓 Free Tier       | 💵 Paid Cost |
| -------------------- | ------------------ | ------------ |
| 🖥️ EC2 t3.micro     | 750 hrs/month      | ~$0.012/hr   |
| 🌐 Load Balancer     | 750 hrs/month      | ~$0.025/hr   |
| 📦 S3 Storage        | 5 GB free          | ~$0.023/GB   |
| 🌍 Data Transfer     | 1 GB free          | ~$0.09/GB    |
| ☁️ Elastic Beanstalk | Free               | Free         |
| 📊 CloudWatch        | Basic free metrics | Minimal      |

## 🛑 Stop All Charges

```powershell
eb terminate cgpa-calculator-env
```

---

# 👤 Project Info

| 📌 Category    | 📄 Details                       |
| -------------- | -------------------------------- |
| 🖥️ Type       | Full Stack Web App + ML          |
| 🐍 Language    | Python Flask                     |
| 🤖 ML Model    | Linear Regression (scikit-learn) |
| ☁️ Deployment  | AWS Elastic Beanstalk            |
| 🌍 Region      | ap-south-1 (Mumbai)              |
| 🖥️ Platform   | Amazon Linux 2023, Python 3.12   |
| ⚡ Instance     | t3.micro                         |
| 🐙 Repository  | GitHub                           |

---

# 📄 License

📜 MIT License

✅ Free to use  
✅ Free to modify  
✅ Educational use allowed  
✅ Commercial use allowed  

---

# 🌟 Final Notes

This project is a great **beginner-to-intermediate** level Full Stack + ML + Cloud Deployment project 🚀.

It teaches:

✅ Flask Web Development  
✅ Machine Learning with scikit-learn  
✅ Model Training, Saving & Loading (joblib)  
✅ Frontend UI Design (CSS Glassmorphism + Animations)  
✅ Dynamic JavaScript  
✅ AWS Elastic Beanstalk Deployment  
✅ Gunicorn + Nginx  
✅ Cloud Infrastructure Basics  
✅ Debugging Real Deployment Errors  
✅ Git + GitHub Version Control  

Perfect for:

🎓 Students  
👨‍💻 Beginners  
☁️ Cloud Learners  
🐍 Python / ML Developers  
🚀 Resume / Portfolio Projects  
