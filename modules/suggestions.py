import re


def generate_suggestions(
    text,
    skills,
    missing_skills,
    ats_score
):

    suggestions = []

    text_lower = text.lower()


    # ==========================================
    # SUMMARY
    # ==========================================

    if not any(
        word in text_lower
        for word in [
            "summary",
            "profile",
            "objective"
        ]
    ):

        suggestions.append(
            "Add a professional summary describing "
            "your profile, technical skills and career goal."
        )


    # ==========================================
    # EDUCATION
    # ==========================================

    if "education" not in text_lower:

        suggestions.append(
            "Add a clear Education section with "
            "degree, college, year and relevant details."
        )


    # ==========================================
    # PROJECTS
    # ==========================================

    if "project" not in text_lower:

        suggestions.append(
            "Add 2–3 relevant projects and explain "
            "the technologies and your contribution."
        )


    # ==========================================
    # EXPERIENCE
    # ==========================================

    if not any(
        word in text_lower
        for word in [
            "experience",
            "internship",
            "employment"
        ]
    ):

        suggestions.append(
            "If you have internship or work experience, "
            "add a dedicated Experience section."
        )


    # ==========================================
    # LINKEDIN
    # ==========================================

    if "linkedin" not in text_lower:

        suggestions.append(
            "Add your LinkedIn profile to improve "
            "professional visibility."
        )


    # ==========================================
    # GITHUB
    # ==========================================

    if "github" not in text_lower:

        suggestions.append(
            "Add your GitHub profile, especially "
            "if you are applying for technical roles."
        )


    # ==========================================
    # CERTIFICATION
    # ==========================================

    if "certification" not in text_lower:

        suggestions.append(
            "Add relevant certifications, courses or "
            "training programs if available."
        )


    # ==========================================
    # SKILLS
    # ==========================================

    if len(skills) < 8:

        suggestions.append(
            "Expand your Skills section with relevant "
            "programming languages, tools, frameworks "
            "and technologies you actually know."
        )


    # ==========================================
    # MISSING SKILLS
    # ==========================================

    if missing_skills:

        skills_text = ", ".join(
            missing_skills[:6]
        )

        suggestions.append(
            f"Consider learning or adding relevant "
            f"skills such as: {skills_text}."
        )


    # ==========================================
    # ACTION WORDS
    # ==========================================

    action_words = [

        "developed",
        "implemented",
        "created",
        "designed",
        "built",
        "managed",
        "optimized"

    ]


    action_count = sum(
        text_lower.count(word)
        for word in action_words
    )


    if action_count < 3:

        suggestions.append(
            "Use strong action words such as Developed, "
            "Implemented, Designed, Built and Optimized "
            "when describing your work."
        )


    # ==========================================
    # ATS SCORE
    # ==========================================

    if ats_score < 70:

        suggestions.append(
            "Improve ATS compatibility by using clear "
            "section headings and relevant job keywords."
        )


    # ==========================================
    # WORD COUNT
    # ==========================================

    word_count = len(
        text.split()
    )


    if word_count < 200:

        suggestions.append(
            "Your resume appears short. Add relevant "
            "projects, skills, achievements and experience."
        )


    if word_count > 1200:

        suggestions.append(
            "Your resume is quite long. Remove unnecessary "
            "information and keep the content focused."
        )


    return suggestions[:10]