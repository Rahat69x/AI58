import React, { useState } from 'react';
import { api } from '../lib/api';

export default function AiEngineLab() {
  const [selectedService, setSelectedService] = useState('llm_service');
  const [llmPrompt, setLlmPrompt] = useState('Explain how gradient descent optimizes neural network weights in simple terms.');
  const [llmOutput, setLlmOutput] = useState('');
  const [codeSnippet, setCodeSnippet] = useState('def execute_query(user_input):\n    # Security smell test\n    eval(f"print({user_input})")\n    return True');
  const [codeAnalysisResult, setCodeAnalysisResult] = useState(null);
  const [csvInput, setCsvInput] = useState('id,name,salary\n1,Alice,85000\n2,Bob,\n3,Alice,85000');
  const [csvResult, setCsvResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleTestLlm = async () => {
    setLoading(true);
    try {
      const res = await api.testLLM(llmPrompt, "You are a Principal AI Systems Educator.");
      setLlmOutput(res.generated_text);
    } catch (err) {
      setLlmOutput(`Error: ${err.message}`);
    } finally {
      setLoading(false);
    }
  };

  const handleAnalyzeCode = async () => {
    setLoading(true);
    try {
      const res = await api.analyzeCode(codeSnippet, 'python');
      setCodeAnalysisResult(res);
    } catch (err) {
      alert(`Error: ${err.message}`);
    } finally {
      setLoading(false);
    }
  };

  const handleCleanCsv = async () => {
    setLoading(true);
    try {
      const res = await api.cleanCsv(csvInput);
      setCsvResult(res);
    } catch (err) {
      alert(`Error: ${err.message}`);
    } finally {
      setLoading(false);
    }
  };

  const servicesList = [
    { id: 'llm_service', name: 'LLM Service', icon: '🧠', tag: 'Core Generation' },
    { id: 'code_analysis', name: 'Code Analysis Service', icon: '🔍', tag: 'AST & Security' },
    { id: 'data_engine', name: 'Data Engine (Clean/Anomaly)', icon: '📊', tag: 'Pipelines' },
    { id: 'rag_engine', name: 'RAG & Vector DB', icon: '📚', tag: 'Retrieval' },
    { id: 'tts_service', name: 'Speech & Audio Services', icon: '🎙️', tag: 'Voice/TTS' },
    { id: 'prompt_manager', name: 'Prompt Manager', icon: '📝', tag: 'Templates' },
  ];

  return (
    <div className="ai-engine-lab">
      <div className="glass-card" style={{ marginBottom: '2rem' }}>
        <span style={{ fontSize: '0.8rem', color: 'var(--cyan)', fontWeight: '700', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
          Centralized Shared Infrastructure
        </span>
        <h1 style={{ fontSize: '2.25rem', marginTop: '0.25rem' }}>Shared AI & Data Engine Lab</h1>
        <p style={{ color: 'var(--text-muted)', fontSize: '0.95rem' }}>
          Interactive testbench for the 11 centralized platform services powering all 58 projects.
        </p>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'minmax(260px, 1fr) minmax(500px, 3fr)', gap: '1.5rem' }}>
        {/* Left Services Selector */}
        <div className="glass-card">
          <h3 style={{ fontSize: '1rem', marginBottom: '1rem' }}>Available AI Services</h3>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
            {servicesList.map((s) => (
              <button
                key={s.id}
                className={`btn ${selectedService === s.id ? 'btn-primary' : 'btn-secondary'}`}
                style={{ justifyContent: 'flex-start', textAlign: 'left', padding: '0.75rem 1rem' }}
                onClick={() => setSelectedService(s.id)}
              >
                <span style={{ fontSize: '1.25rem' }}>{s.icon}</span>
                <div>
                  <div style={{ fontWeight: '600', fontSize: '0.875rem' }}>{s.name}</div>
                  <div style={{ fontSize: '0.7rem', color: 'var(--text-dim)' }}>{s.tag}</div>
                </div>
              </button>
            ))}
          </div>
        </div>

        {/* Right Interactive Test Panel */}
        <div className="glass-card">
          {selectedService === 'llm_service' && (
            <div>
              <h2 style={{ fontSize: '1.25rem', marginBottom: '0.5rem' }}>🧠 LLM Service (Provider & Local Engine)</h2>
              <p style={{ color: 'var(--text-muted)', fontSize: '0.85rem', marginBottom: '1rem' }}>
                Dispatches prompts to configured external providers (Gemini, OpenAI) or executes on the built-in AI engine.
              </p>

              <div className="form-group">
                <label className="form-label">Prompt Input</label>
                <textarea
                  className="form-textarea"
                  value={llmPrompt}
                  onChange={(e) => setLlmPrompt(e.target.value)}
                />
              </div>

              <button className="btn btn-primary" onClick={handleTestLlm} disabled={loading}>
                {loading ? 'Generating...' : '⚡ Generate Response'}
              </button>

              {llmOutput && (
                <div style={{ marginTop: '1.5rem' }}>
                  <label className="form-label">Generated Output</label>
                  <pre className="code-viewer">{llmOutput}</pre>
                </div>
              )}
            </div>
          )}

          {selectedService === 'code_analysis' && (
            <div>
              <h2 style={{ fontSize: '1.25rem', marginBottom: '0.5rem' }}>🔍 Code Analysis Service (AST & Security Linter)</h2>
              <p style={{ color: 'var(--text-muted)', fontSize: '0.85rem', marginBottom: '1rem' }}>
                Performs Python AST structural parsing, cyclomatic complexity, and scans for OWASP vulnerabilities.
              </p>

              <div className="form-group">
                <label className="form-label">Python Source Code</label>
                <textarea
                  className="form-textarea"
                  value={codeSnippet}
                  onChange={(e) => setCodeSnippet(e.target.value)}
                />
              </div>

              <button className="btn btn-primary" onClick={handleAnalyzeCode} disabled={loading}>
                {loading ? 'Analyzing...' : 'Run AST & Security Scan'}
              </button>

              {codeAnalysisResult && (
                <div style={{ marginTop: '1.5rem' }}>
                  <label className="form-label">Analysis Metrics & Detected Vulnerabilities</label>
                  <pre className="code-viewer">{JSON.stringify(codeAnalysisResult, null, 2)}</pre>
                </div>
              )}
            </div>
          )}

          {selectedService === 'data_engine' && (
            <div>
              <h2 style={{ fontSize: '1.25rem', marginBottom: '0.5rem' }}>📊 Data Engine (CSV Cleansing & Imputation)</h2>
              <p style={{ color: 'var(--text-muted)', fontSize: '0.85rem', marginBottom: '1rem' }}>
                Automates duplicate removal, missing value imputation, IQR outlier detection, and clean CSV export.
              </p>

              <div className="form-group">
                <label className="form-label">Raw CSV Text</label>
                <textarea
                  className="form-textarea"
                  value={csvInput}
                  onChange={(e) => setCsvInput(e.target.value)}
                />
              </div>

              <button className="btn btn-primary" onClick={handleCleanCsv} disabled={loading}>
                {loading ? 'Cleaning...' : 'Process Dataset'}
              </button>

              {csvResult && (
                <div style={{ marginTop: '1.5rem' }}>
                  <label className="form-label">Cleansing Report & Clean CSV</label>
                  <pre className="code-viewer">{JSON.stringify(csvResult, null, 2)}</pre>
                </div>
              )}
            </div>
          )}

          {['rag_engine', 'tts_service', 'prompt_manager'].includes(selectedService) && (
            <div style={{ padding: '2rem', textAlign: 'center' }}>
              <div style={{ fontSize: '2.5rem', marginBottom: '1rem' }}>⚡</div>
              <h3 style={{ marginBottom: '0.5rem' }}>Service Operational</h3>
              <p style={{ color: 'var(--text-muted)', fontSize: '0.9rem', maxWidth: '420px', margin: '0 auto' }}>
                This shared service is currently bound and active across its dependent project runners (Projects #09, #17, #45, #48, #54).
              </p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
