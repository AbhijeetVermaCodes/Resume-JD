import React from 'react';
import { ShieldCheck, Lock, Trash2, CheckCircle2, X } from 'lucide-react';

interface PrivacyNoticeModalProps {
  isOpen: boolean;
  onClose: () => void;
}

export const PrivacyNoticeModal: React.FC<PrivacyNoticeModalProps> = ({ isOpen, onClose }) => {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-sm animate-in fade-in">
      <div className="bg-slate-900 border border-slate-700 rounded-2xl w-full max-w-lg p-6 space-y-5 shadow-2xl">
        
        {/* Header */}
        <div className="flex items-center justify-between pb-3 border-b border-slate-800">
          <div className="flex items-center space-x-2">
            <ShieldCheck className="w-5 h-5 text-emerald-400" />
            <h3 className="text-base font-bold text-white">Privacy & Data Security Policy</h3>
          </div>
          <button
            onClick={onClose}
            className="text-slate-400 hover:text-white transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Policy Points */}
        <div className="space-y-3.5 text-xs text-slate-300">
          <div className="flex items-start space-x-3 p-3 rounded-xl bg-slate-950/60 border border-slate-800">
            <Lock className="w-4 h-4 text-indigo-400 shrink-0 mt-0.5" />
            <div>
              <strong className="text-white block mb-0.5">Ephemeral & Confidential Processing</strong>
              Candidate CVs and Job Descriptions are analyzed strictly for matching. Resumes are not shared, sold, or used for model pre-training.
            </div>
          </div>

          <div className="flex items-start space-x-3 p-3 rounded-xl bg-slate-950/60 border border-slate-800">
            <Trash2 className="w-4 h-4 text-rose-400 shrink-0 mt-0.5" />
            <div>
              <strong className="text-white block mb-0.5">1-Click Immediate Data Erasure</strong>
              Use the "Delete Resume" button at any time to purge your uploaded document and all analysis records from the server immediately.
            </div>
          </div>

          <div className="flex items-start space-x-3 p-3 rounded-xl bg-slate-950/60 border border-slate-800">
            <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
            <div>
              <strong className="text-white block mb-0.5">No Persistent PII Tracking</strong>
              Application logs redact sensitive personally identifiable information (PII). No public indexing occurs.
            </div>
          </div>
        </div>

        {/* Close Action */}
        <div className="pt-3 border-t border-slate-800 flex justify-end">
          <button
            type="button"
            onClick={onClose}
            className="px-4 py-2 text-xs font-bold rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white transition-colors"
          >
            I Understand
          </button>
        </div>

      </div>
    </div>
  );
};
