"""
train_model.py
--------------
Train a Linear Regression model on Student_Performance1.csv
and save it as model.pkl for use in the Flask app.

Run this script once (or whenever you update your dataset):
    python train_model.py
"""

import matplotlib
matplotlib.use('Agg')  # Non-interactive backend (no GUI window needed)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import os
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# ─────────────────────────────────────────────
# 1. Load dataset
# ─────────────────────────────────────────────
CSV_PATH = os.path.join(os.path.dirname(__file__), "Student_Performance1.csv")
data = pd.read_csv(CSV_PATH)

print("Dataset loaded successfully:")
print(data.to_string())
print(f"\nShape: {data.shape}")

# ─────────────────────────────────────────────
# 2. Features & Target
# ─────────────────────────────────────────────
FEATURE_COLS = ["SGPA1", "SGPA2", "SGPA3", "SGPA4"]
TARGET_COL   = "CGPA"

X = data[FEATURE_COLS]
y = data[TARGET_COL]

# ─────────────────────────────────────────────
# 3. Train / Test Split
# ─────────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"\nTraining samples : {len(X_train)}")
print(f"Testing  samples : {len(X_test)}")

# ─────────────────────────────────────────────
# 4. Train Linear Regression
# ─────────────────────────────────────────────
model = LinearRegression()
model.fit(X_train, y_train)

print("\nModel trained successfully!")
print(f"Coefficients : {dict(zip(FEATURE_COLS, model.coef_.round(4)))}")
print(f"Intercept    : {model.intercept_:.4f}")

# ─────────────────────────────────────────────
# 5. Evaluate
# ─────────────────────────────────────────────
y_pred = model.predict(X_test)
mse  = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2   = r2_score(y_test, y_pred)

print(f"\n-- Evaluation on Test Set --")
print(f"  MSE  : {mse:.4f}")
print(f"  RMSE : {rmse:.4f}")
print(f"  R2   : {r2:.4f}")

# ─────────────────────────────────────────────
# 6. Quick sanity-check prediction
# ─────────────────────────────────────────────
sample = pd.DataFrame([[7.48, 7.78, 7.83, 7.9]], columns=FEATURE_COLS)
pred   = model.predict(sample)
print(f"\nSample prediction for {sample.values.tolist()[0]}: CGPA = {pred[0]:.2f}")

# ─────────────────────────────────────────────
# 7. Save model
# ─────────────────────────────────────────────
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")
joblib.dump(model, MODEL_PATH)
print(f"\n[OK] Model saved to: {MODEL_PATH}")

# ─────────────────────────────────────────────
# 8. Optional: Visualise Actual vs Predicted
# ─────────────────────────────────────────────
plt.figure(figsize=(7, 5))
plt.scatter(y_test, y_pred, color="#a855f7", edgecolors="white", s=100, zorder=3)
plt.plot([y_test.min(), y_test.max()],
         [y_test.min(), y_test.max()],
         color="#6366f1", linewidth=2, linestyle="--", label="Perfect fit")
plt.xlabel("Actual CGPA", fontsize=12)
plt.ylabel("Predicted CGPA", fontsize=12)
plt.title(f"Actual vs Predicted CGPA  (R² = {r2:.4f})", fontsize=13, fontweight="bold")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(os.path.dirname(__file__), "model_evaluation.png"), dpi=150)
plt.show()
print("[DONE] Evaluation plot saved as model_evaluation.png")
