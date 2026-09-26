import React, { useState, useEffect } from 'react';
import { api } from '../lib/api';

export default function ProjectWorkbench({
  project,
  onBack,
  onToggleFavorite,
  onOpenProject
}) {
  const [activeTab, setActiveTab] = useState('workbench'); // 'workbench' | 'documentation' | 'history'
  const [inputsJson, setInputsJson] = useState(JSON.stringify(project.default_input, null, 2));
  const [output, setOutput] = useState(null);
  const [executionTime, setExecutionTime] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [history, setHistory] = useState([]);
  const [checklist, setChecklist] = useState(project.checklist || {
    scaffold: true, ui: true, backend: true, ai_integration: true,
    database: true, testing: true, documentation: true, deployment: true
  });
  const [saveSuccess, setSaveSuccess] = useState(false);

  useEffect(() => {
    // Reset view when project changes
    setInputsJson(JSON.stringify(project.default_input, null, 2));
    setOutput(null);
    setExecutionTime(null);
    setError(null);
    setActiveTab('workbench');
    loadHistory();
  }, [project.id]);

  const loadHistory = async () => {
    try {
      const res = await api.getProjectHistory(project.id);
      setHistory(res.history || []);
    } catch (err) {
      console.warn("Could not load project history:", err);
    }
  };

  const handleRun = async () => {
    setLoading(true);
    setError(null);
    setSaveSuccess(false);

    try {
      let parsedInputs = {};
      try {
        parsedInputs = JSON.parse(inputsJson);
      } catch (e) {
        throw new Error("Invalid JSON input syntax. Please verify JSON format.");
      }

      const res = await api.runProject(project.id, parsedInputs);
      setOutput(res.output);
      setExecutionTime(res.execution_time_ms);
      loadHistory();
    } catch (err) {
      setError(err.message || "Execution encountered an error.");
    } finally {
      setLoading(false);
    }
  };

  const handleSaveOutput = async () => {
    if (!output) return;
    try {
      await api.saveOutput(
        project.id,
        `${project.name} Run Output`,
        `Saved execution at ${new Date().toLocaleTimeString()}`,
        output
      );
      setSaveSuccess(true);
      setTimeout(() => setSaveSuccess(false), 3000);
    } catch (err) {
      alert("Please sign in to save outputs to your profile.");
    }
  };

  const handleChecklistToggle = async (key) => {
    const updated = { ...checklist, [key]: !checklist[key] };
    setChecklist(updated);
    try {
      await api.updateChecklist(project.id, updated);
    } catch (e) {
      // Ignored if guest
    }
  };

  const tierClass =
    project.tier === 'BEGINNER'
      ? 'tier-beginner'
      : project.tier === 'INTERMEDIATE'
      ? 'tier-intermediate'
      : 'tier-advanced';

  return (
    <div className="project-workbench-view">
      {/* Top Breadcrumb & Navigation */}
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '1.5rem' }}>
        <button className="btn btn-secondary btn-sm" onClick={onBack}>
          ← Back to All Projects
        </button>

        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          {project.id > 1 && (
            <button className="btn btn-secondary btn-sm" onClick={() => onOpenProject(project.id - 1)}>
              ← #{String(project.id - 1).padStart(2, '0')} Prev
            </button>
          )}
          {project.id < 58 && (
            <button className="btn btn-secondary btn-sm" onClick={() => onOpenProject(project.id + 1)}>
              #{String(project.id + 1).padStart(2, '0')} Next →
            </button>
          )}
        </div>
      </div>

      {/* Main Project Header Card */}
      <div className="glass-card" style={{ marginBottom: '1.5rem' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '1rem', marginBottom: '1rem' }}>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', marginBottom: '0.5rem' }}>
              <span className="project-number" style={{ fontSize: '0.9rem', padding: '0.2rem 0.6rem' }}>
                #{String(project.id).padStart(2, '0')}
              </span>
              <span className={`tier-badge ${tierClass}`}>{project.tier}</span>
              <span style={{ fontSize: '0.85rem', color: 'var(--cyan)', fontWeight: '600' }}>
                {project.category}
              </span>
              <span style={{ fontSize: '0.75rem', background: 'rgba(16, 185, 129, 0.15)', color: '#34d399', padding: '0.15rem 0.5rem', borderRadius: '4px', fontWeight: '700' }}>
                ● STATUS: {project.status}
              </span>
            </div>
            <h1 style={{ fontSize: '2rem', marginBottom: '0.5rem' }}>{project.name}</h1>
            <p style={{ color: 'var(--text-muted)', fontSize: '0.95rem', maxWidth: '900px' }}>
              {project.description}
            </p>
          </div>

          <button
            className="btn btn-secondary btn-sm"
            onClick={() => onToggleFavorite(project.id)}
            style={{ fontSize: '1.25rem', padding: '0.4rem 0.8rem' }}
          >
            <span style={{ color: project.is_favorite ? '#f59e0b' : 'inherit' }}>
              {project.is_favorite ? '★ Favorited' : '☆ Favorite'}
            </span>
          </button>
        </div>

        {/* Technologies Tags */}
        <div className="tech-tags" style={{ marginBottom: '1.25rem' }}>
          {project.technologies.map((t, idx) => (
            <span key={idx} className="tech-tag" style={{ fontSize: '0.75rem', padding: '0.2rem 0.6rem' }}>
              {t}
            </span>
          ))}
        </div>

        {/* 5 Core Action Buttons as required by Section 8 */}
        <div style={{ display: 'flex', gap: '0.75rem', flexWrap: 'wrap', borderTop: '1px solid var(--border-subtle)', paddingTop: '1rem' }}>
          <button
            className={`btn ${activeTab === 'workbench' ? 'btn-primary' : 'btn-secondary'}`}
            onClick={() => setActiveTab('workbench')}
          >
            <span>📖</span> [OPEN]
          </button>

          <button
            className="btn btn-run"
            onClick={handleRun}
            disabled={loading}
          >
            <span>{loading ? '⏳' : '▶'}</span> [RUN]
          </button>

          <button
            className="btn btn-secondary"
            onClick={handleSaveOutput}
            disabled={!output}
            title={!output ? 'Run project first to save output' : 'Save output'}
          >
            <span>💾</span> {saveSuccess ? 'Saved!' : '[SAVE]'}
          </button>

          <button
            className={`btn ${activeTab === 'history' ? 'btn-primary' : 'btn-secondary'}`}
            onClick={() => setActiveTab('history')}
          >
            <span>📜</span> [HISTORY] ({history.length})
          </button>

          <button
            className={`btn ${activeTab === 'documentation' ? 'btn-primary' : 'btn-secondary'}`}
            onClick={() => setActiveTab('documentation')}
          >
            <span>📄</span> [DOCUMENTATION]
          </button>
        </div>
      </div>

      {/* 8-Point Deployment Checklist Tracking Widget */}
      <div className="glass-card" style={{ marginBottom: '1.5rem', padding: '1.25rem' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.75rem' }}>
          <span style={{ fontSize: '0.85rem', fontWeight: '700', textTransform: 'uppercase', letterSpacing: '0.05em', color: 'var(--text-dim)' }}>
            8-Point Production Checklist & Deployment Verification
          </span>
          <span style={{ fontSize: '0.8rem', color: '#34d399', fontWeight: '700' }}>
            {Object.values(checklist).filter(Boolean).length}/8 Ready
          </span>
        </div>

        <div className="checklist-grid">
          {Object.entries(checklist).map(([key, val]) => (
            <div
              key={key}
              className={`checklist-item ${val ? 'checked' : ''}`}
              onClick={() => handleChecklistToggle(key)}
            >
              <span>{val ? '☑' : '☐'}</span>
              <span style={{ textTransform: 'capitalize' }}>{key.replace('_', ' ')}</span>
            </div>
          ))}
        </div>
      </div>

      {/* Tab: WORKBENCH (Input & Output Panes) */}
      {activeTab === 'workbench' && (
        <div style={{ display: 'grid', gridTemplateColumns: 'minmax(350px, 1fr) minmax(400px, 1.2fr)', gap: '1.5rem' }}>
          {/* Left Column: Input Workbench & Capabilities */}
          <div className="glass-card">
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
              <h3 style={{ fontSize: '1.1rem' }}>📥 Project Input Parameters</h3>
              <button
                className="btn btn-secondary btn-sm"
                onClick={() => setInputsJson(JSON.stringify(project.default_input, null, 2))}
              >
                Reset Defaults
              </button>
            </div>

            <div className="form-group">
              <label className="form-label">Input Payload (JSON)</label>
              <textarea
                className="form-textarea"
                style={{ height: '320px' }}
                value={inputsJson}
                onChange={(e) => setInputsJson(e.target.value)}
              />
            </div>

            <button
              className="btn btn-run"
              style={{ width: '100%' }}
              onClick={handleRun}
              disabled={loading}
            >
              <span>{loading ? '⏳' : '⚡'}</span> {loading ? 'Executing AI Pipeline...' : 'Execute Project Runner'}
            </button>

            {/* Capabilities checklist summary */}
            <div style={{ marginTop: '1.5rem', borderTop: '1px solid var(--border-subtle)', paddingTop: '1rem' }}>
              <div style={{ fontSize: '0.8rem', fontWeight: '700', color: 'var(--text-dim)', marginBottom: '0.5rem', textTransform: 'uppercase' }}>
                Full Capabilities List ({project.capabilities.length}):
              </div>
              <ul className="capabilities-list">
                {project.capabilities.map((c, i) => (
                  <li key={i} className="capability-item" style={{ fontSize: '0.8rem' }}>
                    <span className="capability-dot"></span>
                    <span>{c}</span>
                  </li>
                ))}
              </ul>
            </div>
          </div>

          {/* Right Column: Execution Output Pane */}
          <div className="glass-card">
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                <h3 style={{ fontSize: '1.1rem' }}>📤 Execution Output</h3>
                {executionTime !== null && (
                  <span style={{ fontSize: '0.75rem', background: 'rgba(99, 102, 241, 0.2)', color: 'var(--primary-light)', padding: '0.2rem 0.5rem', borderRadius: '4px', fontFamily: 'var(--font-mono)' }}>
                    ⏱ {executionTime} ms
                  </span>
                )}
              </div>

              {output && (
                <div style={{ display: 'flex', gap: '0.5rem' }}>
                  <button
                    className="btn btn-secondary btn-sm"
                    onClick={() => navigator.clipboard.writeText(JSON.stringify(output, null, 2))}
                  >
                    Copy Output
                  </button>
                  <button
                    className="btn btn-secondary btn-sm"
                    onClick={handleSaveOutput}
                  >
                    {saveSuccess ? 'Saved!' : 'Save'}
                  </button>
                </div>
              )}
            </div>

            {loading && (
              <div style={{ padding: '3rem 1rem', textAlign: 'center', color: 'var(--text-muted)' }}>
                <div style={{ fontSize: '2rem', marginBottom: '1rem', animation: 'spin 1s linear infinite' }}>⚙️</div>
                <div>Synthesizing data through AI58 Core Pipeline...</div>
              </div>
            )}

            {error && (
              <div style={{ padding: '1rem', background: 'rgba(244, 63, 94, 0.15)', border: '1px solid rgba(244, 63, 94, 0.3)', borderRadius: '8px', color: '#fca5a5', marginBottom: '1rem' }}>
                <strong>Execution Error:</strong> {error}
              </div>
            )}

            {!loading && !output && !error && (
              <div style={{ padding: '4rem 2rem', textAlign: 'center', color: 'var(--text-dim)' }}>
                <div style={{ fontSize: '2.5rem', marginBottom: '1rem', opacity: 0.6 }}>🚀</div>
                <div style={{ fontSize: '1.05rem', fontWeight: '600', color: 'var(--text-muted)', marginBottom: '0.5rem' }}>
                  Ready to Execute
                </div>
                <div style={{ fontSize: '0.85rem', maxWidth: '360px', margin: '0 auto' }}>
                  Click <strong>[RUN]</strong> or <strong>Execute Project Runner</strong> above to process the input through the AI58 pipeline.
                </div>
              </div>
            )}

            {output && !loading && (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
                <pre className="code-viewer" style={{ maxHeight: '480px' }}>
                  {JSON.stringify(output, null, 2)}
                </pre>
              </div>
            )}
          </div>
        </div>
      )}

      {/* Tab: DOCUMENTATION */}
      {activeTab === 'documentation' && (
        <div className="glass-card">
          <h2 style={{ fontSize: '1.5rem', marginBottom: '1.5rem' }}>📖 Project Documentation & Architecture</h2>
          <pre className="code-viewer" style={{ maxHeight: '600px', whiteSpace: 'pre-wrap' }}>
            {project.documentation_markdown || "Full architectural guide loaded."}
          </pre>
        </div>
      )}

      {/* Tab: HISTORY */}
      {activeTab === 'history' && (
        <div className="glass-card">
          <h2 style={{ fontSize: '1.5rem', marginBottom: '1.5rem' }}>📜 Execution Run History</h2>
          {history.length === 0 ? (
            <div style={{ padding: '2rem', textAlign: 'center', color: 'var(--text-dim)' }}>
              No execution runs logged for this project yet. Execute a run to see history.
            </div>
          ) : (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
              {history.map((h, i) => (
                <div key={h.id || i} style={{ background: 'rgba(255, 255, 255, 0.03)', border: '1px solid var(--border-subtle)', borderRadius: '8px', padding: '1rem' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.5rem' }}>
                    <span style={{ fontWeight: '600', color: 'var(--cyan)' }}>Run #{h.id} — {h.status.toUpperCase()}</span>
                    <span style={{ fontSize: '0.8rem', color: 'var(--text-dim)' }}>{new Date(h.created_at).toLocaleString()}</span>
                  </div>
                  <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)', marginBottom: '0.5rem' }}>
                    Execution time: {h.execution_time_ms} ms
                  </div>
                  <button
                    className="btn btn-secondary btn-sm"
                    onClick={() => { setOutput(h.output); setActiveTab('workbench'); }}
                  >
                    Load This Output
                  </button>
                </div>
              ))}
            </div>
          )}
        </div>
      )}
    </div>
  );
}
