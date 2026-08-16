export interface ContactInfo {
  name?: string;
  email?: string;
  phone?: string;
  location?: string;
  linkedin?: string;
  github?: string;
  portfolio?: string;
}

export interface ResumeStructure {
  candidate_name?: string;
  contact_info: ContactInfo;
  professional_summary?: string;
  skills: string[];
  work_experience: Array<{
    role?: string;
    company?: string;
    duration?: string;
    bullets?: string[];
  }>;
  projects: Array<{
    name?: string;
    description?: string;
    tech_stack?: string[];
    bullets?: string[];
  }>;
  education: Array<{
    degree_or_institution?: string;
  }>;
  certifications: string[];
  achievements: string[];
  raw_sections: Record<string, string>;
  detected_hazards: string[];
}

export interface JDStructure {
  job_title?: string;
  company_name?: string;
  required_skills: string[];
  preferred_skills: string[];
  programming_languages: string[];
  frameworks: string[];
  cloud_technologies: string[];
  databases: string[];
  tools_and_devops: string[];
  required_years_experience?: number;
  educational_requirements: string[];
  certifications: string[];
  responsibilities: string[];
  domain_knowledge: string[];
  soft_skills: string[];
}

export interface SkillMatchItem {
  name: string;
  category: string;
  status: 'strong' | 'partial' | 'missing';
  importance: 'critical' | 'important' | 'nice-to-have';
  is_required: boolean;
  reason: string;
  resume_evidence?: string | null;
}

export interface SkillsAnalysisResult {
  strong_matches: SkillMatchItem[];
  partial_matches: SkillMatchItem[];
  missing: SkillMatchItem[];
  total_required: number;
  matched_required: number;
  total_preferred: number;
  matched_preferred: number;
  overall_skill_score: number;
}

export interface ExperienceGapItem {
  jd_requirement: string;
  resume_evidence: string;
  match_type: 'Strong' | 'Partial' | 'Missing' | 'Weak';
  importance: 'Critical' | 'Important' | 'Nice-to-have';
  notes?: string;
}

export interface ATSIssueItem {
  severity: 'high' | 'medium' | 'low';
  rule: string;
  description: string;
  fix_tip: string;
}

export interface ATSCompatibilityResult {
  score: number;
  status: 'Excellent' | 'Good' | 'Warning' | 'Critical';
  issues: ATSIssueItem[];
  passed_checks: string[];
  formatting_summary: Record<string, any>;
}

export interface ImprovementItem {
  section: string;
  original_snippet: string;
  recommended_rewrite: string;
  why: string;
  cautionary_note: string;
}

export interface MissingKeywordRecommendation {
  keyword: string;
  importance: string;
  where_to_add: string;
  advice: string;
  cautionary_note: string;
}

export interface SideBySideItem {
  jd_requirement: string;
  resume_evidence: string;
  match_status: 'strong' | 'partial' | 'missing';
  match_badge: string;
  importance: string;
  notes: string;
}

export interface CriticalGapItem {
  priority: 'High' | 'Medium' | 'Low';
  requirement: string;
  gap_description: string;
  impact_level: string;
}

export interface FinalAssessmentResult {
  overall_score: number;
  estimated_screening_probability: number;
  probability_disclaimer: string;
  match_category: string;
  recommendation_verdict: string;
  why_matches_summary: string;
  biggest_weaknesses: string[];
  priority_keywords_to_add: string[];
  is_qualified_verdict: string;
  what_to_change_before_applying: string[];
}

export interface CategoryScores {
  skills_score: number;
  experience_score: number;
  responsibilities_score: number;
  education_score: number;
  projects_score: number;
  soft_skills_score: number;
  ats_quality_score: number;
}

export interface ScoringWeights {
  weight_skills: number;
  weight_experience: number;
  weight_responsibilities: number;
  weight_education: number;
  weight_projects: number;
  weight_soft_skills: number;
  weight_ats_quality: number;
}

export interface AnalysisResponse {
  id: string;
  resume_id?: string | null;
  job_description_id?: string | null;
  overall_score: number;
  estimated_screening_probability: number;
  category_scores: CategoryScores;
  scoring_weights_applied: Record<string, number>;
  skills: SkillsAnalysisResult;
  experience_gap: ExperienceGapItem[];
  ats_compatibility: ATSCompatibilityResult;
  strengths: string[];
  critical_gaps: CriticalGapItem[];
  recommendations: ImprovementItem[];
  missing_keyword_recommendations: MissingKeywordRecommendation[];
  side_by_side: SideBySideItem[];
  final_assessment: FinalAssessmentResult;
  provider_used: string;
}
