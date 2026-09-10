from modules.skill_extractor import SKILL_DATABASE


# Skills commonly required by major technology roles

RECOMMENDED_SKILLS = [

    "Python",
    "Java",
    "JavaScript",
    "HTML",
    "CSS",
    "SQL",
    "Git",
    "GitHub",
    "React",
    "Node.js",
    "Express.js",
    "MongoDB",
    "MySQL",
    "PostgreSQL",
    "Machine Learning",
    "Deep Learning",
    "Pandas",
    "NumPy",
    "Scikit-learn",
    "TensorFlow",
    "Power BI",
    "Docker",
    "AWS",
    "REST API",
    "Communication",
    "Problem Solving",
    "Teamwork"
]


def find_missing_skills(
    skills
):

    skill_set = set(
        skill.lower()
        for skill in skills
    )


    missing = []


    for skill in RECOMMENDED_SKILLS:

        if skill.lower() not in skill_set:

            missing.append(
                skill
            )


    return missing[:12]