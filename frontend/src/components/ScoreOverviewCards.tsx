import React, { useState } from 'react';
import { Target, TrendingUp, CheckCircle, Award, Clock, FileCheck2, Info, AlertTriangle, ShieldAlert } from 'lucide-react';
import { AnalysisResponse } from '../types';

interface ScoreOverviewCardsProps {
  analysis: AnalysisResponse;
}

export const ScoreOverviewCards: React.FC<ScoreOverviewCardsProps> = ({ analysis }) => {
  const [showProbabilityInfo, setShowProbabilityInfo] = useState(false);

  const { overall_score, estimated_screening_probability, skills, category_scores, ats_compatibility, final_assessment } = analysis;

  // Determine score colors
  const getScoreColor = (score: number) => {
    if (score >= 80) return 'text-emerald-400 border-emerald-500/30 bg-emerald-500/10 shadow-glow-emerald';
    if (score >= 60) return 'text-amber-400 border-amber-500/30 bg-amber-500/10 shadow-glow-amber';
    return 'text-rose-400 border-rose-500/30 bg-rose-500/10';
  };

  const getStrokeColor = (score: number) => {
    if (score >= 80) return '#10b981';
    if (score >= 60) return '#f59e0b';
    return '#f43f5e';
  };

  return (
    <div className="space-y-6">
      
      {/* Disclaimer Banner for Screening Probability */}
      <div className="bg-slate-900/90 border border-indigo-500/30 rounded-xl p-3.5 sm:p-4 flex items-start space-x-3 text-xs text-slate-300">
        <Info className="w-5 h-5 text-indigo-400 shrink-0 mt-0.5" />
        <div className="flex-1">
          <span className="font-bold text-white mr-1.5">Explainable AI Scoring:</span>
          <span>
            Scoring evaluates technical taxonomy alignment, evidence in work bullets, and ATS format extractability. 
            Estimated screening probability is a statistical guide based solely on provided text.
          </span>
        </div>
      </div>

      {/* Main KPI Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-6 gap-4">
        
        {/* Card 1: Resume Match Score */}
        <div className="lg:col-span-2 glass-panel rounded-2xl p-5 border border-slate-800 flex items-center justify-between relative overflow-hidden">
          <div className="space-y-1">
            <div className="flex items-center space-x-1.5 text-xs font-semibold text-slate-400">
              <Target className="w-4 h-4 text-indigo-400" />
              <span>Resume Match Score</span>
            </div>
            <div className="flex items-baseline space-x-1.5">
              <span className="text-4xl sm:text-5xl font-black tracking-tight text-white">
                {Math.round(overall_score)}
              </span>
              <span className="text-xl font-bold text-slate-500">/100</span>
            </div>
            <div className="text-xs font-medium text-indigo-300">
              {final_assessment.match_category.split(' ')[0]} {final_assessment.match_category.split(' ')[1]}
            </div>
          </div>

          {/* Radial SVG Gauge */}
          <div className="relative w-24 h-24 flex items-center justify-center">
            <svg className="w-full h-full transform -rotate-90" viewBox="0 0 36 36">
              <path
                className="text-slate-800"
                strokeWidth="3.5"
                stroke="currentColor"
                fill="none"
                d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
              />
              <path
                strokeDasharray={`${overall_score}, 100`}
                strokeWidth="3.5"
                strokeLinecap="round"
                stroke={getStrokeColor(overall_score)}
                fill="none"
                d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
              />
            </svg>
            <div className="absolute font-black text-sm text-slate-200">
              {Math.round(overall_score)}%
            </div>
          </div>
        </div>

        {/* Card 2: Estimated ATS Shortlist Probability */}
        <div className="lg:col-span-2 glass-panel rounded-2xl p-5 border border-slate-800 flex items-center justify-between relative">
          <div className="space-y-1">
            <div className="flex items-center space-x-1.5 text-xs font-semibold text-slate-400">
              <TrendingUp className="w-4 h-4 text-emerald-400" />
              <span>Estimated Screening Prob.</span>
              <button
                onClick={() => setShowProbabilityInfo(!showProbabilityInfo)}
                className="text-slate-500 hover:text-slate-300 transition-colors"
                title="Click to view probability calculation factors"
              >
                <Info className="w-3.5 h-3.5" />
              </button>
            </div>
            <div className="flex items-baseline space-x-1">
              <span className="text-4xl sm:text-5xl font-black tracking-tight text-emerald-400">
                {Math.round(estimated_screening_probability)}%
              </span>
            </div>
            <div className="text-[11px] text-slate-400 truncate max-w-[190px]">
              Initial ATS / Recruiter Screen
            </div>
          </div>

          <div className="relative w-24 h-24 flex items-center justify-center">
            <svg className="w-full h-full transform -rotate-90" viewBox="0 0 36 36">
              <path
                className="text-slate-800"
                strokeWidth="3.5"
                stroke="currentColor"
                fill="none"
                d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
              />
              <path
                strokeDasharray={`${estimated_screening_probability}, 100`}
                strokeWidth="3.5"
                strokeLinecap="round"
                stroke="#10b981"
                fill="none"
                d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
              />
            </svg>
            <div className="absolute font-black text-sm text-emerald-400">
              {Math.round(estimated_screening_probability)}%
            </div>
          </div>
        </div>

        {/* Card 3: Required Skills */}
        <div className="glass-panel rounded-2xl p-4 border border-slate-800 flex flex-col justify-between">
          <div className="text-xs font-semibold text-slate-400 flex items-center mb-1">
            <CheckCircle className="w-3.5 h-3.5 text-emerald-400 mr-1.5" /> Required Skills
          </div>
          <div>
            <div className="text-2xl sm:text-3xl font-extrabold text-white">
              {skills.matched_required} <span className="text-slate-500 text-lg">/ {skills.total_required}</span>
            </div>
            <div className="w-full bg-slate-800 h-1.5 rounded-full mt-2 overflow-hidden">
              <div
                className="bg-emerald-400 h-full rounded-full transition-all duration-500"
                style={{ width: `${skills.total_required > 0 ? (skills.matched_required / skills.total_required) * 100 : 0}%` }}
              />
            </div>
          </div>
          <div className="text-[11px] text-slate-400 mt-1">
            {skills.total_required - skills.matched_required === 0 ? 'All mandatory met' : `${skills.total_required - skills.matched_required} missing/partial`}
          </div>
        </div>

        {/* Card 4: Preferred Skills */}
        <div className="glass-panel rounded-2xl p-4 border border-slate-800 flex flex-col justify-between">
          <div className="text-xs font-semibold text-slate-400 flex items-center mb-1">
            <Award className="w-3.5 h-3.5 text-amber-400 mr-1.5" /> Preferred Skills
          </div>
          <div>
            <div className="text-2xl sm:text-3xl font-extrabold text-white">
              {skills.matched_preferred} <span className="text-slate-500 text-lg">/ {skills.total_preferred}</span>
            </div>
            <div className="w-full bg-slate-800 h-1.5 rounded-full mt-2 overflow-hidden">
              <div
                className="bg-amber-400 h-full rounded-full transition-all duration-500"
                style={{ width: `${skills.total_preferred > 0 ? (skills.matched_preferred / skills.total_preferred) * 100 : 0}%` }}
              />
            </div>
          </div>
          <div className="text-[11px] text-slate-400 mt-1">
            Bonus differentiator
          </div>
        </div>

        {/* Card 5: Experience Match */}
        <div className="glass-panel rounded-2xl p-4 border border-slate-800 flex flex-col justify-between">
          <div className="text-xs font-semibold text-slate-400 flex items-center mb-1">
            <Clock className="w-3.5 h-3.5 text-indigo-400 mr-1.5" /> Experience
          </div>
          <div>
            <div className="text-2xl sm:text-3xl font-extrabold text-white">
              {Math.round(category_scores.experience_score)}%
            </div>
            <div className="w-full bg-slate-800 h-1.5 rounded-full mt-2 overflow-hidden">
              <div
                className="bg-indigo-400 h-full rounded-full transition-all duration-500"
                style={{ width: `${category_scores.experience_score}%` }}
              />
            </div>
          </div>
          <div className="text-[11px] text-slate-400 mt-1">
            Seniority & role tenure
          </div>
        </div>

        {/* Card 6: ATS Compatibility */}
        <div className="glass-panel rounded-2xl p-4 border border-slate-800 flex flex-col justify-between">
          <div className="text-xs font-semibold text-slate-400 flex items-center mb-1">
            <FileCheck2 className="w-3.5 h-3.5 text-purple-400 mr-1.5" /> ATS Score
          </div>
          <div>
            <div className="text-2xl sm:text-3xl font-extrabold text-white">
              {ats_compatibility.score}<span className="text-slate-500 text-lg">/100</span>
            </div>
            <div className="w-full bg-slate-800 h-1.5 rounded-full mt-2 overflow-hidden">
              <div
                className="bg-purple-400 h-full rounded-full transition-all duration-500"
                style={{ width: `${ats_compatibility.score}%` }}
              />
            </div>
          </div>
          <div className="text-[11px] text-slate-400 mt-1">
            {ats_compatibility.status} layout
          </div>
        </div>

      </div>

      {/* Expandable Probability Modal / Detailed Factor Breakdown */}
      {showProbabilityInfo && (
        <div className="bg-slate-900 border border-slate-700 p-5 rounded-2xl text-xs text-slate-300 space-y-3 animate-in fade-in slide-in-from-top-2">
          <div className="flex items-center justify-between">
            <h4 className="text-sm font-bold text-white flex items-center">
              <ShieldAlert className="w-4 h-4 text-emerald-400 mr-2" />
              Understanding "Estimated Initial Screening Probability"
            </h4>
            <button
              onClick={() => setShowProbabilityInfo(false)}
              className="text-slate-400 hover:text-white font-bold"
            >
              ✕
            </button>
          </div>
          <p className="text-slate-300 leading-relaxed">
            {final_assessment.probability_disclaimer}
          </p>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-2 text-slate-400">
            <div className="bg-slate-950/60 p-2.5 rounded-xl border border-slate-800">
              <strong className="text-slate-200 block mb-1">Included in Estimation:</strong>
              • Exact and synonym skill match coverage<br/>
              • Contextual evidence within work experience bullets<br/>
              • ATS section parseability and layout health<br/>
              • Seniority and educational criteria overlap
            </div>
            <div className="bg-slate-950/60 p-2.5 rounded-xl border border-slate-800">
              <strong className="text-slate-200 block mb-1">Real-World External Variables:</strong>
              • Total applicant volume for the role<br/>
              • Specific recruiter keyword filters & Boolean queries<br/>
              • Location, work visa & compensation alignment<br/>
              • Interview performance and internal referral quotas
            </div>
          </div>
        </div>
      )}

    </div>
  );
};
