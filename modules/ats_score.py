import re


def calculate_ats_score(
    text,
    skills
):

    text_lower = text.lower()

    score = 0


    # -----------------------------------------
    # 1. CONTACT INFORMATION - 15
    # -----------------------------------------

    contact_score = 0

    if re.search(
        r"[\w\.-]+@[\w\.-]+\.\w+",
        text
    ):

        contact_score += 7


    if re.search(
        r"(\+91[\s-]?)?[6-9]\d{9}",
        text
    ):

        contact_score += 5


    if (
        "linkedin" in text_lower
        or "github" in text_lower
    ):

        contact_score += 3


    # -----------------------------------------
    # 2. SKILLS - 25
    # -----------------------------------------

    skill_score = min(
        len(skills) * 2.5,
        25
    )


    # -----------------------------------------
    # 3. IMPORTANT SECTIONS - 25
    # -----------------------------------------

    sections = {

        "summary": [
            "summary",
            "profile",
            "objective"
        ],

        "education": [
            "education",
            "qualification",
            "academic"
        ],

        "experience": [
            "experience",
            "employment",
            "work history"
        ],

        "projects": [
            "projects",
            "project"
        ],

        "skills": [
            "skills",
            "technical skills"
        ],

        "certifications": [
            "certification",
            "certifications"
        ]

    }


    section_score = 0


    for keywords in sections.values():

        if any(
            keyword in text_lower
            for keyword in keywords
        ):

            section_score += 4


    section_score = min(
        section_score,
        25
    )


    # -----------------------------------------
    # 4. KEYWORDS - 15
    # -----------------------------------------

    important_keywords = [

        "developed",
        "designed",
        "implemented",
        "managed",
        "created",
        "built",
        "tested",
        "optimized",
        "analyzed",
        "improved",
        "deployed"

    ]


    keyword_count = sum(
        text_lower.count(keyword)
        for keyword in important_keywords
    )


    keyword_score = min(
        keyword_count * 1.5,
        15
    )


    # -----------------------------------------
    # 5. RESUME LENGTH - 10
    # -----------------------------------------

    word_count = len(
        text.split()
    )


    if 250 <= word_count <= 900:

        length_score = 10

    elif 150 <= word_count < 250:

        length_score = 7

    elif 900 < word_count <= 1200:

        length_score = 7

    else:

        length_score = 4


    # -----------------------------------------
    # TOTAL
    # -----------------------------------------

    score = (
        contact_score
        + skill_score
        + section_score
        + keyword_score
        + length_score
    )


    return int(
        max(
            0,
            min(
                score,
                100
            )
        )
    )


def get_score_label(score):

    if score >= 80:

        return "Excellent"

    elif score >= 65:

        return "Good"

    elif score >= 50:

        return "Average"

    else:

        return "Needs Improvement"