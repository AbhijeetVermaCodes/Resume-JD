import React, { useState, useEffect } from 'react';
import {
  Sparkles,
  ArrowRight,
  RefreshCw,
  AlertCircle,
  CheckCircle2,
  FileCheck,
  SplitSquareVertical,
  ShieldCheck,
  Table,
  Lightbulb,
  Award,
  Layers,
  Download,
} from 'lucide-react';

import { apiClient } from './api/client';
import {
  ResumeStructure,
  JDStructure,
  AnalysisResponse,
  ScoringWeights,
} from './types';

import { Navbar } from './components/Navbar';
import { ResumeUploader } from './components/ResumeUploader';
import { JDUploader } from './components/JDUploader';
import { ScoreOverviewCards } from './components/ScoreOverviewCards';
import { KeywordAnalysisTab } from './components/KeywordAnalysisTab';
import { ExperienceGapTable } from './components/ExperienceGapTable';
import { SideBySideView } from './components/SideBySideView';
import { ATSCompatibilityCard } from './components/ATSCompatibilityCard';
import { StrengthsAndGaps } from './components/StrengthsAndGaps';
import { ImprovementSuggestions } from './components/ImprovementSuggestions';
import { FinalAssessmentBanner } from './components/FinalAssessmentBanner';
import { WeightConfigModal } from './components/WeightConfigModal';
import { PrivacyNoticeModal } from './components/PrivacyNoticeModal';
import { ExportModal } from './components/ExportModal';

const DEFAULT_WEIGHTS: ScoringWeights = {
  weight_skills: 0.35,
  weight_experience: 0.20,
  weight_responsibilities: 0.15,
  weight_education: 0.10,
  weight_projects: 0.10,
  weight_soft_skills: 0.05,
  weight_ats_quality: 0.05,
};

export const App: React.FC = () => {
  // Input State
  const [resumeText, setResumeText] = useState<string>('');
  const [resumeId, setResumeId] = useState<string | null>(null);
  const [structuredResume, setStructuredResume] = useState<ResumeStructure | null>(null);

  const [jdText, setJDText] = useState<string>('');
  const [jdId, setJDId] = useState<string | null>(null);
  const [structuredJD, setStructuredJD] = useState<JDStructure | null>(null);

  // Analysis State
  const [analysis, setAnalysis] = useState<AnalysisResponse | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [loadingStep, setLoadingStep] = useState<string>('');
  const [error, setError] = useState<string | null>(null);

  // UI Tabs & Modals State
  const [activeTab, setActiveTab] = useState<
    'overview' | 'keywords' | 'experience' | 'side-by-side' | 'ats' | 'suggestions'
  >('overview');
  const [isWeightsModalOpen, setIsWeightsModalOpen] = useState<boolean>(false);
  const [isPrivacyModalOpen, setIsPrivacyModalOpen] = useState<boolean>(false);
  const [isExportModalOpen, setIsExportModalOpen] = useState<boolean>(false);
  const [customWeights, setCustomWeights] = useState<ScoringWeights>(DEFAULT_WEIGHTS);

  // 1-Click Demo Loader
  const handleLoadDemo = async () => {
    try {
      setIsLoading(true);
      setError(null);
      setLoadingStep('Loading Senior Software Engineer Demo...');
      const sample = await apiClient.getSampleData();
      
      setResumeText(sample.sample_resume_text);
      setStructuredResume(sample.sample_resume_structured);
      setResumeId(null);

      setJDText(sample.sample_jd_text);
      setStructuredJD(sample.sample_jd_structured);
      setJDId(null);

      setLoadingStep('Analyzing sample resume against cloud platforms role...');
      const res = await apiClient.analyze({
        resume_text: sample.sample_resume_text,
        job_description_text: sample.sample_jd_text,
        custom_weights: customWeights,
      });

      setAnalysis(res);
      setActiveTab('overview');
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Failed to load demo data. Please try again.');
    } finally {
      setIsLoading(false);
      setLoadingStep('');
    }
  };

  // Resume File Upload
  const handleResumeFileUpload = async (file: File) => {
    try {
      setIsLoading(true);
      setError(null);
      setLoadingStep('Parsing resume document & extracting sections...');
      const formData = new FormData();
      formData.append('file', file);
      
      const res = await apiClient.uploadResume(formData);
      setResumeId(res.id);
      setResumeText(res.raw_text);
      setStructuredResume(res.structured_data);
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Failed to parse resume file.');
    } finally {
      setIsLoading(false);
      setLoadingStep('');
    }
  };

  // Resume Privacy Deletion
  const handleDeleteResume = async () => {
    if (resumeId) {
      try {
        await apiClient.deleteResume(resumeId);
      } catch (err) {
        console.warn('Failed to delete on server:', err);
      }
    }
    setResumeId(null);
    setResumeText('');
    setStructuredResume(null);
    setAnalysis(null);
  };

  // JD File Upload
  const handleJDFileUpload = async (file: File) => {
    try {
      setIsLoading(true);
      setError(null);
      setLoadingStep('Extracting job description requirements...');
      const formData = new FormData();
      formData.append('file', file);

      const res = await apiClient.uploadJD(formData);
      setJDId(res.id);
      setJDText(res.raw_text);
      setStructuredJD(res.structured_data);
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Failed to parse job description file.');
    } finally {
      setIsLoading(false);
      setLoadingStep('');
    }
  };

  // Run Match Analysis
  const handleAnalyze = async () => {
    if (!resumeText.trim()) {
      setError('Please upload or paste a candidate resume before analyzing.');
      return;
    }
    if (!jdText.trim()) {
      setError('Please provide a Job Description to match against.');
      return;
    }

    try {
      setIsLoading(true);
      setError(null);
      setLoadingStep('Synthesizing semantic skill alignment & ATS heuristics...');

      const res = await apiClient.analyze({
        resume_id: resumeId,
        job_description_id: jdId,
        resume_text: !resumeId ? resumeText : undefined,
        job_description_text: !jdId ? jdText : undefined,
        custom_weights: customWeights,
      });

      setAnalysis(res);
      setActiveTab('overview');

      // Smooth scroll to results
      setTimeout(() => {
        const resultsEl = document.getElementById('analysis-results-section');
        if (resultsEl) {
          resultsEl.scrollIntoView({ behavior: 'smooth' });
        }
      }, 100);
    } catch (err: any) {
      setError(err.response?.data?.detail || 'An error occurred during analysis. Please check your inputs.');
    } finally {
      setIsLoading(false);
      setLoadingStep('');
    }
  };

  // Recalculate weights
  const handleSaveWeights = async (newWeights: ScoringWeights) => {
    setCustomWeights(newWeights);
    if (analysis && (resumeText || resumeId) && (jdText || jdId)) {
      try {
        setIsLoading(true);
        setLoadingStep('Recalculating match scores with updated weights...');
        const res = await apiClient.analyze({
          resume_id: resumeId,
          job_description_id: jdId,
          resume_text: !resumeId ? resumeText : undefined,
          job_description_text: !jdId ? jdText : undefined,
          custom_weights: newWeights,
        });
        setAnalysis(res);
      } catch (err) {
        console.error('Failed to recalculate with custom weights:', err);
      } finally {
        setIsLoading(false);
        setLoadingStep('');
      }
    }
  };

  const handleReset = () => {
    setResumeText('');
    setResumeId(null);
    setStructuredResume(null);
    setJDText('');
    setJDId(null);
    setStructuredJD(null);
    setAnalysis(null);
    setError(null);
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col">
      
      {/* Navigation */}
      <Navbar
        onLoadDemo={handleLoadDemo}
        onOpenWeightsModal={() => setIsWeightsModalOpen(true)}
        onOpenPrivacyModal={() => setIsPrivacyModalOpen(true)}
        onReset={handleReset}
        hasAnalysis={!!analysis}
        isLoading={isLoading}
      />

      {/* Main Container */}
      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
        
        {/* Hero Section */}
        <div className="text-center space-y-3 max-w-3xl mx-auto pt-2 pb-2">
          <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-indigo-500/10 border border-indigo-500/20 text-xs font-semibold text-indigo-400 mb-1">
            <Sparkles className="w-3.5 h-3.5" />
            <span>AI Semantic Matching • ATS Optimization • Zero Hallucination</span>
          </div>
          <h1 className="text-3xl sm:text-4xl lg:text-5xl font-black tracking-tight text-white leading-tight">
            Analyze Your CV Against Any{' '}
            <span className="bg-gradient-to-r from-indigo-400 via-emerald-400 to-amber-300 bg-clip-text text-transparent">
              Job Description
            </span>
          </h1>
          <p className="text-sm sm:text-base text-slate-400 max-w-2xl mx-auto leading-relaxed">
            Estimate your screening probability, detect missing technical keywords with precision reasoning, audit ATS compatibility, and receive tailored bullet improvements.
          </p>
        </div>

        {/* Error Alert */}
        {error && (
          <div className="max-w-4xl mx-auto p-4 rounded-xl bg-rose-950/40 border border-rose-500/40 text-rose-200 text-xs flex items-center justify-between animate-in fade-in">
            <div className="flex items-center space-x-2.5">
              <AlertCircle className="w-5 h-5 text-rose-400 shrink-0" />
              <span>{error}</span>
            </div>
            <button
              onClick={() => setError(null)}
              className="text-rose-400 hover:text-white font-bold ml-2"
            >
              ✕
            </button>
          </div>
        )}

        {/* Input Grid: Step 1 (Resume) & Step 2 (JD) */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <ResumeUploader
            resumeText={resumeText}
            onResumeTextChange={setResumeText}
            resumeId={resumeId}
            onResumeIdChange={setResumeId}
            structuredResume={structuredResume}
            onStructuredResumeChange={setStructuredResume}
            onFileUpload={handleResumeFileUpload}
            onDeleteResume={handleDeleteResume}
            isLoading={isLoading}
          />

          <JDUploader
            jdText={jdText}
            onJDTextChange={setJDText}
            jdId={jdId}
            onJDIdChange={setJDId}
            structuredJD={structuredJD}
            onStructuredJDChange={setStructuredJD}
            onFileUpload={handleJDFileUpload}
            isLoading={isLoading}
          />
        </div>

        {/* CTA Action Button */}
        <div className="flex flex-col items-center justify-center pt-2 space-y-3">
          <button
            type="button"
            onClick={handleAnalyze}
            disabled={isLoading || !resumeText.trim() || !jdText.trim()}
            className="w-full sm:w-auto min-w-[280px] px-8 py-4 rounded-2xl bg-gradient-to-r from-indigo-600 via-indigo-500 to-emerald-500 hover:from-indigo-500 hover:to-emerald-400 text-white font-extrabold text-base shadow-glow hover:scale-[1.01] active:scale-[0.99] transition-all flex items-center justify-center space-x-2.5 disabled:opacity-40 disabled:pointer-events-none"
          >
            {isLoading ? (
              <>
                <RefreshCw className="w-5 h-5 animate-spin" />
                <span>{loadingStep || 'Analyzing Resume...'}</span>
              </>
            ) : (
              <>
                <Sparkles className="w-5 h-5 text-emerald-200" />
                <span>Analyze My Resume</span>
                <ArrowRight className="w-5 h-5" />
              </>
            )}
          </button>

          {!analysis && (
            <p className="text-xs text-slate-500">
              Or click <button onClick={handleLoadDemo} className="text-indigo-400 hover:underline font-medium">Load Demo</button> to test with a realistic Senior Software Engineer CV and Job Description.
            </p>
          )}
        </div>

        {/* Analysis Results Section */}
        {analysis && (
          <div id="analysis-results-section" className="space-y-8 pt-8 border-t border-slate-800 animate-in fade-in duration-500">
            
            {/* Header with Export Action */}
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-2">
              <div>
                <div className="text-xs font-bold uppercase tracking-wider text-indigo-400 mb-1 flex items-center">
                  <CheckCircle2 className="w-4 h-4 mr-1.5 text-emerald-400" />
                  Analysis Complete
                </div>
                <h2 className="text-2xl sm:text-3xl font-black text-white">
                  Match & ATS Screening Report
                </h2>
              </div>

              <div className="flex items-center space-x-3">
                <button
                  onClick={() => setIsExportModalOpen(true)}
                  className="flex items-center space-x-1.5 px-4 py-2 text-xs font-semibold rounded-xl bg-slate-900 hover:bg-slate-800 text-slate-200 border border-slate-700 transition-colors shadow-sm"
                >
                  <Download className="w-4 h-4 text-indigo-400" />
                  <span>Export Report</span>
                </button>
              </div>
            </div>

            {/* KPI Cards */}
            <ScoreOverviewCards analysis={analysis} />

            {/* Final Assessment Banner */}
            <FinalAssessmentBanner assessment={analysis.final_assessment} />

            {/* Navigation Tabs */}
            <div className="border-b border-slate-800 overflow-x-auto">
              <nav className="flex space-x-2 sm:space-x-4 min-w-max pb-px">
                <button
                  onClick={() => setActiveTab('overview')}
                  className={`py-3 px-4 text-xs sm:text-sm font-bold border-b-2 flex items-center space-x-2 transition-all ${
                    activeTab === 'overview'
                      ? 'border-indigo-500 text-indigo-400'
                      : 'border-transparent text-slate-400 hover:text-slate-200'
                  }`}
                >
                  <Award className="w-4 h-4" />
                  <span>Strengths & Gaps</span>
                </button>

                <button
                  onClick={() => setActiveTab('keywords')}
                  className={`py-3 px-4 text-xs sm:text-sm font-bold border-b-2 flex items-center space-x-2 transition-all ${
                    activeTab === 'keywords'
                      ? 'border-indigo-500 text-indigo-400'
                      : 'border-transparent text-slate-400 hover:text-slate-200'
                  }`}
                >
                  <Sparkles className="w-4 h-4" />
                  <span>Keyword Analysis</span>
                </button>

                <button
                  onClick={() => setActiveTab('experience')}
                  className={`py-3 px-4 text-xs sm:text-sm font-bold border-b-2 flex items-center space-x-2 transition-all ${
                    activeTab === 'experience'
                      ? 'border-indigo-500 text-indigo-400'
                      : 'border-transparent text-slate-400 hover:text-slate-200'
                  }`}
                >
                  <Table className="w-4 h-4" />
                  <span>Experience Gap Matrix</span>
                </button>

                <button
                  onClick={() => setActiveTab('side-by-side')}
                  className={`py-3 px-4 text-xs sm:text-sm font-bold border-b-2 flex items-center space-x-2 transition-all ${
                    activeTab === 'side-by-side'
                      ? 'border-indigo-500 text-indigo-400'
                      : 'border-transparent text-slate-400 hover:text-slate-200'
                  }`}
                >
                  <SplitSquareVertical className="w-4 h-4" />
                  <span>Side-by-Side View</span>
                </button>

                <button
                  onClick={() => setActiveTab('ats')}
                  className={`py-3 px-4 text-xs sm:text-sm font-bold border-b-2 flex items-center space-x-2 transition-all ${
                    activeTab === 'ats'
                      ? 'border-indigo-500 text-indigo-400'
                      : 'border-transparent text-slate-400 hover:text-slate-200'
                  }`}
                >
                  <ShieldCheck className="w-4 h-4" />
                  <span>ATS Compatibility</span>
                </button>

                <button
                  onClick={() => setActiveTab('suggestions')}
                  className={`py-3 px-4 text-xs sm:text-sm font-bold border-b-2 flex items-center space-x-2 transition-all ${
                    activeTab === 'suggestions'
                      ? 'border-indigo-500 text-indigo-400'
                      : 'border-transparent text-slate-400 hover:text-slate-200'
                  }`}
                >
                  <Lightbulb className="w-4 h-4" />
                  <span>Improvement Rewrites</span>
                </button>
              </nav>
            </div>

            {/* Active Tab Panel */}
            <div className="pt-2">
              {activeTab === 'overview' && (
                <StrengthsAndGaps
                  strengths={analysis.strengths}
                  criticalGaps={analysis.critical_gaps}
                />
              )}

              {activeTab === 'keywords' && (
                <KeywordAnalysisTab skills={analysis.skills} />
              )}

              {activeTab === 'experience' && (
                <ExperienceGapTable items={analysis.experience_gap} />
              )}

              {activeTab === 'side-by-side' && (
                <SideBySideView items={analysis.side_by_side} />
              )}

              {activeTab === 'ats' && (
                <ATSCompatibilityCard ats={analysis.ats_compatibility} />
              )}

              {activeTab === 'suggestions' && (
                <ImprovementSuggestions
                  recommendations={analysis.recommendations}
                  missingKeywordRecs={analysis.missing_keyword_recommendations}
                />
              )}
            </div>

          </div>
        )}

      </main>

      {/* Footer */}
      <footer className="w-full border-t border-slate-900 bg-slate-950 py-6 text-center text-xs text-slate-500">
        <div className="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-2">
          <span>MatchCraft AI • Production Resume & Job Description Semantic Engine</span>
          <span>Zero-Data Retention Guarantee • ATS Parser v2.5</span>
        </div>
      </footer>

      {/* Modals */}
      <WeightConfigModal
        isOpen={isWeightsModalOpen}
        onClose={() => setIsWeightsModalOpen(false)}
        currentWeights={customWeights}
        onSaveWeights={handleSaveWeights}
      />

      <PrivacyNoticeModal
        isOpen={isPrivacyModalOpen}
        onClose={() => setIsPrivacyModalOpen(false)}
      />

      {analysis && (
        <ExportModal
          isOpen={isExportModalOpen}
          onClose={() => setIsExportModalOpen(false)}
          analysis={analysis}
        />
      )}

    </div>
  );
};

export default App;
