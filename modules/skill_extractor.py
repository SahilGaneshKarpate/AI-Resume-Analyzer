import re


SKILL_DATABASE = {

    # Programming Languages
    "Python": [
        "python"
    ],

    "Java": [
        "java"
    ],

    "C": [
        r"\bc\b",
        "c programming"
    ],

    "C++": [
        "c++"
    ],

    "C#": [
        "c#",
        "c sharp"
    ],

    "JavaScript": [
        "javascript",
        "js"
    ],

    "TypeScript": [
        "typescript"
    ],

    "PHP": [
        "php"
    ],

    "R": [
        r"\br programming\b"
    ],

    "Go": [
        "golang",
        r"\bgo language\b"
    ],


    # Web Development
    "HTML": [
        "html",
        "html5"
    ],

    "CSS": [
        "css",
        "css3"
    ],

    "React": [
        "react",
        "react.js",
        "reactjs"
    ],

    "Angular": [
        "angular"
    ],

    "Vue.js": [
        "vue",
        "vue.js",
        "vuejs"
    ],

    "Node.js": [
        "node",
        "node.js",
        "nodejs"
    ],

    "Express.js": [
        "express",
        "express.js"
    ],

    "Django": [
        "django"
    ],

    "Flask": [
        "flask"
    ],

    "FastAPI": [
        "fastapi",
        "fast api"
    ],


    # Database
    "SQL": [
        "sql"
    ],

    "MySQL": [
        "mysql"
    ],

    "PostgreSQL": [
        "postgresql",
        "postgres"
    ],

    "MongoDB": [
        "mongodb",
        "mongo db"
    ],

    "SQLite": [
        "sqlite"
    ],

    "Oracle": [
        "oracle database"
    ],


    # Data Science / AI
    "Machine Learning": [
        "machine learning",
        "machine-learning"
    ],

    "Deep Learning": [
        "deep learning"
    ],

    "Artificial Intelligence": [
        "artificial intelligence",
        "artificial intelligence",
        "ai"
    ],

    "NLP": [
        "natural language processing",
        "nlp"
    ],

    "Pandas": [
        "pandas"
    ],

    "NumPy": [
        "numpy",
        "num py"
    ],

    "Scikit-learn": [
        "scikit-learn",
        "sklearn",
        "scikit learn"
    ],

    "TensorFlow": [
        "tensorflow"
    ],

    "Keras": [
        "keras"
    ],

    "PyTorch": [
        "pytorch"
    ],

    "Matplotlib": [
        "matplotlib"
    ],

    "Seaborn": [
        "seaborn"
    ],


    # Data Analytics
    "Power BI": [
        "power bi",
        "powerbi"
    ],

    "Tableau": [
        "tableau"
    ],

    "Excel": [
        "excel",
        "microsoft excel"
    ],


    # DevOps / Cloud
    "Git": [
        "git"
    ],

    "GitHub": [
        "github",
        "git hub"
    ],

    "Docker": [
        "docker"
    ],

    "Kubernetes": [
        "kubernetes",
        "k8s"
    ],

    "AWS": [
        "aws",
        "amazon web services"
    ],

    "Azure": [
        "azure",
        "microsoft azure"
    ],

    "Google Cloud": [
        "google cloud",
        "gcp"
    ],


    # APIs / Tools
    "REST API": [
        "rest api",
        "restful api"
    ],

    "Postman": [
        "postman"
    ],

    "Jupyter": [
        "jupyter",
        "jupyter notebook"
    ],

    "VS Code": [
        "vs code",
        "visual studio code"
    ],


    # Soft Skills
    "Communication": [
        "communication",
        "communication skills"
    ],

    "Leadership": [
        "leadership",
        "leadership skills"
    ],

    "Teamwork": [
        "teamwork",
        "team work"
    ],

    "Problem Solving": [
        "problem solving",
        "problem-solving"
    ]
}


def extract_skills(text):

    text_lower = text.lower()

    found_skills = []

    for skill, keywords in SKILL_DATABASE.items():

        for keyword in keywords:

            try:

                pattern = keyword

                if re.search(
                    pattern,
                    text_lower,
                    flags=re.IGNORECASE
                ):

                    found_skills.append(
                        skill
                    )

                    break

            except re.error:

                if keyword.lower() in text_lower:

                    found_skills.append(
                        skill
                    )

                    break


    return sorted(
        list(
            set(found_skills)
        )
    )