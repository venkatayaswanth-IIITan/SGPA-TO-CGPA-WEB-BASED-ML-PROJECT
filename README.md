# 🎓✨ CGPA Calculator — Full Stack Web App on AWS Elastic Beanstalk ☁️🚀

> 📚 A fully functional, beautifully designed **CGPA (Cumulative Grade Point Average) Calculator** web application built using **Python Flask** 🐍 and deployed live to **AWS Elastic Beanstalk** ☁️.
>
> 🌈 Features include:
>
> * 🎨 4 switchable UI themes
> * 📅 Dynamic semester selection
> * 📊 Animated CGPA results
> * 🏆 Grade classification
> * 🎉 Confetti celebration effects
> * 📤 Share button
> * ⚡ Fast deployment without GitHub
>
> 👨‍💻 Beginner-friendly + easy to understand for viewers.

---

# 🌐 Live Project URL

👉 [http://cgpa-calculator-env.eba-mkrp46vf.ap-south-1.elasticbeanstalk.com](http://cgpa-calculator-env.eba-mkrp46vf.ap-south-1.elasticbeanstalk.com)

---

# 📋 Table of Contents

1. 📖 About the Project
2. ✨ Features
3. 🛠️ Technology Stack
4. 📐 Calculation Logic
5. 📁 Project Structure
6. 🎨 UI Themes
7. 💻 Local Development Setup
8. ☁️ AWS Elastic Beanstalk Deployment
9. 📋 All Commands Reference
10. 🐛 Errors & Fixes
11. 💰 AWS Cost Estimate
12. 👤 Project Info
13. 📄 License

---

# 📖 About the Project

This project was built as a practical web application 🖥️ to help students calculate their **CGPA (Cumulative Grade Point Average)** across multiple semesters 📚.

🎓 Most universities in India use a **10-point GPA scale**, and this calculator fully supports that system.

## 🚀 Project Evolution

Initially, the app started as a very simple:

* 🧮 Marks Calculator
* Only 3 subject inputs

Later, it was redesigned and upgraded into a complete CGPA Calculator with:

✅ Dynamic semester selector (1–8 semesters)
✅ GPA input fields generated automatically
✅ Multi-theme animated UI
✅ Glassmorphism design ✨
✅ Result page with animations
✅ Progress bars 📊
✅ Grade badges 🏆
✅ Confetti effects 🎉
✅ Share result feature 📤

The entire project was deployed directly from a **Windows local machine** 💻 using the **EB CLI**.

⚡ No GitHub.
⚡ No CI/CD pipeline.
⚡ Direct deployment to AWS.

---

# ✨ Features

| 🌟 Feature              | 📄 Description                                                   |
| ----------------------- | ---------------------------------------------------------------- |
| 🎨 4 UI Themes          | Cosmic Purple 🟣, Ocean Blue 🔵, Sunset Glow 🟠, Forest Green 🟢 |
| 📅 Semester Selector    | Select 1–8 semesters dynamically                                 |
| 📊 CGPA Calculation     | Calculates CGPA instantly on a 10-point scale                    |
| 🏆 Grade Classification | Automatically assigns grade based on CGPA                        |
| 📈 Progress Bar         | Animated performance bar                                         |
| 🎉 Confetti Effect      | Celebration animation when CGPA ≥ 6.0                            |
| 📊 Semester Breakdown   | Displays GPA of each semester                                    |
| 📤 Share / Copy         | Share results using Web Share API                                |
| 🌊 Animated Background  | Moving gradient effects                                          |
| ✨ Floating Particles    | 18 animated particles in background                              |
| 🔄 Ripple Effect        | Button click ripple animation                                    |
| 🧠 Theme Memory         | Saves selected theme using localStorage                          |
| 📱 Responsive Design    | Mobile + Tablet + Desktop support                                |

---

# 🛠️ Technology Stack

# 🐍 Backend Technologies

| ⚙️ Technology | 📌 Version         | 📄 Description                   |
| ------------- | ------------------ | -------------------------------- |
| 🐍 Python     | 3.13.3             | Core programming language        |
| 🌶️ Flask     | 3.1.0              | Lightweight Python web framework |
| 🧩 Jinja2     | Bundled with Flask | Dynamic HTML templating engine   |
| 🚀 Gunicorn   | 22.0.0             | Production-grade WSGI server     |

## 🖥️ Frontend Technologies

| 💻 Technology       | 📄 Description                      |
| ------------------- | ----------------------------------- |
| 🌐 HTML5            | Structure of the web pages          |
| 🎨 Vanilla CSS      | Styling + animations + themes       |
| ⚡ JavaScript (ES6+) | Dynamic UI interactions             |
| 🔤 Google Fonts     | Modern typography using Outfit font |

## ☁️ Cloud Infrastructure

| ☁️ Service               | 📄 Description                       |
| ------------------------ | ------------------------------------ |
| ☁️ AWS Elastic Beanstalk | Manages deployment + infrastructure  |
| 🖥️ Amazon EC2           | Runs Flask app + Gunicorn            |
| 📦 Amazon S3             | Stores deployment ZIP files          |
| 🌐 Elastic Load Balancer | Distributes incoming traffic         |
| 🔁 Nginx                 | Reverse proxy server                 |
| 🔐 AWS IAM               | User permissions + access management |
| 📊 CloudWatch            | Monitoring + alarms                  |

## 🧰 Developer Tools

| 🛠️ Tool   | 📄 Description                  |
| ---------- | ------------------------------- |
| ☁️ AWS CLI | Configure AWS locally           |
| 🚀 EB CLI  | Deploy/manage Elastic Beanstalk |
| 📦 pip     | Install Python packages         |

---

# 📐 Calculation Logic (NOT ML — Pure Statistics) 📊

> ⚠️ Important:
> This project does NOT use:
>
> * 🤖 Machine Learning
> * 🧠 Neural Networks
> * 📉 Regression Models
> * 🤖 AI Algorithms
>
> ✅ It only uses a simple arithmetic mean formula.

## 🧮 Formula Used

```text
CGPA = (GPA_Sem1 + GPA_Sem2 + GPA_Sem3 + ... + GPA_SemN) / N
```

## ⚙️ How it Works in Python (`application.py`)

```python
@application.route('/calculate', methods=['POST'])
def calculate():
    # Step 1: Read how many semesters were selected
    num_sems = int(request.form.get('num_sems', 0))

    # Step 2: Collect GPA values
    sem_gpas = []
    for i in range(1, num_sems + 1):
        val = request.form.get(f'sem{i}', 0)
        try:
            gpa = float(val)
        except ValueError:
            gpa = 0.0
        sem_gpas.append(round(gpa, 2))

    # Step 3: Calculate CGPA
    cgpa = round(sum(sem_gpas) / num_sems, 2) if num_sems > 0 else 0.0

    # Step 4: Send result to HTML page
    return render_template('result.html', cgpa=cgpa, sem_gpas=sem_gpas, num_sems=num_sems)
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

## ❓ Why This is NOT Machine Learning

| 🤖 Machine Learning      | 🧮 This Project         |
| ------------------------ | ----------------------- |
| Uses training data       | Uses direct user input  |
| Predicts unknown outputs | Calculates exact result |
| Uses models & weights    | Uses arithmetic formula |
| Requires training        | No training needed      |

---

# 📁 Project Structure

```text
cal project/
│
├── application.py
├── app.py
├── requirements.txt
├── Procfile
├── .ebignore
├── .ebextensions/
│   └── python.config
├── .elasticbeanstalk/
│   └── config.yml
└── templates/
    ├── index.html
    └── result.html
```

## 📄 File Explanations

| 📁 File             | 📄 Purpose                        |
| ------------------- | --------------------------------- |
| 🐍 application.py   | AWS Elastic Beanstalk entry point |
| 🧪 app.py           | Local testing file                |
| 📦 requirements.txt | Python dependencies               |
| 🚀 Procfile         | Gunicorn startup command          |
| 🚫 .ebignore        | Excludes unnecessary files        |
| ⚙️ python.config    | EB configuration settings         |
| 🌐 index.html       | Main input form page              |
| 📊 result.html      | Result display page               |

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

# Step 4: Run the app
python app.py
```

## 🌐 Open Browser

```text
http://127.0.0.1:5000
```

⚠️ Flask debug server should only be used for development.

---

# ☁️ Deploy to AWS Elastic Beanstalk (No GitHub Required)

> 🚀 Direct deployment from local machine to AWS.
>
> ❌ No GitHub
> ❌ No CI/CD
> ✅ Only EB CLI

---

# 🛠️ Step 1 — Install AWS CLI & EB CLI

```powershell
pip install awscli
pip install awsebcli

aws --version
eb --version
```

---

# 🔐 Step 2 — Create IAM User

## Steps:

1️⃣ Open AWS IAM Console
2️⃣ Create user → `cgpa-deployer`
3️⃣ Attach `AdministratorAccess`
4️⃣ Create Access Keys
5️⃣ Copy Access Key + Secret Key

⚠️ Secret Key appears only once.

---

# ⚙️ Step 3 — Configure AWS Credentials

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

# 🚀 Step 4 — Initialize Elastic Beanstalk

```powershell
eb init -p python-3.12 cgpa-calculator --region ap-south-1
```

This creates:

```text
.elasticbeanstalk/config.yml
```

---

# ☁️ Step 5 — Create Environment & Deploy

```powershell
eb create cgpa-calculator-env --instance-type t3.micro
```

## 🔄 What Happens Automatically?

✅ ZIP project files
✅ Upload to Amazon S3
✅ Launch EC2 instance
✅ Install dependencies
✅ Start Gunicorn
✅ Configure Load Balancer
✅ Generate live URL

⏳ Takes around 3–5 minutes.

---

# 🌐 Step 6 — Open Live App

```powershell
eb open
```

---

# 🔄 Update App After Code Changes

```powershell
eb deploy
```

This redeploys updated code automatically.

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

eb status | findstr CNAME

eb terminate cgpa-calculator-env

eb terminate --all
```

---

# 🐛 Errors Encountered & Fixes

# ❌ Error 1 — `aws` Command Not Found

## 📄 Error Message

```text
aws : The term 'aws' is not recognized
```

## 💥 Cause

AWS CLI was not installed.

## ✅ Fix

```powershell
pip install awscli
```

---

# ❌ Error 2 — Internal Server Error (500)

## 💥 Cause

Old Jinja2 formatting syntax issue.

## ❌ Broken Code

```html
{{ "%.1f"|format(avg) }}
```

## ✅ Fixed Version

```python
cgpa = round(sum(sem_gpas) / num_sems, 2)
```

```html
{{ cgpa }}
```

---

# ❌ Error 3 — 502 Bad Gateway

## 💥 Cause

Nginx expected port 8000 but Gunicorn was running on 8080.

## ❌ Wrong Procfile

```text
web: gunicorn --bind :8080 --workers 3 application:application
```

## ✅ Fixed Procfile

```text
web: gunicorn --bind :8000 --workers 3 application:application
```

---

# ❌ Error 4 — EB Could Not Find Flask App

## 💥 Cause

Elastic Beanstalk requires:

✅ File name → `application.py`
✅ Flask object → `application`

## ✅ Correct Code

```python
application = Flask(__name__)
```

---

# ❌ Error 5 — Dependency Conflicts

## ⚠️ Warning

```text
boto3 requires botocore<1.39.0
```

## ✅ Impact

No major issue.
Both `aws` and `eb` commands worked properly.

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

| 📌 Category   | 📄 Details            |
| ------------- | --------------------- |
| 🖥️ Type      | Full Stack Web App    |
| 🐍 Language   | Python Flask          |
| ☁️ Deployment | AWS Elastic Beanstalk |
| 🌍 Region     | ap-south-1 (Mumbai)   |
| 🖥️ Platform  | Amazon Linux 2023     |
| ⚡ Instance    | t3.micro              |

---

# 📄 License

📜 MIT License

✅ Free to use
✅ Free to modify
✅ Educational use allowed
✅ Commercial use allowed

---

# 🌟 Final Notes

This project is a great beginner-to-intermediate level Full Stack + Cloud Deployment project 🚀.

It teaches:

✅ Flask Development
✅ Frontend UI Design
✅ Dynamic JavaScript
✅ AWS Deployment
✅ Elastic Beanstalk
✅ Gunicorn + Nginx
✅ Cloud Infrastructure Basics
✅ Debugging Real Deployment Errors

Perfect for:

🎓 Students
👨‍💻 Beginners
☁️ Cloud Learners
🐍 Python Developers
🚀 Resume Projects

---

📄 Source File Reference: fileciteturn0file0
