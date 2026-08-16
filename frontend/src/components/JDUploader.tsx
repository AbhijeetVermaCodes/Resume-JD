import React, { useState, useRef } from 'react';
import { Briefcase, Upload, FileText, CheckCircle2, Sparkles, Layers, Clock, Cpu } from 'lucide-react';
import { JDStructure } from '../types';

interface JDUploaderProps {
  jdText: string;
  onJDTextChange: (text: string) => void;
  jdId: string | null;
  onJDIdChange: (id: string | null) => void;
  structuredJD: JDStructure | null;
  onStructuredJDChange: (data: JDStructure | null) => void;
  onFileUpload: (file: File) => Promise<void>;
  isLoading: boolean;
}

export const JDUploader: React.FC<JDUploaderProps> = ({
  jdText,
  onJDTextChange,
  structuredJD,
  onFileUpload,
  isLoading,
}) => {
  const [mode, setMode] = useState<'paste' | 'upload'>('paste');
  const [isDragging, setIsDragging] = useState(false);
  const [fileName, setFileName] = useState<string | null>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(true);
  };

  const handleDragLeave = () => {
    setIsDragging(false);
  };

  const handleDrop = async (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(false);
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      const file = e.dataTransfer.files[0];
      setFileName(file.name);
      await onFileUpload(file);
    }
  };

  const handleFileChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      const file = e.target.files[0];
      setFileName(file.name);
      await onFileUpload(file);
    }
  };

  return (
    <div className="glass-panel rounded-2xl p-5 sm:p-6 border border-slate-800 flex flex-col h-full shadow-lg">
      
      {/* Card Header */}
      <div className="flex items-center justify-between pb-4 border-b border-slate-800/80 mb-4">
        <div className="flex items-center space-x-2.5">
          <div className="w-8 h-8 rounded-lg bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center">
            <Briefcase className="w-4 h-4 text-emerald-400" />
          </div>
          <div>
            <h2 className="text-base font-bold text-white flex items-center space-x-2">
              <span>Step 2 — Job Description (JD)</span>
              {structuredJD && (
                <span className="flex items-center text-xs font-semibold text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded-full border border-emerald-500/20">
                  <CheckCircle2 className="w-3 h-3 mr-1" /> Ready
                </span>
              )}
            </h2>
            <p className="text-xs text-slate-400">Target role responsibilities & requirements</p>
          </div>
        </div>

        {/* Tab Toggle */}
        <div className="flex items-center bg-slate-900/90 p-1 rounded-lg border border-slate-800">
          <button
            type="button"
            onClick={() => setMode('paste')}
            className={`px-3 py-1 text-xs font-semibold rounded-md transition-all ${
              mode === 'paste'
                ? 'bg-emerald-600 text-white shadow-sm'
                : 'text-slate-400 hover:text-slate-200'
            }`}
          >
            Paste Text
          </button>
          <button
            type="button"
            onClick={() => setMode('upload')}
            className={`px-3 py-1 text-xs font-semibold rounded-md transition-all ${
              mode === 'upload'
                ? 'bg-emerald-600 text-white shadow-sm'
                : 'text-slate-400 hover:text-slate-200'
            }`}
          >
            File Upload
          </button>
        </div>
      </div>

      {/* Content Area */}
      <div className="flex-1 flex flex-col">
        {mode === 'paste' ? (
          <div className="flex-1 flex flex-col">
            <textarea
              value={jdText}
              onChange={(e) => onJDTextChange(e.target.value)}
              placeholder="Paste Job Description text here... (Including Job Title, Required Qualifications, Must-Haves, Preferred Skills, and Responsibilities)"
              className="w-full flex-1 min-h-[220px] p-4 text-xs font-mono bg-slate-900/60 border border-slate-700/80 rounded-xl text-slate-200 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent resize-none"
            />
          </div>
        ) : (
          <div
            onDragOver={handleDragOver}
            onDragLeave={handleDragLeave}
            onDrop={handleDrop}
            onClick={() => fileInputRef.current?.click()}
            className={`flex-1 min-h-[220px] rounded-xl border-2 border-dashed flex flex-col items-center justify-center p-6 text-center cursor-pointer transition-all ${
              isDragging
                ? 'border-emerald-500 bg-emerald-500/10 scale-[0.99]'
                : 'border-slate-700/80 bg-slate-900/40 hover:border-emerald-500/50 hover:bg-slate-900/70'
            }`}
          >
            <input
              ref={fileInputRef}
              type="file"
              accept=".pdf,.docx,.txt"
              onChange={handleFileChange}
              className="hidden"
            />
            <div className="w-12 h-12 rounded-2xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center mb-3">
              <Upload className="w-6 h-6 text-emerald-400" />
            </div>
            <p className="text-sm font-semibold text-slate-200 mb-1">
              {fileName ? fileName : 'Drop Job Description file here or click to browse'}
            </p>
            <p className="text-xs text-slate-400 max-w-xs mb-3">
              Supports: <strong className="text-slate-300">.PDF, .DOCX, .TXT</strong>
            </p>
            {fileName && (
              <span className="inline-flex items-center text-xs font-medium text-emerald-300 bg-emerald-500/10 border border-emerald-500/30 px-3 py-1 rounded-full">
                <FileText className="w-3.5 h-3.5 mr-1.5" /> {fileName}
              </span>
            )}
          </div>
        )}

        {/* Structured JD Requirements Preview */}
        {structuredJD && (
          <div className="mt-4 p-3.5 rounded-xl bg-slate-900/70 border border-slate-800 text-xs">
            <div className="flex items-center justify-between mb-2">
              <span className="font-semibold text-slate-300 flex items-center">
                <Sparkles className="w-3.5 h-3.5 text-emerald-400 mr-1.5" />
                Detected Role Requirements
              </span>
              {structuredJD.job_title && (
                <span className="text-emerald-400 font-semibold text-[11px] truncate max-w-[200px]">
                  {structuredJD.job_title}
                </span>
              )}
            </div>

            <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 text-[11px]">
              <div className="bg-slate-800/60 p-2 rounded-lg border border-slate-700/40">
                <div className="text-slate-400 flex items-center mb-0.5">
                  <Layers className="w-3 h-3 mr-1 text-emerald-400" /> Required
                </div>
                <div className="font-bold text-white text-sm">
                  {structuredJD.required_skills?.length || 0} skills
                </div>
              </div>

              <div className="bg-slate-800/60 p-2 rounded-lg border border-slate-700/40">
                <div className="text-slate-400 flex items-center mb-0.5">
                  <Cpu className="w-3 h-3 mr-1 text-amber-400" /> Preferred
                </div>
                <div className="font-bold text-white text-sm">
                  {structuredJD.preferred_skills?.length || 0} bonus
                </div>
              </div>

              <div className="bg-slate-800/60 p-2 rounded-lg border border-slate-700/40">
                <div className="text-slate-400 flex items-center mb-0.5">
                  <Clock className="w-3 h-3 mr-1 text-indigo-400" /> Min Exp
                </div>
                <div className="font-bold text-white text-sm">
                  {structuredJD.required_years_experience ? `${structuredJD.required_years_experience}+ yrs` : 'Not specified'}
                </div>
              </div>

              <div className="bg-slate-800/60 p-2 rounded-lg border border-slate-700/40">
                <div className="text-slate-400 flex items-center mb-0.5">
                  <Briefcase className="w-3 h-3 mr-1 text-purple-400" /> Duties
                </div>
                <div className="font-bold text-white text-sm">
                  {structuredJD.responsibilities?.length || 0} bullets
                </div>
              </div>
            </div>
          </div>
        )}
      </div>

    </div>
  );
};
