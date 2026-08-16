import axios from 'axios';
import { AnalysisResponse, ScoringWeights, ResumeStructure, JDStructure } from '../types';

const API_BASE = '/api';

export const apiClient = {
  // Upload or paste resume
  async uploadResume(formData: FormData): Promise<{
    id: string;
    filename?: string;
    file_type: string;
    raw_text: string;
    structured_data: ResumeStructure;
    ats_preliminary_score: number;
  }> {
    const res = await axios.post(`${API_BASE}/resume/upload`, formData);
    return res.data;
  },

  // Delete resume (privacy compliant)
  async deleteResume(resumeId: string): Promise<{ message: string }> {
    const res = await axios.delete(`${API_BASE}/resume/${resumeId}`);
    return res.data;
  },

  // Upload or paste JD
  async uploadJD(formData: FormData): Promise<{
    id: string;
    raw_text: string;
    structured_data: JDStructure;
  }> {
    const res = await axios.post(`${API_BASE}/job-description/upload`, formData);
    return res.data;
  },

  // Perform full semantic matching analysis
  async analyze(params: {
    resume_id?: string | null;
    job_description_id?: string | null;
    resume_text?: string;
    job_description_text?: string;
    custom_weights?: Partial<ScoringWeights>;
  }): Promise<AnalysisResponse> {
    const res = await axios.post(`${API_BASE}/analyze`, params);
    return res.data;
  },

  // Get sample demo data
  async getSampleData(): Promise<{
    sample_resume_text: string;
    sample_jd_text: string;
    sample_resume_structured: ResumeStructure;
    sample_jd_structured: JDStructure;
    meta: { title: string; scenario: string };
  }> {
    const res = await axios.get(`${API_BASE}/sample-data`);
    return res.data;
  },

  // Get scoring weights
  async getWeights(): Promise<{
    raw_weights: ScoringWeights;
    normalized_weights: Record<string, number>;
  }> {
    const res = await axios.get(`${API_BASE}/config/weights`);
    return res.data;
  },

  // Update scoring weights
  async updateWeights(weights: ScoringWeights): Promise<{
    message: string;
    raw_weights: ScoringWeights;
    normalized_weights: Record<string, number>;
  }> {
    const res = await axios.post(`${API_BASE}/config/weights`, weights);
    return res.data;
  },
};
