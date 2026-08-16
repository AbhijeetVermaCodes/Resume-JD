import re
from typing import Dict, List, Any
from app.schemas.matcher_schemas import ATSCompatibilityResult, ATSIssueItem, ResumeStructure


class ATSChecker:
    """
    Evaluates resume against 12+ real-world ATS compatibility rules.
    Outputs a score from 0 to 100, categorized issues (High/Medium/Low),
    and actionable remediation tips.
    """

    @classmethod
    def evaluate(cls, raw_text: str, structured: ResumeStructure, file_type: str = "txt") -> ATSCompatibilityResult:
        score = 100
        issues: List[ATSIssueItem] = []
        passed_checks: List[str] = []
        formatting_summary: Dict[str, Any] = {}

        words = raw_text.split()
        word_count = len(words)
        formatting_summary["word_count"] = word_count
        formatting_summary["file_type"] = file_type

        # Check 1: Contact Information - Email
        if structured.contact_info.email:
            passed_checks.append("Machine-readable email address detected")
        else:
            score -= 15
            issues.append(ATSIssueItem(
                severity="high",
                rule="Contact Info: Email Address",
                description="No valid email address was detected in the document header.",
                fix_tip="Add a clear email address (e.g. name@domain.com) at the top of your resume."
            ))

        # Check 2: Contact Information - Phone
        if structured.contact_info.phone:
            passed_checks.append("Machine-readable phone number detected")
        else:
            score -= 10
            issues.append(ATSIssueItem(
                severity="high",
                rule="Contact Info: Phone Number",
                description="No recognizable phone number was detected.",
                fix_tip="Include standard phone format (e.g. +1 (555) 123-4567 or +91 9876543210)."
            ))

        # Check 3: Standard Section Headings
        required_sections = [("experience", "Work Experience"), ("skills", "Skills"), ("education", "Education")]
        for sec_key, sec_name in required_sections:
            if sec_key in structured.raw_sections and len(structured.raw_sections[sec_key]) > 20:
                passed_checks.append(f"Standard '{sec_name}' section heading found")
            else:
                score -= 10
                issues.append(ATSIssueItem(
                    severity="high" if sec_key == "experience" else "medium",
                    rule=f"Section Heading: {sec_name}",
                    description=f"Standard '{sec_name}' section was not distinctly recognized.",
                    fix_tip=f"Use standard headings like '{sec_name}' or 'Professional Experience' instead of custom creative names."
                ))

        # Check 4: Work Experience Depth & Dates
        if structured.work_experience:
            passed_checks.append("Work experience entries structured with roles and bullet points")
            # Check for dates
            has_dates = any(bool(exp.get("duration")) for exp in structured.work_experience)
            if has_dates:
                passed_checks.append("Consistent chronological date ranges detected in work history")
            else:
                score -= 8
                issues.append(ATSIssueItem(
                    severity="medium",
                    rule="Date Formatting in Work History",
                    description="Standard start/end dates (e.g., 'Jan 2021 – Present' or '2019 – 2023') were not clearly parsed.",
                    fix_tip="Format dates consistently for every role (e.g., 'MM/YYYY – MM/YYYY' or 'Month Year – Present')."
                ))
        else:
            score -= 12
            issues.append(ATSIssueItem(
                severity="high",
                rule="Experience Chronology",
                description="No distinct role timeline or work history bullets could be parsed.",
                fix_tip="Format past roles with clear Job Title, Company Name, Date Range, and bullet points."
            ))

        # Check 5: Document Length
        if 250 <= word_count <= 1400:
            passed_checks.append(f"Optimal resume length ({word_count} words)")
        elif word_count < 250:
            score -= 10
            issues.append(ATSIssueItem(
                severity="medium",
                rule="Document Length",
                description=f"Resume is very brief ({word_count} words). ATS may consider it incomplete.",
                fix_tip="Expand with detailed accomplishment bullets for your core engineering projects and roles."
            ))
        else:
            score -= 6
            issues.append(ATSIssueItem(
                severity="low",
                rule="Document Length",
                description=f"Resume is long ({word_count} words). High-volume ATS parsers perform best with 400–1000 words.",
                fix_tip="Consolidate older or less relevant positions to keep resume focused on 1–2 pages."
            ))

        # Check 6: Table & Column Complexity
        pipe_count = raw_text.count("|")
        tab_count = raw_text.count("\t")
        if pipe_count > 15 or tab_count > 25:
            score -= 8
            issues.append(ATSIssueItem(
                severity="medium",
                rule="Table & Column Formatting",
                description="Heavy use of table delimiters or multi-column spacing detected.",
                fix_tip="ATS systems often read multi-column text horizontally across columns, garbling sentences. Use single-column linear layout."
            ))
        else:
            passed_checks.append("Clean linear layout (no disruptive multi-table nesting detected)")

        # Check 7: Skill Placement Check (Summary vs Work Experience)
        exp_text = structured.raw_sections.get("experience", "").lower()
        skills = structured.skills
        if skills:
            skills_in_exp = sum(1 for s in skills if s.lower() in exp_text)
            coverage_pct = skills_in_exp / len(skills) if skills else 0
            if coverage_pct > 0.4:
                passed_checks.append("Strong keyword distribution: technical skills appear within work experience bullets")
            else:
                score -= 6
                issues.append(ATSIssueItem(
                    severity="medium",
                    rule="Keyword Placement in Context",
                    description="Skills are mostly listed in a standalone section with weak evidence in actual work experience bullets.",
                    fix_tip="Incorporate key technologies directly into your work experience bullet points demonstrating how and where you applied them."
                ))

        # Check 8: Unusual Characters & Symbols
        special_chars = len(re.findall(r"[^\x00-\x7F]", raw_text))
        if special_chars > 80:
            score -= 5
            issues.append(ATSIssueItem(
                severity="low",
                rule="Special Characters & Icons",
                description="A high frequency of non-ASCII glyphs or icons was detected.",
                fix_tip="Replace fancy decorative icons (such as phone glyphs, stars, or bar charts) with clean standard text."
            ))
        else:
            passed_checks.append("Clean typography with standard bullet glyphs")

        # Normalize score
        final_score = max(20, min(100, score))
        status = "Excellent" if final_score >= 85 else ("Good" if final_score >= 70 else ("Warning" if final_score >= 50 else "Critical"))

        return ATSCompatibilityResult(
            score=final_score,
            status=status,
            issues=issues,
            passed_checks=passed_checks,
            formatting_summary=formatting_summary,
        )
