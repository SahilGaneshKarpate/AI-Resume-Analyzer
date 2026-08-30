# 📄 AI Resume Analyzer

### Smart Resume & Career Intelligence

AI Resume Analyzer is an AI/ML-based web application that analyzes resumes and provides intelligent career-related insights using **Natural Language Processing (NLP)** and **Machine Learning**.

The system extracts information from a resume, identifies skills, predicts a suitable job role, calculates an ATS score, detects missing skills, recommends relevant job roles, and generates a detailed PDF report.

---

## 🚀 Features

* 📄 PDF Resume Upload
* 🤖 AI-Based Job Role Prediction
* 🧠 NLP-Based Resume Text Processing
* 🔤 TF-IDF Feature Extraction
* 🎯 Machine Learning Classification
* 📊 ATS Score Analysis
* 🛠️ Skill Extraction
* ⚠️ Missing Skill Detection
* 💼 Job Role Recommendation
* 💡 Resume Improvement Suggestions
* 📑 Resume Statistics
* 📥 PDF Analysis Report Generation
* 🌐 Interactive Streamlit Web Application

---

## 🧠 AIML Components

This project demonstrates the following Artificial Intelligence and Machine Learning concepts:

### Artificial Intelligence

* Intelligent resume analysis
* Career-oriented recommendations
* Automated resume improvement suggestions

### Machine Learning

* Supervised Machine Learning
* Text Classification
* Logistic Regression
* Model Training
* Model Prediction
* Model Evaluation
* Trained Model Persistence

### Natural Language Processing

* Resume text extraction
* Text preprocessing
* TF-IDF vectorization
* Skill extraction
* Text-based job role classification

---

## 📊 Machine Learning Workflow

```text
Resume PDF
    ↓
Resume Text Extraction
    ↓
Text Preprocessing
    ↓
TF-IDF Feature Extraction
    ↓
Machine Learning Model
    ↓
Job Role Prediction
    ↓
Skill Analysis
    ↓
ATS Score Analysis
    ↓
Missing Skill Detection
    ↓
Job Recommendations
    ↓
Resume Improvement Suggestions
    ↓
PDF Report
```

---

## 📁 Dataset

The project uses a resume dataset stored in:

```text
dataset/resume_dataset.csv
```

The dataset is used for training the machine learning model for job role classification.

---

## 🤖 Machine Learning Model

The project uses:

**TF-IDF + Logistic Regression**

TF-IDF converts resume text into numerical feature vectors, while Logistic Regression performs job role classification.

The trained model and supporting files are stored in:

```text
models/
├── job_role_model.pkl
├── tfidf_vectorizer.pkl
└── model_metrics.pkl
```

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* Natural Language Processing (NLP)
* TF-IDF
* Logistic Regression
* PyPDF2
* ReportLab
* Joblib

---

## 📂 Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
│
├── dataset/
│   └── resume_dataset.csv
│
├── models/
│   ├── job_role_model.pkl
│   ├── tfidf_vectorizer.pkl
│   └── model_metrics.pkl
│
├── modules/
│   ├── __init__.py
│   ├── ats_score.py
│   ├── job_recommender.py
│   ├── missing_skills.py
│   ├── pdf_report.py
│   ├── resume_parser.py
│   ├── skill_extractor.py
│   └── suggestions.py
│
└── generated_reports/
    └── AI_Resume_Analysis_Report.pdf
```

---

## ⚙️ Installation

Clone or download the project and open the project directory.

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your web browser.

---

## 🖥️ How to Use

1. Open the AI Resume Analyzer web application.
2. Upload a resume in PDF format.
3. The system extracts the resume text.
4. The NLP pipeline processes the extracted text.
5. The trained Machine Learning model predicts the suitable job role.
6. The system calculates the ATS score.
7. Skills are extracted from the resume.
8. Missing skills are identified.
9. Relevant job roles are recommended.
10. Resume improvement suggestions are generated.
11. A PDF analysis report is generated.

---

## 📈 Analysis Output

The application provides:

* ATS Score
* Skill Match
* Predicted Job Role
* Prediction Confidence
* Detected Skills
* Missing Skills
* Job Recommendations
* Resume Improvement Suggestions
* Resume Statistics
* Extracted Resume Text
* PDF Analysis Report

---

## 🔐 API Requirement

This project does **not require external AI APIs or API keys**.

The core prediction functionality is performed using the locally stored Machine Learning model and NLP components.

---

## 🎯 Project Objective

The main objective of this project is to develop an intelligent resume analysis system that helps users understand their resume quality, identify skill gaps, discover suitable job roles, and improve their resumes using Artificial Intelligence, Machine Learning, and Natural Language Processing.

---

## 🔮 Future Scope

Future versions of the project can include:

* Advanced Deep Learning-based resume classification
* More comprehensive job-market datasets
* Personalized career paths
* Job vacancy matching
* Multi-language resume analysis
* Advanced semantic similarity using transformer models
* Resume comparison and ranking

---

## 👨‍💻 Project Type

**Final Year AIML Project**

**Domain:** Artificial Intelligence, Machine Learning & Natural Language Processing

**Application:** Resume Analysis and Career Intelligence

---

## 📌 Conclusion

AI Resume Analyzer provides an end-to-end AIML solution for automated resume analysis. It combines NLP, TF-IDF, Machine Learning classification, skill analysis, ATS evaluation, job recommendations, and report generation into a single interactive Streamlit application.
