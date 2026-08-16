import React, { useState } from 'react';
import { CheckCircle2, AlertTriangle, XCircle, ShieldAlert, Sparkles, Filter, Info } from 'lucide-react';
import { SkillsAnalysisResult, SkillMatchItem } from '../types';

interface KeywordAnalysisTabProps {
  skills: SkillsAnalysisResult;
}

export const KeywordAnalysisTab: React.FC<KeywordAnalysisTabProps> = ({ skills }) => {
  const [activeFilter, setActiveFilter] = useState<'all' | 'strong' | 'partial' | 'missing'>('all');

  const { strong_matches, partial_matches, missing } = skills;

  const totalCount = strong_matches.length + partial_matches.length + missing.length;

  const getFilteredItems = (): SkillMatchItem[] => {
    if (activeFilter === 'strong') return strong_matches;
    if (activeFilter === 'partial') return partial_matches;
    if (activeFilter === 'missing') return missing;
    return [...strong_matches, ...partial_matches, ...missing];
  };

  const filtered = getFilteredItems();

  return (
    <div className="space-y-6">
      
      {/* Header & Filter Controls */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h3 className="text-lg font-bold text-white flex items-center">
            <Sparkles className="w-5 h-5 text-indigo-400 mr-2" />
            Keyword & Technology Alignment
          </h3>
          <p className="text-xs text-slate-400 mt-0.5">
            Distinguishes between exact matches, synonym alignments, semantic sibling technologies, and missing gaps.
          </p>
        </div>

        {/* Filter Pills */}
        <div className="flex items-center bg-slate-900/90 p-1 rounded-xl border border-slate-800 self-start sm:self-auto overflow-x-auto max-w-full">
          <button
            onClick={() => setActiveFilter('all')}
            className={`px-3 py-1.5 text-xs font-semibold rounded-lg transition-all ${
              activeFilter === 'all'
                ? 'bg-slate-700 text-white shadow-sm'
                : 'text-slate-400 hover:text-slate-200'
            }`}
          >
            All ({totalCount})
          </button>
          <button
            onClick={() => setActiveFilter('strong')}
            className={`px-3 py-1.5 text-xs font-semibold rounded-lg flex items-center space-x-1.5 transition-all ${
              activeFilter === 'strong'
                ? 'bg-emerald-600 text-white shadow-sm'
                : 'text-emerald-400 hover:text-emerald-300'
            }`}
          >
            <CheckCircle2 className="w-3.5 h-3.5" />
            <span>Strong ({strong_matches.length})</span>
          </button>
          <button
            onClick={() => setActiveFilter('partial')}
            className={`px-3 py-1.5 text-xs font-semibold rounded-lg flex items-center space-x-1.5 transition-all ${
              activeFilter === 'partial'
                ? 'bg-amber-600 text-white shadow-sm'
                : 'text-amber-400 hover:text-amber-300'
            }`}
          >
            <AlertTriangle className="w-3.5 h-3.5" />
            <span>Partial ({partial_matches.length})</span>
          </button>
          <button
            onClick={() => setActiveFilter('missing')}
            className={`px-3 py-1.5 text-xs font-semibold rounded-lg flex items-center space-x-1.5 transition-all ${
              activeFilter === 'missing'
                ? 'bg-rose-600 text-white shadow-sm'
                : 'text-rose-400 hover:text-rose-300'
            }`}
          >
            <XCircle className="w-3.5 h-3.5" />
            <span>Missing ({missing.length})</span>
          </button>
        </div>
      </div>

      {/* Anti-Hallucination Disclaimer Banner */}
      <div className="bg-amber-500/10 border border-amber-500/30 rounded-xl p-3 sm:p-4 flex items-center space-x-3 text-xs text-amber-200">
        <ShieldAlert className="w-5 h-5 text-amber-400 shrink-0" />
        <div>
          <strong className="text-amber-300 mr-1">Anti-Hallucination Guideline:</strong>
          Only add missing or partial keywords if you genuinely have verifiable experience with them. Never fabricate skills for ATS matching.
        </div>
      </div>

      {/* Grid of Skill Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {filtered.map((item, idx) => {
          const isStrong = item.status === 'strong';
          const isPartial = item.status === 'partial';
          const isMissing = item.status === 'missing';

          return (
            <div
              key={`${item.name}-${idx}`}
              className={`rounded-2xl p-4.5 border transition-all flex flex-col justify-between ${
                isStrong
                  ? 'bg-emerald-950/20 border-emerald-500/30 hover:border-emerald-500/50'
                  : isPartial
                  ? 'bg-amber-950/20 border-amber-500/30 hover:border-amber-500/50'
                  : 'bg-rose-950/20 border-rose-500/30 hover:border-rose-500/50'
              }`}
            >
              <div>
                {/* Card Top: Name & Badges */}
                <div className="flex items-start justify-between gap-2 mb-2">
                  <div className="flex items-center space-x-2">
                    {isStrong && <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />}
                    {isPartial && <AlertTriangle className="w-4 h-4 text-amber-400 shrink-0" />}
                    {isMissing && <XCircle className="w-4 h-4 text-rose-400 shrink-0" />}
                    <h4 className="text-sm font-bold text-white tracking-tight truncate max-w-[180px]">
                      {item.name}
                    </h4>
                  </div>

                  {/* Status & Requirement Badges */}
                  <div className="flex items-center space-x-1.5 shrink-0">
                    <span
                      className={`text-[10px] font-bold px-2 py-0.5 rounded-full uppercase tracking-wider ${
                        isStrong
                          ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/30'
                          : isPartial
                          ? 'bg-amber-500/20 text-amber-300 border border-amber-500/30'
                          : 'bg-rose-500/20 text-rose-300 border border-rose-500/30'
                      }`}
                    >
                      {item.status}
                    </span>
                    <span
                      className={`text-[10px] font-semibold px-2 py-0.5 rounded-full ${
                        item.importance === 'critical'
                          ? 'bg-rose-900/60 text-rose-200 border border-rose-700/50'
                          : item.importance === 'important'
                          ? 'bg-indigo-900/60 text-indigo-200 border border-indigo-700/50'
                          : 'bg-slate-800 text-slate-400'
                      }`}
                    >
                      {item.importance}
                    </span>
                  </div>
                </div>

                {/* Category Pill */}
                <div className="text-[11px] text-slate-400 mb-3 flex items-center">
                  <span className="bg-slate-800/80 px-2 py-0.5 rounded text-slate-300 border border-slate-700/50">
                    {item.category}
                  </span>
                  <span className="mx-2 text-slate-600">•</span>
                  <span className={item.is_required ? 'text-rose-400 font-medium' : 'text-slate-400'}>
                    {item.is_required ? 'Mandatory JD Requirement' : 'Preferred Qualification'}
                  </span>
                </div>

                {/* Reasoning Description */}
                <p className="text-xs text-slate-300 leading-relaxed mb-3">
                  {item.reason}
                </p>
              </div>

              {/* Evidence Snippet (if available) */}
              {item.resume_evidence ? (
                <div className="mt-2 pt-2.5 border-t border-slate-800/80">
                  <div className="text-[10px] font-semibold uppercase tracking-wider text-slate-400 mb-1 flex items-center">
                    <Info className="w-3 h-3 text-indigo-400 mr-1" /> Resume Evidence:
                  </div>
                  <div className="text-[11px] font-mono text-slate-200 bg-slate-900/80 p-2 rounded-lg border border-slate-800 line-clamp-2">
                    "{item.resume_evidence}"
                  </div>
                </div>
              ) : (
                <div className="mt-2 pt-2.5 border-t border-slate-800/80 text-[11px] text-slate-500 italic">
                  No verifiable evidence found in resume.
                </div>
              )}
            </div>
          );
        })}
      </div>

    </div>
  );
};
