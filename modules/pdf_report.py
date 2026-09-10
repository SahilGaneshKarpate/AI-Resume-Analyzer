from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)


def create_pdf_report(
    file_path,
    ats_score,
    score_label,
    skills,
    missing_skills,
    jobs,
    suggestions
):

    # -----------------------------------------
    # PDF DOCUMENT
    # -----------------------------------------

    document = SimpleDocTemplate(
        file_path,
        pagesize=A4,
        rightMargin=20 * mm,
        leftMargin=20 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm
    )


    # -----------------------------------------
    # STYLES
    # -----------------------------------------

    styles = getSampleStyleSheet()

    title_style = styles["Title"]

    heading_style = styles["Heading2"]

    normal_style = styles["BodyText"]


    story = []


    # =========================================
    # TITLE
    # =========================================

    story.append(
        Paragraph(
            "AI Resume Analyzer",
            title_style
        )
    )

    story.append(
        Paragraph(
            "Smart Resume & Career Intelligence",
            normal_style
        )
    )

    story.append(
        Spacer(
            1,
            15
        )
    )


    # =========================================
    # ATS SCORE
    # =========================================

    story.append(
        Paragraph(
            "1. ATS Score Analysis",
            heading_style
        )
    )

    story.append(
        Spacer(
            1,
            5
        )
    )


    score_data = [

        [
            "ATS Score",
            "Status"
        ],

        [
            f"{ats_score}/100",
            str(score_label)
        ]

    ]


    score_table = Table(
        score_data,
        colWidths=[
            70 * mm,
            70 * mm
        ]
    )


    score_table.setStyle(
        TableStyle([

            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.HexColor("#2563EB")
            ),

            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.white
            ),

            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "Helvetica-Bold"
            ),

            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.grey
            ),

            (
                "ALIGN",
                (0, 0),
                (-1, -1),
                "CENTER"
            ),

            (
                "PADDING",
                (0, 0),
                (-1, -1),
                8
            )

        ])
    )


    story.append(
        score_table
    )

    story.append(
        Spacer(
            1,
            15
        )
    )


    # =========================================
    # SKILL EXTRACTION
    # =========================================

    story.append(
        Paragraph(
            "2. Skill Extraction",
            heading_style
        )
    )

    story.append(
        Spacer(
            1,
            5
        )
    )


    if skills:

        skill_text = ", ".join(
            str(skill)
            for skill in skills
        )

    else:

        skill_text = (
            "No technical skills detected."
        )


    story.append(
        Paragraph(
            skill_text,
            normal_style
        )
    )

    story.append(
        Spacer(
            1,
            15
        )
    )


    # =========================================
    # MISSING SKILLS
    # =========================================

    story.append(
        Paragraph(
            "3. Missing Skill Detection",
            heading_style
        )
    )

    story.append(
        Spacer(
            1,
            5
        )
    )


    if missing_skills:

        missing_text = ", ".join(
            str(skill)
            for skill in missing_skills
        )

    else:

        missing_text = (
            "No major missing skills detected."
        )


    story.append(
        Paragraph(
            missing_text,
            normal_style
        )
    )

    story.append(
        Spacer(
            1,
            15
        )
    )


    # =========================================
    # JOB RECOMMENDATION
    # =========================================

    story.append(
        Paragraph(
            "4. Job Recommendation",
            heading_style
        )
    )

    story.append(
        Spacer(
            1,
            5
        )
    )


    job_data = [

        [
            "Job Role",
            "Match",
            "Skills"
        ]

    ]


    if jobs:

        for job in jobs[:8]:

            job_name = str(
                job.get(
                    "Job",
                    "Unknown"
                )
            )

            match = str(
                job.get(
                    "Match",
                    0
                )
            )

            matched = str(
                job.get(
                    "Matched Skills",
                    0
                )
            )

            required = str(
                job.get(
                    "Required Skills",
                    0
                )
            )


            job_data.append(
                [
                    job_name,
                    f"{match}%",
                    f"{matched}/{required}"
                ]
            )


    else:

        job_data.append(
            [
                "No recommendation",
                "0%",
                "0/0"
            ]
        )


    job_table = Table(
        job_data,
        colWidths=[
            80 * mm,
            30 * mm,
            40 * mm
        ]
    )


    job_table.setStyle(
        TableStyle([

            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.HexColor("#2563EB")
            ),

            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.white
            ),

            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "Helvetica-Bold"
            ),

            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.grey
            ),

            (
                "ALIGN",
                (1, 1),
                (-1, -1),
                "CENTER"
            ),

            (
                "VALIGN",
                (0, 0),
                (-1, -1),
                "MIDDLE"
            ),

            (
                "PADDING",
                (0, 0),
                (-1, -1),
                6
            )

        ])
    )


    story.append(
        job_table
    )

    story.append(
        Spacer(
            1,
            15
        )
    )


    # =========================================
    # RESUME IMPROVEMENT
    # =========================================

    story.append(
        Paragraph(
            "5. Resume Improvement",
            heading_style
        )
    )

    story.append(
        Spacer(
            1,
            5
        )
    )


    if suggestions:

        for index, suggestion in enumerate(
            suggestions,
            start=1
        ):

            story.append(
                Paragraph(
                    f"{index}. {str(suggestion)}",
                    normal_style
                )
            )

            story.append(
                Spacer(
                    1,
                    6
                )
            )

    else:

        story.append(
            Paragraph(
                "No major improvement suggestions.",
                normal_style
            )
        )


    # =========================================
    # FOOTER
    # =========================================

    story.append(
        Spacer(
            1,
            20
        )
    )


    story.append(
        Paragraph(
            "Generated by AI Resume Analyzer",
            normal_style
        )
    )


    # =========================================
    # CREATE PDF
    # =========================================

    document.build(
        story
    )