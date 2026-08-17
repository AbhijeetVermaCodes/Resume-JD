import math
from reportlab.graphics.shapes import Drawing, Rect, String, Line, Group, Polygon, Circle
from reportlab.lib import colors

def draw_vector_arrow(drawing, x1, y1, x2, y2, color=colors.HexColor('#64748B'), width=1.2, arrow_len=6):
    drawing.add(Line(x1, y1, x2, y2, strokeColor=color, strokeWidth=width))
    angle = math.atan2(y2 - y1, x2 - x1)
    arrow_angle = math.pi / 6
    x3 = x2 - arrow_len * math.cos(angle - arrow_angle)
    y3 = y2 - arrow_len * math.sin(angle - arrow_angle)
    x4 = x2 - arrow_len * math.cos(angle + arrow_angle)
    y4 = y2 - arrow_len * math.sin(angle + arrow_angle)
    drawing.add(Polygon([x2, y2, x3, y3, x4, y4], fillColor=color, strokeColor=color))

def create_system_architecture_diagram():
    """Figure 7.1: Multi-Tier System Architecture Diagram"""
    w, h = 480, 260
    d = Drawing(w, h)
    
    # Outer Background Container
    d.add(Rect(0, 0, w, h, rx=6, ry=6, fillColor=colors.HexColor('#F8FAFC'), strokeColor=colors.HexColor('#CBD5E1'), strokeWidth=1))
    d.add(String(w/2, h - 18, 'SYSTEM ARCHITECTURE — MULTI-TIER COGNITIVE PIPELINE', fontName='Helvetica-Bold', fontSize=10.5, textAnchor='middle', fillColor=colors.HexColor('#1E3A8A')))
    
    # Tier 1: Presentation Tier (React + TypeScript)
    d.add(Rect(15, h - 55, 450, 30, rx=4, ry=4, fillColor=colors.HexColor('#EFF6FF'), strokeColor=colors.HexColor('#3B82F6'), strokeWidth=1.2))
    d.add(String(240, h - 42, 'PRESENTATION TIER: React 18 SPA + TypeScript + Vite + Tailwind CSS + Lucide Icons', fontName='Helvetica-Bold', fontSize=8.5, textAnchor='middle', fillColor=colors.HexColor('#1E40AF')))
    d.add(String(240, h - 52, 'Dual Ingestion UI | Interactive Gauges | Live Weights Modal | Split-Screen Inspection | Export Engine', fontName='Helvetica', fontSize=7.2, textAnchor='middle', fillColor=colors.HexColor('#3B82F6')))
    
    draw_vector_arrow(d, 240, h - 55, 240, h - 72, color=colors.HexColor('#3B82F6'), width=1.5)
    
    # Tier 2: Application / API Gateway Tier
    d.add(Rect(15, h - 105, 450, 32, rx=4, ry=4, fillColor=colors.HexColor('#F0FDF4'), strokeColor=colors.HexColor('#16A34A'), strokeWidth=1.2))
    d.add(String(240, h - 90, 'APPLICATION & API GATEWAY TIER: Python 3.11 + FastAPI + Pydantic v2 + Uvicorn', fontName='Helvetica-Bold', fontSize=8.5, textAnchor='middle', fillColor=colors.HexColor('#15803D')))
    d.add(String(240, h - 100, 'REST Endpoints: /api/resume/upload | /api/job-description/upload | /api/analyze | /api/config/weights', fontName='Helvetica', fontSize=7.2, textAnchor='middle', fillColor=colors.HexColor('#16A34A')))
    
    draw_vector_arrow(d, 120, h - 105, 120, h - 122, color=colors.HexColor('#16A34A'), width=1.5)
    draw_vector_arrow(d, 360, h - 105, 360, h - 122, color=colors.HexColor('#16A34A'), width=1.5)

    # Tier 3: Left (Document Ingestion Engine) & Right (Semantic AI & Taxonomy Graph)
    # Left box
    d.add(Rect(15, h - 165, 220, 42, rx=4, ry=4, fillColor=colors.HexColor('#FEF3C7'), strokeColor=colors.HexColor('#D97706'), strokeWidth=1.2))
    d.add(String(125, h - 140, 'DOCUMENT PARSING LAYER', fontName='Helvetica-Bold', fontSize=8.2, textAnchor='middle', fillColor=colors.HexColor('#92400E')))
    d.add(String(125, h - 150, 'pypdf | pdfplumber | python-docx', fontName='Helvetica', fontSize=7.2, textAnchor='middle', fillColor=colors.HexColor('#78350F')))
    d.add(String(125, h - 160, '12-Point ATS Hazard Detector & Normalizer', fontName='Helvetica', fontSize=7.0, textAnchor='middle', fillColor=colors.HexColor('#B45309')))
    
    # Right box
    d.add(Rect(245, h - 165, 220, 42, rx=4, ry=4, fillColor=colors.HexColor('#EEF2FF'), strokeColor=colors.HexColor('#6366F1'), strokeWidth=1.2))
    d.add(String(355, h - 140, 'SEMANTIC AI & TAXONOMY LAYER', fontName='Helvetica-Bold', fontSize=8.2, textAnchor='middle', fillColor=colors.HexColor('#3730A3')))
    d.add(String(355, h - 150, 'Synonym Graph + Sibling Tech Clusters', fontName='Helvetica', fontSize=7.2, textAnchor='middle', fillColor=colors.HexColor('#4338CA')))
    d.add(String(355, h - 160, 'Multi-Provider: Gemini-2.5 / GPT-4o-mini', fontName='Helvetica', fontSize=7.0, textAnchor='middle', fillColor=colors.HexColor('#4F46E5')))

    draw_vector_arrow(d, 125, h - 165, 200, h - 180, color=colors.HexColor('#D97706'), width=1.5)
    draw_vector_arrow(d, 355, h - 165, 280, h - 180, color=colors.HexColor('#6366F1'), width=1.5)

    # Tier 4: Scoring & Decision Support Engine
    d.add(Rect(15, h - 215, 450, 32, rx=4, ry=4, fillColor=colors.HexColor('#FDF2F8'), strokeColor=colors.HexColor('#DB2777'), strokeWidth=1.2))
    d.add(String(240, h - 198, 'SCORING & DECISION SUPPORT ENGINE (Deterministic & Explainable)', fontName='Helvetica-Bold', fontSize=8.5, textAnchor='middle', fillColor=colors.HexColor('#9D174D')))
    d.add(String(240, h - 209, '7 Weighted Pillars (35% Skills, 20% Exp, etc.) | Shortlist Probability Model | Anti-Hallucination Rewrites', fontName='Helvetica', fontSize=7.2, textAnchor='middle', fillColor=colors.HexColor('#DB2777')))

    draw_vector_arrow(d, 240, h - 215, 240, h - 230, color=colors.HexColor('#DB2777'), width=1.5)

    # Tier 5: Persistence & Storage Layer
    d.add(Rect(15, 8, 450, 20, rx=3, ry=3, fillColor=colors.HexColor('#F1F5F9'), strokeColor=colors.HexColor('#64748B'), strokeWidth=1.0))
    d.add(String(240, 15, 'PERSISTENCE LAYER: SQLAlchemy ORM | SQLite / PostgreSQL (Relational + JSON Schemas) | Ephemeral Cache', fontName='Helvetica-Bold', fontSize=7.5, textAnchor='middle', fillColor=colors.HexColor('#334155')))

    return d

def create_flowchart_diagram():
    """Figure 7.2: Detailed System Execution Flowchart"""
    w, h = 480, 380
    d = Drawing(w, h)
    
    # Outer frame
    d.add(Rect(0, 0, w, h, rx=6, ry=6, fillColor=colors.HexColor('#F8FAFC'), strokeColor=colors.HexColor('#CBD5E1'), strokeWidth=1))
    d.add(String(w/2, h - 16, 'SYSTEM WORKFLOW & DECISION FLOWCHART', fontName='Helvetica-Bold', fontSize=10, textAnchor='middle', fillColor=colors.HexColor('#1E3A8A')))
    
    # Start Node (pill)
    d.add(Rect(200, h - 45, 80, 20, rx=10, ry=10, fillColor=colors.HexColor('#1E3A8A'), strokeColor=colors.HexColor('#1E3A8A')))
    d.add(String(240, h - 38, 'START', fontName='Helvetica-Bold', fontSize=8, textAnchor='middle', fillColor=colors.white))
    draw_vector_arrow(d, 240, h - 45, 240, h - 60)

    # Step 1: Upload Resume (Parallelogram)
    d.add(Polygon([160, h - 85, 310, h - 85, 330, h - 63, 180, h - 63], fillColor=colors.HexColor('#DBEAFE'), strokeColor=colors.HexColor('#2563EB'), strokeWidth=1))
    d.add(String(245, h - 77, 'Upload Resume (PDF/DOCX/TXT)', fontName='Helvetica', fontSize=7.5, textAnchor='middle', fillColor=colors.HexColor('#1E40AF')))
    draw_vector_arrow(d, 240, h - 85, 240, h - 100)

    # Step 2: Validate File (Diamond)
    d.add(Polygon([240, h - 98, 305, h - 118, 240, h - 138, 175, h - 118], fillColor=colors.HexColor('#FEF3C7'), strokeColor=colors.HexColor('#D97706'), strokeWidth=1))
    d.add(String(240, h - 116, 'Valid File?', fontName='Helvetica-Bold', fontSize=7.5, textAnchor='middle', fillColor=colors.HexColor('#92400E')))
    d.add(String(240, h - 126, 'Size & Type OK', fontName='Helvetica', fontSize=6.5, textAnchor='middle', fillColor=colors.HexColor('#B45309')))
    
    # Decision No:
    draw_vector_arrow(d, 305, h - 118, 410, h - 118)
    d.add(String(350, h - 112, 'No', fontName='Helvetica-Bold', fontSize=7, fillColor=colors.HexColor('#DC2626')))
    d.add(Rect(375, h - 145, 90, 24, rx=3, ry=3, fillColor=colors.HexColor('#FEE2E2'), strokeColor=colors.HexColor('#DC2626'), strokeWidth=1))
    d.add(String(420, h - 134, 'Display Error &', fontName='Helvetica', fontSize=7, textAnchor='middle', fillColor=colors.HexColor('#991B1B')))
    d.add(String(420, h - 142, 'Prompt Retry', fontName='Helvetica', fontSize=7, textAnchor='middle', fillColor=colors.HexColor('#991B1B')))
    
    # Decision Yes:
    draw_vector_arrow(d, 240, h - 138, 240, h - 153)
    d.add(String(248, h - 145, 'Yes', fontName='Helvetica-Bold', fontSize=7, fillColor=colors.HexColor('#16A34A')))

    # Step 3: Extract Text & Audit ATS Hazards
    d.add(Rect(140, h - 175, 200, 22, rx=3, ry=3, fillColor=colors.HexColor('#E0F2FE'), strokeColor=colors.HexColor('#0284C7'), strokeWidth=1))
    d.add(String(240, h - 165, 'Extract Text & Audit ATS Hazards', fontName='Helvetica', fontSize=7.5, textAnchor='middle', fillColor=colors.HexColor('#0369A1')))
    draw_vector_arrow(d, 240, h - 175, 240, h - 190)

    # Step 4: Upload/Paste JD
    d.add(Polygon([160, h - 212, 310, h - 212, 330, h - 192, 180, h - 192], fillColor=colors.HexColor('#DBEAFE'), strokeColor=colors.HexColor('#2563EB'), strokeWidth=1))
    d.add(String(245, h - 204, 'Input Job Description (Text/File)', fontName='Helvetica', fontSize=7.5, textAnchor='middle', fillColor=colors.HexColor('#1E40AF')))
    draw_vector_arrow(d, 240, h - 212, 240, h - 227)

    # Step 5: Structure Resume & JD Requirements
    d.add(Rect(130, h - 248, 220, 20, rx=3, ry=3, fillColor=colors.HexColor('#F3E8FF'), strokeColor=colors.HexColor('#9333EA'), strokeWidth=1))
    d.add(String(240, h - 239, 'Parse & Classify (Req vs Pref Skills, Exp, Edu)', fontName='Helvetica', fontSize=7.2, textAnchor='middle', fillColor=colors.HexColor('#6B21A8')))
    draw_vector_arrow(d, 240, h - 248, 240, h - 263)

    # Step 6: Semantic Skill & Sibling Matching Engine
    d.add(Rect(120, h - 285, 240, 22, rx=3, ry=3, fillColor=colors.HexColor('#EEF2FF'), strokeColor=colors.HexColor('#4F46E5'), strokeWidth=1))
    d.add(String(240, h - 274, 'Match Engine: Exact + Synonyms + Sibling Tech', fontName='Helvetica-Bold', fontSize=7.2, textAnchor='middle', fillColor=colors.HexColor('#3730A3')))
    d.add(String(240, h - 282, 'Detect Missing Required/Preferred Skills', fontName='Helvetica', fontSize=6.8, textAnchor='middle', fillColor=colors.HexColor('#4338CA')))
    draw_vector_arrow(d, 240, h - 285, 240, h - 300)

    # Step 7: Multi-Factor Weighted Scoring & ATS Audit
    d.add(Rect(120, h - 322, 240, 22, rx=3, ry=3, fillColor=colors.HexColor('#FDF2F8'), strokeColor=colors.HexColor('#DB2777'), strokeWidth=1))
    d.add(String(240, h - 311, 'Calculate 7-Factor Weighted Match Score (0-100)', fontName='Helvetica-Bold', fontSize=7.2, textAnchor='middle', fillColor=colors.HexColor('#9D174D')))
    d.add(String(240, h - 319, 'Compute Shortlist Probability & 12-Pt ATS Score', fontName='Helvetica', fontSize=6.8, textAnchor='middle', fillColor=colors.HexColor('#BE185D')))
    draw_vector_arrow(d, 240, h - 322, 240, h - 337)

    # Step 8: Render Results Dashboard & Actionable Rewrites
    d.add(Rect(130, h - 357, 220, 20, rx=3, ry=3, fillColor=colors.HexColor('#DCFCE7'), strokeColor=colors.HexColor('#16A34A'), strokeWidth=1))
    d.add(String(240, h - 348, 'Synthesize Rewrites & Render Rich Dashboard', fontName='Helvetica-Bold', fontSize=7.2, textAnchor='middle', fillColor=colors.HexColor('#15803D')))
    draw_vector_arrow(d, 240, h - 357, 240, h - 368)

    # End Node
    d.add(Rect(200, 2, 80, 16, rx=8, ry=8, fillColor=colors.HexColor('#1E3A8A'), strokeColor=colors.HexColor('#1E3A8A')))
    d.add(String(240, 7, 'END', fontName='Helvetica-Bold', fontSize=8, textAnchor='middle', fillColor=colors.white))

    return d

def create_dfd_level0_diagram():
    """Figure 7.3: Level 0 Context Data Flow Diagram"""
    w, h = 480, 170
    d = Drawing(w, h)
    d.add(Rect(0, 0, w, h, rx=6, ry=6, fillColor=colors.HexColor('#F8FAFC'), strokeColor=colors.HexColor('#CBD5E1'), strokeWidth=1))
    d.add(String(w/2, h - 14, 'LEVEL 0 DATA FLOW DIAGRAM (CONTEXT DIAGRAM)', fontName='Helvetica-Bold', fontSize=9.5, textAnchor='middle', fillColor=colors.HexColor('#1E3A8A')))

    # External Entity: User / Candidate
    d.add(Rect(20, 45, 100, 80, rx=4, ry=4, fillColor=colors.HexColor('#F1F5F9'), strokeColor=colors.HexColor('#475569'), strokeWidth=1.5))
    d.add(String(70, 95, 'EXTERNAL ENTITY', fontName='Helvetica', fontSize=6.5, textAnchor='middle', fillColor=colors.HexColor('#64748B')))
    d.add(String(70, 80, 'User /', fontName='Helvetica-Bold', fontSize=9, textAnchor='middle', fillColor=colors.HexColor('#0F172A')))
    d.add(String(70, 68, 'Candidate', fontName='Helvetica-Bold', fontSize=9, textAnchor='middle', fillColor=colors.HexColor('#0F172A')))

    # Central System: Process 0.0
    d.add(Circle(370, 85, 55, fillColor=colors.HexColor('#1E3A8A'), strokeColor=colors.HexColor('#1E40AF'), strokeWidth=1.5))
    d.add(String(370, 108, 'PROCESS 0.0', fontName='Helvetica-Bold', fontSize=7, textAnchor='middle', fillColor=colors.HexColor('#93C5FD')))
    d.add(String(370, 95, 'AI-Powered', fontName='Helvetica-Bold', fontSize=8.5, textAnchor='middle', fillColor=colors.white))
    d.add(String(370, 82, 'CV & JD Matcher', fontName='Helvetica-Bold', fontSize=8.5, textAnchor='middle', fillColor=colors.white))
    d.add(String(370, 70, 'System Engine', fontName='Helvetica', fontSize=7.5, textAnchor='middle', fillColor=colors.HexColor('#BFDBFE')))

    # Input Flows (Top)
    draw_vector_arrow(d, 120, 105, 315, 105, color=colors.HexColor('#2563EB'), width=1.3)
    d.add(String(215, 110, '1. Resume File (PDF/DOCX/TXT) / Text', fontName='Helvetica-Bold', fontSize=6.8, textAnchor='middle', fillColor=colors.HexColor('#1E40AF')))
    
    draw_vector_arrow(d, 120, 90, 315, 90, color=colors.HexColor('#2563EB'), width=1.3)
    d.add(String(215, 94, '2. Target Job Description Text / Criteria', fontName='Helvetica', fontSize=6.8, textAnchor='middle', fillColor=colors.HexColor('#1E40AF')))

    draw_vector_arrow(d, 120, 75, 315, 75, color=colors.HexColor('#2563EB'), width=1.3)
    d.add(String(215, 79, '3. Custom Scoring Weights Preferences', fontName='Helvetica', fontSize=6.8, textAnchor='middle', fillColor=colors.HexColor('#1E40AF')))

    # Output Flows (Bottom)
    draw_vector_arrow(d, 315, 52, 120, 52, color=colors.HexColor('#059669'), width=1.3)
    d.add(String(215, 56, '4. Match Score, Probability & ATS Audit', fontName='Helvetica-Bold', fontSize=6.8, textAnchor='middle', fillColor=colors.HexColor('#065F46')))

    draw_vector_arrow(d, 315, 36, 120, 36, color=colors.HexColor('#059669'), width=1.3)
    d.add(String(215, 40, '5. Missing Keywords & Actionable Rewrites', fontName='Helvetica', fontSize=6.8, textAnchor='middle', fillColor=colors.HexColor('#065F46')))

    return d

def create_dfd_level1_diagram():
    """Figure 7.4: Level 1 Data Flow Diagram"""
    w, h = 480, 270
    d = Drawing(w, h)
    d.add(Rect(0, 0, w, h, rx=6, ry=6, fillColor=colors.HexColor('#F8FAFC'), strokeColor=colors.HexColor('#CBD5E1'), strokeWidth=1))
    d.add(String(w/2, h - 14, 'LEVEL 1 DATA FLOW DIAGRAM (DECOMPOSED PROCESSES)', fontName='Helvetica-Bold', fontSize=9.5, textAnchor='middle', fillColor=colors.HexColor('#1E3A8A')))

    # 4 Data Stores (Open horizontal lines)
    def draw_datastore(x, y, name, tag):
        d.add(Line(x, y, x + 85, y, strokeColor=colors.HexColor('#334155'), strokeWidth=1.2))
        d.add(Line(x, y - 20, x + 85, y - 20, strokeColor=colors.HexColor('#334155'), strokeWidth=1.2))
        d.add(String(x + 5, y - 13, tag, fontName='Helvetica-Bold', fontSize=6.5, fillColor=colors.HexColor('#1E3A8A')))
        d.add(String(x + 22, y - 13, name, fontName='Helvetica', fontSize=6.5, fillColor=colors.HexColor('#334155')))

    draw_datastore(15, h - 45, 'Resume Data', 'D1')
    draw_datastore(380, h - 45, 'JD Data', 'D2')
    draw_datastore(15, 30, 'Analysis Store', 'D3')
    draw_datastore(380, 30, 'Weight Config', 'D4')

    # Processes
    # P1: Resume Ingest
    d.add(Circle(70, h - 85, 22, fillColor=colors.HexColor('#EFF6FF'), strokeColor=colors.HexColor('#2563EB'), strokeWidth=1))
    d.add(String(70, h - 82, '1.0 Ingest', fontName='Helvetica-Bold', fontSize=6.5, textAnchor='middle', fillColor=colors.HexColor('#1E40AF')))
    d.add(String(70, h - 90, '& Parse CV', fontName='Helvetica', fontSize=6.0, textAnchor='middle', fillColor=colors.HexColor('#1E40AF')))

    # P2: JD Ingest
    d.add(Circle(410, h - 85, 22, fillColor=colors.HexColor('#EFF6FF'), strokeColor=colors.HexColor('#2563EB'), strokeWidth=1))
    d.add(String(410, h - 82, '2.0 Ingest', fontName='Helvetica-Bold', fontSize=6.5, textAnchor='middle', fillColor=colors.HexColor('#1E40AF')))
    d.add(String(410, h - 90, '& Parse JD', fontName='Helvetica', fontSize=6.0, textAnchor='middle', fillColor=colors.HexColor('#1E40AF')))

    # P3: Requirement Structuring
    d.add(Circle(240, h - 85, 24, fillColor=colors.HexColor('#F3E8FF'), strokeColor=colors.HexColor('#9333EA'), strokeWidth=1))
    d.add(String(240, h - 82, '3.0 Extract &', fontName='Helvetica-Bold', fontSize=6.5, textAnchor='middle', fillColor=colors.HexColor('#6B21A8')))
    d.add(String(240, h - 90, 'Normalize', fontName='Helvetica', fontSize=6.0, textAnchor='middle', fillColor=colors.HexColor('#6B21A8')))

    # P4: Semantic Skill Matching
    d.add(Circle(140, h - 145, 24, fillColor=colors.HexColor('#EEF2FF'), strokeColor=colors.HexColor('#4F46E5'), strokeWidth=1))
    d.add(String(140, h - 142, '4.0 Semantic', fontName='Helvetica-Bold', fontSize=6.5, textAnchor='middle', fillColor=colors.HexColor('#3730A3')))
    d.add(String(140, h - 150, 'Skill Match', fontName='Helvetica', fontSize=6.0, textAnchor='middle', fillColor=colors.HexColor('#3730A3')))

    # P5: 12-Pt ATS Compliance Audit
    d.add(Circle(340, h - 145, 24, fillColor=colors.HexColor('#FEF3C7'), strokeColor=colors.HexColor('#D97706'), strokeWidth=1))
    d.add(String(340, h - 142, '5.0 ATS Rule', fontName='Helvetica-Bold', fontSize=6.5, textAnchor='middle', fillColor=colors.HexColor('#92400E')))
    d.add(String(340, h - 150, 'Compliance', fontName='Helvetica', fontSize=6.0, textAnchor='middle', fillColor=colors.HexColor('#92400E')))

    # P6: Multi-Factor Weighted Scoring
    d.add(Circle(240, h - 190, 24, fillColor=colors.HexColor('#FDF2F8'), strokeColor=colors.HexColor('#DB2777'), strokeWidth=1))
    d.add(String(240, h - 187, '6.0 Weighted', fontName='Helvetica-Bold', fontSize=6.5, textAnchor='middle', fillColor=colors.HexColor('#9D174D')))
    d.add(String(240, h - 195, 'Scoring Engine', fontName='Helvetica', fontSize=6.0, textAnchor='middle', fillColor=colors.HexColor('#9D174D')))

    # P7: Recommendation Synthesis
    d.add(Circle(140, h - 235, 22, fillColor=colors.HexColor('#DCFCE7'), strokeColor=colors.HexColor('#16A34A'), strokeWidth=1))
    d.add(String(140, h - 232, '7.0 Actionable', fontName='Helvetica-Bold', fontSize=6.5, textAnchor='middle', fillColor=colors.HexColor('#15803D')))
    d.add(String(140, h - 240, 'Rewrites', fontName='Helvetica', fontSize=6.0, textAnchor='middle', fillColor=colors.HexColor('#15803D')))

    # P8: Results Dashboard & Export
    d.add(Circle(340, h - 235, 22, fillColor=colors.HexColor('#DCFCE7'), strokeColor=colors.HexColor('#16A34A'), strokeWidth=1))
    d.add(String(340, h - 232, '8.0 Dashboard', fontName='Helvetica-Bold', fontSize=6.5, textAnchor='middle', fillColor=colors.HexColor('#15803D')))
    d.add(String(340, h - 240, '& JSON/PDF', fontName='Helvetica', fontSize=6.0, textAnchor='middle', fillColor=colors.HexColor('#15803D')))

    # Connector flows
    draw_vector_arrow(d, 92, h - 85, 216, h - 85)
    draw_vector_arrow(d, 388, h - 85, 264, h - 85)
    draw_vector_arrow(d, 225, h - 102, 155, h - 128)
    draw_vector_arrow(d, 255, h - 102, 325, h - 128)
    draw_vector_arrow(d, 155, h - 162, 225, h - 178)
    draw_vector_arrow(d, 325, h - 162, 255, h - 178)
    draw_vector_arrow(d, 225, h - 202, 155, h - 218)
    draw_vector_arrow(d, 255, h - 202, 325, h - 218)
    draw_vector_arrow(d, 162, h - 235, 318, h - 235)

    return d

def create_erd_diagram():
    """Figure 7.5: Entity Relationship Diagram"""
    w, h = 480, 270
    d = Drawing(w, h)
    d.add(Rect(0, 0, w, h, rx=6, ry=6, fillColor=colors.HexColor('#F8FAFC'), strokeColor=colors.HexColor('#CBD5E1'), strokeWidth=1))
    d.add(String(w/2, h - 14, 'RELATIONAL ENTITY RELATIONSHIP DIAGRAM (ERD)', fontName='Helvetica-Bold', fontSize=9.5, textAnchor='middle', fillColor=colors.HexColor('#1E3A8A')))

    def draw_entity_table(x, y, width, height, title, rows):
        d.add(Rect(x, y, width, height, rx=3, ry=3, fillColor=colors.white, strokeColor=colors.HexColor('#334155'), strokeWidth=1))
        # Header
        d.add(Rect(x, y + height - 16, width, 16, rx=2, ry=2, fillColor=colors.HexColor('#1E3A8A'), strokeColor=colors.HexColor('#1E3A8A')))
        d.add(String(x + width/2, y + height - 12, title, fontName='Helvetica-Bold', fontSize=7.2, textAnchor='middle', fillColor=colors.white))
        
        # Attributes
        row_y = y + height - 26
        for pk_fk, name, data_type in rows:
            if pk_fk == 'PK':
                d.add(String(x + 4, row_y, 'PK', fontName='Helvetica-Bold', fontSize=6.0, fillColor=colors.HexColor('#D97706')))
            elif pk_fk == 'FK':
                d.add(String(x + 4, row_y, 'FK', fontName='Helvetica-Bold', fontSize=6.0, fillColor=colors.HexColor('#2563EB')))
            else:
                d.add(String(x + 4, row_y, '  ', fontName='Helvetica', fontSize=6.0, fillColor=colors.HexColor('#64748B')))
            
            d.add(String(x + 18, row_y, name, fontName='Helvetica', fontSize=6.2, fillColor=colors.HexColor('#0F172A')))
            d.add(String(x + width - 4, row_y, data_type, fontName='Courier', fontSize=5.8, textAnchor='end', fillColor=colors.HexColor('#64748B')))
            row_y -= 10

    # User Entity
    draw_entity_table(15, h - 85, 120, 60, 'USER (Optional Auth)', [
        ('PK', 'user_id', 'VARCHAR(36)'),
        ('', 'email', 'VARCHAR(255)'),
        ('', 'name', 'VARCHAR(120)'),
        ('', 'created_at', 'DATETIME'),
    ])

    # Resume Record
    draw_entity_table(15, h - 180, 130, 80, 'RESUMES', [
        ('PK', 'id', 'VARCHAR(36)'),
        ('FK', 'user_id', 'VARCHAR(36)'),
        ('', 'filename', 'VARCHAR(255)'),
        ('', 'file_type', 'VARCHAR(50)'),
        ('', 'raw_text', 'TEXT'),
        ('', 'structured_data', 'JSON'),
        ('', 'created_at', 'DATETIME'),
    ])

    # Job Description Record
    draw_entity_table(335, h - 180, 130, 80, 'JOB_DESCRIPTIONS', [
        ('PK', 'id', 'VARCHAR(36)'),
        ('', 'title', 'VARCHAR(255)'),
        ('', 'company', 'VARCHAR(255)'),
        ('', 'raw_text', 'TEXT'),
        ('', 'structured_data', 'JSON'),
        ('', 'created_at', 'DATETIME'),
    ])

    # Analysis Record (Central Hub)
    draw_entity_table(175, h - 185, 130, 95, 'ANALYSES', [
        ('PK', 'id', 'VARCHAR(36)'),
        ('FK', 'resume_id', 'VARCHAR(36)'),
        ('FK', 'jd_id', 'VARCHAR(36)'),
        ('', 'overall_score', 'FLOAT'),
        ('', 'screening_prob', 'FLOAT'),
        ('', 'category_scores', 'JSON'),
        ('', 'ats_score', 'INT'),
        ('', 'created_at', 'DATETIME'),
    ])

    # Skill Match Record
    draw_entity_table(15, 15, 130, 70, 'SKILL_MATCHES', [
        ('PK', 'match_id', 'VARCHAR(36)'),
        ('FK', 'analysis_id', 'VARCHAR(36)'),
        ('', 'skill_name', 'VARCHAR(100)'),
        ('', 'match_type', 'VARCHAR(30)'),
        ('', 'evidence', 'TEXT'),
        ('', 'importance', 'VARCHAR(30)'),
    ])

    # Recommendations Record
    draw_entity_table(175, 15, 130, 70, 'RECOMMENDATIONS', [
        ('PK', 'rec_id', 'VARCHAR(36)'),
        ('FK', 'analysis_id', 'VARCHAR(36)'),
        ('', 'section', 'VARCHAR(60)'),
        ('', 'original_text', 'TEXT'),
        ('', 'rewrite_text', 'TEXT'),
        ('', 'why_reason', 'TEXT'),
    ])

    # Weight Config Record
    draw_entity_table(335, 15, 130, 55, 'WEIGHT_CONFIGS', [
        ('PK', 'id', 'INT (AUTO)'),
        ('', 'weights_json', 'JSON'),
        ('', 'updated_at', 'DATETIME'),
    ])

    # Connectors with 1:N relations
    draw_vector_arrow(d, 75, h - 85, 75, h - 100)
    d.add(String(82, h - 94, '1 : N', fontName='Helvetica-Bold', fontSize=6, fillColor=colors.HexColor('#1E3A8A')))

    draw_vector_arrow(d, 145, h - 140, 175, h - 140)
    d.add(String(155, h - 134, '1 : N', fontName='Helvetica-Bold', fontSize=6, fillColor=colors.HexColor('#1E3A8A')))

    draw_vector_arrow(d, 335, h - 140, 305, h - 140)
    d.add(String(312, h - 134, '1 : N', fontName='Helvetica-Bold', fontSize=6, fillColor=colors.HexColor('#1E3A8A')))

    draw_vector_arrow(d, 205, h - 185, 100, 85)
    d.add(String(145, 95, '1 : N', fontName='Helvetica-Bold', fontSize=6, fillColor=colors.HexColor('#1E3A8A')))

    draw_vector_arrow(d, 240, h - 185, 240, 85)
    d.add(String(246, 95, '1 : N', fontName='Helvetica-Bold', fontSize=6, fillColor=colors.HexColor('#1E3A8A')))

    return d

def create_scoring_weights_diagram():
    """Figure 8.1: Scoring Engine Weight Distribution Breakdown"""
    w, h = 480, 110
    d = Drawing(w, h)
    d.add(Rect(0, 0, w, h, rx=5, ry=5, fillColor=colors.HexColor('#F8FAFC'), strokeColor=colors.HexColor('#CBD5E1'), strokeWidth=1))
    d.add(String(w/2, h - 14, 'CONFIGURABLE 7-FACTOR SCORING WEIGHT DISTRIBUTION (DEFAULT: 100%)', fontName='Helvetica-Bold', fontSize=8.5, textAnchor='middle', fillColor=colors.HexColor('#1E3A8A')))

    pillars = [
        ('Skills Match', 35, colors.HexColor('#2563EB'), '35%'),
        ('Experience', 20, colors.HexColor('#4F46E5'), '20%'),
        ('Responsibilities', 15, colors.HexColor('#7C3AED'), '15%'),
        ('Education', 10, colors.HexColor('#059669'), '10%'),
        ('Projects', 10, colors.HexColor('#0891B2'), '10%'),
        ('Soft Skills', 5, colors.HexColor('#D97706'), '5%'),
        ('ATS Quality', 5, colors.HexColor('#E11D48'), '5%'),
    ]

    # Bar layout
    bar_x = 20
    bar_y = 48
    bar_w = 440
    bar_h = 24

    cur_x = bar_x
    for name, pct, color, pct_str in pillars:
        seg_w = (pct / 100.0) * bar_w
        d.add(Rect(cur_x, bar_y, seg_w, bar_h, fillColor=color, strokeColor=colors.white, strokeWidth=1))
        if seg_w > 20:
            d.add(String(cur_x + seg_w/2, bar_y + 8, pct_str, fontName='Helvetica-Bold', fontSize=7.5, textAnchor='middle', fillColor=colors.white))
        cur_x += seg_w

    # Legend underneath
    leg_x = 20
    leg_y = 20
    for idx, (name, pct, color, pct_str) in enumerate(pillars):
        x_pos = 20 + (idx % 4) * 110
        y_pos = 24 if idx < 4 else 10
        d.add(Rect(x_pos, y_pos, 8, 8, rx=1, ry=1, fillColor=color, strokeColor=color))
        d.add(String(x_pos + 12, y_pos + 1, f"{name} ({pct_str})", fontName='Helvetica', fontSize=6.5, fillColor=colors.HexColor('#334155')))

    return d

def create_ui_mockup_dashboard():
    """Figure 11.4: Multi-Metric Overall Match and ATS Dashboard (Mockup)"""
    w, h = 480, 240
    d = Drawing(w, h)
    d.add(Rect(0, 0, w, h, rx=6, ry=6, fillColor=colors.HexColor('#0F172A'), strokeColor=colors.HexColor('#334155'), strokeWidth=1.5))
    
    # App Header Bar
    d.add(Rect(0, h - 26, w, 26, rx=0, ry=0, fillColor=colors.HexColor('#1E293B'), strokeColor=colors.HexColor('#334155'), strokeWidth=0.5))
    d.add(String(15, h - 17, 'MatchCraft AI — CV & Job Description Screening Suite', fontName='Helvetica-Bold', fontSize=8.5, fillColor=colors.HexColor('#38BDF8')))
    d.add(Rect(320, h - 21, 65, 16, rx=3, ry=3, fillColor=colors.HexColor('#3B82F6'), strokeColor=colors.HexColor('#2563EB')))
    d.add(String(352, h - 16, '1-Click Demo', fontName='Helvetica-Bold', fontSize=6.5, textAnchor='middle', fillColor=colors.white))
    d.add(Rect(395, h - 21, 70, 16, rx=3, ry=3, fillColor=colors.HexColor('#334155'), strokeColor=colors.HexColor('#475569')))
    d.add(String(430, h - 16, 'Config Weights', fontName='Helvetica-Bold', fontSize=6.5, textAnchor='middle', fillColor=colors.HexColor('#E2E8F0')))

    # Top KPI Gauge Cards
    # Card 1: Overall Match Score
    d.add(Rect(15, h - 100, 140, 65, rx=4, ry=4, fillColor=colors.HexColor('#1E293B'), strokeColor=colors.HexColor('#334155'), strokeWidth=1))
    d.add(String(85, h - 45, 'OVERALL MATCH SCORE', fontName='Helvetica-Bold', fontSize=6.5, textAnchor='middle', fillColor=colors.HexColor('#94A3B8')))
    d.add(Circle(85, h - 70, 18, fillColor=colors.HexColor('#0F172A'), strokeColor=colors.HexColor('#3B82F6'), strokeWidth=3.5))
    d.add(String(85, h - 74, '78.5%', fontName='Helvetica-Bold', fontSize=8.5, textAnchor='middle', fillColor=colors.HexColor('#38BDF8')))
    d.add(String(85, h - 94, 'Verdict: Moderate Match', fontName='Helvetica', fontSize=6.0, textAnchor='middle', fillColor=colors.HexColor('#FBBF24')))

    # Card 2: Estimated Screening Probability
    d.add(Rect(170, h - 100, 140, 65, rx=4, ry=4, fillColor=colors.HexColor('#1E293B'), strokeColor=colors.HexColor('#334155'), strokeWidth=1))
    d.add(String(240, h - 45, 'ESTIMATED SCREENING PROB.', fontName='Helvetica-Bold', fontSize=6.5, textAnchor='middle', fillColor=colors.HexColor('#94A3B8')))
    d.add(Circle(240, h - 70, 18, fillColor=colors.HexColor('#0F172A'), strokeColor=colors.HexColor('#10B981'), strokeWidth=3.5))
    d.add(String(240, h - 74, '74%', fontName='Helvetica-Bold', fontSize=8.5, textAnchor='middle', fillColor=colors.HexColor('#34D399')))
    d.add(String(240, h - 94, 'Probable Initial Shortlist', fontName='Helvetica', fontSize=6.0, textAnchor='middle', fillColor=colors.HexColor('#34D399')))

    # Card 3: ATS Compatibility Audit Score
    d.add(Rect(325, h - 100, 140, 65, rx=4, ry=4, fillColor=colors.HexColor('#1E293B'), strokeColor=colors.HexColor('#334155'), strokeWidth=1))
    d.add(String(395, h - 45, 'ATS COMPLIANCE SCORE', fontName='Helvetica-Bold', fontSize=6.5, textAnchor='middle', fillColor=colors.HexColor('#94A3B8')))
    d.add(Circle(395, h - 70, 18, fillColor=colors.HexColor('#0F172A'), strokeColor=colors.HexColor('#6366F1'), strokeWidth=3.5))
    d.add(String(395, h - 74, '92/100', fontName='Helvetica-Bold', fontSize=8.5, textAnchor='middle', fillColor=colors.HexColor('#818CF8')))
    d.add(String(395, h - 94, 'Passed 11 of 12 Checks', fontName='Helvetica', fontSize=6.0, textAnchor='middle', fillColor=colors.HexColor('#818CF8')))

    # Lower Panel: Skills Breakdown & Experience Side-by-Side (Split)
    # Left sub-panel
    d.add(Rect(15, 10, 220, 120, rx=4, ry=4, fillColor=colors.HexColor('#1E293B'), strokeColor=colors.HexColor('#334155'), strokeWidth=1))
    d.add(String(25, 118, 'Technical Skill & Keyword Breakdown', fontName='Helvetica-Bold', fontSize=7.5, fillColor=colors.HexColor('#E2E8F0')))
    
    # Strong tags
    d.add(String(25, 102, 'Strong Matches (Exact & Synonyms):', fontName='Helvetica', fontSize=6.5, fillColor=colors.HexColor('#94A3B8')))
    d.add(Rect(25, 86, 40, 12, rx=2, ry=2, fillColor=colors.HexColor('#064E3B'), strokeColor=colors.HexColor('#059669')))
    d.add(String(45, 90, 'Java', fontName='Helvetica-Bold', fontSize=6, textAnchor='middle', fillColor=colors.HexColor('#6EE7B7')))
    d.add(Rect(70, 86, 60, 12, rx=2, ry=2, fillColor=colors.HexColor('#064E3B'), strokeColor=colors.HexColor('#059669')))
    d.add(String(100, 90, 'Spring Boot', fontName='Helvetica-Bold', fontSize=6, textAnchor='middle', fillColor=colors.HexColor('#6EE7B7')))
    d.add(Rect(135, 86, 45, 12, rx=2, ry=2, fillColor=colors.HexColor('#064E3B'), strokeColor=colors.HexColor('#059669')))
    d.add(String(157, 90, 'Docker', fontName='Helvetica-Bold', fontSize=6, textAnchor='middle', fillColor=colors.HexColor('#6EE7B7')))

    # Partial tags
    d.add(String(25, 72, 'Partial / Sibling Match (Taxonomy Linked):', fontName='Helvetica', fontSize=6.5, fillColor=colors.HexColor('#94A3B8')))
    d.add(Rect(25, 56, 120, 12, rx=2, ry=2, fillColor=colors.HexColor('#78350F'), strokeColor=colors.HexColor('#D97706')))
    d.add(String(85, 60, 'Kafka (Found: RabbitMQ)', fontName='Helvetica-Bold', fontSize=6, textAnchor='middle', fillColor=colors.HexColor('#FCD34D')))

    # Missing tags
    d.add(String(25, 42, 'Missing Requirements (Gaps):', fontName='Helvetica', fontSize=6.5, fillColor=colors.HexColor('#94A3B8')))
    d.add(Rect(25, 26, 60, 12, rx=2, ry=2, fillColor=colors.HexColor('#7F1D1D'), strokeColor=colors.HexColor('#DC2626')))
    d.add(String(55, 30, 'Kubernetes', fontName='Helvetica-Bold', fontSize=6, textAnchor='middle', fillColor=colors.HexColor('#FCA5A5')))
    d.add(Rect(90, 26, 50, 12, rx=2, ry=2, fillColor=colors.HexColor('#7F1D1D'), strokeColor=colors.HexColor('#DC2626')))
    d.add(String(115, 30, 'Terraform', fontName='Helvetica-Bold', fontSize=6, textAnchor='middle', fillColor=colors.HexColor('#FCA5A5')))

    # Right sub-panel: Actionable Rewrites
    d.add(Rect(245, 10, 220, 120, rx=4, ry=4, fillColor=colors.HexColor('#1E293B'), strokeColor=colors.HexColor('#334155'), strokeWidth=1))
    d.add(String(255, 118, 'Actionable Bullet Improvement Suggestion', fontName='Helvetica-Bold', fontSize=7.5, fillColor=colors.HexColor('#E2E8F0')))
    
    d.add(String(255, 102, 'Original Snippet:', fontName='Helvetica-Bold', fontSize=6.5, fillColor=colors.HexColor('#F87171')))
    d.add(String(255, 92, '"Built REST APIs using Spring Boot and PostgreSQL."', fontName='Helvetica-Oblique', fontSize=6.2, fillColor=colors.HexColor('#CBD5E1')))

    d.add(String(255, 76, 'Recommended Action-Metric Rewrite:', fontName='Helvetica-Bold', fontSize=6.5, fillColor=colors.HexColor('#4ADE80')))
    d.add(String(255, 66, '"Architected scalable Spring Boot microservices with PostgreSQL,', fontName='Helvetica', fontSize=6.0, fillColor=colors.HexColor('#F8FAFC')))
    d.add(String(255, 57, ' achieving [X%] reduction in API latency for [X,000+] DAU."', fontName='Helvetica', fontSize=6.0, fillColor=colors.HexColor('#F8FAFC')))

    d.add(Rect(255, 18, 200, 24, rx=2, ry=2, fillColor=colors.HexColor('#0F172A'), strokeColor=colors.HexColor('#F59E0B'), strokeWidth=0.8))
    d.add(String(355, 32, 'Anti-Hallucination Guardrail Notice:', fontName='Helvetica-Bold', fontSize=5.8, textAnchor='middle', fillColor=colors.HexColor('#FCD34D')))
    d.add(String(355, 23, 'Only include metric claims if you genuinely achieved them.', fontName='Helvetica', fontSize=5.5, textAnchor='middle', fillColor=colors.HexColor('#CBD5E1')))

    return d

def create_ui_mockup_home():
    """Figure 11.1: Home Page and Navigation Header (Mockup)"""
    w, h = 480, 160
    d = Drawing(w, h)
    d.add(Rect(0, 0, w, h, rx=5, ry=5, fillColor=colors.HexColor('#0F172A'), strokeColor=colors.HexColor('#334155'), strokeWidth=1))
    
    # App Nav Bar
    d.add(Rect(0, h - 26, w, 26, rx=0, ry=0, fillColor=colors.HexColor('#1E293B'), strokeColor=colors.HexColor('#334155'), strokeWidth=0.5))
    d.add(String(15, h - 17, 'MatchCraft AI — Semantic Candidate-JD Screening Suite', fontName='Helvetica-Bold', fontSize=8.5, fillColor=colors.HexColor('#38BDF8')))
    d.add(Rect(320, h - 21, 65, 16, rx=3, ry=3, fillColor=colors.HexColor('#3B82F6'), strokeColor=colors.HexColor('#2563EB')))
    d.add(String(352, h - 16, '1-Click Demo', fontName='Helvetica-Bold', fontSize=6.5, textAnchor='middle', fillColor=colors.white))
    d.add(Rect(395, h - 21, 70, 16, rx=3, ry=3, fillColor=colors.HexColor('#334155'), strokeColor=colors.HexColor('#475569')))
    d.add(String(430, h - 16, 'Config Weights', fontName='Helvetica-Bold', fontSize=6.5, textAnchor='middle', fillColor=colors.HexColor('#E2E8F0')))

    # Hero Banner
    d.add(Rect(15, 15, 450, 110, rx=4, ry=4, fillColor=colors.HexColor('#1E293B'), strokeColor=colors.HexColor('#3B82F6'), strokeWidth=0.8))
    d.add(String(240, 105, 'Bridge the Information Asymmetry in Your Job Applications', fontName='Helvetica-Bold', fontSize=10, textAnchor='middle', fillColor=colors.HexColor('#F8FAFC')))
    d.add(String(240, 90, 'AI-Assisted Semantic Resume Analysis, Missing Keyword Detection & ATS Compliance Audit', fontName='Helvetica', fontSize=7.2, textAnchor='middle', fillColor=colors.HexColor('#94A3B8')))
    
    # 3 Feature Pills
    d.add(Rect(30, 40, 125, 38, rx=3, ry=3, fillColor=colors.HexColor('#0F172A'), strokeColor=colors.HexColor('#334155'), strokeWidth=0.8))
    d.add(String(92, 64, 'Semantic Taxonomy', fontName='Helvetica-Bold', fontSize=7.0, textAnchor='middle', fillColor=colors.HexColor('#60A5FA')))
    d.add(String(92, 50, 'Synonyms & Sibling Tech', fontName='Helvetica', fontSize=6.0, textAnchor='middle', fillColor=colors.HexColor('#94A3B8')))

    d.add(Rect(175, 40, 130, 38, rx=3, ry=3, fillColor=colors.HexColor('#0F172A'), strokeColor=colors.HexColor('#334155'), strokeWidth=0.8))
    d.add(String(240, 64, '12-Point ATS Audit', fontName='Helvetica-Bold', fontSize=7.0, textAnchor='middle', fillColor=colors.HexColor('#34D399')))
    d.add(String(240, 50, 'Detect Layout Hazards', fontName='Helvetica', fontSize=6.0, textAnchor='middle', fillColor=colors.HexColor('#94A3B8')))

    d.add(Rect(325, 40, 125, 38, rx=3, ry=3, fillColor=colors.HexColor('#0F172A'), strokeColor=colors.HexColor('#334155'), strokeWidth=0.8))
    d.add(String(387, 64, 'Actionable Rewrites', fontName='Helvetica-Bold', fontSize=7.0, textAnchor='middle', fillColor=colors.HexColor('#FBBF24')))
    d.add(String(387, 50, 'Non-Hallucinating Bullet Tips', fontName='Helvetica', fontSize=6.0, textAnchor='middle', fillColor=colors.HexColor('#94A3B8')))

    return d

def create_ui_mockup_ingestion():
    """Figure 11.2: Dual Document Ingestion Interface (Mockup)"""
    w, h = 480, 160
    d = Drawing(w, h)
    d.add(Rect(0, 0, w, h, rx=5, ry=5, fillColor=colors.HexColor('#0F172A'), strokeColor=colors.HexColor('#334155'), strokeWidth=1))
    d.add(String(w/2, h - 14, 'DUAL DOCUMENT INGESTION & DRAG-AND-DROP INTERFACE', fontName='Helvetica-Bold', fontSize=8.5, textAnchor='middle', fillColor=colors.HexColor('#38BDF8')))

    # Left Box: Resume Uploader
    d.add(Rect(15, 15, 220, 125, rx=4, ry=4, fillColor=colors.HexColor('#1E293B'), strokeColor=colors.HexColor('#3B82F6'), strokeWidth=1))
    d.add(String(125, 126, 'Candidate Resume / CV Ingestion', fontName='Helvetica-Bold', fontSize=7.5, textAnchor='middle', fillColor=colors.HexColor('#93C5FD')))
    d.add(Rect(30, 45, 190, 65, rx=3, ry=3, fillColor=colors.HexColor('#0F172A'), strokeColor=colors.HexColor('#60A5FA'), strokeWidth=1))
    d.add(String(125, 88, 'Drag & Drop Resume File Here', fontName='Helvetica-Bold', fontSize=7.0, textAnchor='middle', fillColor=colors.HexColor('#E2E8F0')))
    d.add(String(125, 75, 'Supports PDF, DOCX, TXT (Max 5MB)', fontName='Helvetica', fontSize=6.2, textAnchor='middle', fillColor=colors.HexColor('#94A3B8')))
    d.add(Rect(80, 52, 90, 14, rx=2, ry=2, fillColor=colors.HexColor('#2563EB'), strokeColor=colors.HexColor('#1D4ED8')))
    d.add(String(125, 57, 'Browse File / Paste Text', fontName='Helvetica-Bold', fontSize=6.0, textAnchor='middle', fillColor=colors.white))
    d.add(String(125, 26, 'Detected: Senior_Backend_CV.pdf (Clean ATS layout)', fontName='Helvetica', fontSize=6.0, textAnchor='middle', fillColor=colors.HexColor('#34D399')))

    # Right Box: JD Uploader
    d.add(Rect(245, 15, 220, 125, rx=4, ry=4, fillColor=colors.HexColor('#1E293B'), strokeColor=colors.HexColor('#10B981'), strokeWidth=1))
    d.add(String(355, 126, 'Job Description (JD) Ingestion', fontName='Helvetica-Bold', fontSize=7.5, textAnchor='middle', fillColor=colors.HexColor('#A7F3D0')))
    d.add(Rect(260, 45, 190, 65, rx=3, ry=3, fillColor=colors.HexColor('#0F172A'), strokeColor=colors.HexColor('#34D399'), strokeWidth=1))
    d.add(String(355, 88, 'Paste Requisition Text or Upload JD', fontName='Helvetica-Bold', fontSize=7.0, textAnchor='middle', fillColor=colors.HexColor('#E2E8F0')))
    d.add(String(355, 75, 'Automatically extracts required & nice-to-have skills', fontName='Helvetica', fontSize=6.0, textAnchor='middle', fillColor=colors.HexColor('#94A3B8')))
    d.add(Rect(310, 52, 90, 14, rx=2, ry=2, fillColor=colors.HexColor('#059669'), strokeColor=colors.HexColor('#047857')))
    d.add(String(355, 57, 'Extract Requirements', fontName='Helvetica-Bold', fontSize=6.0, textAnchor='middle', fillColor=colors.white))
    d.add(String(355, 26, 'Extracted: 8 Required Skills, 4 Preferred Skills', fontName='Helvetica', fontSize=6.0, textAnchor='middle', fillColor=colors.HexColor('#38BDF8')))

    return d

def create_ui_mockup_weights_modal():
    """Figure 11.3: Interactive Scoring Weights Configuration Modal (Mockup)"""
    w, h = 480, 175
    d = Drawing(w, h)
    d.add(Rect(0, 0, w, h, rx=5, ry=5, fillColor=colors.HexColor('#0F172A'), strokeColor=colors.HexColor('#334155'), strokeWidth=1))
    
    # Modal Box
    d.add(Rect(25, 10, 430, 155, rx=5, ry=5, fillColor=colors.HexColor('#1E293B'), strokeColor=colors.HexColor('#3B82F6'), strokeWidth=1.2))
    d.add(String(40, 148, 'Customize Scoring Weight Allocation', fontName='Helvetica-Bold', fontSize=9, fillColor=colors.HexColor('#F8FAFC')))
    d.add(String(40, 136, 'Adjust category importance. Weights are automatically normalized to sum to 100%.', fontName='Helvetica', fontSize=6.5, fillColor=colors.HexColor('#94A3B8')))

    # Slider Rows
    slider_rows = [
        ('Skills Match Weight', '35%', 0.35, colors.HexColor('#3B82F6')),
        ('Work Experience Weight', '20%', 0.20, colors.HexColor('#6366F1')),
        ('Responsibilities Weight', '15%', 0.15, colors.HexColor('#8B5CF6')),
        ('Education & Certs Weight', '10%', 0.10, colors.HexColor('#10B981')),
        ('Projects & Portfolio Weight', '10%', 0.10, colors.HexColor('#06B6D4')),
        ('Soft Skills & ATS Quality', '10%', 0.10, colors.HexColor('#F59E0B')),
    ]

    cur_y = 118
    for name, pct_str, frac, col in slider_rows:
        d.add(String(40, cur_y, name, fontName='Helvetica', fontSize=6.2, fillColor=colors.HexColor('#E2E8F0')))
        d.add(String(220, cur_y, pct_str, fontName='Helvetica-Bold', fontSize=6.2, fillColor=col))
        
        # Track
        d.add(Rect(245, cur_y + 1, 150, 4, rx=2, ry=2, fillColor=colors.HexColor('#0F172A'), strokeColor=colors.HexColor('#334155')))
        # Fill
        d.add(Rect(245, cur_y + 1, 150 * frac * 2, 4, rx=2, ry=2, fillColor=col, strokeColor=col))
        # Thumb
        d.add(Circle(245 + 150 * frac * 2, cur_y + 3, 4, fillColor=colors.white, strokeColor=col, strokeWidth=1))
        cur_y -= 16

    # Action Buttons
    d.add(Rect(275, 16, 80, 16, rx=3, ry=3, fillColor=colors.HexColor('#334155'), strokeColor=colors.HexColor('#475569')))
    d.add(String(315, 21, 'Reset to Default', fontName='Helvetica', fontSize=6.0, textAnchor='middle', fillColor=colors.HexColor('#CBD5E1')))
    d.add(Rect(365, 16, 80, 16, rx=3, ry=3, fillColor=colors.HexColor('#2563EB'), strokeColor=colors.HexColor('#1D4ED8')))
    d.add(String(405, 21, 'Apply Weights', fontName='Helvetica-Bold', fontSize=6.0, textAnchor='middle', fillColor=colors.white))

    return d

def create_ui_mockup_skill_matrix():
    """Figure 11.5: Semantic Skill & Keyword Analysis Matrix (Mockup)"""
    w, h = 480, 165
    d = Drawing(w, h)
    d.add(Rect(0, 0, w, h, rx=5, ry=5, fillColor=colors.HexColor('#0F172A'), strokeColor=colors.HexColor('#334155'), strokeWidth=1))
    
    # Title
    d.add(String(15, h - 16, 'Semantic Keyword & Skill Alignment Matrix', fontName='Helvetica-Bold', fontSize=8.5, fillColor=colors.HexColor('#38BDF8')))
    
    # Section 1: Strong Matches
    d.add(Rect(15, h - 58, 450, 36, rx=3, ry=3, fillColor=colors.HexColor('#1E293B'), strokeColor=colors.HexColor('#059669'), strokeWidth=0.8))
    d.add(String(25, h - 30, '🟢 Strong Matches (Exact Keywords & Canonical Synonyms):', fontName='Helvetica-Bold', fontSize=6.8, fillColor=colors.HexColor('#34D399')))
    tags_strong = [('Java', 25), ('Spring Boot', 60), ('Docker', 125), ('PostgreSQL (syn: Postgres)', 170), ('REST APIs', 290)]
    for tag_name, x_pos in tags_strong:
        tag_w = len(tag_name) * 4.5 + 10
        d.add(Rect(x_pos, h - 52, tag_w, 14, rx=2, ry=2, fillColor=colors.HexColor('#064E3B'), strokeColor=colors.HexColor('#10B981')))
        d.add(String(x_pos + tag_w/2, h - 43, tag_name, fontName='Helvetica-Bold', fontSize=5.8, textAnchor='middle', fillColor=colors.HexColor('#A7F3D0')))

    # Section 2: Partial Sibling Matches
    d.add(Rect(15, h - 105, 450, 42, rx=3, ry=3, fillColor=colors.HexColor('#1E293B'), strokeColor=colors.HexColor('#D97706'), strokeWidth=0.8))
    d.add(String(25, h - 74, '🟡 Partial / Sibling Matches (Contextually Related Technologies):', fontName='Helvetica-Bold', fontSize=6.8, fillColor=colors.HexColor('#FBBF24')))
    d.add(Rect(25, h - 98, 160, 16, rx=2, ry=2, fillColor=colors.HexColor('#78350F'), strokeColor=colors.HexColor('#F59E0B')))
    d.add(String(105, h - 88, 'Kafka (Resume evidence: RabbitMQ)', fontName='Helvetica-Bold', fontSize=5.8, textAnchor='middle', fillColor=colors.HexColor('#FEF08A')))
    d.add(String(200, h - 90, 'Explanation: Message queuing background demonstrated; streaming Kafka usage not explicit.', fontName='Helvetica', fontSize=5.6, fillColor=colors.HexColor('#CBD5E1')))

    # Section 3: Missing Skills
    d.add(Rect(15, 8, 450, 46, rx=3, ry=3, fillColor=colors.HexColor('#1E293B'), strokeColor=colors.HexColor('#DC2626'), strokeWidth=0.8))
    d.add(String(25, 42, '🔴 Missing Competencies & Requirements (Gaps):', fontName='Helvetica-Bold', fontSize=6.8, fillColor=colors.HexColor('#F87171')))
    d.add(Rect(25, 16, 110, 16, rx=2, ry=2, fillColor=colors.HexColor('#7F1D1D'), strokeColor=colors.HexColor('#EF4444')))
    d.add(String(80, 26, 'Kubernetes (Required - Critical)', fontName='Helvetica-Bold', fontSize=5.8, textAnchor='middle', fillColor=colors.HexColor('#FECACA')))
    d.add(Rect(145, 16, 105, 16, rx=2, ry=2, fillColor=colors.HexColor('#7F1D1D'), strokeColor=colors.HexColor('#EF4444')))
    d.add(String(197, 26, 'Terraform (Preferred - Medium)', fontName='Helvetica-Bold', fontSize=5.8, textAnchor='middle', fillColor=colors.HexColor('#FECACA')))

    return d

def create_ui_mockup_experience_gap():
    """Figure 11.6: Granular Experience Gap & Evidence Matrix (Mockup)"""
    w, h = 480, 155
    d = Drawing(w, h)
    d.add(Rect(0, 0, w, h, rx=5, ry=5, fillColor=colors.HexColor('#0F172A'), strokeColor=colors.HexColor('#334155'), strokeWidth=1))
    
    d.add(String(15, h - 16, 'Granular Requisition vs Resume Evidence Alignment Table', fontName='Helvetica-Bold', fontSize=8.5, fillColor=colors.HexColor('#38BDF8')))
    
    # Table Header
    d.add(Rect(15, h - 38, 450, 18, rx=2, ry=2, fillColor=colors.HexColor('#1E3A8A'), strokeColor=colors.HexColor('#1E3A8A')))
    d.add(String(25, h - 27, 'Job Description Requirement', fontName='Helvetica-Bold', fontSize=6.5, fillColor=colors.white))
    d.add(String(190, h - 27, 'Extracted Resume Sentence Evidence', fontName='Helvetica-Bold', fontSize=6.5, fillColor=colors.white))
    d.add(String(380, h - 27, 'Status Badge', fontName='Helvetica-Bold', fontSize=6.5, fillColor=colors.white))

    # Row 1
    d.add(Rect(15, h - 72, 450, 32, rx=1, ry=1, fillColor=colors.HexColor('#1E293B'), strokeColor=colors.HexColor('#334155'), strokeWidth=0.5))
    d.add(String(25, h - 52, '5+ years backend microservices', fontName='Helvetica-Bold', fontSize=6.0, fillColor=colors.HexColor('#E2E8F0')))
    d.add(String(25, h - 62, 'architecture using Java / Spring Boot', fontName='Helvetica', fontSize=5.8, fillColor=colors.HexColor('#94A3B8')))
    d.add(String(190, h - 52, '"Architected Java Spring Boot microservices handling', fontName='Helvetica', fontSize=5.8, fillColor=colors.HexColor('#CBD5E1')))
    d.add(String(190, h - 62, ' 15M daily requests at CloudScale Systems (2021-Present)"', fontName='Helvetica', fontSize=5.8, fillColor=colors.HexColor('#CBD5E1')))
    d.add(Rect(380, h - 60, 70, 14, rx=2, ry=2, fillColor=colors.HexColor('#064E3B'), strokeColor=colors.HexColor('#059669')))
    d.add(String(415, h - 52, '🟢 Strong Match', fontName='Helvetica-Bold', fontSize=5.8, textAnchor='middle', fillColor=colors.HexColor('#6EE7B7')))

    # Row 2
    d.add(Rect(15, h - 108, 450, 34, rx=1, ry=1, fillColor=colors.HexColor('#1E293B'), strokeColor=colors.HexColor('#334155'), strokeWidth=0.5))
    d.add(String(25, h - 88, 'Event-driven streaming pipeline', fontName='Helvetica-Bold', fontSize=6.0, fillColor=colors.HexColor('#E2E8F0')))
    d.add(String(25, h - 98, 'architecture using Apache Kafka', fontName='Helvetica', fontSize=5.8, fillColor=colors.HexColor('#94A3B8')))
    d.add(String(190, h - 88, '"Developed asynchronous messaging workers using', fontName='Helvetica', fontSize=5.8, fillColor=colors.HexColor('#CBD5E1')))
    d.add(String(190, h - 98, ' RabbitMQ and Python at DataFlow Corp (2019-2021)"', fontName='Helvetica', fontSize=5.8, fillColor=colors.HexColor('#CBD5E1')))
    d.add(Rect(380, h - 96, 70, 14, rx=2, ry=2, fillColor=colors.HexColor('#78350F'), strokeColor=colors.HexColor('#D97706')))
    d.add(String(415, h - 88, '🟡 Sibling Tech', fontName='Helvetica-Bold', fontSize=5.8, textAnchor='middle', fillColor=colors.HexColor('#FDE047')))

    # Row 3
    d.add(Rect(15, 8, 450, 30, rx=1, ry=1, fillColor=colors.HexColor('#1E293B'), strokeColor=colors.HexColor('#334155'), strokeWidth=0.5))
    d.add(String(25, 26, 'Production Kubernetes cluster', fontName='Helvetica-Bold', fontSize=6.0, fillColor=colors.HexColor('#E2E8F0')))
    d.add(String(25, 16, 'orchestration and Helm charts', fontName='Helvetica', fontSize=5.8, fillColor=colors.HexColor('#94A3B8')))
    d.add(String(190, 21, 'No direct textual evidence identified in candidate resume.', fontName='Helvetica-Oblique', fontSize=5.8, fillColor=colors.HexColor('#F87171')))
    d.add(Rect(380, 16, 70, 14, rx=2, ry=2, fillColor=colors.HexColor('#7F1D1D'), strokeColor=colors.HexColor('#DC2626')))
    d.add(String(415, 24, '🔴 Missing', fontName='Helvetica-Bold', fontSize=5.8, textAnchor='middle', fillColor=colors.HexColor('#FCA5A5')))

    return d

def create_ui_mockup_ats_audit():
    """Figure 11.7: 12-Point ATS Audit & Hazard Diagnostic Card (Mockup)"""
    w, h = 480, 155
    d = Drawing(w, h)
    d.add(Rect(0, 0, w, h, rx=5, ry=5, fillColor=colors.HexColor('#0F172A'), strokeColor=colors.HexColor('#334155'), strokeWidth=1))
    
    # Title & Gauge
    d.add(String(15, h - 16, '12-Point ATS Structural Compliance Audit & Hazard Diagnostics', fontName='Helvetica-Bold', fontSize=8.5, fillColor=colors.HexColor('#38BDF8')))
    
    # Score pill
    d.add(Rect(375, h - 23, 90, 16, rx=3, ry=3, fillColor=colors.HexColor('#064E3B'), strokeColor=colors.HexColor('#059669')))
    d.add(String(420, h - 14, 'ATS Score: 92/100', fontName='Helvetica-Bold', fontSize=6.5, textAnchor='middle', fillColor=colors.HexColor('#6EE7B7')))

    # Passed Rules (Left)
    d.add(Rect(15, 10, 220, 120, rx=3, ry=3, fillColor=colors.HexColor('#1E293B'), strokeColor=colors.HexColor('#059669'), strokeWidth=0.8))
    d.add(String(25, 118, 'Passed Compliance Checks (11 Rules):', fontName='Helvetica-Bold', fontSize=7.0, fillColor=colors.HexColor('#34D399')))
    passed_items = [
        '✓ Standard Section Headings Verified',
        '✓ Contact Email Address Extractable',
        '✓ Valid Telephone Number Format Found',
        '✓ Clean Single-Column Top-to-Bottom Layout',
        '✓ Chronological Employment Date Consistency',
        '✓ No Unextractable Text Frames Detected'
    ]
    p_y = 104
    for p_text in passed_items:
        d.add(String(25, p_y, p_text, fontName='Helvetica', fontSize=6.0, fillColor=colors.HexColor('#CBD5E1')))
        p_y -= 14

    # Warning / Action Tip (Right)
    d.add(Rect(245, 10, 220, 120, rx=3, ry=3, fillColor=colors.HexColor('#1E293B'), strokeColor=colors.HexColor('#D97706'), strokeWidth=0.8))
    d.add(String(255, 118, 'Detected Hazard & Remediation Tip:', fontName='Helvetica-Bold', fontSize=7.0, fillColor=colors.HexColor('#FBBF24')))
    d.add(Rect(255, 68, 200, 42, rx=2, ry=2, fillColor=colors.HexColor('#78350F'), strokeColor=colors.HexColor('#F59E0B')))
    d.add(String(260, 98, 'Rule R06 Warning: Embedded Table Hazard', fontName='Helvetica-Bold', fontSize=6.0, fillColor=colors.HexColor('#FEF08A')))
    d.add(String(260, 88, 'Found: 1 nested table structure in skills block.', fontName='Helvetica', fontSize=5.6, fillColor=colors.HexColor('#FEF9C3')))
    d.add(String(260, 78, 'Fix Tip: Replace grid borders with tabbed text.', fontName='Helvetica-Oblique', fontSize=5.6, fillColor=colors.white))
    
    d.add(String(255, 48, 'Keyword Density Audit: 4.2% (Healthy Range)', fontName='Helvetica-Bold', fontSize=6.2, fillColor=colors.HexColor('#38BDF8')))
    d.add(String(255, 36, 'No keyword stuffing or hidden fonts detected.', fontName='Helvetica', fontSize=5.8, fillColor=colors.HexColor('#94A3B8')))

    return d

def create_ui_mockup_recommendations():
    """Figure 11.8: Actionable Improvement Suggestions and Final Assessment (Mockup)"""
    w, h = 480, 165
    d = Drawing(w, h)
    d.add(Rect(0, 0, w, h, rx=5, ry=5, fillColor=colors.HexColor('#0F172A'), strokeColor=colors.HexColor('#334155'), strokeWidth=1))
    
    d.add(String(15, h - 16, 'Actionable Resume Improvement Suggestions & Final Readiness Verdict', fontName='Helvetica-Bold', fontSize=8.5, fillColor=colors.HexColor('#38BDF8')))
    
    # Left: High-Impact Bullet Rewrites
    d.add(Rect(15, 10, 240, 132, rx=3, ry=3, fillColor=colors.HexColor('#1E293B'), strokeColor=colors.HexColor('#3B82F6'), strokeWidth=0.8))
    d.add(String(25, 130, 'Targeted Action-Metric Bullet Rewrite:', fontName='Helvetica-Bold', fontSize=7.0, fillColor=colors.HexColor('#93C5FD')))
    
    d.add(String(25, 114, 'Original Passive Phrasing:', fontName='Helvetica-Bold', fontSize=6.0, fillColor=colors.HexColor('#F87171')))
    d.add(String(25, 104, '"Worked on Spring Boot APIs and fixed PostgreSQL database queries."', fontName='Helvetica-Oblique', fontSize=5.6, fillColor=colors.HexColor('#CBD5E1')))

    d.add(String(25, 88, 'Recommended High-Impact Quantified Rewrite:', fontName='Helvetica-Bold', fontSize=6.0, fillColor=colors.HexColor('#4ADE80')))
    d.add(String(25, 78, '"Architected high-throughput Spring Boot REST microservices and', fontName='Helvetica', fontSize=5.6, fillColor=colors.HexColor('#F8FAFC')))
    d.add(String(25, 69, ' optimized PostgreSQL indexing, reducing P99 latency by [X%]', fontName='Helvetica', fontSize=5.6, fillColor=colors.HexColor('#F8FAFC')))
    d.add(String(25, 60, ' across [X,000,000+] daily active user requests."', fontName='Helvetica', fontSize=5.6, fillColor=colors.HexColor('#F8FAFC')))

    d.add(Rect(25, 18, 220, 32, rx=2, ry=2, fillColor=colors.HexColor('#0F172A'), strokeColor=colors.HexColor('#F59E0B'), strokeWidth=0.6))
    d.add(String(135, 38, 'Anti-Hallucination Guardrail Principle:', fontName='Helvetica-Bold', fontSize=5.6, textAnchor='middle', fillColor=colors.HexColor('#FCD34D')))
    d.add(String(135, 26, 'Only incorporate suggested metrics if you genuinely achieved them.', fontName='Helvetica', fontSize=5.2, textAnchor='middle', fillColor=colors.HexColor('#E2E8F0')))

    # Right: Final Assessment Banner
    d.add(Rect(265, 10, 200, 132, rx=3, ry=3, fillColor=colors.HexColor('#1E293B'), strokeColor=colors.HexColor('#10B981'), strokeWidth=0.8))
    d.add(String(275, 130, 'Final Application Readiness Verdict:', fontName='Helvetica-Bold', fontSize=7.0, fillColor=colors.HexColor('#34D399')))
    
    d.add(Rect(275, 96, 180, 24, rx=2, ry=2, fillColor=colors.HexColor('#064E3B'), strokeColor=colors.HexColor('#059669')))
    d.add(String(365, 108, 'READY TO APPLY (With Minor Edits)', fontName='Helvetica-Bold', fontSize=6.5, textAnchor='middle', fillColor=colors.HexColor('#A7F3D0')))

    d.add(String(275, 84, 'Pre-Application Action Checklist:', fontName='Helvetica-Bold', fontSize=6.2, fillColor=colors.HexColor('#E2E8F0')))
    d.add(String(275, 72, '1. Clarify Kubernetes cluster exposure.', fontName='Helvetica', fontSize=5.6, fillColor=colors.HexColor('#CBD5E1')))
    d.add(String(275, 60, '2. Quantify PostgreSQL latency metrics.', fontName='Helvetica', fontSize=5.6, fillColor=colors.HexColor('#CBD5E1')))
    d.add(String(275, 48, '3. Eliminate table borders in skills section.', fontName='Helvetica', fontSize=5.6, fillColor=colors.HexColor('#CBD5E1')))
    d.add(String(275, 36, '4. Highlight AWS S3 object storage depth.', fontName='Helvetica', fontSize=5.6, fillColor=colors.HexColor('#CBD5E1')))

    return d

