import React from 'react';
import { FileCheck2, AlertTriangle, CheckCircle2, ShieldCheck, HelpCircle, Wrench } from 'lucide-react';
import { ATSCompatibilityResult } from '../types';

interface ATSCompatibilityCardProps {
  ats: ATSCompatibilityResult;
}

export const ATSCompatibilityCard: React.FC<ATSCompatibilityCardProps> = ({ ats }) => {
  const { score, status, issues, passed_checks, formatting_summary } = ats;

  const getStatusBadge = () => {
    if (score >= 85) return 'bg-emerald-500/20 text-emerald-300 border-emerald-500/30';
    if (score >= 70) return 'bg-indigo-500/20 text-indigo-300 border-indigo-500/30';
    if (score >= 50) return 'bg-amber-500/20 text-amber-300 border-amber-500/30';
    return 'bg-rose-500/20 text-rose-300 border-rose-500/30';
  };

  return (
    <div className="space-y-6">
      
      {/* Top Banner / Hero Score */}
      <div className="glass-panel rounded-2xl p-6 border border-slate-800 flex flex-col md:flex-row items-center justify-between gap-6 shadow-lg">
        <div className="space-y-2 text-center md:text-left">
          <div className="flex items-center justify-center md:justify-start space-x-2">
            <span className="text-xs font-bold uppercase tracking-wider text-slate-400">
              ATS Compatibility Audit
            </span>
            <span className={`text-xs font-bold px-2.5 py-0.5 rounded-full border ${getStatusBadge()}`}>
              {status} Rating
            </span>
          </div>
          <h3 className="text-2xl sm:text-3xl font-extrabold text-white">
            ATS Readability Score: {score} / 100
          </h3>
          <p className="text-xs text-slate-400 max-w-xl">
            Measures formatting extractability, section heading standards, keyword placement in context, 
            contact information machine-readability, and absence of parsing obstacles.
          </p>
        </div>

        {/* Score Radial */}
        <div className="flex items-center space-x-6">
          <div className="text-center">
            <div className="text-4xl font-black text-white">{score}%</div>
            <div className="text-[11px] text-slate-400 mt-0.5">Parse Health</div>
          </div>
          <div className="h-12 w-px bg-slate-800" />
          <div className="text-center">
            <div className="text-4xl font-black text-emerald-400">{passed_checks.length}</div>
            <div className="text-[11px] text-slate-400 mt-0.5">Passed Checks</div>
          </div>
          <div className="h-12 w-px bg-slate-800" />
          <div className="text-center">
            <div className={`text-4xl font-black ${issues.length === 0 ? 'text-emerald-400' : 'text-amber-400'}`}>
              {issues.length}
            </div>
            <div className="text-[11px] text-slate-400 mt-0.5">ATS Hazards</div>
          </div>
        </div>
      </div>

      {/* Grid: Passed Checks vs Identified Issues */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        
        {/* Left: Identified ATS Issues & Tips */}
        <div className="glass-panel rounded-2xl p-5 border border-slate-800 space-y-4">
          <h4 className="text-sm font-bold text-white flex items-center">
            <AlertTriangle className="w-4 h-4 text-amber-400 mr-2" />
            Detected Formatting & Parsing Issues ({issues.length})
          </h4>

          {issues.length === 0 ? (
            <div className="p-6 text-center text-xs text-slate-400 bg-slate-900/40 rounded-xl border border-slate-800">
              <CheckCircle2 className="w-8 h-8 text-emerald-400 mx-auto mb-2" />
              No significant ATS layout hazards detected. Your CV has clean extractable formatting!
            </div>
          ) : (
            <div className="space-y-3">
              {issues.map((issue, idx) => {
                const isHigh = issue.severity === 'high';
                const isMedium = issue.severity === 'medium';

                return (
                  <div
                    key={idx}
                    className={`p-4 rounded-xl border text-xs space-y-2 ${
                      isHigh
                        ? 'bg-rose-950/20 border-rose-500/30'
                        : isMedium
                        ? 'bg-amber-950/20 border-amber-500/30'
                        : 'bg-slate-900/60 border-slate-700/40'
                    }`}
                  >
                    <div className="flex items-center justify-between">
                      <span className="font-bold text-white flex items-center">
                        <span
                          className={`w-2 h-2 rounded-full mr-2 ${
                            isHigh ? 'bg-rose-400' : isMedium ? 'bg-amber-400' : 'bg-slate-400'
                          }`}
                        />
                        {issue.rule}
                      </span>
                      <span
                        className={`text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full ${
                          isHigh
                            ? 'bg-rose-500/20 text-rose-300 border border-rose-500/30'
                            : isMedium
                            ? 'bg-amber-500/20 text-amber-300 border border-amber-500/30'
                            : 'bg-slate-800 text-slate-400'
                        }`}
                      >
                        {issue.severity} priority
                      </span>
                    </div>

                    <p className="text-slate-300 leading-relaxed">
                      {issue.description}
                    </p>

                    <div className="pt-2 border-t border-slate-800/80 flex items-start space-x-1.5 text-indigo-300 font-medium">
                      <Wrench className="w-3.5 h-3.5 mt-0.5 shrink-0 text-indigo-400" />
                      <span><strong>Fix Recommendation:</strong> {issue.fix_tip}</span>
                    </div>
                  </div>
                );
              })}
            </div>
          )}
        </div>

        {/* Right: Passed ATS Criteria */}
        <div className="glass-panel rounded-2xl p-5 border border-slate-800 space-y-4">
          <h4 className="text-sm font-bold text-white flex items-center">
            <ShieldCheck className="w-4 h-4 text-emerald-400 mr-2" />
            Verified ATS Standards ({passed_checks.length})
          </h4>

          <div className="space-y-2.5">
            {passed_checks.map((check, idx) => (
              <div
                key={idx}
                className="p-3 rounded-xl bg-slate-900/60 border border-slate-800/80 flex items-start space-x-2.5 text-xs"
              >
                <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
                <span className="text-slate-200 font-medium">{check}</span>
              </div>
            ))}
          </div>

          {formatting_summary.word_count && (
            <div className="mt-4 pt-4 border-t border-slate-800 text-[11px] text-slate-400 flex items-center justify-between">
              <span>Word Count: <strong className="text-slate-200">{formatting_summary.word_count} words</strong></span>
              <span>Layout: <strong className="text-slate-200">Linear Single-Column</strong></span>
            </div>
          )}
        </div>

      </div>

    </div>
  );
};
