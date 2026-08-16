import React from 'react';
import { Table, CheckCircle2, AlertTriangle, XCircle, Info, Sparkles } from 'lucide-react';
import { ExperienceGapItem } from '../types';

interface ExperienceGapTableProps {
  items: ExperienceGapItem[];
}

export const ExperienceGapTable: React.FC<ExperienceGapTableProps> = ({ items }) => {
  return (
    <div className="space-y-4">
      
      {/* Header */}
      <div>
        <h3 className="text-lg font-bold text-white flex items-center">
          <Table className="w-5 h-5 text-indigo-400 mr-2" />
          Experience Gap Matrix
        </h3>
        <p className="text-xs text-slate-400 mt-0.5">
          Detailed requirement-by-requirement audit explaining the exact score derivation and evidence coverage.
        </p>
      </div>

      {/* Table Container */}
      <div className="glass-panel rounded-2xl border border-slate-800 overflow-hidden shadow-lg">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead className="bg-slate-900/90 text-slate-400 uppercase text-[10px] tracking-wider border-b border-slate-800">
              <tr>
                <th className="py-3 px-4 font-bold">JD Requirement</th>
                <th className="py-3 px-4 font-bold">Resume Evidence</th>
                <th className="py-3 px-3 font-bold text-center">Match Status</th>
                <th className="py-3 px-3 font-bold text-center">Importance</th>
                <th className="py-3 px-4 font-bold">Scoring Notes</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60 text-slate-200">
              {items.map((row, idx) => {
                const isStrong = row.match_type.toLowerCase() === 'strong';
                const isPartial = row.match_type.toLowerCase() === 'partial';
                const isMissing = row.match_type.toLowerCase() === 'missing';

                return (
                  <tr key={idx} className="hover:bg-slate-900/40 transition-colors">
                    {/* JD Requirement */}
                    <td className="py-3.5 px-4 font-semibold text-white max-w-xs">
                      {row.jd_requirement}
                    </td>

                    {/* Resume Evidence */}
                    <td className="py-3.5 px-4 font-mono text-[11px] text-slate-300 max-w-md">
                      {row.resume_evidence !== 'Not found in resume' ? (
                        <div className="bg-slate-950/70 p-2 rounded-lg border border-slate-800 text-slate-200 line-clamp-2">
                          "{row.resume_evidence}"
                        </div>
                      ) : (
                        <span className="text-slate-500 italic">Not found in resume</span>
                      )}
                    </td>

                    {/* Match Badge */}
                    <td className="py-3.5 px-3 text-center shrink-0">
                      <span
                        className={`inline-flex items-center space-x-1 px-2.5 py-1 rounded-full text-[11px] font-bold ${
                          isStrong
                            ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/30'
                            : isPartial
                            ? 'bg-amber-500/20 text-amber-300 border border-amber-500/30'
                            : 'bg-rose-500/20 text-rose-300 border border-rose-500/30'
                        }`}
                      >
                        {isStrong && <CheckCircle2 className="w-3 h-3" />}
                        {isPartial && <AlertTriangle className="w-3 h-3" />}
                        {isMissing && <XCircle className="w-3 h-3" />}
                        <span>{row.match_type}</span>
                      </span>
                    </td>

                    {/* Importance Badge */}
                    <td className="py-3.5 px-3 text-center shrink-0">
                      <span
                        className={`inline-block px-2 py-0.5 rounded text-[10px] font-semibold ${
                          row.importance.toLowerCase() === 'critical'
                            ? 'bg-rose-950/80 text-rose-300 border border-rose-800'
                            : row.importance.toLowerCase() === 'important'
                            ? 'bg-indigo-950/80 text-indigo-300 border border-indigo-800'
                            : 'bg-slate-800 text-slate-400'
                        }`}
                      >
                        {row.importance}
                      </span>
                    </td>

                    {/* Notes */}
                    <td className="py-3.5 px-4 text-slate-400 text-xs max-w-xs">
                      {row.notes || (isStrong ? 'Fully satisfied' : 'Requirement gap')}
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>

    </div>
  );
};
