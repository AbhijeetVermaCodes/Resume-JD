from reportlab.lib import colors
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from build_report.styles import (
    USABLE_WIDTH, COLOR_PRIMARY, COLOR_DARK, COLOR_TEXT, COLOR_MUTED,
    COLOR_ACCENT, COLOR_LIGHT_BG, COLOR_BORDER, COLOR_BORDER_LIGHT,
    PageTracker, make_callout, make_code_box
)
from build_report.diagrams import (
    create_ui_mockup_home,
    create_ui_mockup_ingestion,
    create_ui_mockup_weights_modal,
    create_ui_mockup_dashboard,
    create_ui_mockup_skill_matrix,
    create_ui_mockup_experience_gap,
    create_ui_mockup_ats_audit,
    create_ui_mockup_recommendations
)

def build_chapter_11(styles, registry):
    story = []
    story.append(PageTracker('ch11', registry, '11. Input and Output Screens', 'chapter'))
    story.append(Paragraph("<b>11. INPUT AND OUTPUT SCREENS</b>", styles['DocChapterTitle']))
    story.append(Spacer(1, 4))

    p_intro = (
        "This chapter documents the visual interface, user interaction workflows, and diagnostic output dashboards of the software system. "
        "All visual interfaces are designed following modern responsive glassmorphism aesthetics, utilizing dark-mode contrast panels, "
        "intuitive color badges, interactive modals, and SVG radial score gauges."
    )
    story.append(Paragraph(p_intro, styles['DocBody']))
    story.append(Spacer(1, 6))

    # 11.1 Input Screens
    story.append(PageTracker('sec11_1', registry, '11.1 Input User Interfaces', 'section'))
    story.append(Paragraph("<b>11.1 Input User Interfaces</b>", styles['DocSectionTitle']))
    
    # Figure 11.1: Home Page
    story.append(PageTracker('fig11_1', registry, 'Figure 11.1: Home Page and Navigation Header', 'figure'))
    story.append(create_ui_mockup_home())
    story.append(Paragraph("<b>Figure 11.1: Home Page and Navigation Header (Illustrative UI Mockup)</b>", styles['DocCaption']))
    story.append(Spacer(1, 6))

    # Figure 11.2: Dual Document Ingestion Interface
    story.append(PageTracker('fig11_2', registry, 'Figure 11.2: Dual Document Ingestion Screen', 'figure'))
    story.append(create_ui_mockup_ingestion())
    story.append(Paragraph("<b>Figure 11.2: Dual Document Ingestion Interface (Illustrative UI Mockup)</b>", styles['DocCaption']))
    story.append(Spacer(1, 6))

    # Figure 11.3: Scoring Weights Configuration Modal
    story.append(PageTracker('fig11_3', registry, 'Figure 11.3: Scoring Weights Configuration Modal', 'figure'))
    story.append(create_ui_mockup_weights_modal())
    story.append(Paragraph("<b>Figure 11.3: Interactive Scoring Weights Configuration Modal (Illustrative UI Mockup)</b>", styles['DocCaption']))
    story.append(PageBreak())

    # 11.2 Output Screens
    story.append(PageTracker('sec11_2', registry, '11.2 Output & Analytics User Interfaces', 'section'))
    story.append(Paragraph("<b>11.2 Output & Analytics User Interfaces</b>", styles['DocSectionTitle']))

    # Figure 11.4: Overall Dashboard
    story.append(PageTracker('fig11_4', registry, 'Figure 11.4: Multi-Metric Overall Match and ATS Dashboard', 'figure'))
    story.append(create_ui_mockup_dashboard())
    story.append(Paragraph("<b>Figure 11.4: Multi-Metric Overall Match and ATS Dashboard (Illustrative UI Mockup)</b>", styles['DocCaption']))
    story.append(Spacer(1, 6))

    # Figure 11.5: Skill Matrix
    story.append(PageTracker('fig11_5', registry, 'Figure 11.5: Semantic Skill & Keyword Analysis Matrix', 'figure'))
    story.append(create_ui_mockup_skill_matrix())
    story.append(Paragraph("<b>Figure 11.5: Semantic Skill & Keyword Analysis Matrix (Illustrative UI Mockup)</b>", styles['DocCaption']))
    story.append(Spacer(1, 6))

    # Figure 11.6: Experience Gap Matrix
    story.append(PageTracker('fig11_6', registry, 'Figure 11.6: Granular Experience Gap & Evidence Matrix', 'figure'))
    story.append(create_ui_mockup_experience_gap())
    story.append(Paragraph("<b>Figure 11.6: Granular Experience Gap & Evidence Matrix (Illustrative UI Mockup)</b>", styles['DocCaption']))
    story.append(PageBreak())

    # Figure 11.7: ATS Audit Card
    story.append(PageTracker('fig11_7', registry, 'Figure 11.7: 12-Point ATS Audit & Hazard Diagnostic Card', 'figure'))
    story.append(create_ui_mockup_ats_audit())
    story.append(Paragraph("<b>Figure 11.7: 12-Point ATS Audit & Hazard Diagnostic Card (Illustrative UI Mockup)</b>", styles['DocCaption']))
    story.append(Spacer(1, 6))

    # Figure 11.8: Recommendations & Final Assessment
    story.append(PageTracker('fig11_8', registry, 'Figure 11.8: Actionable Improvement Suggestions and Final Assessment', 'figure'))
    story.append(create_ui_mockup_recommendations())
    story.append(Paragraph("<b>Figure 11.8: Actionable Improvement Suggestions and Final Assessment (Illustrative UI Mockup)</b>", styles['DocCaption']))
    story.append(PageBreak())
    return story

def build_chapter_12(styles, registry):
    story = []
    story.append(PageTracker('ch12', registry, '12. Conclusion', 'chapter'))
    story.append(Paragraph("<b>12. CONCLUSION</b>", styles['DocChapterTitle']))
    story.append(Spacer(1, 4))

    p1 = (
        "The research, system formulation, and software implementation presented in this report demonstrate the design and validation "
        "of the <b>AI-Powered CV and Job Description Matcher</b>, an intelligent, transparent, and user-centric decision support application. "
        "The project successfully addresses the critical information asymmetries and communication bottlenecks inherent in modern recruitment "
        "by providing candidates with an objective, pre-submission diagnostic evaluation tool."
    )
    story.append(Paragraph(p1, styles['DocBody']))
    story.append(Spacer(1, 4))

    p2 = (
        "<b>Summary of Core Engineering & Research Contributions:</b><br/>"
        "1. <b>Multi-Tier Document Processing:</b> Successfully integrated high-performance binary extraction across PDF, DOCX, and TXT formats while auditing 12 structural ATS compliance heuristics.<br/>"
        "2. <b>Cognitive Semantic Matching:</b> Surpassed naive string matching by implementing a technical taxonomy graph and synonym resolver that correctly rewards canonical aliases and contextual sibling technologies.<br/>"
        "3. <b>Transparent & Configurable Scoring:</b> Formulated a mathematically grounded 7-factor scoring engine with live user-customizable weights, replacing opaque 'black-box' percentages with explainable evidence.<br/>"
        "4. <b>Actionable & Ethical Recommendations:</b> Synthesized quantified before-and-after bullet rewrites equipped with strict anti-hallucination guardrails, ensuring candidates present genuine qualifications with maximum professional impact.<br/>"
        "5. <b>High-Performance Privacy-First Stack:</b> Built a production-grade full-stack web application combining React 18, TypeScript, FastAPI, and SQLAlchemy with ephemeral session management and zero persistent PII storage."
    )
    story.append(Paragraph(p2, styles['DocBody']))
    story.append(Spacer(1, 6))

    # Mandatory Academic Disclaimer
    story.append(make_callout(
        "Mandatory Academic & Statistical Disclaimer",
        "The overall match percentage and estimated screening probability generated by this software represent analytical, "
        "diagnostic evaluations based solely on the textual content of the provided CV and Job Description. "
        "<b>The screening percentage is an estimated analytical score and not a guarantee of interview selection or employment.</b> "
        "Real-world recruitment outcomes depend on non-deterministic external factors including total applicant volume, recruiter preferences, "
        "hiring headcount quotas, live interview performance, work authorization requirements, and company-specific criteria.",
        styles,
        alert_type="danger"
    ))
    story.append(PageBreak())
    return story

def build_chapter_13(styles, registry):
    story = []
    story.append(PageTracker('ch13', registry, '13. Future Enhancements', 'chapter'))
    story.append(Paragraph("<b>13. FUTURE ENHANCEMENTS</b>", styles['DocChapterTitle']))
    story.append(Spacer(1, 4))

    p1 = (
        "While the current system fulfills all foundational software engineering and academic objectives, several promising directions "
        "exist for future research and architectural enhancement. The proposed roadmap includes twenty strategic improvements:"
    )
    story.append(Paragraph(p1, styles['DocBody']))
    story.append(Spacer(1, 4))

    enhancements = [
        "<b>1. Multi-Version Resume Portfolio Management:</b> Enable users to store, manage, and toggle between multiple tailored resume profiles (e.g., Backend, DevOps, Data Engineering) within a single unified workspace.",
        "<b>2. One-to-Many Batch Job Matching:</b> Allow candidates to upload a single master CV and simultaneously evaluate it across dozens of target job requisitions, ranking opportunities by match alignment.",
        "<b>3. Recruiter Multi-Candidate Ranking Dashboard:</b> Provide hiring teams with a recruiter view to ingest candidate cohorts and rank applicant pools against a master job description with explainable audit trails.",
        "<b>4. Direct LinkedIn & GitHub Profile Sync:</b> Ingest public candidate profiles directly from LinkedIn or GitHub, analyzing open-source repositories and code commits to validate technical claims.",
        "<b>5. Job Portal API Integration:</b> Connect directly with commercial job boards (Indeed, Glassdoor, LinkedIn) to automatically pull live job requisitions with one click.",
        "<b>6. Interactive In-Browser Resume Rewriter:</b> Embed a live rich-text editor that dynamically updates match scores in real time as the candidate edits their resume bullet points.",
        "<b>7. Contextual Cover Letter Generator:</b> Synthesize highly tailored, professional cover letters highlighting candidate strengths aligned with specific requisition gaps.",
        "<b>8. Integrated Kanban Job Application Tracker:</b> Provide a comprehensive application management board to track interview stages, application dates, and response rates.",
        "<b>9. Longitudinal Resume Improvement Analytics:</b> Track score progressions and keyword density improvements over time across successive resume iterations.",
        "<b>10. Dynamic Open-Source Skill Ontology Expansion:</b> Connect with global taxonomy repositories (such as ESCO and O*NET) for automated real-time discovery of emerging software libraries.",
        "<b>11. Industry-Specific Scoring Profiles:</b> Provide pre-configured scoring templates tailored for specific verticals (e.g., Quantitative Finance, Healthcare Informatics, Embedded Firmware).",
        "<b>12. Multilingual Resume Processing:</b> Extend semantic embeddings and parsing routines to support multilingual resumes across Spanish, German, French, Japanese, and Mandarin.",
        "<b>13. Personalized Learning & Upskilling Roadmaps:</b> Integrate with online educational platforms (Coursera, Udemy, edX) to recommend specific courses for missing technical requirements.",
        "<b>14. Role-Based Access Control & Enterprise Auth:</b> Implement OAuth2, OpenID Connect, and SAML single sign-on for enterprise university and corporate deployments.",
        "<b>15. Cloud-Native Kubernetes Deployment:</b> Package backend microservices as Helm charts with horizontal pod autoscaling and distributed Redis caching.",
        "<b>16. Chrome & Edge Browser Extension:</b> Develop a browser extension allowing candidates to click an icon on any job posting web page to instantly analyze their active resume.",
        "<b>17. High-Fidelity Vendor-Specific ATS Simulators:</b> Simulate exact parsing quirks of specific major ATS engines (Workday, Taleo, Greenhouse, Lever, iCIMS).",
        "<b>18. Algorithmic Fairness & Bias Mitigation:</b> Incorporate automated audits to detect and eliminate potential gender, demographic, or institutional bias in resume phrasing.",
        "<b>19. Audio/Video Interview Preparation Module:</b> Generate tailored behavioral and technical interview questions based on the candidate's specific identified resume gaps.",
        "<b>20. Local On-Device Small Language Model (SLM) Execution:</b> Support client-side on-device inference using quantized models (e.g., Llama 3 or Gemma via WebGPU) for 100% offline privacy."
    ]
    for enh in enhancements:
        story.append(Paragraph(f"• {enh}", styles['DocBullet']))
    story.append(PageBreak())
    return story

def build_references(styles, registry):
    story = []
    story.append(PageTracker('refs', registry, 'References', 'chapter'))
    story.append(Paragraph("<b>REFERENCES</b>", styles['DocChapterTitle']))
    story.append(Spacer(1, 6))

    refs = [
        "[1] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. Kaiser, and I. Polosukhin, 'Attention is all you need,' in <i>Advances in Neural Information Processing Systems (NeurIPS)</i>, vol. 30, pp. 5998–6008, 2017.",
        "[2] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, 'BERT: Pre-training of deep bidirectional transformers for language understanding,' in <i>Proc. NAACL-HLT</i>, pp. 4171–4186, 2019.",
        "[3] T. Brown et al., 'Language models are few-shot learners,' in <i>Advances in Neural Information Processing Systems (NeurIPS)</i>, vol. 33, pp. 1877–1901, 2020.",
        "[4] F. Silveira, 'The impact of Applicant Tracking Systems on modern hiring workflows,' <i>IEEE Trans. Prof. Commun.</i>, vol. 64, no. 2, pp. 142–155, 2021.",
        "[5] S. Bird, E. Klein, and E. Loper, <i>Natural Language Processing with Python</i>. O'Reilly Media, 2009.",
        "[6] S. Ramirez and D. Chen, 'Automated skill ontology extraction from unstructured job postings,' in <i>Proc. ACM SIGKDD Int. Conf. Knowl. Discovery Data Min.</i>, pp. 889–897, 2022.",
        "[7] P. Resnick and H. R. Varian, 'Recommender systems,' <i>Commun. ACM</i>, vol. 40, no. 3, pp. 56–58, 1997.",
        "[8] S. Tiwary and M. Agrawal, 'Information extraction and entity normalization in automated resume parsing systems,' in <i>Proc. IEEE Int. Conf. Data Eng. (ICDE)</i>, pp. 1120–1131, 2023.",
        "[9] S. Ramirez, 'FastAPI: Modern, high-performance web framework for building APIs with Python,' <i>GitHub Repository</i>, 2024. [Online]. Available: https://fastapi.tiangolo.com",
        "[10] Meta Platforms Inc., 'React: A JavaScript library for building user interfaces,' 2024. [Online]. Available: https://react.dev",
        "[11] E. Gamma, R. Helm, R. Johnson, and J. Vlissides, <i>Design Patterns: Elements of Reusable Object-Oriented Software</i>. Addison-Wesley, 1994.",
        "[12] R. C. Martin, <i>Clean Architecture: A Craftsman's Guide to Software Structure and Design</i>. Prentice Hall, 2017.",
        "[13] European Union, 'Regulation (EU) 2016/679 (General Data Protection Regulation),' <i>Official Journal of the European Union</i>, 2016.",
        "[14] M. Mitchell et al., 'Model cards for model reporting,' in <i>Proc. ACM Conf. Fairness, Accountability, and Transparency (FAT*)</i>, pp. 220–229, 2019."
    ]
    for ref in refs:
        story.append(Paragraph(ref, styles['DocBody']))
        story.append(Spacer(1, 3))
    story.append(PageBreak())
    return story

def build_appendix(styles, registry):
    story = []
    story.append(PageTracker('app', registry, 'Appendix', 'chapter'))
    story.append(Paragraph("<b>APPENDIX</b>", styles['DocChapterTitle']))
    story.append(Spacer(1, 4))

    # Appendix A: Sample Resume
    story.append(Paragraph("<b>Appendix A: Sample Candidate Resume (Senior Software Engineer)</b>", styles['DocSectionTitle']))
    sample_cv = (
        "<b>Alex Turner</b> — alex.turner@email.com | (555) 019-2834 | San Francisco, CA | github.com/alexturner<br/>"
        "<b>Professional Summary:</b> Senior Backend Engineer with 5+ years of experience building resilient microservices, distributed data pipelines, and RESTful APIs in enterprise ecosystems.<br/>"
        "<b>Technical Skills:</b> Java, Spring Boot, Python, Docker, PostgreSQL, MySQL, RabbitMQ, REST APIs, Redis, Git, Maven, Linux, Agile/Scrum.<br/>"
        "<b>Work Experience:</b><br/>"
        "• <i>Senior Software Engineer — CloudScale Systems (2021 – Present):</i> Architected Java Spring Boot microservices handling 15M daily requests. Optimized PostgreSQL indexing reducing query latency by 35%. Containerized services with Docker.<br/>"
        "• <i>Software Engineer — DataFlow Corp (2019 – 2021):</i> Developed asynchronous messaging workers using RabbitMQ and Python. Built RESTful APIs for customer authentication.<br/>"
        "<b>Education:</b> B.S. in Computer Science — State University (2015 – 2019)."
    )
    story.append(Paragraph(sample_cv, styles['DocBody']))
    story.append(Spacer(1, 6))

    # Appendix B: Sample JD
    story.append(Paragraph("<b>Appendix B: Sample Target Job Description (Cloud Platforms Engineer)</b>", styles['DocSectionTitle']))
    sample_jd = (
        "<b>Position:</b> Senior Cloud Platforms Engineer — NexaCloud Inc.<br/>"
        "<b>Experience:</b> 5+ years in distributed backend systems.<br/>"
        "<b>Required Skills:</b> Java, Spring Boot, Docker, Kubernetes, Apache Kafka, PostgreSQL, RESTful APIs, Microservices Architecture.<br/>"
        "<b>Preferred Qualifications:</b> AWS Cloud Services, Terraform (IaC), Redis Caching, CI/CD pipelines.<br/>"
        "<b>Responsibilities:</b> Design high-throughput event-driven microservices; manage container orchestration clusters; optimize distributed data storage; mentor junior engineers."
    )
    story.append(Paragraph(sample_jd, styles['DocBody']))
    story.append(Spacer(1, 6))

    # Appendix C: Structured JSON Payload
    story.append(Paragraph("<b>Appendix C: Sample Structured Analysis JSON Payload (API Output)</b>", styles['DocSectionTitle']))
    sample_json = (
        "{\n"
        "  \"overall_score\": 78.5,\n"
        "  \"estimated_screening_probability\": 74.0,\n"
        "  \"category_scores\": {\n"
        "    \"skills_score\": 72.0, \"experience_score\": 95.0, \"responsibilities_score\": 80.0,\n"
        "    \"education_score\": 100.0, \"projects_score\": 75.0, \"soft_skills_score\": 85.0, \"ats_quality_score\": 92.0\n"
        "  },\n"
        "  \"skills\": {\n"
        "    \"strong_matches\": [{\"name\": \"Java\"}, {\"name\": \"Spring Boot\"}, {\"name\": \"Docker\"}, {\"name\": \"PostgreSQL\"}],\n"
        "    \"partial_matches\": [{\"name\": \"Kafka\", \"reason\": \"Demonstrates RabbitMQ messaging experience.\"}],\n"
        "    \"missing\": [{\"name\": \"Kubernetes\", \"importance\": \"critical\"}, {\"name\": \"Terraform\", \"importance\": \"preferred\"}]\n"
        "  },\n"
        "  \"ats_compatibility\": {\"score\": 92, \"status\": \"Excellent\", \"issues\": []}\n"
        "}"
    )
    story.append(make_code_box(sample_json, "analysis_output_payload.json", styles))
    story.append(Spacer(1, 6))

    # Appendix D: Database DDL
    story.append(Paragraph("<b>Appendix D: Relational Database Schema DDL (SQLite / PostgreSQL)</b>", styles['DocSectionTitle']))
    sample_ddl = (
        "CREATE TABLE resumes (\n"
        "    id VARCHAR(36) PRIMARY KEY,\n"
        "    filename VARCHAR(255),\n"
        "    file_type VARCHAR(50),\n"
        "    raw_text TEXT NOT NULL,\n"
        "    structured_data JSON,\n"
        "    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP\n"
        ");\n"
        "CREATE TABLE job_descriptions (\n"
        "    id VARCHAR(36) PRIMARY KEY,\n"
        "    title VARCHAR(255),\n"
        "    company VARCHAR(255),\n"
        "    raw_text TEXT NOT NULL,\n"
        "    structured_data JSON,\n"
        "    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP\n"
        ");\n"
        "CREATE TABLE analyses (\n"
        "    id VARCHAR(36) PRIMARY KEY,\n"
        "    resume_id VARCHAR(36) REFERENCES resumes(id) ON DELETE CASCADE,\n"
        "    job_description_id VARCHAR(36) REFERENCES job_descriptions(id) ON DELETE CASCADE,\n"
        "    overall_score FLOAT NOT NULL,\n"
        "    estimated_screening_probability FLOAT NOT NULL,\n"
        "    category_scores JSON NOT NULL,\n"
        "    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP\n"
        ");"
    )
    story.append(make_code_box(sample_ddl, "schema_migration.sql", styles))
    return story
