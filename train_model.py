import os
import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


# =========================================================
# PATHS
# =========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATASET_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "resume_dataset.csv"
)

MODEL_DIR = os.path.join(
    BASE_DIR,
    "models"
)

os.makedirs(MODEL_DIR, exist_ok=True)


# =========================================================
# LOAD DATASET
# =========================================================

df = pd.read_csv(DATASET_PATH)

df = df.dropna(
    subset=["resume_text", "job_role"]
)

X = df["resume_text"].astype(str)
y = df["job_role"].astype(str)


# =========================================================
# TRAIN TEST SPLIT
# =========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# =========================================================
# TF-IDF
# =========================================================

vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    ngram_range=(1, 2)
)

X_train_tfidf = vectorizer.fit_transform(
    X_train
)

X_test_tfidf = vectorizer.transform(
    X_test
)


# =========================================================
# MACHINE LEARNING MODEL
# =========================================================

model = LogisticRegression(
    max_iter=2000,
    random_state=42
)

model.fit(
    X_train_tfidf,
    y_train
)


# =========================================================
# PREDICTION
# =========================================================

y_pred = model.predict(
    X_test_tfidf
)


# =========================================================
# MODEL EVALUATION
# =========================================================

accuracy = accuracy_score(
    y_test,
    y_pred
)

report = classification_report(
    y_test,
    y_pred,
    output_dict=True,
    zero_division=0
)

labels = sorted(y.unique())

matrix = confusion_matrix(
    y_test,
    y_pred,
    labels=labels
)


# =========================================================
# DISPLAY RESULTS
# =========================================================

print("\n======================================")
print("       MODEL TRAINING COMPLETED")
print("======================================")

print(
    f"\nAccuracy: {accuracy * 100:.2f}%"
)

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        zero_division=0
    )
)


# =========================================================
# SAVE MODEL
# =========================================================

model_path = os.path.join(
    MODEL_DIR,
    "job_role_model.pkl"
)

vectorizer_path = os.path.join(
    MODEL_DIR,
    "tfidf_vectorizer.pkl"
)

metrics_path = os.path.join(
    MODEL_DIR,
    "model_metrics.pkl"
)


joblib.dump(
    model,
    model_path
)

joblib.dump(
    vectorizer,
    vectorizer_path
)


# =========================================================
# SAVE MODEL PERFORMANCE DATA
# =========================================================

metrics_data = {

    "accuracy": accuracy,

    "precision": report["weighted avg"]["precision"],

    "recall": report["weighted avg"]["recall"],

    "f1_score": report["weighted avg"]["f1-score"],

    "labels": labels,

    "confusion_matrix": matrix

}


joblib.dump(
    metrics_data,
    metrics_path
)


# =========================================================
# FINAL MESSAGE
# =========================================================

print("\n======================================")
print("         FILES SAVED SUCCESSFULLY")
print("======================================")

print(
    "\nModel:",
    model_path
)

print(
    "Vectorizer:",
    vectorizer_path
)

print(
    "Metrics:",
    metrics_path
)