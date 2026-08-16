import re
import io
from typing import Dict, List, Any, Tuple, Optional
from app.schemas.matcher_schemas import JDStructure


class JDParser:
    """
    Parser for Job Descriptions.
    Extracts structured fields: Job Title, Required vs Preferred Skills,
    Experience requirements, Education, Responsibilities, and Technical Stack.
    """

    KNOWN_LANGUAGES = [
        "python", "java", "javascript", "typescript", "c++", "c#", "golang", "go", "ruby",
        "rust", "php", "swift", "kotlin", "scala", "r", "c", "bash", "shell", "sql"
    ]
    KNOWN_FRAMEWORKS = [
        "react", "angular", "vue", "next.js", "nextjs", "node.js", "nodejs", "express",
        "spring", "spring boot", "django", "fastapi", "flask", "asp.net", "dotnet", ".net",
        "ruby on rails", "nestjs", "laravel", "tailwind", "bootstrap", "graphql", "rest apis",
        "rest api", "microservices", "hibernate", "junit", "mockito"
    ]
    KNOWN_CLOUDS = [
        "aws", "amazon web services", "azure", "gcp", "google cloud", "google cloud platform",
        "aws s3", "aws lambda", "ec2", "rds", "cloudformation", "dynamodb", "serverless"
    ]
    KNOWN_DATABASES = [
        "postgresql", "postgres", "mysql", "mongodb", "redis", "elasticsearch", "cassandra",
        "dynamodb", "oracle", "sql server", "sqlite", "neo4j", "mariadb", "snowflake", "bigquery"
    ]
    KNOWN_TOOLS = [
        "docker", "kubernetes", "k8s", "terraform", "ansible", "jenkins", "gitlab ci", "github actions",
        "git", "linux", "jira", "kafka", "rabbitmq", "prometheus", "grafana", "helm", "ci/cd", "maven"
    ]
    KNOWN_SOFT_SKILLS = [
        "communication", "leadership", "mentoring", "teamwork", "collaboration", "problem solving",
        "critical thinking", "agile", "scrum", "stakeholder management", "adaptability", "ownership"
    ]

    @classmethod
    def parse_file(cls, file_bytes: bytes, filename: str, file_type: Optional[str] = None) -> Tuple[str, JDStructure]:
        raw_text = ""
        ext = filename.lower().split(".")[-1] if filename else ""
        if file_type:
            file_type = file_type.lower()
        else:
            file_type = ext

        if "pdf" in file_type or ext == "pdf":
            raw_text = cls._extract_pdf(file_bytes)
        elif "docx" in file_type or ext == "docx" or "word" in file_type:
            raw_text = cls._extract_docx(file_bytes)
        else:
            raw_text = cls._extract_txt(file_bytes)

        if not raw_text.strip():
            raise ValueError("Extracted Job Description text is empty or unreadable.")

        structured = cls.parse_raw_text(raw_text)
        return raw_text, structured

    @classmethod
    def _extract_pdf(cls, file_bytes: bytes) -> str:
        try:
            from pypdf import PdfReader
            reader = PdfReader(io.BytesIO(file_bytes))
            return "\n".join(page.extract_text() or "" for page in reader.pages).strip()
        except Exception as e:
            raise ValueError(f"Failed to parse JD PDF: {str(e)}")

    @classmethod
    def _extract_docx(cls, file_bytes: bytes) -> str:
        try:
            import docx
            doc = docx.Document(io.BytesIO(file_bytes))
            return "\n".join(p.text for p in doc.paragraphs if p.text.strip()).strip()
        except Exception as e:
            raise ValueError(f"Failed to parse JD DOCX: {str(e)}")

    @classmethod
    def _extract_txt(cls, file_bytes: bytes) -> str:
        for enc in ["utf-8", "latin-1", "cp1252"]:
            try:
                return file_bytes.decode(enc).strip()
            except UnicodeDecodeError:
                continue
        return file_bytes.decode("utf-8", errors="ignore").strip()

    @classmethod
    def parse_raw_text(cls, text: str) -> JDStructure:
        lines = [l.strip() for l in text.splitlines() if l.strip()]
        
        job_title = cls._extract_title(lines, text)
        years_exp = cls._extract_years_experience(text)
        req_skills, pref_skills = cls._extract_required_and_preferred(text)
        tech_entities = cls._extract_tech_entities(text)
        responsibilities = cls._extract_responsibilities(text)
        education = cls._extract_education(text)
        certifications = cls._extract_certifications(text)
        soft_skills = cls._extract_soft_skills(text)

        # Merge tech entities into required/preferred if not already present
        for skill in tech_entities["all"]:
            if skill not in req_skills and skill not in pref_skills:
                # If mentioned near 'preferred' or 'nice', put in preferred, else required
                if re.search(rf"(?:preferred|nice to have|plus|bonus|desired)[^\.\n]*{re.escape(skill)}", text, re.IGNORECASE):
                    pref_skills.append(skill)
                else:
                    req_skills.append(skill)

        return JDStructure(
            job_title=job_title,
            company_name=None,
            required_skills=list(dict.fromkeys(req_skills)),
            preferred_skills=list(dict.fromkeys(pref_skills)),
            programming_languages=tech_entities["languages"],
            frameworks=tech_entities["frameworks"],
            cloud_technologies=tech_entities["clouds"],
            databases=tech_entities["databases"],
            tools_and_devops=tech_entities["tools"],
            required_years_experience=years_exp,
            educational_requirements=education,
            certifications=certifications,
            responsibilities=responsibilities,
            domain_knowledge=[],
            soft_skills=soft_skills,
        )

    @classmethod
    def _extract_title(cls, lines: List[str], full_text: str) -> Optional[str]:
        # Check first 5 lines for common job title keywords
        title_keywords = r"(software|engineer|developer|architect|lead|manager|analyst|scientist|devops|full\s*stack|backend|frontend|qa)"
        for line in lines[:5]:
            if re.search(title_keywords, line, re.IGNORECASE) and len(line.split()) <= 7:
                return re.sub(r"^(?:job\s+title|position|role):\s*", "", line, flags=re.IGNORECASE).strip()
        
        # Regex search for Job Title: ...
        match = re.search(r"(?:job\s+title|role|position):\s*([^\n]+)", full_text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        return lines[0] if lines else "Software Professional"

    @classmethod
    def _extract_years_experience(cls, text: str) -> Optional[float]:
        # Examples: "5+ years of professional software engineering experience", "3-5 years"
        match = re.search(r"(\d+(?:\.\d+)?)\s*(?:\+|-\s*\d+)?\s*(?:to\s*\d+\s*)?years?(?:\s+of)?(?:\s+[\w\s-]{1,35})?\s+experience", text, re.IGNORECASE)
        if match:
            try:
                return float(match.group(1))
            except ValueError:
                pass
        return None

    @classmethod
    def _extract_required_and_preferred(cls, text: str) -> Tuple[List[str], List[str]]:
        required = []
        preferred = []

        # Split text into required vs preferred blocks if present
        req_pattern = r"(?:requirements(?:\s*\(must\s+have\))?|required\s+qualifications|must\s+have|minimum\s+qualifications|what\s+you['’]ll\s+need|basic\s+qualifications)[\s\S]*?(?:preferred|nice\s+to\s+have|bonus|desired|what\s+we['’]d\s+like|benefits|about\s+the\s+team|\Z)"
        pref_pattern = r"(?:preferred\s+qualifications(?:\s*\(nice\s+to\s+have\))?|nice\s+to\s+have|bonus\s+points|desired\s+skills|preferred\s+skills|plus\s+points)[\s\S]*?(?:responsibilities|requirements|benefits|about\s+us|\Z)"

        req_match = re.search(r"(?:requirements|required\s+qualifications|must\s+have|minimum\s+qualifications|what\s+you['’]ll\s+need)[^\n:]*:(.*?)(?:preferred|nice\s+to\s+have|bonus|desired|what\s+we['’]d\s+like|benefits|\Z)", text, re.IGNORECASE | re.DOTALL)
        if req_match:
            required.extend(cls._extract_bullet_items(req_match.group(1)))

        pref_match = re.search(r"(?:preferred\s+qualifications|nice\s+to\s+have|bonus\s+points|desired\s+skills|preferred\s+skills)[^\n:]*:(.*?)(?:responsibilities|requirements|benefits|about\s+us|\Z)", text, re.IGNORECASE | re.DOTALL)
        if pref_match:
            preferred.extend(cls._extract_bullet_items(pref_match.group(1)))

        return required, preferred

    @classmethod
    def _extract_bullet_items(cls, section_text: str) -> List[str]:
        items = []
        for line in section_text.splitlines():
            line_str = line.strip()
            if not line_str or len(line_str) < 3:
                continue
            if line_str.startswith(("•", "-", "*", "–")) or re.match(r"^\d+\.", line_str):
                cleaned = re.sub(r"^[•\-*–\d.]+\s*", "", line_str).strip()
                if cleaned and len(cleaned) < 120:
                    items.append(cleaned)
        return items

    @classmethod
    def _extract_tech_entities(cls, text: str) -> Dict[str, List[str]]:
        text_lower = text.lower()
        res = {
            "languages": [],
            "frameworks": [],
            "clouds": [],
            "databases": [],
            "tools": [],
            "all": []
        }

        def check_matches(kw_list):
            matched = []
            for kw in kw_list:
                # Word boundary check
                pattern = rf"\b{re.escape(kw)}\b"
                if re.search(pattern, text_lower):
                    matched.append(kw.title() if len(kw) > 3 else kw.upper())
            return matched

        res["languages"] = check_matches(cls.KNOWN_LANGUAGES)
        res["frameworks"] = check_matches(cls.KNOWN_FRAMEWORKS)
        res["clouds"] = check_matches(cls.KNOWN_CLOUDS)
        res["databases"] = check_matches(cls.KNOWN_DATABASES)
        res["tools"] = check_matches(cls.KNOWN_TOOLS)
        res["all"] = res["languages"] + res["frameworks"] + res["clouds"] + res["databases"] + res["tools"]
        return res

    @classmethod
    def _extract_responsibilities(cls, text: str) -> List[str]:
        pattern = r"(?:responsibilities|duties|what\s+you['’]ll\s+do|key\s+responsibilities|role\s+overview)(.*?)(?:requirements|qualifications|skills|benefits|\Z)"
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if match:
            return cls._extract_bullet_items(match.group(1))
        return []

    @classmethod
    def _extract_education(cls, text: str) -> List[str]:
        edu = []
        edu_matches = re.findall(r"([^\.\n]*(?:bachelor|master|phd|b\.s|m\.s|degree|computer\s+science)[^\.\n]*)", text, re.IGNORECASE)
        for m in edu_matches:
            if len(m.strip()) < 100:
                edu.append(m.strip())
        return list(dict.fromkeys(edu))

    @classmethod
    def _extract_certifications(cls, text: str) -> List[str]:
        certs = []
        cert_matches = re.findall(r"([^\.\n]*(?:certified|certification|aws\s+certified|cka|pmp|cissp)[^\.\n]*)", text, re.IGNORECASE)
        for m in cert_matches:
            if len(m.strip()) < 100:
                certs.append(m.strip())
        return list(dict.fromkeys(certs))

    @classmethod
    def _extract_soft_skills(cls, text: str) -> List[str]:
        soft = []
        text_lower = text.lower()
        for s in cls.KNOWN_SOFT_SKILLS:
            if re.search(rf"\b{re.escape(s)}\b", text_lower):
                soft.append(s.title())
        return soft
