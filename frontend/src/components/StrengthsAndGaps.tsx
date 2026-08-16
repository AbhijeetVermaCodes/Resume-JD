import React from 'react';
import { ThumbsUp, AlertOctagon, CheckCircle2, ChevronRight, Zap, Target } from 'lucide-react';
import { CriticalGapItem } from '../types';

interface StrengthsAndGapsProps {
  strengths: string[];
  criticalGaps: CriticalGapItem[];
}

export const StrengthsAndGaps: React.FC<StrengthsAndGapsProps> = ({ strengths, criticalGaps }) => {
  return (
    <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
      
      {/* Resume Strengths */}
      <div className="glass-panel rounded-2xl p-6 border border-emerald-500/20 shadow-lg space-y-4">
        <div className="flex items-center space-x-2.5 pb-3 border-b border-slate-800">
          <div className="w-8 h-8 rounded-lg bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center">
            <ThumbsUp className="w-4 h-4 text-emerald-400" />
          </div>
          <div>
            <h3 className="text-base font-bold text-white">
              Key Resume Strengths
            </h3>
            <p className="text-xs text-slate-400">High-conviction alignment with target role</p>
          </div>
        </div>

        <div className="space-y-3">
          {strengths.map((str, idx) => (
            <div
              key={idx}
              className="p-3.5 rounded-xl bg-emerald-950/20 border border-emerald-500/20 flex items-start space-x-3 text-xs"
            >
              <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
              <span className="text-slate-200 font-medium leading-relaxed">{str}</span>
            </div>
          ))}
        </div>
      </div>

      {/* Prioritized Critical Gaps */}
      <div className="glass-panel rounded-2xl p-6 border border-rose-500/20 shadow-lg space-y-4">
        <div className="flex items-center space-x-2.5 pb-3 border-b border-slate-800">
          <div className="w-8 h-8 rounded-lg bg-rose-500/10 border border-rose-500/30 flex items-center justify-center">
            <AlertOctagon className="w-4 h-4 text-rose-400" />
          </div>
          <div>
            <h3 className="text-base font-bold text-white">
              Prioritized Skill & Experience Gaps
            </h3>
            <p className="text-xs text-slate-400">Ranked by hiring manager and ATS priority</p>
          </div>
        </div>

        <div className="space-y-3">
          {criticalGaps.length === 0 ? (
            <div className="p-6 text-center text-xs text-slate-400 bg-slate-900/40 rounded-xl border border-slate-800">
              <CheckCircle2 className="w-8 h-8 text-emerald-400 mx-auto mb-2" />
              No high-priority critical gaps identified!
            </div>
          ) : (
            criticalGaps.map((gap, idx) => {
              const isHigh = gap.priority === 'High';
              const isMed = gap.priority === 'Medium';

              return (
                <div
                  key={idx}
                  className={`p-3.5 rounded-xl border text-xs space-y-1.5 ${
                    isHigh
                      ? 'bg-rose-950/20 border-rose-500/30'
                      : isMed
                      ? 'bg-amber-950/20 border-amber-500/30'
                      : 'bg-slate-900/60 border-slate-700/40'
                  }`}
                >
                  <div className="flex items-center justify-between">
                    <span className="font-bold text-white flex items-center">
                      <span className="text-slate-500 mr-2 font-mono text-[11px]">#{idx + 1}</span>
                      {gap.requirement}
                    </span>
                    <span
                      className={`text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full ${
                        isHigh
                          ? 'bg-rose-500/20 text-rose-300 border border-rose-500/30'
                          : isMed
                          ? 'bg-amber-500/20 text-amber-300 border border-amber-500/30'
                          : 'bg-slate-800 text-slate-400'
                      }`}
                    >
                      {gap.priority} Priority
                    </span>
                  </div>

                  <p className="text-slate-300 leading-relaxed text-[11px]">
                    {gap.gap_description}
                  </p>

                  <div className="text-[10px] font-semibold text-slate-400 flex items-center pt-1">
                    <Target className="w-3 h-3 text-slate-500 mr-1" />
                    <span>Impact: <strong className={isHigh ? 'text-rose-400' : 'text-slate-300'}>{gap.impact_level}</strong></span>
                  </div>
                </div>
              );
            })
          )}
        </div>
      </div>

    </div>
  );
};
