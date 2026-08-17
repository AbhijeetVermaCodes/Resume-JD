from reportlab.lib import colors
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from build_report.styles import (
    USABLE_WIDTH, COLOR_PRIMARY, COLOR_DARK, COLOR_TEXT, COLOR_MUTED,
    COLOR_ACCENT, COLOR_LIGHT_BG, COLOR_BORDER, COLOR_BORDER_LIGHT,
    PageTracker, make_callout
)

def build_chapter_1(styles, registry):
    story = []
    story.append(PageTracker('ch1', registry, '1. Background of the Study', 'chapter'))
    story.append(Paragraph("<b>1. BACKGROUND OF THE STUDY</b>", styles['DocChapterTitle']))
    story.append(Spacer(1, 4))

    # 1.1 Introduction
    story.append(PageTracker('sec1_1', registry, '1.1 Introduction', 'section'))
    story.append(Paragraph("<b>1.1 Introduction</b>", styles['DocSectionTitle']))
    p1 = (
        "The contemporary employment and talent acquisition landscape has experienced a profound structural transformation "
        "driven by the ubiquity of digital job boards, professional networking platforms (e.g., LinkedIn, Indeed, Glassdoor), "
        "and one-click application portals. While these digital platforms have substantially democratized access to career "
        "opportunities, they have simultaneously catalyzed an unprecedented surge in application volumes. Enterprise organizations "
        "and growth-stage technology companies routinely receive hundreds—and in many high-visibility corporate postings, "
        "thousands—of curriculum vitae (CVs) and resumes for every single open requisition."
    )
    story.append(Paragraph(p1, styles['DocBody']))

    p2 = (
        "Faced with this immense administrative bottleneck, human talent acquisition teams are physically unable to perform "
        "exhaustive, manual line-by-line evaluations of every submitted dossier. Consequently, enterprise recruitment workflows "
        "have become heavily reliant on automated <b>Applicant Tracking Systems (ATS)</b>. These automated software suites act as "
        "initial algorithmic gatekeepers, ingesting digital documents, extracting candidate information, filtering out non-conforming "
        "profiles, and ranking candidates based on keyword frequency, lexical overlap, and basic educational thresholds."
    )
    story.append(Paragraph(p2, styles['DocBody']))

    p3 = (
        "However, legacy ATS architectures and unassisted manual screening processes suffer from critical systemic flaws. Traditional "
        "keyword matching relies on exact string equality or basic stemming, which frequently penalizes candidates who express "
        "equivalent competencies using synonymous phrasing, alternative industry terminology, or unexpanded acronyms. Furthermore, "
        "the recruitment screening phase often emphasizes surface-level keyword presence while failing to evaluate the deeper "
        "semantic context of a candidate's demonstrated project impact, engineering responsibilities, and seniority trajectory. "
        "This dynamic creates a profound information asymmetry and communication breakdown between qualified job seekers and "
        "prospective employers."
    )
    story.append(Paragraph(p3, styles['DocBody']))

    # 1.2 Background
    story.append(PageTracker('sec1_2', registry, '1.2 Background', 'section'))
    story.append(Paragraph("<b>1.2 Background</b>", styles['DocSectionTitle']))
    p4 = (
        "The evaluation of a candidate's resume against a complex Job Description (JD) represents a non-trivial information retrieval "
        "and semantic matching challenge. A typical technical job description encapsulates multiple multidimensional constraints, "
        "including core programming languages, modern architectural frameworks, cloud infrastructure platforms, data storage engines, "
        "minimum years of progressive industry experience, educational credentials, domain-specific regulatory knowledge, and essential "
        "collaborative soft skills."
    )
    story.append(Paragraph(p4, styles['DocBody']))

    p5 = (
        "A prevalent issue in recruitment science is the <i>competency articulation gap</i>: a candidate may genuinely possess the requisite "
        "technical expertise, problem-solving acumen, and hands-on domain experience to excel in a role, yet fail to pass the initial automated "
        "or human screening. This failure commonly occurs because the candidate's resume lacks the precise lexical keywords prioritized by "
        "an automated filter, presents critical accomplishments in passive or non-quantified phrasing, or embeds crucial skills in visual "
        "formatting structures (such as multi-column tables, text boxes, or graphical header blocks) that corrupt ATS document parsers. "
        "Without intelligent, pre-submission diagnostic tooling, job seekers are forced to navigate the hiring pipeline blindly, resulting in "
        "high application attrition, demoralization, and substantial loss of qualified talent for hiring organizations."
    )
    story.append(Paragraph(p5, styles['DocBody']))

    # 1.3 Existing Recruitment Process
    story.append(PageTracker('sec1_3', registry, '1.3 Existing Recruitment Process', 'section'))
    story.append(Paragraph("<b>1.3 Existing Recruitment Process</b>", styles['DocSectionTitle']))
    p6 = (
        "The standard end-to-end recruitment lifecycle across modern corporate and technology enterprises follows a structured, "
        "multi-stage pipeline comprising the following eight distinct operational phases:"
    )
    story.append(Paragraph(p6, styles['DocBody']))

    steps = [
        "<b>Stage 1: Requisition Creation & Job Posting:</b> Hiring managers collaborate with talent acquisition specialists to formulate the official Job Description, defining core responsibilities, mandatory technical requirements, preferred qualifications, and organizational expectations.",
        "<b>Stage 2: Candidate Application:</b> Job seekers discover the requisition via corporate careers portals or external job boards and submit their profile data alongside digital CV/resume documents (PDF or DOCX).",
        "<b>Stage 3: Resume Submission & Ingestion:</b> The corporate ATS ingests the submitted document, parsing raw binary streams into plain text and mapping extracted blocks into database fields.",
        "<b>Stage 4: Automated ATS Screening & Parsing:</b> The ATS executes rule-based Boolean queries, keyword density filters, and credential checks, assigning preliminary candidate rankings and automatically rejecting sub-threshold submissions.",
        "<b>Stage 5: Recruiter Manual Review:</b> Human recruiters rapidly scan shortlisted resumes—allocating an industry-average of 6 to 7 seconds per CV—to verify high-level role alignment, current employer pedigree, and keyword prominence.",
        "<b>Stage 6: Technical / Hiring Manager Screening:</b> Resumes that pass the initial recruiter filter are forwarded to the hiring manager and lead engineers for in-depth evaluation of project relevance and architectural depth.",
        "<b>Stage 7: Multi-Round Structured Interviews:</b> Candidates undergo sequential evaluations, including technical coding assessments, system design interviews, behavioral reviews, and cultural alignment discussions.",
        "<b>Stage 8: Offer & Final Selection:</b> Background checks, reference verifications, and compensation negotiations culminate in the final employment contract."
    ]
    for step in steps:
        story.append(Paragraph(f"• {step}", styles['DocBullet']))
    story.append(Spacer(1, 4))

    # 1.4 Role of ATS in Recruitment
    story.append(PageTracker('sec1_4', registry, '1.4 Role of ATS in Recruitment', 'section'))
    story.append(Paragraph("<b>1.4 Role of ATS in Recruitment</b>", styles['DocSectionTitle']))
    p7 = (
        "Applicant Tracking Systems function as the backbone of modern corporate hiring infrastructure. At their core, ATS platforms "
        "execute four fundamental operations: document text parsing, entity extraction, rule-based keyword matching, and candidate ranking. "
        "When an applicant uploads a CV, the ATS attempts to deconstruct the unstructured document into structured semantic entities: "
        "Contact Information, Professional Summary, Work History, Education, and Technical Skills."
    )
    story.append(Paragraph(p7, styles['DocBody']))

    p8 = (
        "<b>Critical Limitations of Commercial ATS Engines:</b><br/>"
        "Despite their widespread adoption, commercial ATS engines exhibit notable technical limitations. Most legacy parsers rely on "
        "inflexible optical or layout assumptions. Complex typographic elements—such as multi-column layouts, floating text frames, "
        "nested tables, non-standard section headers (e.g., 'Core Competencies' vs 'Technical Skills'), and graphical icons—frequently cause "
        "text extraction routines to scramble reading orders, concatenate disparate columns, or completely discard entire sections. "
        "Furthermore, ATS keyword matching algorithms rarely possess deep semantic awareness; they fail to recognize that a developer with "
        "extensive <i>PostgreSQL</i> expertise is inherently qualified for a role specifying <i>Postgres</i>, or that extensive experience "
        "in <i>RabbitMQ</i> distributed queuing provides strong foundational competence for a role seeking <i>Apache Kafka</i>."
    )
    story.append(Paragraph(p8, styles['DocBody']))

    # 1.5 Role of Artificial Intelligence
    story.append(PageTracker('sec1_5', registry, '1.5 Role of Artificial Intelligence', 'section'))
    story.append(Paragraph("<b>1.5 Role of Artificial Intelligence</b>", styles['DocSectionTitle']))
    p9 = (
        "Recent breakthroughs in Natural Language Processing (NLP), semantic knowledge graphs, and Large Language Models (LLMs) "
        "offer powerful capabilities to overcome the brittle heuristics of traditional recruitment systems. By leveraging contextual "
        "word embeddings, transformer-based language representations, and domain-specific technical taxonomies, AI systems can understand "
        "conceptual relationships, evaluate hierarchical competencies, and interpret the semantic depth of project descriptions."
    )
    story.append(Paragraph(p9, styles['DocBody']))

    story.append(make_callout(
        "AI as a Decision Support Assistant",
        "It is fundamentally vital to emphasize that the AI methodologies employed in this system function strictly as an "
        "<b>assistance and decision-support mechanism</b> for candidate preparation. The software does not make automated employment decisions, "
        "nor can it guarantee corporate interview selection or hiring outcomes. Real-world hiring decisions depend on external non-deterministic "
        "variables including total applicant volume, recruiter preferences, live interview performance, cultural dynamics, and budgetary headcount.",
        styles,
        alert_type="warning"
    ))
    story.append(Spacer(1, 6))

    # 1.6 Need for the Proposed System
    story.append(PageTracker('sec1_6', registry, '1.6 Need for the Proposed System', 'section'))
    story.append(Paragraph("<b>1.6 Need for the Proposed System</b>", styles['DocSectionTitle']))
    p10 = (
        "Given the steep asymmetries of the modern recruitment pipeline, there exists an acute, compelling need for an intelligent, "
        "transparent, pre-application evaluation system that job seekers can utilize prior to formal submission. Candidates require a tool "
        "that can objectively evaluate their resume against a specific target Job Description, highlight critical missing technical keywords, "
        "diagnose ATS parsing and formatting hazards, quantify their alignment across weighted evaluation categories, and provide actionable, "
        "honest recommendations for improvement without fabricating false claims. The system described in this report directly fulfills this "
        "critical technological need."
    )
    story.append(Paragraph(p10, styles['DocBody']))
    story.append(PageBreak())
    return story

def build_chapter_2(styles, registry):
    story = []
    story.append(PageTracker('ch2', registry, '2. Problem Statement', 'chapter'))
    story.append(Paragraph("<b>2. PROBLEM STATEMENT</b>", styles['DocChapterTitle']))
    story.append(Spacer(1, 4))

    p1 = (
        "Job seekers face significant challenges when preparing and optimizing their resumes for specific job requisitions. "
        "The traditional process of tailoring a CV to a Job Description is manual, labor-intensive, error-prone, and lacking in objective feedback. "
        "Specifically, applicants encounter the following critical problems in the current recruitment landscape:"
    )
    story.append(Paragraph(p1, styles['DocBody']))

    problems = [
        "<b>High Manual Overhead & Inefficiency:</b> Line-by-line manual comparison between a lengthy multi-page CV and a detailed Job Description requires substantial time and cognitive effort, making it impractical for candidates applying to multiple requisitions.",
        "<b>Information Asymmetry & Match Ambiguity:</b> Candidates submit applications without knowing how closely their profile aligns with the algorithmic screening thresholds established by the employer's ATS.",
        "<b>Silent Omission of Critical Keywords:</b> Applicants frequently omit mandatory technical keywords, industry-standard acronyms, or specific tool names that they genuinely know, resulting in immediate automated rejection.",
        "<b>Obscured Work Experience & Impact:</b> Candidates often describe past engineering accomplishments in passive, generic terms without highlighting measurable business impact, quantified scale, or relevant technologies.",
        "<b>Failure to Distinguish Required vs Preferred Criteria:</b> Job seekers treat all JD bullet points equally, failing to recognize that missing a <i>mandatory</i> core requirement (e.g., Python backend development) is fatal, whereas missing a <i>nice-to-have</i> tool (e.g., GraphQL) is secondary.",
        "<b>Generic, Non-Actionable Resume Advice:</b> Existing online resume review tools provide broad, generic feedback (e.g., 'Use more action verbs') rather than specific, JD-aligned diagnostic guidance.",
        "<b>Keyword-Only False Positives & Negatives:</b> Naive keyword counting software either falsely rejects qualified candidates who use synonyms (e.g., AWS vs Amazon Web Services) or rewards unethical keyword-stuffing.",
        "<b>Unnoticed ATS Formatting Pitfalls:</b> Formatting traps such as multi-column layouts, tables, and unextractable header text silently destroy document parsability in corporate ATS systems without the applicant's knowledge."
    ]
    for prob in problems:
        story.append(Paragraph(f"• {prob}", styles['DocBullet']))
    story.append(Spacer(1, 6))

    # 2.1 Existing System
    story.append(PageTracker('sec2_1', registry, '2.1 Existing System', 'section'))
    story.append(Paragraph("<b>2.1 Existing System</b>", styles['DocSectionTitle']))
    p2 = (
        "The current approaches utilized by job seekers to evaluate and refine their resumes fall primarily into three categories:<br/>"
        "1. <b>Manual Self-Inspection:</b> Candidates manually read the job posting and attempt to visually cross-reference their resume bullets against stated requirements. This process is inherently subjective, prone to confirmation bias, and incapable of detecting ATS parsing issues.<br/>"
        "2. <b>Generic Online Resume Scanners:</b> First-generation automated tools perform basic string searching and keyword counting. These tools lack semantic comprehension, treat all keywords with identical importance regardless of context, and offer generic stylistic rules.<br/>"
        "3. <b>Unstructured Generative AI Prompts:</b> Applicants paste their resume and JD into general-purpose AI chat interfaces. While flexible, raw chat prompts lack structured scoring reproducibility, fail to audit document layout/ATS parsing rules, and frequently hallucinate false candidate qualifications."
    )
    story.append(Paragraph(p2, styles['DocBody']))

    # 2.2 Limitations of Existing System
    story.append(PageTracker('sec2_2', registry, '2.2 Limitations of Existing System', 'section'))
    story.append(Paragraph("<b>2.2 Limitations of Existing System</b>", styles['DocSectionTitle']))
    p3 = (
        "The systemic limitations and negative impacts of existing candidate screening and evaluation approaches are summarized "
        "in Table 2.1 below:"
    )
    story.append(Paragraph(p3, styles['DocBody']))
    story.append(Spacer(1, 4))

    # Table 2.1
    story.append(PageTracker('tab2_1', registry, 'Table 2.1: Limitations of Existing Systems', 'table'))
    story.append(Paragraph("<b>Table 2.1: Critical Limitations of Legacy CV Screening Systems</b>", styles['DocCaption']))
    
    table_data = [
        [
            Paragraph("<b>Limitation Dimension</b>", styles['DocTableHead']),
            Paragraph("<b>Operational Nature</b>", styles['DocTableHead']),
            Paragraph("<b>Impact on Candidate & Hiring Process</b>", styles['DocTableHead'])
        ],
        [
            Paragraph("<b>Manual Comparison</b>", styles['DocTableCellBold']),
            Paragraph("Human visual scan", styles['DocTableCell']),
            Paragraph("Extremely time-consuming, highly subjective, inconsistent across applications, and prone to severe cognitive fatigue.", styles['DocTableCell'])
        ],
        [
            Paragraph("<b>Keyword-Only Matching</b>", styles['DocTableCellBold']),
            Paragraph("Exact string equality / regex", styles['DocTableCell']),
            Paragraph("Fails to recognize canonical synonyms, acronyms, or sibling tools (e.g., RabbitMQ vs Kafka), causing false rejection of qualified talent.", styles['DocTableCell'])
        ],
        [
            Paragraph("<b>Generic Suggestions</b>", styles['DocTableCellBold']),
            Paragraph("Template rule heuristics", styles['DocTableCell']),
            Paragraph("Provides one-size-fits-all advice without evaluating the unique technical nuances of the specific target job requisition.", styles['DocTableCell'])
        ],
        [
            Paragraph("<b>No Requirement Priority</b>", styles['DocTableCellBold']),
            Paragraph("Flat list processing", styles['DocTableCell']),
            Paragraph("Treats mandatory core qualifications identically to optional preferences; critical gaps are frequently overlooked by the applicant.", styles['DocTableCell'])
        ],
        [
            Paragraph("<b>Opaque Scoring Model</b>", styles['DocTableCellBold']),
            Paragraph("Black-box percentage", styles['DocTableCell']),
            Paragraph("Candidate receives an arbitrary match number without explainable factor breakdown, category weights, or evidence citations.", styles['DocTableCell'])
        ],
        [
            Paragraph("<b>Zero ATS Layout Audit</b>", styles['DocTableCellBold']),
            Paragraph("Ignores visual structure", styles['DocTableCell']),
            Paragraph("Multi-column and tabular layout traps remain undetected, causing total text parsing failure in enterprise ATS workflows.", styles['DocTableCell'])
        ]
    ]

    t_lim = Table(table_data, colWidths=[USABLE_WIDTH * 0.25, USABLE_WIDTH * 0.22, USABLE_WIDTH * 0.53])
    t_lim.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), COLOR_PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.5, COLOR_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, COLOR_LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_lim)
    story.append(Spacer(1, 8))

    # 2.3 Proposed System
    story.append(PageTracker('sec2_3', registry, '2.3 Proposed System', 'section'))
    story.append(Paragraph("<b>2.3 Proposed System</b>", styles['DocSectionTitle']))
    p4 = (
        "The proposed <b>AI-Powered CV and Job Description Matcher</b> directly overcomes all the aforementioned limitations through an integrated, "
        "multi-tier software architecture. The system combines robust multi-format document text extraction (PDF, DOCX, TXT), automated 12-point "
        "ATS structural compliance checking, semantic skill taxonomy normalization, transparent 7-factor weighted scoring, probabilistic shortlist "
        "screening estimation, and explainable, evidence-backed resume improvement suggestions equipped with strict anti-hallucination guardrails."
    )
    story.append(Paragraph(p4, styles['DocBody']))
    story.append(PageBreak())
    return story

def build_chapter_3(styles, registry):
    story = []
    story.append(PageTracker('ch3', registry, '3. Objectives and Scope of the Project', 'chapter'))
    story.append(Paragraph("<b>3. OBJECTIVES AND SCOPE OF THE PROJECT</b>", styles['DocChapterTitle']))
    story.append(Spacer(1, 4))

    # 3.1 Objectives
    story.append(PageTracker('sec3_1', registry, '3.1 Objectives', 'section'))
    story.append(Paragraph("<b>3.1 Objectives</b>", styles['DocSectionTitle']))
    p1 = (
        "The overarching aim of this project is to research, design, develop, and validate an intelligent, transparent, and user-friendly "
        "decision-support web application for resume optimization and job screening assistance. The specific academic and technical "
        "objectives of the system are formulated as follows:"
    )
    story.append(Paragraph(p1, styles['DocBody']))

    objectives = [
        "<b>1. Automated Multi-Format Ingestion & Comparison:</b> Ingest candidate CVs across PDF, DOCX, and TXT formats alongside unstructured Job Descriptions, executing automated text extraction and structural normalization.",
        "<b>2. Structured Entity & Requirement Extraction:</b> Parse resumes and JDs into discrete semantic entities including contact metadata, professional summaries, technical skills, employment chronologies, educational degrees, and project portfolios.",
        "<b>3. Exact Keyword & Lexical Identification:</b> Identify direct, verbatim matches between candidate credentials and JD specifications.",
        "<b>4. Semantic & Canonical Synonym Matching:</b> Resolve acronyms and equivalent technical synonyms (e.g., AWS ↔ Amazon Web Services, K8s ↔ Kubernetes, Postgres ↔ PostgreSQL) without penalizing wording variations.",
        "<b>5. Sibling Technology & Partial Match Analysis:</b> Detect related sibling technologies (e.g., RabbitMQ in resume vs Kafka in JD) and articulate clear contextual explanations of partial alignment.",
        "<b>6. Missing Competency Detection:</b> Accurately isolate and catalog technical skills, libraries, frameworks, and methodologies present in the JD but absent from the candidate's resume.",
        "<b>7. Requirement Prioritization:</b> Distinguish between mandatory (Must-Have) core qualifications and optional (Nice-to-Have) preferred proficiencies, weighting their impact accordingly.",
        "<b>8. Experience & Seniority Alignment:</b> Evaluate candidate chronological work history, leadership tenure, and domain alignment against stated requisition seniority thresholds.",
        "<b>9. Multi-Factor Weighted Scoring:</b> Formulate and compute an overall match score (0–100%) across seven configurable evaluation pillars.",
        "<b>10. Probabilistic Shortlist Estimation:</b> Model an estimated ATS shortlist screening probability paired with explicit statistical disclosures.",
        "<b>11. 12-Point ATS Compliance Audit:</b> Systematically inspect document structural integrity, section headers, font extractability, and layout hazards to prevent parsing failure.",
        "<b>12. Critical Competency Gap Isolation:</b> Prioritize high-impact qualification deficits that pose immediate risks to candidate shortlisting.",
        "<b>13. Actionable & Non-Hallucinating Recommendations:</b> Synthesize quantified, high-impact bullet point rewrites utilizing metric placeholders without fabricating false candidate claims.",
        "<b>14. Ethical AI & Anti-Hallucination Guardrails:</b> Ensure the system never recommends adding unverified skills or claims that the candidate does not genuinely possess."
    ]
    for obj in objectives:
        story.append(Paragraph(f"• {obj}", styles['DocBullet']))
    story.append(Spacer(1, 6))

    # 3.2 Scope
    story.append(PageTracker('sec3_2', registry, '3.2 Scope', 'section'))
    story.append(Paragraph("<b>3.2 Scope</b>", styles['DocSectionTitle']))
    
    story.append(Paragraph("<b>3.2.1 In-Scope Capabilities:</b>", styles['DocSubsectionTitle']))
    in_scope = [
        "Asynchronous client-side file upload supporting PDF, DOCX, and raw TXT document formats up to 5MB.",
        "Direct text paste functionality for both candidate resume content and corporate job descriptions.",
        "Server-side binary stream parsing with layout hazard detection (multi-column text, tables, non-standard section headers).",
        "Deterministic heuristic taxonomy mapping combined with fallback Large Language Model (LLM) semantic reasoning.",
        "Granular side-by-side split screen inspection mapping JD requirements directly to extracted resume sentence evidence.",
        "Real-time dynamic adjustment of category scoring weights via interactive UI modal controls.",
        "Immediate ephemeral data deletion capability ensuring zero persistent storage of sensitive candidate PII upon user request.",
        "Client-side report exporting supporting JSON structured downloads and browser print-to-PDF generation."
    ]
    for item in in_scope:
        story.append(Paragraph(f"• {item}", styles['DocBullet']))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>3.2.2 Out-of-Scope Boundaries:</b>", styles['DocSubsectionTitle']))
    out_scope = [
        "<b>No Guarantee of Employment or Selection:</b> The system does not guarantee candidate interview selection or employment offers.",
        "<b>No Automated Application Bots:</b> The system does not execute automated form-filling or auto-apply scripts on third-party job boards.",
        "<b>No Replacement of Human Hiring Teams:</b> The software is designed exclusively as candidate-side assistance tooling, not an autonomous recruiter.",
        "<b>No Live Candidate Background Verification:</b> The system evaluates documented textual claims and cannot independently verify whether a candidate genuinely possesses a claimed degree or tenure.",
        "<b>No Autonomous Interviewing:</b> Conducting video or live technical interviews is outside the scope of this project."
    ]
    for item in out_scope:
        story.append(Paragraph(f"• {item}", styles['DocBullet']))
    story.append(Spacer(1, 6))

    # 3.3 Limitations
    story.append(PageTracker('sec3_3', registry, '3.3 Limitations of the Study', 'section'))
    story.append(Paragraph("<b>3.3 Limitations of the Study</b>", styles['DocSectionTitle']))
    p2 = (
        "The research and implementation boundaries of this project are subject to the following technical limitations:<br/>"
        "1. <b>Natural Language Ambiguity:</b> Resumes with heavily narrative, poetic, or unconventional phrasing may reduce the precision of automated entity extraction algorithms.<br/>"
        "2. <b>Document Layout Variance:</b> Scanned raster images of resumes lacking optical character recognition (OCR) text streams cannot be parsed without dedicated OCR preprocessing.<br/>"
        "3. <b>Proprietary ATS Divergence:</b> Commercial ATS vendors (Workday, Taleo, Greenhouse, Lever, iCIMS) employ distinct proprietary parsing algorithms; our 12-point audit simulates industry-standard consensus rules rather than a single vendor's private codebase.<br/>"
        "4. <b>LLM API Latency & Rate Limits:</b> When operating in cloud LLM provider mode, analysis duration is subject to external network latency and upstream API quotas (mitigated by the system's built-in offline hybrid semantic engine)."
    )
    story.append(Paragraph(p2, styles['DocBody']))
    story.append(PageBreak())
    return story

def build_chapter_4(styles, registry):
    story = []
    story.append(PageTracker('ch4', registry, '4. Advantages of Proposed System', 'chapter'))
    story.append(Paragraph("<b>4. ADVANTAGES OF PROPOSED SYSTEM</b>", styles['DocChapterTitle']))
    story.append(Spacer(1, 4))

    # 4.1 Key Advantages
    story.append(PageTracker('sec4_1', registry, '4.1 Key Advantages and Innovations', 'section'))
    story.append(Paragraph("<b>4.1 Key Advantages and Innovations</b>", styles['DocSectionTitle']))
    p1 = (
        "The proposed <b>AI-Powered CV and Job Description Matcher</b> introduces substantial functional, algorithmic, and practical "
        "advantages over traditional manual preparation and first-generation resume scanners:"
    )
    story.append(Paragraph(p1, styles['DocBody']))

    advs = [
        "<b>1. End-to-End Automated Comparison:</b> Eliminates tedious manual cross-referencing by analyzing multi-page resumes against detailed job requisitions within sub-second to low-second processing windows.",
        "<b>2. Semantic Comprehension Over Blind Counting:</b> Incorporates a comprehensive technical taxonomy graph and LLM embeddings, correctly rewarding canonical synonyms (e.g., Postgres ↔ PostgreSQL) and acknowledging related sibling architectures (e.g., RabbitMQ ↔ Kafka).",
        "<b>3. Precision Missing Keyword Isolation:</b> Explicitly identifies critical technical terms and tools missing from the CV, providing targeted guidance on exactly where and how to integrate them if the candidate possesses genuine experience.",
        "<b>4. Requirement Priority Weighting:</b> Evaluates mandatory Must-Have qualifications separately from optional Nice-to-Have preferences, preventing trivial omissions from heavily depressing overall candidate scores.",
        "<b>5. 12-Point ATS Structural Compliance Audit:</b> Audits document formatting integrity, section headers, and contact information extractability to ensure the candidate's CV parses flawlessly in enterprise ATS engines.",
        "<b>6. Transparent & Configurable 7-Factor Scoring:</b> Deconstructs overall alignment into seven distinct evaluation pillars (Skills, Experience, Responsibilities, Education, Projects, Soft Skills, ATS Quality), allowing real-time user customization of scoring weights.",
        "<b>7. Actionable, Non-Hallucinating Bullet Rewrites:</b> Synthesizes impactful before-and-after bullet rewrites using quantified metric placeholders (`[X% reduction]`, `[X,000+ users]`) without inventing fictitious numbers or experiences.",
        "<b>8. High-Performance, Privacy-First Architecture:</b> Operates with zero persistent PII retention, offering instant 1-click resume deletion and full offline heuristic matching capability."
    ]
    for adv in advs:
        story.append(Paragraph(f"• {adv}", styles['DocBullet']))
    story.append(Spacer(1, 8))

    # 4.2 Comparative Feature Analysis Matrix
    story.append(PageTracker('sec4_2', registry, '4.2 Comparative Feature Analysis Matrix', 'section'))
    story.append(Paragraph("<b>4.2 Comparative Feature Analysis Matrix</b>", styles['DocSectionTitle']))
    p2 = (
        "Table 4.1 illustrates a systematic feature-by-feature comparison contrasting the traditional manual approach, legacy keyword "
        "counting tools, and the proposed AI-powered system:"
    )
    story.append(Paragraph(p2, styles['DocBody']))
    story.append(Spacer(1, 4))

    # Table 4.1
    story.append(PageTracker('tab4_1', registry, 'Table 4.1: Feature Comparison Matrix', 'table'))
    story.append(Paragraph("<b>Table 4.1: Comprehensive Comparative Analysis Matrix (Traditional vs Proposed)</b>", styles['DocCaption']))

    comp_data = [
        [
            Paragraph("<b>Evaluation Feature</b>", styles['DocTableHead']),
            Paragraph("<b>Traditional Manual Approach</b>", styles['DocTableHead']),
            Paragraph("<b>Generic Keyword Scanners</b>", styles['DocTableHead']),
            Paragraph("<b>Proposed AI-Powered System</b>", styles['DocTableHead'])
        ],
        [
            Paragraph("<b>CV-JD Comparison</b>", styles['DocTableCellBold']),
            Paragraph("Manual line-by-line", styles['DocTableCell']),
            Paragraph("Keyword search only", styles['DocTableCell']),
            Paragraph("<b>Fully Automated Multi-Tier Analysis</b>", styles['DocTableCellBold'])
        ],
        [
            Paragraph("<b>Semantic Analysis</b>", styles['DocTableCellBold']),
            Paragraph("Subjective human intuition", styles['DocTableCell']),
            Paragraph("None (exact string match only)", styles['DocTableCell']),
            Paragraph("<b>Taxonomy Graph + LLM Embeddings</b>", styles['DocTableCellBold'])
        ],
        [
            Paragraph("<b>Synonym Resolution</b>", styles['DocTableCellBold']),
            Paragraph("Prone to human oversight", styles['DocTableCell']),
            Paragraph("Unsupported (false negatives)", styles['DocTableCell']),
            Paragraph("<b>Automatic Canonical Mapping</b>", styles['DocTableCellBold'])
        ],
        [
            Paragraph("<b>Sibling Tool Context</b>", styles['DocTableCellBold']),
            Paragraph("Varies with reviewer tech depth", styles['DocTableCell']),
            Paragraph("Flagged as completely missing", styles['DocTableCell']),
            Paragraph("<b>Identifies Partial Sibling Alignment</b>", styles['DocTableCellBold'])
        ],
        [
            Paragraph("<b>Missing Skills Audit</b>", styles['DocTableCellBold']),
            Paragraph("High cognitive effort", styles['DocTableCell']),
            Paragraph("Flat unclassified keyword list", styles['DocTableCell']),
            Paragraph("<b>Categorized (Required vs Preferred)</b>", styles['DocTableCellBold'])
        ],
        [
            Paragraph("<b>ATS Layout Audit</b>", styles['DocTableCellBold']),
            Paragraph("Cannot simulate ATS parsing", styles['DocTableCell']),
            Paragraph("Basic character counter", styles['DocTableCell']),
            Paragraph("<b>12-Point Structural Compliance Check</b>", styles['DocTableCellBold'])
        ],
        [
            Paragraph("<b>Scoring Transparency</b>", styles['DocTableCellBold']),
            Paragraph("No numerical score", styles['DocTableCell']),
            Paragraph("Opaque percentage density", styles['DocTableCell']),
            Paragraph("<b>7-Pillar Configurable Weighted Score</b>", styles['DocTableCellBold'])
        ],
        [
            Paragraph("<b>Actionable Rewrites</b>", styles['DocTableCellBold']),
            Paragraph("Unassisted manual drafting", styles['DocTableCell']),
            Paragraph("Generic template tips", styles['DocTableCell']),
            Paragraph("<b>Quantified Rewrites + Metric Placeholders</b>", styles['DocTableCellBold'])
        ],
        [
            Paragraph("<b>Privacy & Ephemerality</b>", styles['DocTableCellBold']),
            Paragraph("Local files on candidate PC", styles['DocTableCell']),
            Paragraph("Data retention for ad tracking", styles['DocTableCell']),
            Paragraph("<b>1-Click Immediate Purge / Zero Storage</b>", styles['DocTableCellBold'])
        ]
    ]

    t_comp = Table(comp_data, colWidths=[USABLE_WIDTH * 0.22, USABLE_WIDTH * 0.23, USABLE_WIDTH * 0.25, USABLE_WIDTH * 0.30])
    t_comp.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), COLOR_PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.5, COLOR_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, COLOR_LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 4.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4.5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_comp)
    story.append(PageBreak())
    return story
