# MatchCraft AI — AI-Powered Resume & Job Description Matcher

A modern, production-grade semantic web application that analyzes a candidate's CV/resume against a Job Description (JD), estimates ATS shortlist probability, identifies missing technical keywords with explainable reasoning, audits ATS compatibility, and generates actionable, non-hallucinating CV improvement suggestions.

---

## Key Capabilities

1. **Semantic Skill & Technology Matcher**:
   - Differentiates between **Exact Matches** (e.g., *Java*, *Docker*), **Synonyms** (e.g., *Amazon Web Services* ↔ *AWS*, *PostgreSQL* ↔ *Postgres*), **Partial Sibling Technologies** (e.g., *Kafka* required vs. *RabbitMQ* in resume with explicit reasoning), and **Missing Keywords**.
   - Distinguishes **Required (Must-Have)** vs. **Preferred (Nice-to-Have)** qualifications.

2. **Transparent Scoring Engine & Configurable Weights**:
   - **Skill & Keyword Match** (35%)
   - **Experience & Seniority Match** (20%)
   - **Responsibilities & Domain Match** (15%)
   - **Education & Certifications** (10%)
   - **Projects & Achievements** (10%)
   - **Soft Skills & Methodologies** (5%)
   - **Resume Quality & ATS Compatibility** (5%)
   - Weights are fully configurable in real-time via the interactive UI weights panel.

3. **Estimated ATS Screening Probability**:
   - Computes an estimated shortlist probability (0–100%) paired with a prominent statistical disclosure explaining non-deterministic real-world variables (applicant volume, recruiter keyword filters, hiring quotas, interview performance, work visa requirements).

4. **Experience Gap Matrix & Side-by-Side View**:
   - Granular tabular breakdown mapping each Job Description requirement directly to extracted Resume Evidence.
   - Side-by-side split screen for line-by-line inspection.

5. **12-Point ATS Compatibility Audit**:
   - Evaluates section headings, contact information extractability, chronological date consistency, single-column layout, and keyword distribution across work experience vs. summary.

6. **Actionable Rewrites & Anti-Hallucination Guardrails**:
   - High-impact bullet point rewrites using metric placeholders (`[X% improvement]`, `[X,000+ users]`) without fabricating fake numbers or employers.
   - Explicit warnings: *"Only add a keyword if you genuinely have experience with it."*

7. **1-Click Realistic Demo**:
   - Instantly loads a realistic Senior Software Engineer CV (Java, Spring Boot, REST APIs, RabbitMQ, Docker, AWS S3, PostgreSQL) vs. Cloud Platforms JD (requiring Kafka, Kubernetes, Terraform).

8. **Privacy-First Architecture**:
   - Ephemeral session processing with a **"Delete Resume"** option for immediate data purging.

---

## Technology Stack

- **Backend**: Python 3.11, FastAPI, Pydantic v2, SQLAlchemy, Uvicorn
- **Document Processing**: `pypdf`, `pdfplumber`, `python-docx`
- **AI Abstraction Layer**: Multi-provider support for Google Gemini (`gemini-2.5-flash`), OpenAI (`gpt-4o-mini`), and a built-in zero-dependency `HybridHeuristicSemanticProvider` with comprehensive technical taxonomy and synonym graph.
- **Frontend**: React 18, TypeScript, Vite, Tailwind CSS, Lucide React, SVG Radial Gauges, Axios
- **Database**: SQLite (default, migration-ready for PostgreSQL)
- **Testing**: pytest (12/12 unit and integration tests passing)

---

## Project Structure

```
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes/
│   │   │       ├── resume.py            # POST /api/resume/upload, DELETE /api/resume/{id}
│   │   │       ├── job_description.py   # POST /api/job-description/upload
│   │   │       ├── analyze.py           # POST /api/analyze, GET /api/analysis/{id}
│   │   │       ├── config_routes.py     # GET/POST /api/config/weights
│   │   │       └── sample_data.py       # GET /api/sample-data
│   │   ├── models/
│   │   │   └── schema_models.py         # SQLAlchemy ORM models
│   │   ├── parsers/
│   │   │   ├── resume_parser.py         # PDF, DOCX, TXT parser & ATS hazard detector
│   │   │   └── jd_parser.py             # Structured JD extractor
│   │   ├── schemas/
│   │   │   └── matcher_schemas.py       # Pydantic request/response schemas
│   │   ├── services/
│   │   │   ├── ats_checker.py           # 12-point ATS compliance evaluator
│   │   │   ├── llm_service.py           # Multi-provider LLM & Semantic Matcher
│   │   │   └── scoring_engine.py        # Configurable weighted scoring engine
│   │   ├── config.py                    # App settings & default weights
│   │   ├── database.py                  # SQLAlchemy engine & session maker
│   │   ├── sample_data.py               # Demo resume and JD datasets
│   │   └── main.py                      # FastAPI app entry point
│   ├── tests/
│   │   ├── test_parsers.py              # Resume & JD parser tests
│   │   ├── test_skill_matching.py       # Exact, synonym, partial, and missing tests
│   │   ├── test_scoring_engine.py       # Scoring weights & probability tests
│   │   └── test_api.py                  # Full REST API integration tests
│   ├── requirements.txt
│   └── pytest.ini
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   │   └── client.ts                # Axios REST client
│   │   ├── components/
│   │   │   ├── Navbar.tsx               # Header, 1-Click Demo & settings toggles
│   │   │   ├── ResumeUploader.tsx       # Drag & drop PDF/DOCX/TXT + paste + preview
│   │   │   ├── JDUploader.tsx           # JD upload/paste + requirements preview
│   │   │   ├── ScoreOverviewCards.tsx   # Radial score gauges & metric KPIs
│   │   │   ├── KeywordAnalysisTab.tsx   # Filterable Strong/Partial/Missing skills
│   │   │   ├── ExperienceGapTable.tsx   # Requirements vs Evidence matrix table
│   │   │   ├── SideBySideView.tsx       # Split comparison view
│   │   │   ├── ATSCompatibilityCard.tsx # 0-100 ATS score & fix recommendations
│   │   │   ├── StrengthsAndGaps.tsx     # Strengths & prioritized gaps
│   │   │   ├── ImprovementSuggestions.tsx # Before & after bullet rewrites
│   │   │   ├── FinalAssessmentBanner.tsx# Final verdict & application checklist
│   │   │   ├── WeightConfigModal.tsx    # Live scoring weight adjustments
│   │   │   ├── PrivacyNoticeModal.tsx   # Privacy policy & data deletion info
│   │   │   └── ExportModal.tsx          # Export JSON & Print to PDF
│   │   ├── types/
│   │   │   └── index.ts                 # TypeScript interfaces
│   │   ├── App.tsx                      # Main app orchestrator
│   │   ├── index.css                    # Tailwind design tokens & styles
│   │   └── main.tsx                     # React entrypoint
│   ├── package.json
│   ├── vite.config.ts
│   └── tailwind.config.js
├── .env.example
└── README.md
```

---

## Getting Started (Local Development)

### 1. Prerequisites
- **Python**: 3.10+ (tested on Python 3.11)
- **Node.js**: 18+ (tested on Node v24 LTS)
- **npm**: 9+

---

### 2. Backend Setup

```bash
cd backend

# Create virtual environment (Windows)
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# (Optional) Set your Gemini API key in .env or environment
# If omitted, the built-in offline Semantic Engine will be used automatically.
set GEMINI_API_KEY=your_api_key_here

# Run backend test suite
pytest tests -v

# Start FastAPI development server
uvicorn app.main:app --reload --port 8000
```

The Backend API will be live at `http://localhost:8000`.
Interactive Swagger API documentation: `http://localhost:8000/docs`.

---

### 3. Frontend Setup

In a separate terminal:

```bash
cd frontend

# Install npm dependencies
npm install

# Start Vite development server
npm run dev
```

Open `http://localhost:5173` in your browser.

---

## Running Tests

Run the backend test suite covering all parsers, skill matching rules, scoring weights, and API endpoints:

```bash
cd backend
venv\Scripts\activate
pytest tests -v
```

---

## Production Deployment

### 1. Build the Frontend
```bash
cd frontend
npm run build
```
The optimized production bundle will be generated in `frontend/dist`.

### 2. Run Backend with Production Server
```bash
cd backend
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

### 3. Containerization (Optional Dockerfile)
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY backend/ .
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## API Endpoints Reference

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/resume/upload` | Upload PDF/DOCX/TXT or paste text; returns structured sections & preliminary ATS score |
| `DELETE`| `/api/resume/{id}` | Permanently purges candidate resume and associated analyses (Privacy) |
| `POST` | `/api/job-description/upload` | Upload PDF/DOCX/TXT or paste JD text; returns structured requirements |
| `POST` | `/api/analyze` | Executes semantic matching, scoring, ATS audit, and recommendation generation |
| `GET` | `/api/analysis/{id}` | Retrieves historical analysis report |
| `GET` | `/api/sample-data` | Returns pre-configured realistic Software Engineer CV & JD for 1-click demo |
| `GET` | `/api/config/weights` | Retrieves configurable category scoring weights |
| `POST` | `/api/config/weights` | Updates scoring weights configuration |
| `GET` | `/api/health` | Backend health check & active LLM provider status |

---

## License

MIT License. Designed with best practices in modern web development, semantic matching, and applicant privacy.
