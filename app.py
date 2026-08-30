import os
import uuid
import joblib
import streamlit as st
import plotly.graph_objects as go

from modules.resume_parser import extract_text_from_pdf
from modules.skill_extractor import extract_skills
from modules.ats_score import calculate_ats_score, get_score_label
from modules.missing_skills import find_missing_skills
from modules.job_recommender import recommend_jobs
from modules.suggestions import generate_suggestions
from modules.pdf_report import create_pdf_report


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


# =========================================================
# PROJECT PATHS
# =========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_DIR = os.path.join(BASE_DIR, "models")

MODEL_PATH = os.path.join(
    MODEL_DIR,
    "job_role_model.pkl"
)

VECTORIZER_PATH = os.path.join(
    MODEL_DIR,
    "tfidf_vectorizer.pkl"
)


# =========================================================
# LOAD ML MODEL
# =========================================================

job_role_model = None
tfidf_vectorizer = None
ml_model_loaded = False
model_error = ""

try:

    if not os.path.isfile(MODEL_PATH):
        raise FileNotFoundError(
            "job_role_model.pkl not found in models folder."
        )

    if not os.path.isfile(VECTORIZER_PATH):
        raise FileNotFoundError(
            "tfidf_vectorizer.pkl not found in models folder."
        )

    job_role_model = joblib.load(MODEL_PATH)

    tfidf_vectorizer = joblib.load(VECTORIZER_PATH)

    ml_model_loaded = True

except Exception as error:

    model_error = str(error)


# =========================================================
# PROFESSIONAL DARK BLUE THEME
# =========================================================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #172033;
        color: #F8FAFC;
    }

    .main {
        background-color: #172033;
        color: #F8FAFC;
    }

    section[data-testid="stMain"] {
        background-color: #172033;
    }

    /* SIDEBAR */

    section[data-testid="stSidebar"] {
        background-color: #202D44;
        border-right: 1px solid #3E506A;
    }

    section[data-testid="stSidebar"] * {
        color: #F8FAFC !important;
    }

    section[data-testid="stSidebar"] .stCaption {
        color: #B8C4D6 !important;
    }

    /* HEADINGS */

    h1 {
        color: #FFFFFF !important;
        font-weight: 750 !important;
        letter-spacing: -0.5px;
    }

    h2 {
        color: #F8FAFC !important;
        font-weight: 700 !important;
    }

    h3 {
        color: #E8EEF7 !important;
        font-weight: 650 !important;
    }

    /* TEXT */

    p {
        color: #D5DEEA !important;
    }

    label {
        color: #E8EEF7 !important;
    }

    small {
        color: #B8C4D6 !important;
    }

    /* METRICS */

    div[data-testid="stMetric"] {
        background-color: #26354D;
        padding: 18px;
        border-radius: 14px;
        border: 1px solid #40536F;
        box-shadow: 0 4px 14px rgba(0,0,0,0.20);
    }

    div[data-testid="stMetricLabel"] {
        color: #BFCBDD !important;
    }

    div[data-testid="stMetricValue"] {
        color: #FFFFFF !important;
        font-weight: 700 !important;
    }

    /* FILE UPLOADER */

    div[data-testid="stFileUploader"] {
        background-color: #26354D;
        padding: 18px;
        border-radius: 16px;
        border: 1px solid #526783;
        box-shadow: 0 5px 18px rgba(0,0,0,0.20);
    }

    section[data-testid="stFileUploaderDropzone"] {
        background-color: #F8FAFC !important;
        border: 2px dashed #6B8DB8 !important;
        border-radius: 14px !important;
        min-height: 180px;
    }

    section[data-testid="stFileUploaderDropzone"]:hover {
        background-color: #EEF4FB !important;
        border-color: #41678F !important;
    }

    section[data-testid="stFileUploaderDropzone"] * {
        color: #172033 !important;
    }

    section[data-testid="stFileUploaderDropzone"] button {
        background-color: #334E6F !important;
        color: #FFFFFF !important;
        border: 1px solid #41678F !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
    }

    section[data-testid="stFileUploaderDropzone"] button:hover {
        background-color: #41678F !important;
        color: #FFFFFF !important;
    }

    div[data-testid="stFileUploaderFile"] {
        background-color: #33445D !important;
        border: 1px solid #526783 !important;
        border-radius: 10px !important;
    }

    div[data-testid="stFileUploaderFile"] * {
        color: #FFFFFF !important;
    }

    /* BUTTONS */

    .stButton > button {
        background-color: #334E6F !important;
        color: #FFFFFF !important;
        border: 1px solid #587392 !important;
        border-radius: 10px !important;
        font-weight: 650 !important;
        min-height: 44px;
    }

    .stButton > button:hover {
        background-color: #41678F !important;
        color: #FFFFFF !important;
        border-color: #7293B7 !important;
    }

    .stButton > button[kind="primary"] {
        background-color: #41678F !important;
        color: #FFFFFF !important;
        border: 1px solid #7293B7 !important;
        font-weight: 700 !important;
    }

    .stButton > button[kind="primary"]:hover {
        background-color: #527AA3 !important;
        color: #FFFFFF !important;
    }

    /* DOWNLOAD */

    .stDownloadButton > button {
        background-color: #334E6F !important;
        color: #FFFFFF !important;
        border: 1px solid #587392 !important;
        border-radius: 10px !important;
        font-weight: 650 !important;
        min-height: 44px;
    }

    .stDownloadButton > button:hover {
        background-color: #41678F !important;
        color: #FFFFFF !important;
        border-color: #7293B7 !important;
    }

    /* CONTAINERS */

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #26354D !important;
        border-radius: 14px !important;
        border: 1px solid #40536F !important;
        box-shadow: 0 4px 14px rgba(0,0,0,0.18);
    }

    /* EXPANDERS */

    div[data-testid="stExpander"] {
        background-color: #26354D !important;
        border: 1px solid #40536F !important;
        border-radius: 12px !important;
    }

    div[data-testid="stExpander"] summary {
        color: #FFFFFF !important;
    }

    div[data-testid="stExpander"] * {
        color: #E8EEF7;
    }

    /* TEXTAREA */

    textarea {
        background-color: #202D44 !important;
        color: #F8FAFC !important;
        border: 1px solid #526783 !important;
        border-radius: 10px !important;
    }

    textarea:focus {
        border-color: #7293B7 !important;
    }

    /* INPUT */

    input {
        background-color: #26354D !important;
        color: #FFFFFF !important;
        border: 1px solid #526783 !important;
    }

    /* ALERTS */

    div[data-testid="stAlert"] {
        border-radius: 10px !important;
    }

    div[data-testid="stAlert"][kind="success"] {
        background-color: #243D36 !important;
    }

    div[data-testid="stAlert"][kind="warning"] {
        background-color: #4A3D25 !important;
    }

    div[data-testid="stAlert"][kind="info"] {
        background-color: #263D58 !important;
    }

    div[data-testid="stAlert"][kind="error"] {
        background-color: #492D35 !important;
    }

    /* LINES */

    hr {
        border-color: #3E506A !important;
    }

    /* UPLOAD TITLE */

    .upload-title {
        background-color: #26354D;
        padding: 18px 22px;
        border-radius: 14px 14px 0 0;
        border-left: 4px solid #7293B7;
    }

    .upload-title h3 {
        margin: 0;
        color: #FFFFFF !important;
    }

    .upload-title p {
        margin-top: 6px;
        margin-bottom: 0;
        color: #BFCBDD !important;
    }

    /* FOOTER */

    .footer {
        text-align: center;
        color: #9EADC1;
        padding: 20px;
        font-size: 14px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# SESSION STATE
# =========================================================

if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("📄 AI Resume Analyzer")

    st.write("Smart Resume & Career Intelligence")

    st.divider()

    st.subheader("🚀 Features")

    st.write("✓ AI Job Role Prediction")
    st.write("✓ ATS Score Analysis")
    st.write("✓ NLP Skill Extraction")
    st.write("✓ Missing Skill Detection")
    st.write("✓ Job Recommendation")
    st.write("✓ Resume Improvement")
    st.write("✓ PDF Report")

    st.divider()

    if ml_model_loaded:
        st.success("🤖 ML Model Loaded")
    else:
        st.warning("⚠ ML Model Not Loaded")

    st.divider()

    st.info("Final Year AIML Project")


# =========================================================
# MAIN HEADER
# =========================================================

st.title("📄 AI Resume Analyzer")

st.subheader("Smart Resume & Career Intelligence")

st.write(
    "Analyze your resume. Improve your skills. "
    "Discover better career opportunities using "
    "Artificial Intelligence, Machine Learning and NLP."
)

st.divider()


# =========================================================
# UPLOAD RESUME
# =========================================================

st.markdown(
    """
    <div class="upload-title">
        <h3>📄 Upload Your Resume</h3>
        <p>
            Upload your resume in PDF format to begin
            AI-powered analysis.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


uploaded_file = st.file_uploader(
    "Choose Resume PDF",
    type=["pdf"],
    help="Only PDF resume files are supported."
)


# =========================================================
# ANALYZE RESUME
# =========================================================

if uploaded_file is not None:

    st.success(
        f"✓ Resume uploaded successfully: {uploaded_file.name}"
    )

    file_size = uploaded_file.size / 1024

    col1, col2 = st.columns(2)

    with col1:
        st.metric("📄 File Type", "PDF")

    with col2:
        st.metric("📦 File Size", f"{file_size:.1f} KB")

    st.divider()

    if st.button(
        "🚀 Analyze Resume",
        type="primary",
        use_container_width=True
    ):

        try:

            with st.spinner(
                "Analyzing resume using AI, ML and NLP..."
            ):

                # -------------------------------------------------
                # Upload folder
                # -------------------------------------------------

                upload_folder = os.path.join(
                    BASE_DIR,
                    "uploads"
                )

                os.makedirs(
                    upload_folder,
                    exist_ok=True
                )

                # -------------------------------------------------
                # Save uploaded resume
                # -------------------------------------------------

                extension = os.path.splitext(
                    uploaded_file.name
                )[1]

                filename = (
                    str(uuid.uuid4())
                    + extension
                )

                resume_path = os.path.join(
                    upload_folder,
                    filename
                )

                with open(
                    resume_path,
                    "wb"
                ) as file:

                    file.write(
                        uploaded_file.getbuffer()
                    )

                # -------------------------------------------------
                # Extract text
                # -------------------------------------------------

                resume_text = extract_text_from_pdf(
                    uploaded_file
                )

                if not resume_text:
                    st.error(
                        "Could not extract text from PDF."
                    )
                    st.stop()

                # -------------------------------------------------
                # ML Job Role Prediction
                # -------------------------------------------------

                predicted_job_role = "Not Available"
                prediction_confidence = None

                if ml_model_loaded:

                    resume_vector = (
                        tfidf_vectorizer.transform(
                            [resume_text]
                        )
                    )

                    predicted_job_role = (
                        job_role_model.predict(
                            resume_vector
                        )[0]
                    )

                    if hasattr(
                        job_role_model,
                        "predict_proba"
                    ):

                        probabilities = (
                            job_role_model.predict_proba(
                                resume_vector
                            )[0]
                        )

                        prediction_confidence = (
                            max(probabilities) * 100
                        )

                # -------------------------------------------------
                # NLP Skill Extraction
                # -------------------------------------------------

                skills = extract_skills(
                    resume_text
                )

                # -------------------------------------------------
                # ATS Score
                # -------------------------------------------------

                ats_score = calculate_ats_score(
                    resume_text,
                    skills
                )

                score_label = get_score_label(
                    ats_score
                )

                # -------------------------------------------------
                # Missing Skills
                # -------------------------------------------------

                missing_skills = find_missing_skills(
                    skills
                )

                # -------------------------------------------------
                # Job Recommendation
                # -------------------------------------------------

                jobs = recommend_jobs(
                    skills
                )

                # -------------------------------------------------
                # Resume Suggestions
                # -------------------------------------------------

                suggestions = generate_suggestions(
                    resume_text,
                    skills,
                    missing_skills,
                    ats_score
                )

                # -------------------------------------------------
                # Save results
                # -------------------------------------------------

                st.session_state.resume_text = resume_text

                st.session_state.predicted_job_role = (
                    predicted_job_role
                )

                st.session_state.prediction_confidence = (
                    prediction_confidence
                )

                st.session_state.skills = skills

                st.session_state.ats_score = ats_score

                st.session_state.score_label = score_label

                st.session_state.missing_skills = (
                    missing_skills
                )

                st.session_state.jobs = jobs

                st.session_state.suggestions = suggestions

                st.session_state.analysis_done = True

            st.success(
                "🎉 Resume analysis completed successfully!"
            )

        except Exception as error:

            st.error(
                f"Analysis Error: {error}"
            )


# =========================================================
# RESULTS
# =========================================================

if st.session_state.analysis_done:

    resume_text = st.session_state.resume_text

    predicted_job_role = (
        st.session_state.predicted_job_role
    )

    prediction_confidence = (
        st.session_state.prediction_confidence
    )

    skills = st.session_state.skills

    ats_score = st.session_state.ats_score

    score_label = st.session_state.score_label

    missing_skills = (
        st.session_state.missing_skills
    )

    jobs = st.session_state.jobs

    suggestions = st.session_state.suggestions


    # =====================================================
    # DASHBOARD
    # =====================================================

    st.divider()

    st.header("📊 Resume Dashboard")

    word_count = len(
        resume_text.split()
    )

    skill_match = min(
        len(skills) * 8,
        100
    )

    top_job_match = (
        jobs[0]["Match"]
        if jobs
        else 0
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "🎯 ATS Score",
            f"{ats_score}/100",
            score_label
        )

    with col2:

        st.metric(
            "🧠 Skill Match",
            f"{skill_match}%"
        )

    with col3:

        st.metric(
            "💼 Top Job Match",
            f"{top_job_match}%"
        )

    with col4:

        st.metric(
            "📝 Word Count",
            word_count
        )


    # =====================================================
    # AI JOB ROLE PREDICTION
    # =====================================================

    st.divider()

    st.header("🤖 AI Job Role Prediction")

    if ml_model_loaded:

        st.success(
            "Machine Learning model successfully analyzed your resume."
        )

        col1, col2 = st.columns(2)

        with col1:

            st.subheader(
                "🎯 Predicted Job Role"
            )

            st.info(
                f"**{predicted_job_role}**"
            )

        with col2:

            if prediction_confidence is not None:

                st.subheader(
                    "📊 Prediction Confidence"
                )

                st.metric(
                    "Confidence",
                    f"{prediction_confidence:.2f}%"
                )

        st.caption(
            "Model: TF-IDF + Logistic Regression"
        )

    else:

        st.error(
            "Machine Learning model could not be loaded."
        )

        st.caption(
            f"Model Error: {model_error}"
        )


    # =====================================================
    # ATS SCORE
    # =====================================================

    st.divider()

    st.header("🎯 ATS Score Analysis")

    col1, col2 = st.columns(2)

    with col1:

        gauge = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=ats_score,
                title={
                    "text": score_label
                },
                gauge={
                    "axis": {
                        "range": [0, 100],
                        "tickcolor": "#D5DEEA"
                    },
                    "bar": {
                        "color": "#8AA6C5"
                    },
                    "bgcolor": "#26354D",
                    "bordercolor": "#526783",
                    "steps": [
                        {
                            "range": [0, 50],
                            "color": "#39475B"
                        },
                        {
                            "range": [50, 75],
                            "color": "#52627A"
                        },
                        {
                            "range": [75, 100],
                            "color": "#6D829E"
                        }
                    ]
                }
            )
        )

        gauge.update_layout(
            height=350,
            paper_bgcolor="#172033",
            plot_bgcolor="#172033",
            font={
                "color": "#FFFFFF"
            },
            margin={
                "l": 20,
                "r": 20,
                "t": 50,
                "b": 20
            }
        )

        st.plotly_chart(
            gauge,
            use_container_width=True
        )

    with col2:

        st.subheader(
            "📋 Score Interpretation"
        )

        if ats_score >= 80:

            st.success(
                "Excellent! Your resume has a strong ATS profile."
            )

        elif ats_score >= 65:

            st.info(
                "Good resume. Some improvements can make it stronger."
            )

        elif ats_score >= 50:

            st.warning(
                "Average resume. Consider improving keywords and sections."
            )

        else:

            st.error(
                "Your resume needs significant improvement."
            )

        st.write(
            f"Current ATS Score: **{ats_score}/100**"
        )

        st.write(
            f"Status: **{score_label}**"
        )


    # =====================================================
    # SKILL EXTRACTION
    # =====================================================

    st.divider()

    st.header("🧠 Skill Extraction")

    if skills:

        st.write(
            f"Detected {len(skills)} skills."
        )

        columns = st.columns(3)

        for index, skill in enumerate(skills):

            with columns[index % 3]:

                st.success(
                    f"✓ {skill}"
                )

    else:

        st.warning(
            "No skills detected."
        )


    # =====================================================
    # MISSING SKILLS
    # =====================================================

    st.divider()

    st.header("⚠️ Missing Skill Detection")

    if missing_skills:

        st.write(
            f"Potentially relevant missing skills: "
            f"{len(missing_skills)}"
        )

        columns = st.columns(3)

        for index, skill in enumerate(
            missing_skills
        ):

            with columns[index % 3]:

                st.warning(
                    f"⚠ {skill}"
                )

    else:

        st.success(
            "No major missing skills detected."
        )


    # =====================================================
    # JOB RECOMMENDATION
    # =====================================================

    st.divider()

    st.header("💼 Job Recommendation")

    if jobs:

        for index, job in enumerate(
            jobs[:8],
            start=1
        ):

            with st.container(
                border=True
            ):

                col1, col2 = st.columns(
                    [4, 1]
                )

                with col1:

                    st.subheader(
                        f"{index}. {job['Job']}"
                    )

                    st.write(
                        f"Matched Skills: "
                        f"{job['Matched Skills']} / "
                        f"{job['Required Skills']}"
                    )

                with col2:

                    st.metric(
                        "Match",
                        f"{job['Match']}%"
                    )

    else:

        st.warning(
            "No suitable job role found."
        )


    # =====================================================
    # RESUME IMPROVEMENT
    # =====================================================

    st.divider()

    st.header("💡 Resume Improvement")

    if suggestions:

        for index, suggestion in enumerate(
            suggestions,
            start=1
        ):

            st.info(
                f"**{index}.** {suggestion}"
            )

    else:

        st.success(
            "No major improvement suggestions."
        )


    # =====================================================
    # RESUME STATISTICS
    # =====================================================

    st.divider()

    st.header("📈 Resume Statistics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Words",
            word_count
        )

    with col2:

        st.metric(
            "Skills",
            len(skills)
        )

    with col3:

        st.metric(
            "Missing Skills",
            len(missing_skills)
        )

    with col4:

        st.metric(
            "Job Roles",
            len(jobs)
        )


    # =====================================================
    # EXTRACTED TEXT
    # =====================================================

    st.divider()

    st.header("🔍 Extracted Resume Text")

    with st.expander(
        "View Resume Content"
    ):

        st.text_area(
            "Resume Text",
            resume_text,
            height=400
        )


    # =====================================================
    # PDF REPORT
    # =====================================================

    st.divider()

    st.header("📄 PDF Report")

    try:

        report_folder = os.path.join(
            BASE_DIR,
            "reports"
        )

        if os.path.exists(report_folder):

            if not os.path.isdir(report_folder):

                report_folder = os.path.join(
                    BASE_DIR,
                    "generated_reports"
                )

        os.makedirs(
            report_folder,
            exist_ok=True
        )

        pdf_filename = (
            "AI_Resume_Analysis_Report.pdf"
        )

        pdf_path = os.path.join(
            report_folder,
            pdf_filename
        )

        create_pdf_report(
            pdf_path,
            ats_score,
            score_label,
            skills,
            missing_skills,
            jobs,
            suggestions
        )

        if os.path.isfile(pdf_path):

            st.success(
                "✓ PDF Report generated successfully!"
            )

            with open(
                pdf_path,
                "rb"
            ) as pdf_file:

                pdf_data = pdf_file.read()

            st.download_button(
                label="📥 Download Complete PDF Report",
                data=pdf_data,
                file_name=pdf_filename,
                mime="application/pdf",
                use_container_width=True
            )

        else:

            st.error(
                "PDF file was not created."
            )

    except Exception as error:

        st.error(
            f"PDF Report Error: {error}"
        )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown(
    """
    <div class="footer">
        AI Resume Analyzer | Python | Streamlit | NLP |
        Machine Learning | AIML Final Year Project
    </div>
    """,
    unsafe_allow_html=True
)