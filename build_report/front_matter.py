from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from build_report.styles import (
    PAGE_WIDTH, PAGE_HEIGHT, USABLE_WIDTH, COLOR_PRIMARY, COLOR_DARK,
    COLOR_TEXT, COLOR_MUTED, COLOR_ACCENT, PageTracker
)

def build_cover_page(styles):
    story = []
    
    # Outer academic decorative double frame
    story.append(Spacer(1, 20))
    story.append(Paragraph("<font size=12 color='#64748B'><b>A PROJECT REPORT ON</b></font>", styles['CoverSubtitle']))
    story.append(Spacer(1, 15))
    
    story.append(Paragraph("<b>AI-Powered CV and Job Description Matcher</b>", styles['CoverTitle']))
    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>An AI-Based Resume Analysis and Job Screening Assistance System</b>", styles['CoverSubtitle']))
    story.append(Spacer(1, 25))
    
    story.append(Paragraph("<i>Submitted in partial fulfillment of the requirements for the award of the degree of</i>", styles['CoverSubtitle']))
    story.append(Spacer(1, 8))
    story.append(Paragraph("<font size=12 color='#0F172A'><b>BACHELOR OF TECHNOLOGY / MASTER OF SCIENCE</b></font><br/><font size=10 color='#64748B'>IN</font><br/><font size=11 color='#1E3A8A'><b>COMPUTER SCIENCE AND ENGINEERING / SOFTWARE ENGINEERING</b></font>", styles['CoverSubtitle']))
    story.append(Spacer(1, 40))

    # Meta Table: Submitted By & Supervised By
    left_meta = [
        Paragraph("<b>Submitted By:</b>", styles['CoverMetaLabel']),
        Spacer(1, 4),
        Paragraph("<b>Name:</b> [Student Name]", styles['CoverMetaValue']),
        Paragraph("<b>Roll / Reg No:</b> [Roll Number]", styles['CoverMetaValue']),
        Paragraph("<b>Degree:</b> [Course/Degree]", styles['CoverMetaValue']),
        Paragraph("<b>Department:</b> [Department]", styles['CoverMetaValue']),
    ]
    
    right_meta = [
        Paragraph("<b>Supervised / Guided By:</b>", styles['CoverMetaLabel']),
        Spacer(1, 4),
        Paragraph("<b>Project Guide:</b> [Project Guide]", styles['CoverMetaValue']),
        Paragraph("<b>Designation:</b> Associate Professor / Project Mentor", styles['CoverMetaValue']),
        Paragraph("<b>Department:</b> [Department]", styles['CoverMetaValue']),
        Paragraph("<b>Institution:</b> [College/University]", styles['CoverMetaValue']),
    ]

    meta_table = Table([[left_meta, right_meta]], colWidths=[USABLE_WIDTH * 0.5, USABLE_WIDTH * 0.5])
    meta_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#CBD5E1')),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 45))

    # Institutional Footer
    inst_block = [
        Paragraph("<font size=11 color='#1E3A8A'><b>DEPARTMENT OF [Department]</b></font>", styles['CoverSubtitle']),
        Paragraph("<font size=12 color='#0F172A'><b>[College/University]</b></font>", styles['CoverSubtitle']),
        Paragraph("<font size=9 color='#64748B'>Academic Year: [Academic Year] | Submission Date: [Submission Date]</font>", styles['CoverSubtitle']),
    ]
    story.extend(inst_block)
    story.append(PageBreak())
    return story

def build_certificate(styles, registry):
    story = []
    story.append(PageTracker('cert', registry, 'Certificate of Approval', 'front'))
    story.append(Paragraph("<b>DEPARTMENT OF [Department]</b>", styles['CoverSubtitle']))
    story.append(Paragraph("<b>[College/University]</b>", styles['CoverSubtitle']))
    story.append(Spacer(1, 15))
    
    story.append(Paragraph("<b>CERTIFICATE</b>", styles['DocChapterTitle']))
    story.append(Spacer(1, 15))
    
    cert_text = (
        "This is to certify that the project report entitled <b>\"AI-Powered CV and Job Description Matcher: "
        "An AI-Based Resume Analysis and Job Screening Assistance System\"</b> submitted by <b>[Student Name]</b> "
        "(Roll Number: <b>[Roll Number]</b>) in partial fulfillment of the requirements for the award of the degree of "
        "<b>[Course/Degree]</b> in <b>[Department]</b> at <b>[College/University]</b> is an authentic record of the "
        "academic software engineering work carried out under my supervision and guidance during the academic year <b>[Academic Year]</b>.<br/><br/>"
        "The results embodied in this report have been verified for technical soundness, software engineering rigor, and ethical compliance, "
        "and have not been submitted elsewhere for the award of any other degree or diploma."
    )
    story.append(Paragraph(cert_text, styles['DocBody']))
    story.append(Spacer(1, 60))

    # Signature Table
    sig_data = [
        [
            Paragraph("____________________________<br/><b>[Project Guide]</b><br/>Project Guide & Supervisor<br/>Department of [Department]<br/>[College/University]", styles['DocTableCell']),
            Paragraph("____________________________<br/><b>Head of Department</b><br/>Department of [Department]<br/>[College/University]", styles['DocTableCell'])
        ],
        [
            Paragraph("<br/><br/>____________________________<br/><b>Internal Examiner</b><br/>Date: [Submission Date]", styles['DocTableCell']),
            Paragraph("<br/><br/>____________________________<br/><b>External Examiner</b><br/>Date: [Submission Date]", styles['DocTableCell'])
        ]
    ]
    sig_table = Table(sig_data, colWidths=[USABLE_WIDTH * 0.5, USABLE_WIDTH * 0.5])
    sig_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 15),
    ]))
    story.append(sig_table)
    story.append(PageBreak())
    return story

def build_declaration(styles, registry):
    story = []
    story.append(PageTracker('decl', registry, 'Candidate Declaration', 'front'))
    story.append(Paragraph("<b>CANDIDATE DECLARATION</b>", styles['DocChapterTitle']))
    story.append(Spacer(1, 15))
    
    decl_text = (
        "I hereby declare that the software project entitled <b>\"AI-Powered CV and Job Description Matcher: "
        "An AI-Based Resume Analysis and Job Screening Assistance System\"</b> presented in this report is an original "
        "work developed by me under the academic guidance of <b>[Project Guide]</b>, Department of <b>[Department]</b>, "
        "<b>[College/University]</b>.<br/><br/>"
        "I explicitly confirm that:<br/>"
        "1. The conceptual design, system architecture, database models, algorithmic scoring mechanisms, ATS audit checks, "
        "and user interface mockups documented herein represent bona fide academic investigation and technical implementation.<br/>"
        "2. All literature, libraries, algorithms, third-party software frameworks, and application programming interfaces (APIs) "
        "consulted or incorporated during this project have been fully acknowledged and cited according to standard academic conventions.<br/>"
        "3. The analytical scoring models, match percentages, and estimated shortlist probabilities generated by this system are "
        "diagnostic estimations designed for candidate feedback and do not constitute absolute guarantees of corporate employment or interview selection.<br/>"
        "4. This work has not formed the basis for the award of any other academic degree, diploma, associate-ship, or fellowship at this or any other university."
    )
    story.append(Paragraph(decl_text, styles['DocBody']))
    story.append(Spacer(1, 70))

    sub_data = [
        [
            Paragraph("<b>Place:</b> [City / Campus]<br/><b>Date:</b> [Submission Date]", styles['DocTableCell']),
            Paragraph("____________________________<br/><b>[Student Name]</b><br/>Roll Number: [Roll Number]<br/>Department of [Department]<br/>[College/University]", styles['DocTableCell'])
        ]
    ]
    sub_table = Table(sub_data, colWidths=[USABLE_WIDTH * 0.5, USABLE_WIDTH * 0.5])
    sub_table.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP')]))
    story.append(sub_table)
    story.append(PageBreak())
    return story

def build_acknowledgement(styles, registry):
    story = []
    story.append(PageTracker('ack', registry, 'Acknowledgement', 'front'))
    story.append(Paragraph("<b>ACKNOWLEDGEMENT</b>", styles['DocChapterTitle']))
    story.append(Spacer(1, 15))
    
    ack_text = (
        "The successful completion of this academic software project on <b>AI-Powered CV and Job Description Matcher</b> "
        "has been made possible through the support, encouragement, and intellectual guidance of numerous individuals and institutions.<br/><br/>"
        "First and foremost, I express my deepest gratitude and profound respect to my project guide, <b>[Project Guide]</b>, "
        "for their invaluable guidance, insightful technical reviews, and constant encouragement throughout the system design, "
        "algorithmic formulation, and report preparation phases.<br/><br/>"
        "I extend my sincere thanks to the <b>Head of the Department, [Department]</b>, and the faculty members of <b>[College/University]</b> "
        "for providing state-of-the-art computational infrastructure, laboratories, and an intellectually stimulating environment that fostered this work.<br/><br/>"
        "I am grateful to my fellow student peers and open-source software communities across FastAPI, React, and NLP research for their collaborative "
        "discussions and foundational software frameworks that enabled the realization of this project.<br/><br/>"
        "Finally, I express my heartfelt indebtedness to my family and friends for their enduring patience, moral encouragement, and unwavering support "
        "throughout the duration of my academic program."
    )
    story.append(Paragraph(ack_text, styles['DocBody']))
    story.append(Spacer(1, 40))
    story.append(Paragraph("<b>[Student Name]</b><br/>Department of [Department]<br/>[College/University]", styles['DocBodyBold']))
    story.append(PageBreak())
    return story

def build_abstract(styles, registry):
    story = []
    story.append(PageTracker('abstract', registry, 'Abstract', 'front'))
    story.append(Paragraph("<b>ABSTRACT</b>", styles['DocChapterTitle']))
    story.append(Spacer(1, 10))
    
    p1 = (
        "In the contemporary global recruitment ecosystem, the volume of digital job applications submitted to corporate requisitions "
        "has grown exponentially, regularly exceeding several hundred resumes per open position. To cope with this immense influx, enterprise "
        "organizations heavily deploy Applicant Tracking Systems (ATS) to automate initial candidate screening, filtering, and ranking. "
        "However, this reliance on automated parsing introduces substantial friction and systemic information asymmetry. Qualified candidates "
        "frequently fail initial automated screenings due to lexical mismatches (e.g., using synonymous terminology or unexpanded acronyms), "
        "unfavorable document formatting (such as complex tables, multi-column layouts, or unreadable headers), or subtle omissions of required "
        "technical competencies. Conversely, manual CV-JD cross-referencing is highly tedious, subjective, and prone to oversight."
    )
    story.append(Paragraph(p1, styles['DocBody']))
    story.append(Spacer(1, 6))

    p2 = (
        "To resolve these challenges, this project presents the design, architectural formulation, and implementation of the "
        "<b>AI-Powered CV and Job Description Matcher</b>, an intelligent, web-based software system that combines natural language processing (NLP), "
        "semantic knowledge graphs, heuristic rule engines, and Large Language Model (LLM) abstractions to perform rigorous, explainable resume-job "
        "description compatibility analysis. The system accepts candidate CVs across diverse file formats (PDF, DOCX, TXT) alongside target job requisitions, "
        "extracts unstructured textual content, detects potential ATS parsing hazards, and normalizes candidate qualifications against requisition demands."
    )
    story.append(Paragraph(p2, styles['DocBody']))
    story.append(Spacer(1, 6))

    p3 = (
        "The cognitive core of the proposed system introduces a multi-tier matching and scoring architecture. Rather than relying on naive keyword counting, "
        "the engine differentiates between <b>Exact Matches</b>, <b>Canonical Synonyms</b> (e.g., <i>Postgres</i> ↔ <i>PostgreSQL</i>), and "
        "<b>Partial Sibling Technologies</b> (e.g., correlating <i>RabbitMQ</i> experience against a <i>Kafka</i> requirement via taxonomy graphs), while "
        "explicitly flagging missing mandatory and preferred skills. Furthermore, the system incorporates a 12-point ATS structural compliance audit, "
        "computes a transparent 7-factor weighted match score (0–100%), models an estimated shortlist screening probability, and synthesizes actionable, "
        "quantified bullet-point improvement suggestions equipped with strict anti-hallucination guardrails."
    )
    story.append(Paragraph(p3, styles['DocBody']))
    story.append(Spacer(1, 6))

    p4 = (
        "The software is engineered using a robust full-stack architecture comprising a React 18 and TypeScript single-page frontend styled with Tailwind CSS, "
        "a high-performance Python 3.11 and FastAPI backend, and an extensible persistence layer built on SQLAlchemy supporting SQLite and PostgreSQL. "
        "The application empowers job seekers to identify critical competency gaps, optimize document ATS compliance, and articulate their genuine qualifications "
        "with maximum clarity prior to official submission."
    )
    story.append(Paragraph(p4, styles['DocBody']))
    story.append(Spacer(1, 10))

    keywords = (
        "<b>Keywords:</b> Resume Analysis, Job Description Matching, Applicant Tracking Systems (ATS), "
        "Natural Language Processing (NLP), Semantic Similarity, Large Language Models (LLM), Keyword Extraction, "
        "Recruitment Technology, Decision Support System."
    )
    story.append(Paragraph(keywords, styles['DocBodyBold']))
    story.append(PageBreak())
    return story

def build_table_of_contents(styles, registry):
    story = []
    story.append(PageTracker('toc', registry, 'Table of Contents', 'front'))
    story.append(Paragraph("<b>TABLE OF CONTENTS</b>", styles['DocChapterTitle']))
    story.append(Spacer(1, 10))

    # TOC Structure definition
    toc_items = [
        ("Certificate of Approval", 'cert', False),
        ("Candidate Declaration", 'decl', False),
        ("Acknowledgement", 'ack', False),
        ("Abstract", 'abstract', False),
        ("1. BACKGROUND OF THE STUDY", 'ch1', True),
        ("    1.1 Introduction", 'sec1_1', False),
        ("    1.2 Background", 'sec1_2', False),
        ("    1.3 Existing Recruitment Process", 'sec1_3', False),
        ("    1.4 Role of ATS in Recruitment", 'sec1_4', False),
        ("    1.5 Role of Artificial Intelligence", 'sec1_5', False),
        ("    1.6 Need for the Proposed System", 'sec1_6', False),
        ("2. PROBLEM STATEMENT", 'ch2', True),
        ("    2.1 Existing System", 'sec2_1', False),
        ("    2.2 Limitations of Existing System", 'sec2_2', False),
        ("    2.3 Proposed System", 'sec2_3', False),
        ("3. OBJECTIVES AND SCOPE OF THE PROJECT", 'ch3', True),
        ("    3.1 Objectives", 'sec3_1', False),
        ("    3.2 Scope (In Scope & Out of Scope)", 'sec3_2', False),
        ("    3.3 Limitations of the Study", 'sec3_3', False),
        ("4. ADVANTAGES OF PROPOSED SYSTEM", 'ch4', True),
        ("    4.1 Key Advantages and Innovations", 'sec4_1', False),
        ("    4.2 Comparative Feature Analysis Matrix", 'sec4_2', False),
        ("5. REQUIREMENT ANALYSIS AND FEASIBILITY STUDY", 'ch5', True),
        ("    5.1 Functional Requirements Specification", 'sec5_1', False),
        ("    5.2 Non-Functional Requirements Specification", 'sec5_2', False),
        ("    5.3 User Requirements & Persona Workflows", 'sec5_3', False),
        ("    5.4 System & Operational Requirements", 'sec5_4', False),
        ("    5.5 Feasibility Study (Technical, Economic, Operational, Legal/Ethical)", 'sec5_5', False),
        ("6. SOFTWARE AND HARDWARE REQUIREMENTS", 'ch6', True),
        ("    6.1 Software Requirements Matrix", 'sec6_1', False),
        ("    6.2 Hardware Requirements Specification", 'sec6_2', False),
        ("7. SYSTEM DESIGN AND DATABASE DESIGN", 'ch7', True),
        ("    7.1 System Architecture", 'sec7_1', False),
        ("    7.2 System Workflow & Execution Flowchart", 'sec7_2', False),
        ("    7.3 Data Flow Diagrams (Level 0 & Level 1 DFD)", 'sec7_3', False),
        ("    7.4 Entity Relationship Diagram & Relational Schemas", 'sec7_4', False),
        ("8. DEVELOPMENT ENVIRONMENT & CODING STANDARDS", 'ch8', True),
        ("    8.1 Frontend & UI Development Environment", 'sec8_1', False),
        ("    8.2 Backend & API Development Environment", 'sec8_2', False),
        ("    8.3 AI Integration & Prompt Engineering Architecture", 'sec8_3', False),
        ("    8.4 Database Management & ORM Integration", 'sec8_4', False),
        ("    8.5 Software Coding Standards & Best Practices", 'sec8_5', False),
        ("    8.6 Detailed System Module Descriptions (Modules 1–9)", 'sec8_6', False),
        ("9. SOURCE CODE (IMPORTANT MODULES)", 'ch9', True),
        ("    9.1 Resume Upload API Controller", 'sec9_1', False),
        ("    9.2 Job Description Ingestion API Controller", 'sec9_2', False),
        ("    9.3 PDF and DOCX Document Text Extraction", 'sec9_3', False),
        ("    9.4 Structured Resume Parser Engine", 'sec9_4', False),
        ("    9.5 Structured Job Requirement Extractor", 'sec9_5', False),
        ("    9.6 Semantic Skill and Sibling Matching Engine", 'sec9_6', False),
        ("    9.7 Configurable Multi-Factor Scoring Engine", 'sec9_7', False),
        ("    9.8 12-Point ATS Structural Compliance Checker", 'sec9_8', False),
        ("    9.9 Multi-Provider LLM & AI Service Layer", 'sec9_9', False),
        ("    9.10 Anti-Hallucinating Recommendation Generator", 'sec9_10', False),
        ("    9.11 SQLAlchemy Database Relational Models", 'sec9_11', False),
        ("    9.12 Frontend REST API Client & Dispatcher", 'sec9_12', False),
        ("10. TESTING AND QUALITY ASSURANCE", 'ch10', True),
        ("    10.1 Testing Objectives & Quality Goals", 'sec10_1', False),
        ("    10.2 Testing Methodologies & Classification", 'sec10_2', False),
        ("    10.3 Comprehensive Test Cases & Execution Specification", 'sec10_3', False),
        ("    10.4 Automated Test Suite Execution Results", 'sec10_4', False),
        ("11. INPUT AND OUTPUT SCREENS", 'ch11', True),
        ("    11.1 Input User Interfaces", 'sec11_1', False),
        ("    11.2 Output & Analytics User Interfaces", 'sec11_2', False),
        ("12. CONCLUSION", 'ch12', True),
        ("13. FUTURE ENHANCEMENTS", 'ch13', True),
        ("REFERENCES", 'refs', True),
        ("APPENDIX", 'app', True),
    ]

    table_data = []
    for title, key, is_chapter in toc_items:
        page_val = registry.get(key, {}).get('page', '--')
        # Format Roman numerals for front matter
        if key in ['cert', 'decl', 'ack', 'abstract', 'toc']:
            roman_map = {'cert': 'ii', 'decl': 'iii', 'ack': 'iv', 'abstract': 'v', 'toc': 'vi'}
            page_str = roman_map.get(key, str(page_val))
        else:
            page_str = str(page_val)

        p_style = styles['TOCChapter'] if is_chapter else styles['TOCItem']
        
        # Leader dots
        title_para = Paragraph(f"<b>{title}</b>" if is_chapter else title, p_style)
        page_para = Paragraph(f"<b>{page_str}</b>" if is_chapter else page_str, ParagraphStyle('TOCP', parent=p_style, alignment=2))
        table_data.append([title_para, page_para])

    toc_table = Table(table_data, colWidths=[USABLE_WIDTH * 0.88, USABLE_WIDTH * 0.12])
    toc_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 1.8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.8),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(toc_table)
    story.append(PageBreak())
    return story

def build_list_of_figures_and_tables(styles, registry):
    story = []
    story.append(Paragraph("<b>LIST OF FIGURES</b>", styles['DocChapterTitle']))
    story.append(Spacer(1, 8))

    figures = [
        ("Figure 7.1: Multi-Tier System Architecture Diagram", 'fig7_1'),
        ("Figure 7.2: Detailed System Execution Flowchart", 'fig7_2'),
        ("Figure 7.3: Level 0 Data Flow Diagram (Context Diagram)", 'fig7_3'),
        ("Figure 7.4: Level 1 Data Flow Diagram (Decomposed Processes)", 'fig7_4'),
        ("Figure 7.5: Relational Entity Relationship Diagram (ERD)", 'fig7_5'),
        ("Figure 8.1: Configurable 7-Factor Scoring Weight Distribution", 'fig8_1'),
        ("Figure 11.1: Home Page and Navigation Header (Illustrative UI Mockup)", 'fig11_1'),
        ("Figure 11.2: Dual Document Ingestion Interface (Illustrative UI Mockup)", 'fig11_2'),
        ("Figure 11.3: Interactive Scoring Weights Configuration Modal (Illustrative UI Mockup)", 'fig11_3'),
        ("Figure 11.4: Multi-Metric Overall Match and ATS Dashboard (Illustrative UI Mockup)", 'fig11_4'),
        ("Figure 11.5: Semantic Skill & Keyword Analysis Matrix (Illustrative UI Mockup)", 'fig11_5'),
        ("Figure 11.6: Granular Experience Gap & Evidence Matrix (Illustrative UI Mockup)", 'fig11_6'),
        ("Figure 11.7: 12-Point ATS Audit & Hazard Diagnostic Card (Illustrative UI Mockup)", 'fig11_7'),
        ("Figure 11.8: Actionable Improvement Suggestions and Final Assessment (Illustrative UI Mockup)", 'fig11_8'),
    ]

    fig_data = []
    for title, key in figures:
        p_num = str(registry.get(key, {}).get('page', '--'))
        fig_data.append([Paragraph(title, styles['TOCItem']), Paragraph(p_num, ParagraphStyle('FP', parent=styles['TOCItem'], alignment=2))])

    t_fig = Table(fig_data, colWidths=[USABLE_WIDTH * 0.88, USABLE_WIDTH * 0.12])
    t_fig.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t_fig)
    story.append(Spacer(1, 16))

    story.append(Paragraph("<b>LIST OF TABLES</b>", styles['DocChapterTitle']))
    story.append(Spacer(1, 8))

    tables = [
        ("Table 2.1: Critical Limitations of Legacy CV Screening Systems", 'tab2_1'),
        ("Table 4.1: Comprehensive Comparative Analysis Matrix (Traditional vs Proposed)", 'tab4_1'),
        ("Table 6.1: Complete Software Environment & Development Toolchain", 'tab6_1'),
        ("Table 6.2: Minimum and Recommended Hardware Specifications", 'tab6_2'),
        ("Table 8.1: Scoring Engine Weight Allocations & Evaluation Focus", 'tab8_1'),
        ("Table 8.2: 12-Point ATS Compatibility Audit Rulebook", 'tab8_2'),
        ("Table 10.1: Comprehensive Test Suite Cases & Execution Results", 'tab10_1'),
        ("Table 10.2: Automated Pytest Execution Verification Summary", 'tab10_2'),
        ("Table E.1: ATS Hazard Detection Regex and Pattern Rules", 'tab_app_e'),
        ("Table F.1: Scoring Weights Sensitivity Analysis Scenarios", 'tab_app_f'),
    ]

    tab_data = []
    for title, key in tables:
        p_num = str(registry.get(key, {}).get('page', '--'))
        tab_data.append([Paragraph(title, styles['TOCItem']), Paragraph(p_num, ParagraphStyle('TP', parent=styles['TOCItem'], alignment=2))])

    t_tab = Table(tab_data, colWidths=[USABLE_WIDTH * 0.88, USABLE_WIDTH * 0.12])
    t_tab.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t_tab)
    story.append(PageBreak())
    return story
