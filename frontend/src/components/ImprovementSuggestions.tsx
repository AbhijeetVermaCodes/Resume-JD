import React, { useState } from 'react';
import { Lightbulb, Copy, Check, ShieldAlert, ArrowRight, Sparkles, MapPin } from 'lucide-react';
import { ImprovementItem, MissingKeywordRecommendation } from '../types';

interface ImprovementSuggestionsProps {
  recommendations: ImprovementItem[];
  missingKeywordRecs: MissingKeywordRecommendation[];
}

export const ImprovementSuggestions: React.FC<ImprovementSuggestionsProps> = ({
  recommendations,
  missingKeywordRecs,
}) => {
  const [copiedIndex, setCopiedIndex] = useState<number | null>(null);

  const handleCopy = (text: string, idx: number) => {
    navigator.clipboard.writeText(text);
    setCopiedIndex(idx);
    setTimeout(() => setCopiedIndex(null), 2000);
  };

  return (
    <div className="space-y-8">
      
      {/* Section 1: Bullet Point Rewrites with Placeholders */}
      <div className="space-y-4">
        <div className="flex items-center justify-between">
          <div>
            <h3 className="text-lg font-bold text-white flex items-center">
              <Lightbulb className="w-5 h-5 text-amber-400 mr-2" />
              Actionable Resume Bullet Rewrites
            </h3>
            <p className="text-xs text-slate-400 mt-0.5">
              Specific, high-impact bullet improvements with quantifiable placeholders. Replace <code className="text-amber-300 font-mono">[X%]</code> with your genuine metrics.
            </p>
          </div>
        </div>

        {/* Rewrites Grid */}
        <div className="space-y-4">
          {recommendations.map((rec, idx) => (
            <div
              key={idx}
              className="glass-panel rounded-2xl p-5 border border-slate-800 space-y-3 shadow-lg"
            >
              {/* Header */}
              <div className="flex items-center justify-between text-xs pb-2.5 border-b border-slate-800">
                <span className="font-bold text-indigo-400 flex items-center">
                  <Sparkles className="w-3.5 h-3.5 mr-1" />
                  Target Section: {rec.section}
                </span>
                <span className="text-[11px] text-slate-400">
                  {rec.why}
                </span>
              </div>

              {/* Original vs Recommended */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                
                {/* Original */}
                <div className="bg-slate-950/80 p-3.5 rounded-xl border border-slate-800 flex flex-col justify-between">
                  <div>
                    <div className="text-[10px] font-bold text-slate-500 uppercase tracking-wider mb-1">
                      Current Resume Snippet
                    </div>
                    <p className="text-slate-300 italic font-mono text-xs line-clamp-3">
                      "{rec.original_snippet}"
                    </p>
                  </div>
                  <div className="text-[10px] text-slate-500 mt-2">
                    Lacks action verbs & quantified business impact.
                  </div>
                </div>

                {/* Recommended */}
                <div className="bg-emerald-950/20 p-3.5 rounded-xl border border-emerald-500/30 flex flex-col justify-between">
                  <div>
                    <div className="flex items-center justify-between mb-1">
                      <span className="text-[10px] font-bold text-emerald-400 uppercase tracking-wider">
                        Recommended ATS Rewrite
                      </span>
                      <button
                        onClick={() => handleCopy(rec.recommended_rewrite, idx)}
                        className="flex items-center text-[11px] text-indigo-300 hover:text-white bg-indigo-600/20 hover:bg-indigo-600/30 px-2.5 py-0.5 rounded-md border border-indigo-500/30 transition-all"
                      >
                        {copiedIndex === idx ? (
                          <>
                            <Check className="w-3 h-3 text-emerald-400 mr-1" /> Copied
                          </>
                        ) : (
                          <>
                            <Copy className="w-3 h-3 mr-1" /> Copy
                          </>
                        )}
                      </button>
                    </div>
                    <p className="text-slate-100 font-semibold text-xs leading-relaxed">
                      "{rec.recommended_rewrite}"
                    </p>
                  </div>
                  <div className="text-[10px] text-amber-300/80 mt-2 flex items-center">
                    <ShieldAlert className="w-3 h-3 text-amber-400 mr-1 shrink-0" />
                    {rec.cautionary_note}
                  </div>
                </div>

              </div>

            </div>
          ))}
        </div>
      </div>

      {/* Section 2: Missing Keyword Natural Placement Advice */}
      {missingKeywordRecs.length > 0 && (
        <div className="space-y-4 pt-4 border-t border-slate-800">
          <div>
            <h3 className="text-lg font-bold text-white flex items-center">
              <MapPin className="w-5 h-5 text-indigo-400 mr-2" />
              Where to Naturally Add Missing Keywords
            </h3>
            <p className="text-xs text-slate-400 mt-0.5">
              Suggestions on where to incorporate priority technologies without keyword stuffing.
            </p>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            {missingKeywordRecs.map((m, idx) => (
              <div
                key={idx}
                className="glass-panel rounded-2xl p-4.5 border border-slate-800 text-xs flex flex-col justify-between space-y-3"
              >
                <div>
                  <div className="flex items-center justify-between mb-2">
                    <span className="font-bold text-white text-sm">{m.keyword}</span>
                    <span
                      className={`text-[10px] font-bold px-2 py-0.5 rounded-full ${
                        m.importance === 'Critical'
                          ? 'bg-rose-500/20 text-rose-300 border border-rose-500/30'
                          : 'bg-indigo-500/20 text-indigo-300 border border-indigo-500/30'
                      }`}
                    >
                      {m.importance}
                    </span>
                  </div>

                  <div className="text-[11px] text-indigo-300 font-semibold mb-1 flex items-center">
                    <span className="w-1.5 h-1.5 rounded-full bg-indigo-400 mr-1.5" />
                    Best Placement: {m.where_to_add}
                  </div>

                  <p className="text-slate-300 text-xs leading-relaxed">
                    {m.advice}
                  </p>
                </div>

                <div className="pt-2 border-t border-slate-800/80 text-[10px] text-amber-300/90 italic flex items-center">
                  <ShieldAlert className="w-3 h-3 text-amber-400 mr-1 shrink-0" />
                  {m.cautionary_note}
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

    </div>
  );
};
