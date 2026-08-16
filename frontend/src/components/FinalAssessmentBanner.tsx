import React from 'react';
import { Award, CheckCircle2, AlertCircle, ArrowRight, ShieldCheck, ListChecks, HelpCircle } from 'lucide-react';
import { FinalAssessmentResult } from '../types';

interface FinalAssessmentBannerProps {
  assessment: FinalAssessmentResult;
}

export const FinalAssessmentBanner: React.FC<FinalAssessmentBannerProps> = ({ assessment }) => {
  const {
    overall_score,
    estimated_screening_probability,
    match_category,
    recommendation_verdict,
    why_matches_summary,
    biggest_weaknesses,
    priority_keywords_to_add,
    is_qualified_verdict,
    what_to_change_before_applying,
  } = assessment;

  const isStrong = overall_score >= 80;
  const isModerate = overall_score >= 60 && overall_score < 80;
  const isWeak = overall_score >= 40 && overall_score < 60;

  const getVerdictStyle = () => {
    if (isStrong) return 'bg-emerald-500/10 border-emerald-500/30 text-emerald-300';
    if (isModerate) return 'bg-amber-500/10 border-amber-500/30 text-amber-300';
    return 'bg-rose-500/10 border-rose-500/30 text-rose-300';
  };

  return (
    <div className="glass-panel rounded-2xl p-6 sm:p-7 border border-slate-800 space-y-6 shadow-xl relative overflow-hidden">
      
      {/* Top Banner */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-5 border-b border-slate-800">
        <div>
          <div className="flex items-center space-x-2 mb-1.5">
            <span className="text-xs font-bold uppercase tracking-wider text-slate-400">
              Executive Evaluation
            </span>
            <span className={`text-xs font-extrabold px-3 py-0.5 rounded-full border ${getVerdictStyle()}`}>
              {match_category}
            </span>
          </div>
          <h3 className="text-xl sm:text-2xl font-black text-white">
            Recommendation: {recommendation_verdict}
          </h3>
          <p className="text-xs text-slate-300 mt-1 max-w-2xl font-medium">
            {is_qualified_verdict}
          </p>
        </div>

        {/* Action Summary Pill */}
        <div className="flex items-center space-x-4 bg-slate-900/90 p-3 rounded-xl border border-slate-800 shrink-0">
          <div className="text-center">
            <div className="text-xs text-slate-400">Match</div>
            <div className="text-2xl font-black text-white">{Math.round(overall_score)}/100</div>
          </div>
          <div className="h-8 w-px bg-slate-800" />
          <div className="text-center">
            <div className="text-xs text-slate-400">Est. Screen</div>
            <div className="text-2xl font-black text-emerald-400">{Math.round(estimated_screening_probability)}%</div>
          </div>
        </div>
      </div>

      {/* Narrative Breakdown */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 text-xs">
        
        {/* Box 1: Why the Resume Matches */}
        <div className="bg-slate-900/60 p-4.5 rounded-xl border border-slate-800 space-y-2">
          <h4 className="font-bold text-white flex items-center text-sm">
            <CheckCircle2 className="w-4 h-4 text-emerald-400 mr-2" />
            Why You Match
          </h4>
          <p className="text-slate-300 leading-relaxed">
            {why_matches_summary}
          </p>
        </div>

        {/* Box 2: Biggest Weaknesses */}
        <div className="bg-slate-900/60 p-4.5 rounded-xl border border-slate-800 space-y-2">
          <h4 className="font-bold text-white flex items-center text-sm">
            <AlertCircle className="w-4 h-4 text-amber-400 mr-2" />
            Areas of Concern
          </h4>
          <ul className="space-y-1.5 text-slate-300">
            {biggest_weaknesses.map((w, idx) => (
              <li key={idx} className="flex items-start">
                <span className="text-amber-400 mr-1.5">•</span>
                <span>{w}</span>
              </li>
            ))}
          </ul>
        </div>

        {/* Box 3: Priority Keywords to Add */}
        <div className="bg-slate-900/60 p-4.5 rounded-xl border border-slate-800 space-y-2">
          <h4 className="font-bold text-white flex items-center text-sm">
            <Award className="w-4 h-4 text-indigo-400 mr-2" />
            Priority Keywords to Add
          </h4>
          <p className="text-slate-400 text-[11px]">
            If you have genuine experience, incorporate these into your Skills and Projects:
          </p>
          <div className="flex flex-wrap gap-1.5 pt-1">
            {priority_keywords_to_add.map((kw, idx) => (
              <span
                key={idx}
                className="bg-indigo-500/10 text-indigo-300 border border-indigo-500/30 px-2.5 py-1 rounded-lg text-xs font-semibold"
              >
                + {kw}
              </span>
            ))}
          </div>
        </div>

      </div>

      {/* Pre-Application Checklist */}
      <div className="pt-2 border-t border-slate-800/80">
        <h4 className="text-xs font-bold uppercase tracking-wider text-slate-400 mb-3 flex items-center">
          <ListChecks className="w-4 h-4 text-emerald-400 mr-2" />
          Recommended Action Checklist Before Applying
        </h4>
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5 text-xs text-slate-200">
          {what_to_change_before_applying.map((item, idx) => (
            <div key={idx} className="flex items-start space-x-2 bg-slate-950/60 p-2.5 rounded-xl border border-slate-800/80">
              <span className="w-4 h-4 rounded-full bg-indigo-500/20 text-indigo-300 border border-indigo-500/40 flex items-center justify-center font-bold text-[10px] shrink-0 mt-0.5">
                {idx + 1}
              </span>
              <span>{item}</span>
            </div>
          ))}
        </div>
      </div>

    </div>
  );
};
