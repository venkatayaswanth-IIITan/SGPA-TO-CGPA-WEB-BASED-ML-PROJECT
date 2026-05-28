# 🎓 CGPA Calculator — Full Stack Web App on AWS Elastic Beanstalk

> A fully functional, beautifully designed **CGPA (Cumulative Grade Point Average) Calculator**
> web application built using **Python Flask** and deployed live to **AWS Elastic Beanstalk**.
> Features 4 switchable UI themes, dynamic semester selection, animated results,
> grade classification, confetti effects, and a share button — all without using GitHub.

**🌐 Live URL:**
👉 [http://cgpa-calculator-env.eba-mkrp46vf.ap-south-1.elasticbeanstalk.com](http://cgpa-calculator-env.eba-mkrp46vf.ap-south-1.elasticbeanstalk.com)

---

## 📋 Table of Contents

1. [About the Project](#-about-the-project)
2. [Features](#-features)
3. [Technology Stack](#️-technology-stack)
4. [Calculation Logic](#-calculation-logic-not-ml--pure-statistics)
5. [Project Structure](#-project-structure)
6. [UI Themes](#-ui-themes)
7. [Local Development Setup](#-local-development-setup)
8. [AWS Elastic Beanstalk Deployment (No GitHub)](#️-deploy-to-aws-elastic-beanstalk-no-github-required)
9. [All Commands Reference](#-all-commands-reference)
10. [Errors & Fixes](#-errors-encountered--how-they-were-fixed)
11. [AWS Cost Estimate](#-aws-cost-estimate)

---

## 📖 About the Project

This project was built as a practical web application to help students calculate their **CGPA** (Cumulative Grade Point Average) across multiple semesters. Most university systems in India use a **10-point GPA scale**, and this calculator supports that standard.

The app was originally a simple "Marks Calculator" with 3 subject inputs. It was then redesigned and upgraded into a full CGPA Calculator with:
- A dynamic semester selector (1–8 semesters)
- Per-semester GPA inputs that animate in based on selection
- A beautiful multi-theme UI with glassmorphism and animated backgrounds
- A results page with per-semester breakdown, animated progress bar, and grade classification

The entire project was **deployed to AWS Elastic Beanstalk directly from a local Windows machine** using the EB CLI — no GitHub push, no CI/CD pipeline required.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎨 **4 UI Themes** | Cosmic Purple, Ocean Blue, Sunset Glow, Forest Green — switchable with one click, saved in browser localStorage |
| 📅 **Semester Selector** | A `<select>` dropdown (1–8 semesters) — GPA input fields appear dynamically via JavaScript |
| 📊 **CGPA Calculation** | Instantly calculates CGPA on a 10-point scale using arithmetic mean |
| 🏆 **Grade Classification** | Auto-detects grade: O (Outstanding) / A+ / A / B+ / B / Below Average |
| 📈 **Progress Bar** | Animated bar counts from 0% to your performance percentage |
| 🎉 **Confetti Effect** | 55 colorful confetti pieces fire when CGPA ≥ 6.0 |
| 📊 **Semester Breakdown** | Result page shows each semester's GPA with an animated mini-bar |
| 📤 **Share / Copy** | Share results using Web Share API or copies to clipboard as fallback |
| 🌊 **Animated Background** | Gradient background shifts continuously, glowing orbs float in background |
| ✨ **Floating Particles** | 18 animated particles rise in the background |
| 🔄 **Ripple Effect** | Button click triggers a ripple animation |
| 🧠 **Theme Memory** | Selected theme persists across both pages via `localStorage` |
| 📱 **Responsive Design** | Works on mobile, tablet, and desktop |

---

## 🛠️ Technology Stack

### Backend

| Technology | Version | Description |
|---|---|---|
| **Python** | 3.13.3 | Core programming language used to write the application logic |
| **Flask** | 3.1.0 | Lightweight Python web framework that handles HTTP routes, form POST data, and renders HTML templates. Used `render_template()` for Jinja2 templating and `request.form` to receive semester GPA values from the frontend form |
| **Jinja2** | (bundled with Flask) | Template engine that lets Python variables render inside HTML. Used `{{ cgpa }}`, `{% for gpa in sem_gpas %}`, `{{ loop.index }}` etc. to dynamically generate the result page |
| **Gunicorn** | 22.0.0 | Production-grade WSGI (Web Server Gateway Interface) HTTP server. Flask's built-in server is only for development. Gunicorn handles multiple workers (3 parallel processes) in the AWS environment |

### Frontend

| Technology | Description |
|---|---|
| **HTML5** | Semantic page structure — uses `<form>`, `<select>`, `<input type="number">`, `<button>` elements with proper `id` and `name` attributes for form submission |
| **Vanilla CSS** | All styles written in pure CSS — no frameworks. Uses CSS Variables (`--accent-from`, `--btn-shadow` etc.) for 4 complete themes, `backdrop-filter: blur()` for glassmorphism, `@keyframes` for all animations |
| **JavaScript (ES6+)** | Handles dynamic UI: theme switching, semester selector change event, dynamic GPA field injection, ripple effect, progress bar animation, confetti generation, Web Share API |
| **Google Fonts (Outfit)** | Modern, premium font loaded from Google CDN for clean readable typography |

### Cloud Infrastructure

| Service | Description |
|---|---|
| **AWS Elastic Beanstalk** | Fully managed PaaS that automatically handles EC2 provisioning, load balancing, auto-scaling, and deployment. We only provide code + Procfile |
| **Amazon EC2 (t3.micro)** | The virtual server instance that runs gunicorn + the Flask app. Free tier eligible for 12 months |
| **Amazon S3** | Auto-created bucket stores each deployment zip (`app-XXXXXX.zip`) uploaded by `eb create` and `eb deploy` |
| **Elastic Load Balancer (ALB)** | Auto-created Application Load Balancer that distributes incoming HTTP requests to the EC2 instance. Also sends health check requests every 15s |
| **Nginx** | Managed web server auto-installed by EB on the EC2 instance. Acts as a reverse proxy: Internet → Nginx (port 80) → Gunicorn (port 8000) → Flask app |
| **AWS IAM** | Identity and Access Management. We created a user `cgpa-deployer` with `AdministratorAccess` policy to allow CLI-based deployments |
| **CloudWatch** | Auto-created alarms for CPU high/low — triggers Auto Scaling policies |

### Developer Tools

| Tool | Description |
|---|---|
| **AWS CLI** | Command line tool to configure AWS credentials (`aws configure`) and verify identity (`aws sts get-caller-identity`) |
| **EB CLI** | Elastic Beanstalk CLI — the primary tool to `init`, `create`, `deploy`, `open`, `logs`, and `terminate` EB environments |
| **pip** | Python package installer — used to install Flask, gunicorn, awscli, awsebcli |

---

## 📐 Calculation Logic (NOT ML — Pure Statistics)

> **Important Note:** This project does **not** use any Machine Learning, Regression models, Neural Networks, or any AI/ML algorithms.
> It uses simple **arithmetic mean** — a fundamental statistical calculation.

### Formula

```
CGPA = (GPA_Sem1 + GPA_Sem2 + GPA_Sem3 + ... + GPA_SemN) / N
```

### How it works in code (`application.py`):

```python
@application.route('/calculate', methods=['POST'])
def calculate():
    # Step 1: Read how many semesters were selected
    num_sems = int(request.form.get('num_sems', 0))

    # Step 2: Loop through each semester and collect GPA value
    sem_gpas = []
    for i in range(1, num_sems + 1):
        val = request.form.get(f'sem{i}', 0)   # reads sem1, sem2, sem3...
        try:
            gpa = float(val)
        except ValueError:
            gpa = 0.0                            # default to 0 if invalid
        sem_gpas.append(round(gpa, 2))

    # Step 3: Calculate CGPA using arithmetic mean
    cgpa = round(sum(sem_gpas) / num_sems, 2) if num_sems > 0 else 0.0

    # Step 4: Pass results to result.html template
    return render_template('result.html', cgpa=cgpa, sem_gpas=sem_gpas, num_sems=num_sems)
```

### Grade Classification (in `result.html` JavaScript):

```javascript
if      (cgpa >= 9.0) → Grade O  — Outstanding
else if (cgpa >= 8.0) → Grade A+ — Excellent
else if (cgpa >= 7.0) → Grade A  — Very Good
else if (cgpa >= 6.0) → Grade B+ — Good
else if (cgpa >= 5.0) → Grade B  — Average
else                  → Below Average
```

### Why this is NOT Machine Learning:
- **ML Regression** would: Take historical data, train a model, and **predict** an unknown output
- **This app** does: Take known inputs (your own GPA values), apply a fixed mathematical formula, and compute a deterministic result
- There is no training, no model, no weights, no prediction — only calculation

---

## 📁 Project Structure

```
cal project/
│
├── application.py              ← AWS EB entry point
│                                  Flask instance MUST be named 'application'
│                                  EB's Python platform auto-detects this file
│
├── app.py                      ← Local development runner
│                                  Flask instance named 'app', runs on debug mode
│                                  Used only for local testing with 'python app.py'
│
├── requirements.txt            ← Python dependencies list
│                                  EB reads this file to pip install on EC2
│                                  Contains: Flask==3.1.0, gunicorn==22.0.0
│
├── Procfile                    ← Process startup command for EB
│                                  Tells gunicorn: bind to port 8000, use 3 workers
│                                  'web: gunicorn --bind :8000 --workers 3 application:application'
│
├── .ebignore                   ← Files to EXCLUDE from deployment zip
│                                  Similar to .gitignore but for Elastic Beanstalk
│                                  Excludes: __pycache__, venv, .git, .idea etc.
│
├── .ebextensions/
│   └── python.config           ← EB platform configuration file (YAML format)
│                                  Explicitly sets WSGIPath to application:application
│                                  Maps /static directory for nginx to serve directly
│
├── .elasticbeanstalk/
│   └── config.yml              ← Auto-generated by 'eb init'
│                                  Stores app name, region, platform settings
│
└── templates/
    ├── index.html              ← CGPA input form page
    │                              Multi-theme UI, semester selector,
    │                              Dynamic GPA field generation via JS
    │
    └── result.html             ← Results display page
                                   Shows CGPA hero value, animated progress bar,
                                   Per-semester breakdown with mini bars,
                                   Grade badge, confetti, share button
```

---

## 🎨 UI Themes

All 4 themes use CSS custom properties (variables) and are applied via `data-theme` attribute on the `<html>` element. Theme preference is saved in `localStorage` key `cgpa-theme` and automatically restored on page load.

| Theme | Colors | CSS Selector |
|---|---|---|
| 🟣 **Cosmic Purple** (default) | Deep purple `#0f0c29` → Indigo `#6366f1` → Purple `#a855f7` | `:root` (no data-theme) |
| 🔵 **Ocean Blue** | Dark navy `#0a2342` → Teal `#126872` → Cyan `#00e5ff` | `[data-theme="ocean"]` |
| 🟠 **Sunset Glow** | Dark crimson `#1a0533` → Red `#6b1a2a` → Orange `#ff9800` | `[data-theme="sunset"]` |
| 🟢 **Forest Green** | Deep forest `#0b1d11` → Emerald `#1b4332` → Mint `#52b788` | `[data-theme="forest"]` |

---

## 💻 Local Development Setup

### Prerequisites
- Python 3.10 or higher installed
- pip package manager

### Step-by-Step

```powershell
# Step 1: Open terminal and navigate to project folder
cd "c:\Users\pesal\Music\ML folder\cal project"

# Step 2: (Optional) Create a virtual environment
python -m venv venv
venv\Scripts\activate

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Run the development server
python app.py

# Step 5: Open browser and go to:
# http://127.0.0.1:5000
```

> **Note:** `app.py` uses Flask's built-in development server with `debug=True`.
> This auto-reloads on file changes. Never use this in production.

---

## ☁️ Deploy to AWS Elastic Beanstalk (No GitHub Required)

> This method deploys **directly from your local machine to AWS** using the EB CLI tool.
> No Git repository, no GitHub push, no CI/CD pipeline is needed.
> The EB CLI zips your project files and uploads them directly to AWS S3.

### Step 1 — Install AWS CLI and EB CLI

```powershell
# Install AWS Command Line Interface
pip install awscli

# Install Elastic Beanstalk Command Line Interface
pip install awsebcli

# Verify both are installed correctly
aws --version      # Should show: aws-cli/1.x.x
eb --version       # Should show: EB CLI 3.x.x
```

### Step 2 — Create IAM User in AWS Console

An IAM (Identity and Access Management) user gives the CLI permission to create and manage AWS resources.

1. Go to 👉 **https://console.aws.amazon.com/iam/home#/users**
2. Click **"Create user"**
   - User name: `cgpa-deployer`
   - Click **Next**
3. Under "Set permissions" select **"Attach policies directly"**
   - Search `AdministratorAccess` → ✅ check it
   - Click **Next** → **Create user**
4. Click on the user `cgpa-deployer` you just created
5. Go to **"Security credentials"** tab
6. Scroll to **"Access keys"** → click **"Create access key"**
7. Choose **"Command Line Interface (CLI)"** → check confirmation → **Next** → **Create access key**
8. ⚠️ **COPY BOTH KEYS NOW** — Secret Key is shown only once!

### Step 3 — Configure AWS Credentials Locally

```powershell
aws configure
```

Enter when prompted:
```
AWS Access Key ID [None]:      AKIAXXXXXXXXXXXXXXXX   ← your Access Key ID
AWS Secret Access Key [None]:  xxxxxxxxxxxxxxxx       ← your Secret Access Key
Default region name [None]:    ap-south-1             ← Mumbai (closest to India)
Default output format [None]:  json
```

Verify it worked:
```powershell
aws sts get-caller-identity
# Should return your Account ID, UserID, and ARN
```

### Step 4 — Initialize Elastic Beanstalk App

```powershell
eb init -p python-3.12 cgpa-calculator --region ap-south-1
```

- `-p python-3.12` → Use Python 3.12 platform
- `cgpa-calculator` → Name of your EB application
- `--region ap-south-1` → Deploy in Mumbai region
- When asked **"Do you want to set up SSH?"** → type `n`

This creates a `.elasticbeanstalk/config.yml` file locally.

### Step 5 — Create Environment and Deploy

```powershell
eb create cgpa-calculator-env --instance-type t3.micro
```

What happens automatically:
1. 📦 Zips all project files (excluding `.ebignore` entries)
2. ☁️ Uploads zip to an auto-created S3 bucket
3. 🖥️ Launches a new EC2 t3.micro instance
4. 🔧 Installs Python, reads `requirements.txt`, runs `pip install`
5. 🚀 Reads `Procfile` and starts gunicorn on port 8000
6. 🌐 Creates Load Balancer, Security Groups, Auto Scaling rules
7. ✅ Reports environment URL when ready

Takes approximately **3–5 minutes**.

### Step 6 — Open Live App

```powershell
eb open
# Automatically opens your live URL in the default browser
```

---

## 🔄 Update App After Code Changes

Whenever you change any code file, just run:

```powershell
eb deploy
```

This will:
1. Zip the updated project
2. Upload to S3
3. Deploy to the running EC2 instance (hot-reload, ~30 seconds)

No need to terminate and recreate the environment.

---

## 📋 All Commands Reference

### AWS CLI Commands

```powershell
# Configure AWS credentials
aws configure

# Verify credentials and get account info
aws sts get-caller-identity

# List all S3 buckets (to verify AWS access)
aws s3 ls
```

### EB CLI Commands

```powershell
# Initialize EB application in current directory
eb init -p python-3.12 cgpa-calculator --region ap-south-1

# Create new environment and deploy for the first time
eb create cgpa-calculator-env --instance-type t3.micro

# Deploy updated code to existing environment
eb deploy

# Open live URL in browser
eb open

# Check environment status and health
eb status

# Stream last 100 lines of server logs
eb logs

# Download full logs to .elasticbeanstalk/logs/ folder
eb logs --all

# Detailed real-time instance health
eb health

# SSH into the EC2 instance (if SSH key was set up)
eb ssh

# Modify environment configuration settings
eb config

# List all EB environments in the app
eb list

# Print the live URL without opening browser
eb status | findstr CNAME

# ⚠️ TERMINATE environment (stops all billing for that env)
eb terminate cgpa-calculator-env

# ⚠️ Delete the entire EB application
eb terminate --all
```

---

## 🐛 Errors Encountered & How They Were Fixed

### ❌ Error 1 — `aws` command not found in PowerShell

**Full Error Message:**
```
aws : The term 'aws' is not recognized as the name of a cmdlet,
function, script file, or operable program.
CommandNotFoundException
```

**Why it happened:**
AWS CLI was not installed on the machine. PowerShell could not find the `aws` binary.

**How it was fixed:**
```powershell
pip install awscli
```
After install, `aws --version` confirmed it worked:
```
aws-cli/1.45.16 Python/3.13.3 Windows/11
```

---

### ❌ Error 2 — Internal Server Error on Result Page (Jinja2 Format Filter Bug)

**What happened:**
After submitting the marks form, the result page crashed with a `500 Internal Server Error`.

**Root Cause in Code:**
```html
<!-- This line was broken in newer Jinja2 -->
{{ "%.1f"|format(avg) }}
```
The `"%.1f"|format()` filter uses Python's old `%` string formatting syntax inside Jinja2 — this stopped working reliably in newer Jinja2 versions bundled with Flask 3.x.

**How it was fixed:**
Moved the formatting to Python (Flask) side:
```python
# In app.py — round the value in Python before sending to template
cgpa = round(sum(sem_gpas) / num_sems, 2)
```
Then in the template:
```html
<!-- Just display directly — already rounded to 2 decimal places -->
{{ cgpa }}
```

---

### ❌ Error 3 — 502 Bad Gateway After Deployment

**Full Error:**
Browser showed: `502 Bad Gateway`

**Nginx Error Log showed:**
```
connect() failed (111: Connection refused) while connecting to upstream
upstream: http://127.0.0.1:8000/
```

**Root Cause:**
AWS Elastic Beanstalk's Nginx configuration by default proxies all incoming requests to the application on **port 8000**. However, the `Procfile` told gunicorn to listen on **port 8080**:

```
# Wrong Procfile
web: gunicorn --bind :8080 --workers 3 application:application
                      ^^^^^ nginx sends to 8000, gunicorn listens on 8080 → mismatch!
```

**How it was fixed:**
Changed port in `Procfile` from `8080` → `8000`:
```diff
- web: gunicorn --bind :8080 --workers 3 application:application
+ web: gunicorn --bind :8000 --workers 3 application:application
```

Then redeployed:
```powershell
eb deploy
```

**Verified fixed by:**
```powershell
Invoke-WebRequest -Uri "http://cgpa-calculator-env.eba-mkrp46vf.ap-south-1.elasticbeanstalk.com" -UseBasicParsing | Select-Object StatusCode
# Output: StatusCode 200 ✅
```

---

### ❌ Error 4 — EB Could Not Find Flask App (WSGI Entry Point)

**Root Cause:**
AWS Elastic Beanstalk's Python platform automatically looks for:
- A file named **`application.py`**
- A WSGI callable named **`application`** inside it

The original file was `app.py` with `app = Flask(__name__)` — both the filename and variable name were wrong for EB.

**How it was fixed:**
Created a new file `application.py`:
```python
# application.py — correct EB entry point
application = Flask(__name__)   # must be named 'application'

@application.route('/')
def index():
    return render_template('index.html')
```

Also added to `.ebextensions/python.config`:
```yaml
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: application:application
```

---

### ❌ Error 5 — Dependency Conflicts During awscli Install

**Warning shown:**
```
ERROR: pip's dependency resolver does not currently take into account all the packages...
boto3 1.38.35 requires botocore<1.39.0,>=1.38.35, but you have botocore 1.43.16
```

**Why it happened:**
`awscli` was installed after `awsebcli`. Both use `boto3`/`botocore` internally but require different version ranges, causing a conflict warning.

**Impact:** None — the warning was informational only. Both `aws` and `eb` commands worked correctly despite the conflict warning.

**Lesson:** This is a known pip dependency resolver limitation. Always verify with `aws --version` and `eb --version` rather than trusting warning messages.

---

## 💰 AWS Cost Estimate

| AWS Resource | Free Tier Allowance | Cost After Free Tier |
|---|---|---|
| **EC2 t3.micro** | 750 hours/month for 12 months | ~$0.012/hour |
| **Elastic Load Balancer** | 750 hours/month for 12 months | ~$0.025/hour |
| **S3 Storage** | 5 GB storage + 20,000 GET requests/month | Minimal (~$0.023/GB) |
| **Data Transfer** | 1 GB/month outbound | $0.09/GB after |
| **Elastic Beanstalk** | Always free | Free |
| **CloudWatch** | 10 metrics + basic alarms free | Minimal |

### To Stop All Charges:

```powershell
# Terminates EC2, Load Balancer, Auto Scaling Group, Security Groups
eb terminate cgpa-calculator-env

# Confirm when prompted: type 'cgpa-calculator-env'
```

> **Note:** S3 bucket and stored deployment zips may persist. Delete them manually from the AWS S3 console if needed.

---

## 👤 Project Info

- **Type:** Full-Stack Web Application
- **Language:** Python (Flask)
- **Deployment:** AWS Elastic Beanstalk (Direct CLI deploy, no GitHub)
- **Region:** `ap-south-1` — Mumbai, India
- **Platform:** Python 3.12 on 64-bit Amazon Linux 2023
- **Instance:** t3.micro (Free Tier eligible)

---

## 📄 License

MIT License — free to use, modify, and distribute for educational and commercial purposes.
#   S G P A - T O - C G P A - W E B - B A S E D - M L - P R O J E C T  
 