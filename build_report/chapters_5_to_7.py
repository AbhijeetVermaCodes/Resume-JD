from reportlab.lib import colors
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from build_report.styles import (
    USABLE_WIDTH, COLOR_PRIMARY, COLOR_DARK, COLOR_TEXT, COLOR_MUTED,
    COLOR_ACCENT, COLOR_LIGHT_BG, COLOR_BORDER, COLOR_BORDER_LIGHT,
    PageTracker, make_callout
)
from build_report.diagrams import (
    create_system_architecture_diagram,
    create_flowchart_diagram,
    create_dfd_level0_diagram,
    create_dfd_level1_diagram,
    create_erd_diagram
)

def build_chapter_5(styles, registry):
    story = []
    story.append(PageTracker('ch5', registry, '5. Requirement Analysis and Feasibility Study', 'chapter'))
    story.append(Paragraph("<b>5. REQUIREMENT ANALYSIS AND FEASIBILITY STUDY</b>", styles['DocChapterTitle']))
    story.append(Spacer(1, 4))

    # 5.1 Functional Requirements
    story.append(PageTracker('sec5_1', registry, '5.1 Functional Requirements Specification', 'section'))
    story.append(Paragraph("<b>5.1 Functional Requirements Specification</b>", styles['DocSectionTitle']))
    p1 = (
        "The functional requirements delineate the core capabilities, operations, data transformations, and behavioral responses "
        "that the software system must exhibit. The requirements are formally enumerated as follows:"
    )
    story.append(Paragraph(p1, styles['DocBody']))

    frs = [
        ("FR-01: Multi-Format Resume Upload", "The system shall allow users to upload resume files in PDF, DOCX, and TXT formats with a maximum file size threshold of 5.0 Megabytes (MB)."),
        ("FR-02: Job Description Ingestion", "The system shall provide capabilities for users to either upload a JD document (PDF/DOCX/TXT) or paste raw unstructured job requisition text directly via an interactive text editor."),
        ("FR-03: Document Format & MIME Validation", "The system shall validate document magic bytes, file extensions, and file payload sizes prior to processing, returning descriptive error messages upon detecting corrupt or unsupported formats."),
        ("FR-04: Robust Text Stream Extraction", "The system shall utilize dedicated document extraction libraries (pdfplumber, pypdf, python-docx) to extract raw textual streams while handling character encoding variants (UTF-8, Latin-1)."),
        ("FR-05: Structural Resume Parsing & Sectioning", "The system shall parse extracted resume text into discrete semantic entities, including candidate contact metadata, professional summaries, technical skill arrays, employment histories, educational credentials, and projects."),
        ("FR-06: 12-Point ATS Hazard Auditing", "The system shall inspect the raw document structure for ATS parsing traps, such as multi-column text ordering, non-standard section headers, embedded graphic text, and missing contact information."),
        ("FR-07: Structured Job Requirement Extraction", "The system shall parse job descriptions into structured categories, classifying skills into programming languages, frameworks, cloud platforms, databases, developer tools, and domain proficiencies."),
        ("FR-08: Mandatory vs Preferred Classification", "The system shall differentiate between mandatory (Must-Have) and optional (Nice-to-Have) requirements using linguistic modal analysis (e.g., 'must have', 'required', 'preferred', 'plus')."),
        ("FR-09: Exact & Canonical Synonym Skill Matching", "The system shall match extracted resume skills against JD requirements, resolving canonical synonyms (e.g., K8s ↔ Kubernetes, AWS ↔ Amazon Web Services, Postgres ↔ PostgreSQL)."),
        ("FR-10: Sibling Technology Alignment Detection", "The system shall evaluate related sibling technologies via taxonomy graphs (e.g., RabbitMQ in resume vs Kafka in JD) and assign partial alignment with explicit explanations."),
        ("FR-11: Precision Missing Competency Cataloging", "The system shall isolate all required and preferred JD skills that are completely absent from the candidate's resume."),
        ("FR-12: Experience & Seniority Gap Evaluation", "The system shall compare candidate chronological work tenure and leadership depth against the minimum years of experience specified in the job requisition."),
        ("FR-13: Transparent 7-Factor Weighted Scoring", "The system shall compute an overall match score (0–100%) by executing a deterministic, weighted mathematical aggregation across seven configurable evaluation pillars."),
        ("FR-14: Probabilistic Shortlist Screening Modeling", "The system shall calculate an estimated initial shortlist screening probability (0–100%) paired with prominent statistical disclosure disclaimers."),
        ("FR-15: Actionable Non-Hallucinating Bullet Rewrites", "The system shall synthesize quantified resume bullet rewrites utilizing metric placeholders (`[X% improvement]`, `[X,000+ users]`) without fabricating false employer claims."),
        ("FR-16: Interactive Side-by-Side Diagnostic Dashboard", "The system shall render an interactive split-screen matrix mapping each JD requirement directly to extracted resume sentence evidence and match badges."),
        ("FR-17: Instant Ephemeral Resume Data Purge", "The system shall provide a 1-click 'Delete Resume' function that immediately purges candidate text and extracted entities from database and session storage.")
    ]
    for code, desc in frs:
        story.append(Paragraph(f"• <b>{code}:</b> {desc}", styles['DocBullet']))
    story.append(Spacer(1, 6))

    # 5.2 Non-Functional Requirements
    story.append(PageTracker('sec5_2', registry, '5.2 Non-Functional Requirements Specification', 'section'))
    story.append(Paragraph("<b>5.2 Non-Functional Requirements Specification</b>", styles['DocSectionTitle']))
    p2 = (
        "Non-functional requirements specify the operational criteria, performance constraints, and quality attributes governing the software system:"
    )
    story.append(Paragraph(p2, styles['DocBody']))

    nfrs = [
        ("NFR-01: Performance & Response Latency", "Document text extraction and deterministic heuristic matching shall complete in under 500 milliseconds. End-to-end multi-provider LLM analysis shall execute within 2.5 to 5.0 seconds under standard broadband network conditions."),
        ("NFR-02: System Scalability", "The stateless FastAPI application layer shall support horizontal scaling across multiple containerized worker instances behind an asynchronous ASGI server (Uvicorn)."),
        ("NFR-03: Security & Input Sanitization", "All uploaded files and textual payloads shall be strictly sanitized to prevent SQL injection, cross-site scripting (XSS), server-side request forgery (SSRF), and zip bomb decompression exploits."),
        ("NFR-04: Data Privacy & Ephemerality (GDPR/CCPA)", "The system shall maintain a zero-persistent storage default for candidate Personally Identifiable Information (PII), offering full session ephemerality and immediate database purging upon user command."),
        ("NFR-05: System Reliability & Fault Tolerance", "The system shall implement graceful multi-tier fallback architecture: if external LLM APIs fail or experience rate limits, the built-in offline hybrid semantic taxonomy engine shall complete the evaluation seamlessly."),
        ("NFR-06: High Availability", "The backend service shall maintain 99.9% uptime with automated health-check endpoints (`/health`) for container orchestration monitoring."),
        ("NFR-07: Maintainability & Code Quality", "The codebase shall adhere to strict modular software architecture, PEP 8 Python style guidelines, TypeScript strict type checking, and maintain over 90% automated test coverage."),
        ("NFR-08: Usability & User Experience", "The React frontend shall present intuitive drag-and-drop file upload zones, responsive SVG score gauges, accessible color-coded badges, and clear typographical contrast meeting WCAG 2.1 AA standards."),
        ("NFR-09: Cross-Platform Portability", "The client application shall execute flawlessly across all modern desktop browsers (Chrome, Firefox, Safari, Edge). The backend shall deploy consistently across Linux, macOS, and Windows runtime environments."),
        ("NFR-10: Algorithmic Explainability", "Every score, badge, and recommendation generated by the engine shall include human-interpretable mathematical weightings and direct textual evidence references."),
        ("NFR-11: Anti-Hallucination Guardrails", "The recommendation engine shall embed strict cautionary warnings instructing candidates never to incorporate skills or metric claims that they did not genuinely perform.")
    ]
    for code, desc in nfrs:
        story.append(Paragraph(f"• <b>{code}:</b> {desc}", styles['DocBullet']))
    story.append(Spacer(1, 6))

    # 5.3 User Requirements
    story.append(PageTracker('sec5_3', registry, '5.3 User Requirements & Persona Workflows', 'section'))
    story.append(Paragraph("<b>5.3 User Requirements & Persona Workflows</b>", styles['DocSectionTitle']))
    p3 = (
        "The primary user persona is the <b>Active Job Seeker / Software Engineer</b> seeking to optimize their application materials "
        "for competitive technical roles. The user requires an intuitive, friction-free workflow that allows them to upload their current CV, "
        "paste a target job requisition, receive instantaneous multi-dimensional scoring feedback, view exact keyword gaps, inspect ATS "
        "formatting compliance, and review actionable bullet rewrites without navigating complex configuration menus."
    )
    story.append(Paragraph(p3, styles['DocBody']))

    # 5.4 System Requirements
    story.append(PageTracker('sec5_4', registry, '5.4 System & Operational Requirements', 'section'))
    story.append(Paragraph("<b>5.4 System & Operational Requirements</b>", styles['DocSectionTitle']))
    p4 = (
        "The system requires an asynchronous client-server architecture capable of processing binary document streams, executing "
        "multithreaded NLP tokenization routines, managing relational metadata with JSON schema extensions, and communicating over secure "
        "HTTPS/WSS protocols."
    )
    story.append(Paragraph(p4, styles['DocBody']))

    # 5.5 Feasibility Study
    story.append(PageTracker('sec5_5', registry, '5.5 Feasibility Study', 'section'))
    story.append(Paragraph("<b>5.5 Feasibility Study</b>", styles['DocSectionTitle']))
    p5 = (
        "A comprehensive four-dimensional feasibility study was conducted to evaluate the viability of the proposed system:"
    )
    story.append(Paragraph(p5, styles['DocBody']))

    story.append(Paragraph("<b>1. Technical Feasibility:</b>", styles['DocSubsectionTitle']))
    p_tf = (
        "The technical feasibility is validated through the selection of mature, production-proven open-source technologies: "
        "Python 3.11, FastAPI, Pydantic v2, React 18, TypeScript, and SQLAlchemy. The integration of modern document parsing libraries "
        "(pdfplumber, python-docx) combined with a deterministic offline taxonomy engine and cloud LLM APIs (Gemini 2.5 Flash / GPT-4o-mini) "
        "ensures exceptional analytical accuracy, low compute overhead, and high execution speed."
    )
    story.append(Paragraph(p_tf, styles['DocBody']))

    story.append(Paragraph("<b>2. Economic Feasibility:</b>", styles['DocSubsectionTitle']))
    p_ef = (
        "<i>(Conceptual Cost Model & Architectural Assumptions):</i> Development and operational costs are exceptionally minimal due to "
        "the extensive utilization of open-source libraries (MIT/Apache 2.0 licenses). Cloud hosting overhead is constrained to basic compute "
        "instances (e.g., standard container VPS or serverless execution). By architecting an intelligent local taxonomy and synonym graph, "
        "the application minimizes external LLM API token consumption by up to 80%, ensuring sustainable long-term economic viability."
    )
    story.append(Paragraph(p_ef, styles['DocBody']))

    story.append(Paragraph("<b>3. Operational Feasibility:</b>", styles['DocSubsectionTitle']))
    p_of = (
        "The software requires zero client-side installation, operating universally within standard web browsers. The user interface "
        "features 1-click demo loading, drag-and-drop file ingestion, clear color-coded indicators, and real-time tooltips, ensuring that "
        "users of varying technical literacy can operate the system effortlessly."
    )
    story.append(Paragraph(p_of, styles['DocBody']))

    story.append(Paragraph("<b>4. Legal, Ethical & Privacy Feasibility:</b>", styles['DocSubsectionTitle']))
    p_lf = (
        "The system complies with global data privacy frameworks (GDPR, CCPA) by implementing ephemeral session processing, zero unencrypted "
        "PII caching, and 1-click candidate data purging. Ethically, the system incorporates strict anti-hallucination guardrails and explicit "
        "disclaimers, ensuring candidates are never misled into believing automated screening scores guarantee corporate employment."
    )
    story.append(Paragraph(p_lf, styles['DocBody']))
    story.append(PageBreak())
    return story

def build_chapter_6(styles, registry):
    story = []
    story.append(PageTracker('ch6', registry, '6. Software and Hardware Requirements', 'chapter'))
    story.append(Paragraph("<b>6. SOFTWARE AND HARDWARE REQUIREMENTS</b>", styles['DocChapterTitle']))
    story.append(Spacer(1, 4))

    # 6.1 Software Requirements
    story.append(PageTracker('sec6_1', registry, '6.1 Software Requirements Matrix', 'section'))
    story.append(Paragraph("<b>6.1 Software Requirements Matrix</b>", styles['DocSectionTitle']))
    p1 = (
        "The software architecture, development toolchain, runtime dependencies, and framework specifications utilized across the system "
        "are detailed in Table 6.1:"
    )
    story.append(Paragraph(p1, styles['DocBody']))
    story.append(Spacer(1, 4))

    # Table 6.1
    story.append(PageTracker('tab6_1', registry, 'Table 6.1: Software Requirements Toolchain', 'table'))
    story.append(Paragraph("<b>Table 6.1: Complete Software Environment & Development Toolchain</b>", styles['DocCaption']))

    sw_data = [
        [
            Paragraph("<b>Architecture Layer</b>", styles['DocTableHead']),
            Paragraph("<b>Technology / Framework</b>", styles['DocTableHead']),
            Paragraph("<b>Version / Specification</b>", styles['DocTableHead']),
            Paragraph("<b>Operational Role & Purpose</b>", styles['DocTableHead'])
        ],
        [
            Paragraph("<b>Frontend Framework</b>", styles['DocTableCellBold']),
            Paragraph("React + TypeScript", styles['DocTableCell']),
            Paragraph("React 18.3.1 / TS 5.4.5", styles['DocTableCell']),
            Paragraph("Component-driven single page application (SPA) with strong type safety.", styles['DocTableCell'])
        ],
        [
            Paragraph("<b>Build Tool & Bundler</b>", styles['DocTableCellBold']),
            Paragraph("Vite", styles['DocTableCell']),
            Paragraph("Vite 5.3.1", styles['DocTableCell']),
            Paragraph("Ultra-fast Hot Module Replacement (HMR) and optimized rollup production bundling.", styles['DocTableCell'])
        ],
        [
            Paragraph("<b>UI Styling & Icons</b>", styles['DocTableCellBold']),
            Paragraph("Tailwind CSS + Lucide", styles['DocTableCell']),
            Paragraph("Tailwind 3.4.4 / Lucide 0.395", styles['DocTableCell']),
            Paragraph("Utility-first responsive design tokens, glassmorphism panels, and modern SVG icons.", styles['DocTableCell'])
        ],
        [
            Paragraph("<b>Backend Engine</b>", styles['DocTableCellBold']),
            Paragraph("Python + FastAPI", styles['DocTableCell']),
            Paragraph("Python 3.11 / FastAPI 0.141", styles['DocTableCell']),
            Paragraph("High-performance asynchronous REST API framework with native OpenAPI/Swagger docs.", styles['DocTableCell'])
        ],
        [
            Paragraph("<b>Data Validation</b>", styles['DocTableCellBold']),
            Paragraph("Pydantic v2", styles['DocTableCell']),
            Paragraph("Pydantic 2.13.4", styles['DocTableCell']),
            Paragraph("Strict schema enforcement, type coercion, and JSON schema serialization.", styles['DocTableCell'])
        ],
        [
            Paragraph("<b>Document Processing</b>", styles['DocTableCellBold']),
            Paragraph("pdfplumber, pypdf, python-docx", styles['DocTableCell']),
            Paragraph("pdfplumber 0.11 / pypdf 6.16", styles['DocTableCell']),
            Paragraph("Binary PDF/DOCX stream extraction, text flow analysis, and ATS layout hazard detection.", styles['DocTableCell'])
        ],
        [
            Paragraph("<b>AI & Semantic Layer</b>", styles['DocTableCellBold']),
            Paragraph("Hybrid Semantic Graph + Multi-LLM", styles['DocTableCell']),
            Paragraph("Gemini 2.5 Flash / GPT-4o-mini", styles['DocTableCell']),
            Paragraph("Offline taxonomy graph + cloud LLM provider abstraction for contextual matching.", styles['DocTableCell'])
        ],
        [
            Paragraph("<b>Database & ORM</b>", styles['DocTableCellBold']),
            Paragraph("SQLAlchemy + SQLite / Postgres", styles['DocTableCell']),
            Paragraph("SQLAlchemy 2.0.52", styles['DocTableCell']),
            Paragraph("Object-Relational Mapping with native JSON data type column support.", styles['DocTableCell'])
        ],
        [
            Paragraph("<b>Testing Framework</b>", styles['DocTableCellBold']),
            Paragraph("pytest + anyio", styles['DocTableCell']),
            Paragraph("pytest 9.1.1", styles['DocTableCell']),
            Paragraph("Automated unit and integration test suite across parsers, scoring, and APIs.", styles['DocTableCell'])
        ]
    ]

    t_sw = Table(sw_data, colWidths=[USABLE_WIDTH * 0.22, USABLE_WIDTH * 0.24, USABLE_WIDTH * 0.22, USABLE_WIDTH * 0.32])
    t_sw.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), COLOR_PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.5, COLOR_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, COLOR_LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 4.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4.5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_sw)
    story.append(Spacer(1, 8))

    # 6.2 Hardware Requirements
    story.append(PageTracker('sec6_2', registry, '6.2 Hardware Requirements Specification', 'section'))
    story.append(Paragraph("<b>6.2 Hardware Requirements Specification</b>", styles['DocSectionTitle']))
    p2 = (
        "The minimum and recommended hardware specifications for development, testing, and production deployment are listed in Table 6.2:"
    )
    story.append(Paragraph(p2, styles['DocBody']))
    story.append(Spacer(1, 4))

    # Table 6.2
    story.append(PageTracker('tab6_2', registry, 'Table 6.2: Hardware Specifications', 'table'))
    story.append(Paragraph("<b>Table 6.2: Minimum and Recommended Hardware Specifications</b>", styles['DocCaption']))

    hw_data = [
        [
            Paragraph("<b>Hardware Resource</b>", styles['DocTableHead']),
            Paragraph("<b>Minimum Specification (Client / Dev)</b>", styles['DocTableHead']),
            Paragraph("<b>Recommended Specification (Server / Deployment)</b>", styles['DocTableHead'])
        ],
        [
            Paragraph("<b>Processor (CPU)</b>", styles['DocTableCellBold']),
            Paragraph("Dual-Core 2.0 GHz (x86_64 or Apple Silicon)", styles['DocTableCell']),
            Paragraph("Quad-Core 3.0 GHz+ (Intel Xeon / AMD EPYC / Apple M-Series)", styles['DocTableCell'])
        ],
        [
            Paragraph("<b>System Memory (RAM)</b>", styles['DocTableCellBold']),
            Paragraph("4 GB DDR4 / Unified Memory", styles['DocTableCell']),
            Paragraph("16 GB+ DDR4/DDR5 for high-concurrency request parsing", styles['DocTableCell'])
        ],
        [
            Paragraph("<b>Storage Space</b>", styles['DocTableCellBold']),
            Paragraph("2 GB available SSD storage", styles['DocTableCell']),
            Paragraph("20 GB+ NVMe SSD storage for OS, runtime logs, and cache", styles['DocTableCell'])
        ],
        [
            Paragraph("<b>Network Connectivity</b>", styles['DocTableCellBold']),
            Paragraph("Standard Broadband (1 Mbps+)", styles['DocTableCell']),
            Paragraph("High-Speed Dedicated Fiber (100 Mbps+ low-latency connection)", styles['DocTableCell'])
        ],
        [
            Paragraph("<b>Display / Resolution</b>", styles['DocTableCellBold']),
            Paragraph("1366 x 768 standard display", styles['DocTableCell']),
            Paragraph("1920 x 1080 (Full HD) or higher for optimal split-view inspection", styles['DocTableCell'])
        ]
    ]

    t_hw = Table(hw_data, colWidths=[USABLE_WIDTH * 0.25, USABLE_WIDTH * 0.37, USABLE_WIDTH * 0.38])
    t_hw.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), COLOR_PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.5, COLOR_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, COLOR_LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_hw)
    story.append(PageBreak())
    return story

def build_chapter_7(styles, registry):
    story = []
    story.append(PageTracker('ch7', registry, '7. System Design and Database Design', 'chapter'))
    story.append(Paragraph("<b>7. SYSTEM DESIGN AND DATABASE DESIGN</b>", styles['DocChapterTitle']))
    story.append(Spacer(1, 4))

    # 7.1 System Architecture
    story.append(PageTracker('sec7_1', registry, '7.1 System Architecture', 'section'))
    story.append(Paragraph("<b>7.1 System Architecture</b>", styles['DocSectionTitle']))
    p1 = (
        "The system is engineered following a modular, multi-tier architectural pattern separating presentation, API routing, "
        "document processing, semantic intelligence, multi-factor scoring, and data persistence. Figure 7.1 illustrates the "
        "comprehensive multi-tier architecture of the system:"
    )
    story.append(Paragraph(p1, styles['DocBody']))
    story.append(Spacer(1, 4))

    # Figure 7.1
    story.append(PageTracker('fig7_1', registry, 'Figure 7.1: Multi-Tier System Architecture', 'figure'))
    story.append(create_system_architecture_diagram())
    story.append(Paragraph("<b>Figure 7.1: Multi-Tier System Architecture Diagram</b>", styles['DocCaption']))
    story.append(Spacer(1, 6))

    p2 = (
        "<b>Architectural Layer Breakdown:</b><br/>"
        "1. <b>Presentation Tier:</b> Built with React 18, TypeScript, and Vite, featuring componentized UI modules for dual document upload, "
        "dynamic weights adjustment modals, SVG radial score gauges, and split-screen side-by-side verification.<br/>"
        "2. <b>Application Gateway Tier:</b> Implemented in FastAPI, providing asynchronous REST endpoints with Pydantic schema validation, "
        "CORS middleware, and exception handling.<br/>"
        "3. <b>Document Processing Layer:</b> Utilizes `pdfplumber`, `pypdf`, and `python-docx` to extract text and audit ATS formatting traps.<br/>"
        "4. <b>Semantic AI & Taxonomy Layer:</b> Combines a deterministic technical taxonomy graph with multi-provider LLM abstractions (Gemini/OpenAI).<br/>"
        "5. <b>Scoring & Decision Support Tier:</b> Computes 7-factor weighted match scores and models estimated shortlist screening probability.<br/>"
        "6. <b>Persistence Tier:</b> Employs SQLAlchemy ORM with SQLite (development) and PostgreSQL (production) with JSON document columns."
    )
    story.append(Paragraph(p2, styles['DocBody']))
    story.append(Spacer(1, 8))

    # 7.2 System Workflow
    story.append(PageTracker('sec7_2', registry, '7.2 System Workflow & Execution Flowchart', 'section'))
    story.append(Paragraph("<b>7.2 System Workflow & Execution Flowchart</b>", styles['DocSectionTitle']))
    p3 = (
        "The operational lifecycle of the system executes across seventeen sequential steps:<br/>"
        "1. Candidate uploads resume (PDF/DOCX/TXT) or pastes text. &nbsp; 2. System validates file size and MIME type. &nbsp; "
        "3. Text is extracted via binary parsers. &nbsp; 4. Job Description is uploaded or pasted. &nbsp; 5. JD text is extracted and normalized. &nbsp; "
        "6. Resume content is segmented into structured sections. &nbsp; 7. JD requirements are classified into categories. &nbsp; "
        "8. Technical skills are normalized. &nbsp; 9. Exact keyword matches are identified. &nbsp; 10. Canonical synonyms are resolved. &nbsp; "
        "11. Sibling technologies are detected. &nbsp; 12. Missing required/preferred skills are isolated. &nbsp; 13. Experience and seniority are compared. &nbsp; "
        "14. 12-point ATS compliance audit is executed. &nbsp; 15. 7-factor weighted match score is computed. &nbsp; 16. Shortlist probability and bullet rewrites are generated. &nbsp; "
        "17. Interactive diagnostic results are rendered on the dashboard."
    )
    story.append(Paragraph(p3, styles['DocBody']))
    story.append(Spacer(1, 4))

    # Figure 7.2
    story.append(PageTracker('fig7_2', registry, 'Figure 7.2: Detailed System Execution Flowchart', 'figure'))
    story.append(create_flowchart_diagram())
    story.append(Paragraph("<b>Figure 7.2: Detailed System Execution Flowchart</b>", styles['DocCaption']))
    story.append(PageBreak())

    # 7.3 Data Flow Diagrams
    story.append(PageTracker('sec7_3', registry, '7.3 Data Flow Diagrams (Level 0 & Level 1 DFD)', 'section'))
    story.append(Paragraph("<b>7.3 Data Flow Diagrams (Level 0 & Level 1 DFD)</b>", styles['DocSectionTitle']))
    p4 = (
        "Data Flow Diagrams depict how data enters, flows through, is transformed by, and exits the software system. "
        "Figure 7.3 illustrates the Level 0 Context Diagram representing external entity interactions:"
    )
    story.append(Paragraph(p4, styles['DocBody']))
    story.append(Spacer(1, 4))

    # Figure 7.3
    story.append(PageTracker('fig7_3', registry, 'Figure 7.3: Level 0 Data Flow Diagram', 'figure'))
    story.append(create_dfd_level0_diagram())
    story.append(Paragraph("<b>Figure 7.3: Level 0 Data Flow Diagram (Context Diagram)</b>", styles['DocCaption']))
    story.append(Spacer(1, 6))

    p5 = (
        "Figure 7.4 illustrates the decomposed Level 1 Data Flow Diagram showing internal processes and data stores:"
    )
    story.append(Paragraph(p5, styles['DocBody']))
    story.append(Spacer(1, 4))

    # Figure 7.4
    story.append(PageTracker('fig7_4', registry, 'Figure 7.4: Level 1 Data Flow Diagram', 'figure'))
    story.append(create_dfd_level1_diagram())
    story.append(Paragraph("<b>Figure 7.4: Level 1 Data Flow Diagram (Decomposed Processes)</b>", styles['DocCaption']))
    story.append(Spacer(1, 8))

    # 7.4 ERD
    story.append(PageTracker('sec7_4', registry, '7.4 Entity Relationship Diagram & Relational Schemas', 'section'))
    story.append(Paragraph("<b>7.4 Entity Relationship Diagram & Relational Schemas</b>", styles['DocSectionTitle']))
    p6 = (
        "The relational database schema is modeled to ensure high data integrity, referential constraints, and fast query execution. "
        "Figure 7.5 details the Entity Relationship Diagram (ERD) with primary keys, foreign keys, and cardinalities:"
    )
    story.append(Paragraph(p6, styles['DocBody']))
    story.append(Spacer(1, 4))

    # Figure 7.5
    story.append(PageTracker('fig7_5', registry, 'Figure 7.5: Relational Entity Relationship Diagram', 'figure'))
    story.append(create_erd_diagram())
    story.append(Paragraph("<b>Figure 7.5: Relational Entity Relationship Diagram (ERD)</b>", styles['DocCaption']))
    story.append(PageBreak())
    return story
