JOB_ROLES = {

    "Python Developer": [

        "Python",
        "Django",
        "Flask",
        "SQL",
        "Git",
        "REST API"
    ],


    "Full Stack Developer": [

        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Node.js",
        "Express.js",
        "SQL",
        "Git"
    ],


    "Java Developer": [

        "Java",
        "SQL",
        "MySQL",
        "Git",
        "REST API"
    ],


    "Frontend Developer": [

        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Git"
    ],


    "Backend Developer": [

        "Python",
        "Java",
        "Node.js",
        "SQL",
        "REST API",
        "Git"
    ],


    "Data Analyst": [

        "Python",
        "SQL",
        "Pandas",
        "NumPy",
        "Excel",
        "Power BI"
    ],


    "Machine Learning Engineer": [

        "Python",
        "Machine Learning",
        "Pandas",
        "NumPy",
        "Scikit-learn",
        "TensorFlow",
        "SQL"
    ],


    "Data Scientist": [

        "Python",
        "Machine Learning",
        "Pandas",
        "NumPy",
        "Scikit-learn",
        "SQL",
        "Matplotlib"
    ],


    "Web Developer": [

        "HTML",
        "CSS",
        "JavaScript",
        "Git"
    ],


    "DevOps Engineer": [

        "Git",
        "Docker",
        "Kubernetes",
        "AWS",
        "Linux"
    ],


    "Cloud Engineer": [

        "AWS",
        "Azure",
        "Docker",
        "Kubernetes",
        "Git"
    ]

}


def recommend_jobs(
    skills
):

    user_skills = set(
        skill.lower()
        for skill in skills
    )


    recommendations = []


    for job, required_skills in JOB_ROLES.items():

        matched = [

            skill

            for skill in required_skills

            if skill.lower() in user_skills

        ]


        required_count = len(
            required_skills
        )

        matched_count = len(
            matched
        )


        if required_count > 0:

            match_percentage = int(
                (
                    matched_count
                    /
                    required_count
                ) * 100
            )

        else:

            match_percentage = 0


        recommendations.append({

            "Job": job,

            "Match": match_percentage,

            "Matched Skills": matched_count,

            "Required Skills": required_count

        })


    recommendations.sort(
        key=lambda x: x["Match"],
        reverse=True
    )


    return recommendations