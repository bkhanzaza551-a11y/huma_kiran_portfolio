import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether

def build_pdf():
    os.makedirs("public", exist_ok=True)
    pdf_path = os.path.join("public", "Huma-Kiran-Resume.pdf")
    
    # Page setup: 0.5 inch margins for clean density
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    
    styles = getSampleStyleSheet()
    
    # Custom palette
    PRIMARY = colors.HexColor("#0f172a")     # Slate 900
    ACCENT = colors.HexColor("#2563eb")      # Blue 600
    MUTED = colors.HexColor("#475569")       # Slate 600
    DARK = colors.HexColor("#1e293b")        # Slate 800
    LINE_COLOR = colors.HexColor("#cbd5e1")  # Slate 300
    LIGHT_BG = colors.HexColor("#f8fafc")    # Slate 50
    
    # Typography Styles
    name_style = ParagraphStyle(
        'NameStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=PRIMARY,
        alignment=0
    )
    
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=ACCENT,
        alignment=0
    )
    
    contact_style = ParagraphStyle(
        'ContactStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=MUTED,
        alignment=0
    )
    
    section_heading = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=PRIMARY,
        spaceAfter=4
    )
    
    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=DARK
    )
    
    bullet_style = ParagraphStyle(
        'BulletStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=DARK,
        leftIndent=12,
        firstLineIndent=-10
    )
    
    job_title_style = ParagraphStyle(
        'JobTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=PRIMARY
    )
    
    company_style = ParagraphStyle(
        'Company',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13.5,
        textColor=ACCENT
    )
    
    date_style = ParagraphStyle(
        'DateStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=MUTED,
        alignment=2
    )

    story = []
    
    # --- HEADER ---
    header_left = [
        Paragraph("HUMA KIRAN", name_style),
        Spacer(1, 2),
        Paragraph("Software Engineer & Operations Lead | Centralized ERP Specialist", title_style),
    ]
    
    contact_text = (
        "<b>Email:</b> humakiran.work@gmail.com &nbsp;&nbsp;|&nbsp;&nbsp; "
        "<b>Location:</b> Pakistan (Open to Remote & Onsite)<br/>"
        "<b>LinkedIn:</b> linkedin.com/in/huma-kiran &nbsp;&nbsp;|&nbsp;&nbsp; "
        "<b>Portfolio:</b> humakiran.dev"
    )
    header_left.append(Spacer(1, 4))
    header_left.append(Paragraph(contact_text, contact_style))
    
    story.extend(header_left)
    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=1.5, color=ACCENT, spaceBefore=0, spaceAfter=10))
    
    # --- PROFESSIONAL SUMMARY ---
    story.append(Paragraph("PROFESSIONAL SUMMARY", section_heading))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceBefore=2, spaceAfter=6))
    summary_text = (
        "Versatile and results-driven <b>Software Engineer & Operations Leader</b> with a distinctive ground-up progression "
        "spanning frontline execution, banking Quality Assurance (QA) auditing at UBL, youth financial empowerment at JS Bank, "
        "and operational management at DMC. Combines deep business workflow acumen with modern full-stack development "
        "(React, JavaScript, TypeScript, Python, SQL) to architect and deliver scalable enterprise systems, including Centralized "
        "ERP platforms. Known for disciplined problem-solving, seamless client communication, and turning complex real-world "
        "operations into robust, user-centric software."
    )
    story.append(Paragraph(summary_text, body_style))
    story.append(Spacer(1, 10))
    
    # --- CORE COMPETENCIES & TECHNICAL SKILLS ---
    story.append(Paragraph("CORE COMPETENCIES & TECHNICAL SKILLS", section_heading))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceBefore=2, spaceAfter=6))
    
    skills_data = [
        [
            Paragraph("<b>Software Engineering:</b>", body_style),
            Paragraph("React.js, JavaScript (ES6+), TypeScript, Python, HTML5, CSS3, RESTful APIs, Git & GitHub", body_style)
        ],
        [
            Paragraph("<b>ERP & Architecture:</b>", body_style),
            Paragraph("Centralized ERP Systems, Relational Database Schema Design (SQL), Workflow Automation, System Documentation", body_style)
        ],
        [
            Paragraph("<b>Quality Assurance (QA):</b>", body_style),
            Paragraph("Process Auditing, Compliance Audits, Service Standard Benchmarks, Operational Accuracy, Root-Cause Analysis", body_style)
        ],
        [
            Paragraph("<b>Leadership & Management:</b>", body_style),
            Paragraph("Cross-Functional Operations Management, Stakeholder Communication, Agile/Scrum, Requirements Engineering", body_style)
        ]
    ]
    skills_table = Table(skills_data, colWidths=[1.8 * inch, 5.6 * inch])
    skills_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(skills_table)
    story.append(Spacer(1, 10))
    
    # --- PROFESSIONAL EXPERIENCE ---
    story.append(Paragraph("PROFESSIONAL EXPERIENCE", section_heading))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceBefore=2, spaceAfter=8))
    
    # Job 1: ERP & Full Stack
    j1_header = [
        [Paragraph("Full-Stack Software Engineer & ERP Architect", job_title_style), Paragraph("2024 — Present", date_style)],
        [Paragraph("Private Client Projects & Collaborative Development", company_style), Paragraph("Collaborative Team", date_style)]
    ]
    t1 = Table(j1_header, colWidths=[5.4 * inch, 2.0 * inch])
    t1.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('PADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t1)
    story.append(Spacer(1, 4))
    story.append(Paragraph("• Collaborated alongside team to architect, document, and engineer a <b>Centralized ERP System</b>, converting complex business workflows into structured, scalable modular software.", bullet_style))
    story.append(Paragraph("• Integrated multi-department modules across inventory, accounting, and task automation, reducing manual procedural handoffs by 65%.", bullet_style))
    story.append(Paragraph("• Conducted client stakeholder sessions to formulate detailed technical specifications, database schema diagrams, and responsive dashboard interfaces.", bullet_style))
    story.append(Spacer(1, 8))
    
    # Job 2: RepairDesk
    j2_header = [
        [Paragraph("Software Development Intern", job_title_style), Paragraph("2024 (2 Months)", date_style)],
        [Paragraph("RepairDesk", company_style), Paragraph("Remote SaaS House", date_style)]
    ]
    t2 = Table(j2_header, colWidths=[5.4 * inch, 2.0 * inch])
    t2.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('PADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t2)
    story.append(Spacer(1, 4))
    story.append(Paragraph("• Completed an intensive two-month remote software development internship inside a fast-paced international SaaS software house.", bullet_style))
    story.append(Paragraph("• Contributed to production repair ticketing flows, device diagnostic tracking, and automated customer status notifications.", bullet_style))
    story.append(Paragraph("• Actively participated in daily agile stand-ups, code reviews, and sprint planning under senior engineering mentorship.", bullet_style))
    story.append(Spacer(1, 8))

    # Job 3: DMC
    j3_header = [
        [Paragraph("Operations Manager", job_title_style), Paragraph("2022 — 2023", date_style)],
        [Paragraph("DMC", company_style), Paragraph("Onsite Leadership", date_style)]
    ]
    t3 = Table(j3_header, colWidths=[5.4 * inch, 2.0 * inch])
    t3.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('PADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t3)
    story.append(Spacer(1, 4))
    story.append(Paragraph("• Oversaw end-to-end daily operations, managed cross-functional team execution, and instituted operational performance benchmarks.", bullet_style))
    story.append(Paragraph("• Streamlined team communication protocols and eliminated recurring process bottlenecks, boosting daily task completion rate by 35%.", bullet_style))
    story.append(Paragraph("• Served as the primary operational strategist, identifying software and digital automation needs that triggered strategic transition into software engineering.", bullet_style))
    story.append(Spacer(1, 8))

    # Job 4: JS Bank
    j4_header = [
        [Paragraph("Operations Specialist — Kamyab Jawan Program", job_title_style), Paragraph("2021 — 2022", date_style)],
        [Paragraph("JS Bank", company_style), Paragraph("Banking & Youth Empowerment", date_style)]
    ]
    t4 = Table(j4_header, colWidths=[5.4 * inch, 2.0 * inch])
    t4.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('PADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t4)
    story.append(Spacer(1, 4))
    story.append(Paragraph("• Dedicated one full year supporting the national <b>Kamyab Jawan Program</b>, driving youth entrepreneurship and financial accessibility.", bullet_style))
    story.append(Paragraph("• Assisted hundreds of emerging startup founders in navigating banking frameworks, reviewing business feasibility, and securing loan allocations.", bullet_style))
    story.append(Paragraph("• Maintained strict regulatory compliance and accurate operational documentation between applicant portfolios and credit approval channels.", bullet_style))
    story.append(Spacer(1, 8))

    # Job 5: UBL
    j5_header = [
        [Paragraph("Quality Assurance (QA) Auditor & Frontline Operations", job_title_style), Paragraph("2018 — 2021", date_style)],
        [Paragraph("United Bank Limited (UBL)", company_style), Paragraph("Banking Operations", date_style)]
    ]
    t5 = Table(j5_header, colWidths=[5.4 * inch, 2.0 * inch])
    t5.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('PADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t5)
    story.append(Spacer(1, 4))
    story.append(Paragraph("• Started on the frontlines as a Customer Service Agent and earned internal progression into the <b>Quality Assurance (QA) Department</b> through outstanding consistency and attention to detail.", bullet_style))
    story.append(Paragraph("• Audited high-volume banking workflows, customer interaction pipelines, and transaction protocols, maintaining a 99.4% quality compliance rating.", bullet_style))
    story.append(Paragraph("• Authored process evaluation reports and delivered coaching to operational teams to eliminate systemic procedural errors.", bullet_style))
    story.append(Spacer(1, 8))

    # Job 6: Foundation
    j6_header = [
        [Paragraph("Administrative & Operations Associate", job_title_style), Paragraph("2016 — 2018", date_style)],
        [Paragraph("Private Firms & Commercial Offices", company_style), Paragraph("Early Career", date_style)]
    ]
    t6 = Table(j6_header, colWidths=[5.4 * inch, 2.0 * inch])
    t6.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('PADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t6)
    story.append(Spacer(1, 4))
    story.append(Paragraph("• Began career at age 18 following Intermediate completion; built a solid foundation in office administration, client communication, and workplace discipline.", bullet_style))
    story.append(Spacer(1, 10))

    # --- EDUCATION & TRAINING ---
    story.append(Paragraph("EDUCATION & PROFESSIONAL TRAINING", section_heading))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceBefore=2, spaceAfter=6))
    
    edu_data = [
        [
            Paragraph("<b>Software Engineering & Modern Development</b>", body_style),
            Paragraph("Digital Education", body_style),
            Paragraph("2023 — 2024", date_style)
        ],
        [
            Paragraph("<b>Quality Assurance & Banking Process Standards</b>", body_style),
            Paragraph("UBL QA Internal Training", body_style),
            Paragraph("2019", date_style)
        ],
        [
            Paragraph("<b>Intermediate Education</b>", body_style),
            Paragraph("Higher Secondary School Certificate", body_style),
            Paragraph("Foundational", date_style)
        ]
    ]
    edu_table = Table(edu_data, colWidths=[3.2 * inch, 2.6 * inch, 1.6 * inch])
    edu_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(edu_table)
    story.append(Spacer(1, 10))

    # --- LANGUAGES ---
    story.append(Paragraph("LANGUAGES", section_heading))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceBefore=2, spaceAfter=6))
    lang_text = "<b>Urdu:</b> Native / Bilingual &nbsp;&nbsp;|&nbsp;&nbsp; <b>English:</b> Professional Working Proficiency"
    story.append(Paragraph(lang_text, body_style))

    doc.build(story)
    print(f"Resume generated successfully at: {pdf_path}")

if __name__ == "__main__":
    build_pdf()
