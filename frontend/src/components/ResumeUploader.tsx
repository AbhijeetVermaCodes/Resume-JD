import React, { useState, useRef } from 'react';
import { Upload, FileText, Trash2, CheckCircle2, AlertCircle, Sparkles, User, Code, Briefcase, GraduationCap } from 'lucide-react';
import { ResumeStructure } from '../types';

interface ResumeUploaderProps {
  resumeText: string;
  onResumeTextChange: (text: string) => void;
  resumeId: string | null;
  onResumeIdChange: (id: string | null) => void;
  structuredResume: ResumeStructure | null;
  onStructuredResumeChange: (data: ResumeStructure | null) => void;
  onFileUpload: (file: File) => Promise<void>;
  onDeleteResume: () => Promise<void>;
  isLoading: boolean;
}

export const ResumeUploader: React.FC<ResumeUploaderProps> = ({
  resumeText,
  onResumeTextChange,
  resumeId,
  structuredResume,
  onFileUpload,
  onDeleteResume,
  isLoading,
}) => {
  const [mode, setMode] = useState<'upload' | 'paste'>('upload');
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
          <div className="w-8 h-8 rounded-lg bg-indigo-500/10 border border-indigo-500/30 flex items-center justify-center">
            <User className="w-4 h-4 text-indigo-400" />
          </div>
          <div>
            <h2 className="text-base font-bold text-white flex items-center space-x-2">
              <span>Step 1 — Candidate Resume</span>
              {structuredResume && (
                <span className="flex items-center text-xs font-semibold text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded-full border border-emerald-500/20">
                  <CheckCircle2 className="w-3 h-3 mr-1" /> Ready
                </span>
              )}
            </h2>
            <p className="text-xs text-slate-400">PDF, DOCX, TXT or manual text</p>
          </div>
        </div>

        {/* Tab Toggle */}
        <div className="flex items-center bg-slate-900/90 p-1 rounded-lg border border-slate-800">
          <button
            type="button"
            onClick={() => setMode('upload')}
            className={`px-3 py-1 text-xs font-semibold rounded-md transition-all ${
              mode === 'upload'
                ? 'bg-indigo-600 text-white shadow-sm'
                : 'text-slate-400 hover:text-slate-200'
            }`}
          >
            File Upload
          </button>
          <button
            type="button"
            onClick={() => setMode('paste')}
            className={`px-3 py-1 text-xs font-semibold rounded-md transition-all ${
              mode === 'paste'
                ? 'bg-indigo-600 text-white shadow-sm'
                : 'text-slate-400 hover:text-slate-200'
            }`}
          >
            Paste Text
          </button>
        </div>
      </div>

      {/* Content Area */}
      <div className="flex-1 flex flex-col">
        {mode === 'upload' ? (
          <div
            onDragOver={handleDragOver}
            onDragLeave={handleDragLeave}
            onDrop={handleDrop}
            onClick={() => fileInputRef.current?.click()}
            className={`flex-1 min-h-[220px] rounded-xl border-2 border-dashed flex flex-col items-center justify-center p-6 text-center cursor-pointer transition-all ${
              isDragging
                ? 'border-indigo-500 bg-indigo-500/10 scale-[0.99]'
                : 'border-slate-700/80 bg-slate-900/40 hover:border-indigo-500/50 hover:bg-slate-900/70'
            }`}
          >
            <input
              ref={fileInputRef}
              type="file"
              accept=".pdf,.docx,.txt"
              onChange={handleFileChange}
              className="hidden"
            />
            <div className="w-12 h-12 rounded-2xl bg-indigo-500/10 border border-indigo-500/20 flex items-center justify-center mb-3">
              <Upload className="w-6 h-6 text-indigo-400" />
            </div>
            <p className="text-sm font-semibold text-slate-200 mb-1">
              {fileName ? fileName : 'Drop resume file here or click to browse'}
            </p>
            <p className="text-xs text-slate-400 max-w-xs mb-3">
              Supports standard ATS formats: <strong className="text-slate-300">.PDF, .DOCX, .TXT</strong> (Max 10MB)
            </p>
            {fileName && (
              <span className="inline-flex items-center text-xs font-medium text-indigo-300 bg-indigo-500/10 border border-indigo-500/30 px-3 py-1 rounded-full">
                <FileText className="w-3.5 h-3.5 mr-1.5" /> {fileName}
              </span>
            )}
          </div>
        ) : (
          <div className="flex-1 flex flex-col">
            <textarea
              value={resumeText}
              onChange={(e) => onResumeTextChange(e.target.value)}
              placeholder="Paste candidate resume or CV text here... (Including Work Experience, Technical Skills, Education, Projects, and Summary)"
              className="w-full flex-1 min-h-[220px] p-4 text-xs font-mono bg-slate-900/60 border border-slate-700/80 rounded-xl text-slate-200 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent resize-none"
            />
          </div>
        )}

        {/* Structured Sections Preview */}
        {structuredResume && (
          <div className="mt-4 p-3.5 rounded-xl bg-slate-900/70 border border-slate-800 text-xs">
            <div className="flex items-center justify-between mb-2">
              <span className="font-semibold text-slate-300 flex items-center">
                <Sparkles className="w-3.5 h-3.5 text-indigo-400 mr-1.5" />
                Parsed Structure Preview
              </span>
              {structuredResume.candidate_name && (
                <span className="text-slate-400 font-mono text-[11px]">
                  {structuredResume.candidate_name}
                </span>
              )}
            </div>

            <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 text-[11px]">
              <div className="bg-slate-800/60 p-2 rounded-lg border border-slate-700/40">
                <div className="text-slate-400 flex items-center mb-0.5">
                  <Code className="w-3 h-3 mr-1 text-emerald-400" /> Skills
                </div>
                <div className="font-bold text-white text-sm">
                  {structuredResume.skills?.length || 0} items
                </div>
              </div>

              <div className="bg-slate-800/60 p-2 rounded-lg border border-slate-700/40">
                <div className="text-slate-400 flex items-center mb-0.5">
                  <Briefcase className="w-3 h-3 mr-1 text-indigo-400" /> Roles
                </div>
                <div className="font-bold text-white text-sm">
                  {structuredResume.work_experience?.length || 0} entries
                </div>
              </div>

              <div className="bg-slate-800/60 p-2 rounded-lg border border-slate-700/40">
                <div className="text-slate-400 flex items-center mb-0.5">
                  <GraduationCap className="w-3 h-3 mr-1 text-amber-400" /> Education
                </div>
                <div className="font-bold text-white text-sm">
                  {structuredResume.education?.length || 0} degrees
                </div>
              </div>

              <div className="bg-slate-800/60 p-2 rounded-lg border border-slate-700/40">
                <div className="text-slate-400 flex items-center mb-0.5">
                  <FileText className="w-3 h-3 mr-1 text-purple-400" /> Projects
                </div>
                <div className="font-bold text-white text-sm">
                  {structuredResume.projects?.length || 0} projects
                </div>
              </div>
            </div>

            {/* Privacy Delete Action */}
            {(resumeId || resumeText) && (
              <div className="mt-3 pt-2.5 border-t border-slate-800 flex items-center justify-between">
                <span className="text-[11px] text-slate-400">
                  Data kept in memory & ephemeral DB session.
                </span>
                <button
                  type="button"
                  onClick={onDeleteResume}
                  disabled={isLoading}
                  className="flex items-center text-[11px] font-semibold text-rose-400 hover:text-rose-300 transition-colors"
                >
                  <Trash2 className="w-3 h-3 mr-1" /> Delete Resume
                </button>
              </div>
            )}
          </div>
        )}
      </div>

    </div>
  );
};
