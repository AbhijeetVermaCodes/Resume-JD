import React from 'react';
import { Sparkles, Sliders, ShieldCheck, FileCheck, RotateCcw } from 'lucide-react';

interface NavbarProps {
  onLoadDemo: () => void;
  onOpenWeightsModal: () => void;
  onOpenPrivacyModal: () => void;
  onReset: () => void;
  hasAnalysis: boolean;
  isLoading: boolean;
}

export const Navbar: React.FC<NavbarProps> = ({
  onLoadDemo,
  onOpenWeightsModal,
  onOpenPrivacyModal,
  onReset,
  hasAnalysis,
  isLoading,
}) => {
  return (
    <header className="sticky top-0 z-40 w-full border-b border-slate-800 bg-slate-950/85 backdrop-blur-md">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
        
        {/* Brand */}
        <div className="flex items-center space-x-3 cursor-pointer" onClick={onReset}>
          <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-indigo-600 via-indigo-500 to-emerald-400 flex items-center justify-center shadow-glow">
            <FileCheck className="w-5 h-5 text-white" />
          </div>
          <div>
            <div className="flex items-center space-x-2">
              <span className="text-xl font-extrabold tracking-tight bg-gradient-to-r from-white via-slate-100 to-indigo-200 bg-clip-text text-transparent">
                MatchCraft<span className="text-indigo-400">.AI</span>
              </span>
              <span className="px-2 py-0.5 text-xs font-semibold uppercase tracking-wider bg-indigo-500/10 text-indigo-400 border border-indigo-500/20 rounded-full">
                ATS v2.5
              </span>
            </div>
            <p className="text-xs text-slate-400 font-medium hidden sm:block">
              Semantic Resume & Job Matcher
            </p>
          </div>
        </div>

        {/* Action Controls */}
        <div className="flex items-center space-x-2 sm:space-x-3">
          {/* 1-Click Demo Button */}
          <button
            onClick={onLoadDemo}
            disabled={isLoading}
            className="flex items-center space-x-1.5 px-3 py-1.5 sm:px-4 sm:py-2 text-xs sm:text-sm font-semibold rounded-lg bg-indigo-600/20 hover:bg-indigo-600/30 text-indigo-300 border border-indigo-500/30 transition-all hover:shadow-glow disabled:opacity-50"
            title="Load Software Engineer Resume & Cloud Platforms JD"
          >
            <Sparkles className="w-4 h-4 text-indigo-400 animate-pulse" />
            <span>Load Demo</span>
          </button>

          {/* Weights Config Modal Button */}
          <button
            onClick={onOpenWeightsModal}
            className="flex items-center space-x-1.5 px-3 py-1.5 sm:px-3.5 sm:py-2 text-xs sm:text-sm font-medium rounded-lg bg-slate-900 hover:bg-slate-800 text-slate-300 border border-slate-700/60 transition-colors"
            title="Configure category scoring weights"
          >
            <Sliders className="w-4 h-4 text-slate-400" />
            <span className="hidden md:inline">Weights</span>
          </button>

          {/* Privacy Button */}
          <button
            onClick={onOpenPrivacyModal}
            className="flex items-center space-x-1.5 px-2.5 py-1.5 sm:px-3 sm:py-2 text-xs sm:text-sm font-medium rounded-lg bg-slate-900/80 hover:bg-slate-800 text-emerald-400 border border-emerald-500/20 transition-colors"
            title="Privacy and Data Retention Guarantee"
          >
            <ShieldCheck className="w-4 h-4 text-emerald-400" />
            <span className="hidden lg:inline">Privacy Safe</span>
          </button>

          {/* Reset / New Analysis */}
          {hasAnalysis && (
            <button
              onClick={onReset}
              className="flex items-center space-x-1.5 px-3 py-1.5 sm:px-3.5 sm:py-2 text-xs sm:text-sm font-medium rounded-lg bg-rose-500/10 hover:bg-rose-500/20 text-rose-300 border border-rose-500/30 transition-colors"
            >
              <RotateCcw className="w-4 h-4 text-rose-400" />
              <span className="hidden sm:inline">New Analysis</span>
            </button>
          )}
        </div>

      </div>
    </header>
  );
};
