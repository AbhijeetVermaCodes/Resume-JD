import React, { useState } from 'react';
import { Sliders, RotateCcw, Check, X, Info } from 'lucide-react';
import { ScoringWeights } from '../types';

interface WeightConfigModalProps {
  isOpen: boolean;
  onClose: () => void;
  currentWeights: ScoringWeights;
  onSaveWeights: (newWeights: ScoringWeights) => void;
}

const DEFAULT_WEIGHTS: ScoringWeights = {
  weight_skills: 0.35,
  weight_experience: 0.20,
  weight_responsibilities: 0.15,
  weight_education: 0.10,
  weight_projects: 0.10,
  weight_soft_skills: 0.05,
  weight_ats_quality: 0.05,
};

export const WeightConfigModal: React.FC<WeightConfigModalProps> = ({
  isOpen,
  onClose,
  currentWeights,
  onSaveWeights,
}) => {
  const [weights, setWeights] = useState<ScoringWeights>({ ...currentWeights });

  if (!isOpen) return null;

  const totalRaw =
    weights.weight_skills +
    weights.weight_experience +
    weights.weight_responsibilities +
    weights.weight_education +
    weights.weight_projects +
    weights.weight_soft_skills +
    weights.weight_ats_quality;

  const getPercent = (val: number) => {
    return totalRaw > 0 ? Math.round((val / totalRaw) * 100) : 0;
  };

  const handleSliderChange = (key: keyof ScoringWeights, value: number) => {
    setWeights((prev) => ({
      ...prev,
      [key]: value,
    }));
  };

  const handleReset = () => {
    setWeights({ ...DEFAULT_WEIGHTS });
  };

  const handleSave = () => {
    onSaveWeights(weights);
    onClose();
  };

  const weightSliders = [
    { key: 'weight_skills' as keyof ScoringWeights, label: 'Skill & Tech Keyword Match', desc: 'Programming languages, frameworks, cloud, databases' },
    { key: 'weight_experience' as keyof ScoringWeights, label: 'Experience & Seniority Match', desc: 'Years of experience, relevant industry tenure' },
    { key: 'weight_responsibilities' as keyof ScoringWeights, label: 'Responsibilities & Domain Match', desc: 'Previous work duties matching JD role' },
    { key: 'weight_education' as keyof ScoringWeights, label: 'Education & Certifications', desc: 'Degrees, majors, and verified credentials' },
    { key: 'weight_projects' as keyof ScoringWeights, label: 'Projects & Achievements', desc: 'Hands-on project work and measurable impact' },
    { key: 'weight_soft_skills' as keyof ScoringWeights, label: 'Soft Skills & Collaboration', desc: 'Communication, leadership, Agile/Scrum' },
    { key: 'weight_ats_quality' as keyof ScoringWeights, label: 'Resume Quality & ATS Health', desc: 'Standard headings, layout, and contact data' },
  ];

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-sm animate-in fade-in">
      <div className="bg-slate-900 border border-slate-700 rounded-2xl w-full max-w-xl p-6 space-y-5 shadow-2xl overflow-hidden max-h-[90vh] flex flex-col">
        
        {/* Header */}
        <div className="flex items-center justify-between pb-3 border-b border-slate-800">
          <div className="flex items-center space-x-2">
            <Sliders className="w-5 h-5 text-indigo-400" />
            <h3 className="text-base font-bold text-white">Customize Scoring Weights</h3>
          </div>
          <button
            onClick={onClose}
            className="text-slate-400 hover:text-white transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Info Banner */}
        <div className="bg-indigo-500/10 border border-indigo-500/20 p-3 rounded-xl flex items-start space-x-2 text-xs text-indigo-200">
          <Info className="w-4 h-4 text-indigo-400 shrink-0 mt-0.5" />
          <span>
            Adjust weights to tailor the match calculation to specific hiring manager preferences (e.g. prioritizing raw technical skills vs. domain tenure).
          </span>
        </div>

        {/* Sliders List */}
        <div className="flex-1 overflow-y-auto space-y-4 pr-1 text-xs">
          {weightSliders.map(({ key, label, desc }) => {
            const val = weights[key];
            const pct = getPercent(val);

            return (
              <div key={key} className="space-y-1.5 bg-slate-950/60 p-3 rounded-xl border border-slate-800/80">
                <div className="flex items-center justify-between">
                  <div>
                    <span className="font-bold text-slate-200">{label}</span>
                    <p className="text-[11px] text-slate-400">{desc}</p>
                  </div>
                  <span className="font-extrabold text-indigo-400 font-mono text-sm">
                    {pct}%
                  </span>
                </div>
                <input
                  type="range"
                  min="0.0"
                  max="1.0"
                  step="0.05"
                  value={val}
                  onChange={(e) => handleSliderChange(key, parseFloat(e.target.value))}
                  className="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-indigo-500"
                />
              </div>
            );
          })}
        </div>

        {/* Footer Actions */}
        <div className="flex items-center justify-between pt-3 border-t border-slate-800">
          <button
            type="button"
            onClick={handleReset}
            className="flex items-center text-xs font-semibold text-slate-400 hover:text-slate-200 transition-colors"
          >
            <RotateCcw className="w-3.5 h-3.5 mr-1" /> Reset to Defaults
          </button>

          <div className="flex items-center space-x-2">
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700 transition-colors"
            >
              Cancel
            </button>
            <button
              type="button"
              onClick={handleSave}
              className="px-4 py-2 text-xs font-bold rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white shadow-glow transition-all flex items-center space-x-1"
            >
              <Check className="w-3.5 h-3.5" />
              <span>Apply Weights</span>
            </button>
          </div>
        </div>

      </div>
    </div>
  );
};
