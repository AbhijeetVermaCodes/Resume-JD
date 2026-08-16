import React from 'react';
import { Download, Printer, FileCode, Check, X, FileText } from 'lucide-react';
import { AnalysisResponse } from '../types';

interface ExportModalProps {
  isOpen: boolean;
  onClose: () => void;
  analysis: AnalysisResponse;
}

export const ExportModal: React.FC<ExportModalProps> = ({ isOpen, onClose, analysis }) => {
  if (!isOpen) return null;

  const downloadJSON = () => {
    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(analysis, null, 2));
    const downloadAnchor = document.createElement('a');
    downloadAnchor.setAttribute("href", dataStr);
    downloadAnchor.setAttribute("download", `resume_analysis_${analysis.id.slice(0, 8)}.json`);
    document.body.appendChild(downloadAnchor);
    downloadAnchor.click();
    downloadAnchor.remove();
  };

  const handlePrint = () => {
    window.print();
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-sm animate-in fade-in">
      <div className="bg-slate-900 border border-slate-700 rounded-2xl w-full max-w-md p-6 space-y-5 shadow-2xl">
        
        {/* Header */}
        <div className="flex items-center justify-between pb-3 border-b border-slate-800">
          <div className="flex items-center space-x-2">
            <Download className="w-5 h-5 text-indigo-400" />
            <h3 className="text-base font-bold text-white">Export Match Report</h3>
          </div>
          <button
            onClick={onClose}
            className="text-slate-400 hover:text-white transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Options */}
        <div className="space-y-3">
          <button
            onClick={downloadJSON}
            className="w-full flex items-center justify-between p-4 rounded-xl bg-slate-950/60 hover:bg-slate-800/80 border border-slate-800 transition-all text-left group"
          >
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 rounded-xl bg-indigo-500/10 border border-indigo-500/30 flex items-center justify-center group-hover:scale-105 transition-transform">
                <FileCode className="w-5 h-5 text-indigo-400" />
              </div>
              <div>
                <span className="text-xs font-bold text-white block">Download Full JSON Schema</span>
                <span className="text-[11px] text-slate-400">Complete raw scoring & entity metadata</span>
              </div>
            </div>
            <Download className="w-4 h-4 text-slate-400 group-hover:text-indigo-400 transition-colors" />
          </button>

          <button
            onClick={handlePrint}
            className="w-full flex items-center justify-between p-4 rounded-xl bg-slate-950/60 hover:bg-slate-800/80 border border-slate-800 transition-all text-left group"
          >
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 rounded-xl bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center group-hover:scale-105 transition-transform">
                <Printer className="w-5 h-5 text-emerald-400" />
              </div>
              <div>
                <span className="text-xs font-bold text-white block">Print / Save as PDF</span>
                <span className="text-[11px] text-slate-400">Formatted report with charts and recommendations</span>
              </div>
            </div>
            <Printer className="w-4 h-4 text-slate-400 group-hover:text-emerald-400 transition-colors" />
          </button>
        </div>

        {/* Close Button */}
        <div className="pt-3 border-t border-slate-800 flex justify-end">
          <button
            type="button"
            onClick={onClose}
            className="px-4 py-2 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700 transition-colors"
          >
            Close
          </button>
        </div>

      </div>
    </div>
  );
};
