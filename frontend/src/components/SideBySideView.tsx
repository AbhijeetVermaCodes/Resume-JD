import React, { useState } from 'react';
import { SplitSquareVertical, CheckCircle2, AlertTriangle, XCircle, ArrowRight, Sparkles } from 'lucide-react';
import { SideBySideItem } from '../types';

interface SideBySideViewProps {
  items: SideBySideItem[];
}

export const SideBySideView: React.FC<SideBySideViewProps> = ({ items }) => {
  const [filter, setFilter] = useState<'all' | 'strong' | 'partial' | 'missing'>('all');

  const filtered = items.filter((item) => {
    if (filter === 'all') return true;
    return item.match_status === filter;
  });

  return (
    <div className="space-y-6">
      
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h3 className="text-lg font-bold text-white flex items-center">
            <SplitSquareVertical className="w-5 h-5 text-indigo-400 mr-2" />
            Resume vs Job Description Side-by-Side View
          </h3>
          <p className="text-xs text-slate-400 mt-0.5">
            Compare exact role requirements directly against extracted evidence from the candidate's resume.
          </p>
        </div>

        {/* Filter Pills */}
        <div className="flex items-center bg-slate-900/90 p-1 rounded-xl border border-slate-800 self-start sm:self-auto">
          <button
            onClick={() => setFilter('all')}
            className={`px-3 py-1 text-xs font-semibold rounded-lg transition-all ${
              filter === 'all' ? 'bg-slate-700 text-white' : 'text-slate-400 hover:text-slate-200'
            }`}
          >
            All ({items.length})
          </button>
          <button
            onClick={() => setFilter('strong')}
            className={`px-3 py-1 text-xs font-semibold rounded-lg transition-all ${
              filter === 'strong' ? 'bg-emerald-600 text-white' : 'text-emerald-400 hover:text-emerald-300'
            }`}
          >
            Strong
          </button>
          <button
            onClick={() => setFilter('partial')}
            className={`px-3 py-1 text-xs font-semibold rounded-lg transition-all ${
              filter === 'partial' ? 'bg-amber-600 text-white' : 'text-amber-400 hover:text-amber-300'
            }`}
          >
            Partial
          </button>
          <button
            onClick={() => setFilter('missing')}
            className={`px-3 py-1 text-xs font-semibold rounded-lg transition-all ${
              filter === 'missing' ? 'bg-rose-600 text-white' : 'text-rose-400 hover:text-rose-300'
            }`}
          >
            Missing
          </button>
        </div>
      </div>

      {/* Side-by-Side Cards List */}
      <div className="space-y-4">
        {filtered.map((item, idx) => {
          const isStrong = item.match_status === 'strong';
          const isPartial = item.match_status === 'partial';
          const isMissing = item.match_status === 'missing';

          return (
            <div
              key={idx}
              className={`glass-panel rounded-2xl p-5 border transition-all ${
                isStrong
                  ? 'border-emerald-500/30 bg-slate-900/50'
                  : isPartial
                  ? 'border-amber-500/30 bg-slate-900/50'
                  : 'border-rose-500/30 bg-slate-900/50'
              }`}
            >
              {/* Top Banner: Status & Importance */}
              <div className="flex items-center justify-between pb-3 border-b border-slate-800/80 mb-3 text-xs">
                <div className="flex items-center space-x-2">
                  <span
                    className={`inline-flex items-center space-x-1 px-2.5 py-0.5 rounded-full font-bold ${
                      isStrong
                        ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/30'
                        : isPartial
                        ? 'bg-amber-500/20 text-amber-300 border border-amber-500/30'
                        : 'bg-rose-500/20 text-rose-300 border border-rose-500/30'
                    }`}
                  >
                    {isStrong && <CheckCircle2 className="w-3.5 h-3.5 mr-1" />}
                    {isPartial && <AlertTriangle className="w-3.5 h-3.5 mr-1" />}
                    {isMissing && <XCircle className="w-3.5 h-3.5 mr-1" />}
                    <span>{item.match_badge}</span>
                  </span>
                  <span className="text-slate-400">•</span>
                  <span className="text-slate-300 font-medium">Importance: {item.importance}</span>
                </div>

                <div className="text-[11px] text-slate-400 italic">
                  {item.notes}
                </div>
              </div>

              {/* Grid Comparison */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                {/* Left: JD Requirement */}
                <div className="bg-slate-950/80 p-4 rounded-xl border border-slate-800 flex flex-col justify-between">
                  <div>
                    <div className="text-[10px] font-bold text-slate-400 uppercase tracking-wider mb-1.5 flex items-center">
                      <span className="w-2 h-2 rounded-full bg-indigo-500 mr-2" />
                      Job Description Requirement
                    </div>
                    <p className="text-slate-100 font-semibold text-sm leading-snug">
                      {item.jd_requirement}
                    </p>
                  </div>
                </div>

                {/* Right: Resume Evidence */}
                <div
                  className={`p-4 rounded-xl border flex flex-col justify-between ${
                    isStrong
                      ? 'bg-emerald-950/20 border-emerald-500/30'
                      : isPartial
                      ? 'bg-amber-950/20 border-amber-500/30'
                      : 'bg-rose-950/20 border-rose-500/30'
                  }`}
                >
                  <div>
                    <div className="text-[10px] font-bold text-slate-400 uppercase tracking-wider mb-1.5 flex items-center">
                      <span
                        className={`w-2 h-2 rounded-full mr-2 ${
                          isStrong ? 'bg-emerald-400' : isPartial ? 'bg-amber-400' : 'bg-rose-400'
                        }`}
                      />
                      Resume Evidence
                    </div>
                    <p className="font-mono text-xs text-slate-200 leading-relaxed">
                      {item.resume_evidence !== 'Not found in resume'
                        ? `"${item.resume_evidence}"`
                        : 'No supporting evidence or mention found in candidate CV.'}
                    </p>
                  </div>
                </div>
              </div>

            </div>
          );
        })}
      </div>

    </div>
  );
};
