import React, { useState, useEffect } from 'react';
import { api } from '../lib/api';

export default function RoadmapView({ onOpenProject }) {
  const [roadmapData, setRoadmapData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadRoadmap();
  }, []);

  const loadRoadmap = async () => {
    try {
      const data = await api.getRoadmap();
      setRoadmapData(data);
    } catch (err) {
      console.error("Failed to load roadmap:", err);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div style={{ textAlign: 'center', padding: '4rem', color: 'var(--text-muted)' }}>
        Loading Master Roadmap Pipeline...
      </div>
    );
  }

  return (
    <div className="roadmap-view">
      {/* Header & Overall Metric */}
      <div className="glass-card" style={{ marginBottom: '2rem' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '1rem' }}>
          <div>
            <span style={{ fontSize: '0.8rem', color: 'var(--cyan)', fontWeight: '700', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
              Sequential Progression Architecture
            </span>
            <h1 style={{ fontSize: '2.25rem', marginTop: '0.25rem' }}>AI58 Master Roadmap & Checklists</h1>
            <p style={{ color: 'var(--text-muted)', fontSize: '0.95rem' }}>
              Track the full progression from Level 1 Beginner through Level 3 Advanced across all 58 projects.
            </p>
          </div>

          <div style={{ textAlign: 'right', background: 'rgba(255, 255, 255, 0.03)', padding: '1rem 1.5rem', borderRadius: '12px', border: '1px solid var(--border-subtle)' }}>
            <div style={{ fontSize: '0.75rem', color: 'var(--text-dim)', fontWeight: '700', textTransform: 'uppercase' }}>
              Overall Readiness
            </div>
            <div style={{ fontSize: '2.5rem', fontWeight: '800', color: '#34d399', fontFamily: 'var(--font-heading)' }}>
              {roadmapData?.overall_completion_percentage || 100}%
            </div>
            <div style={{ fontSize: '0.75rem', color: 'var(--text-dim)' }}>
              {roadmapData?.completed_checklist_items} / {roadmapData?.total_checklist_items} checkpoints
            </div>
          </div>
        </div>
      </div>

      {/* 3 Tier Levels */}
      {roadmapData?.levels?.map((lvl) => {
        const borderAccent =
          lvl.tier === 'BEGINNER' ? '#34d399' : lvl.tier === 'INTERMEDIATE' ? '#38bdf8' : '#c084fc';

        return (
          <div key={lvl.level} className="glass-card" style={{ marginBottom: '2rem', borderLeft: `4px solid ${borderAccent}` }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.25rem', flexWrap: 'wrap' }}>
              <div>
                <h2 style={{ fontSize: '1.4rem', color: '#fff' }}>{lvl.title}</h2>
                <p style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>{lvl.description}</p>
              </div>
              <span className="tech-tag" style={{ fontSize: '0.8rem', padding: '0.3rem 0.75rem' }}>
                {lvl.projects.length} Verified Modules
              </span>
            </div>

            {/* Project List with individual 8-point status */}
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(320px, 1fr))', gap: '1rem' }}>
              {lvl.projects.map((p) => (
                <div
                  key={p.id}
                  style={{
                    background: 'rgba(7, 9, 14, 0.6)',
                    border: '1px solid var(--border-subtle)',
                    borderRadius: '10px',
                    padding: '1rem',
                    display: 'flex',
                    flexDirection: 'column',
                    justifyContent: 'space-between',
                    cursor: 'pointer',
                    transition: 'all 0.2s ease',
                  }}
                  onClick={() => onOpenProject(p.id)}
                  onMouseEnter={(e) => { e.currentTarget.style.borderColor = borderAccent; e.currentTarget.style.transform = 'translateY(-2px)'; }}
                  onMouseLeave={(e) => { e.currentTarget.style.borderColor = 'var(--border-subtle)'; e.currentTarget.style.transform = 'translateY(0)'; }}
                >
                  <div>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.4rem' }}>
                      <span className="project-number">#{String(p.id).padStart(2, '0')}</span>
                      <span style={{ fontSize: '0.72rem', color: '#34d399', fontWeight: '700' }}>
                        ✓ {p.checklist_completed}/8
                      </span>
                    </div>
                    <div style={{ fontWeight: '700', fontSize: '0.95rem', color: '#fff', marginBottom: '0.25rem' }}>
                      {p.name}
                    </div>
                    <div style={{ fontSize: '0.75rem', color: 'var(--text-dim)', marginBottom: '0.75rem' }}>
                      {p.category}
                    </div>
                  </div>

                  {/* 8 mini dots representing the 8 checkpoints */}
                  <div style={{ display: 'flex', gap: '4px', alignItems: 'center' }}>
                    {Object.entries(p.checklist).map(([chkKey, chkVal]) => (
                      <div
                        key={chkKey}
                        title={`${chkKey}: ${chkVal ? 'Done' : 'Pending'}`}
                        style={{
                          flex: 1,
                          height: '5px',
                          borderRadius: '2px',
                          background: chkVal ? borderAccent : 'rgba(255,255,255,0.1)',
                        }}
                      />
                    ))}
                  </div>
                </div>
              ))}
            </div>
          </div>
        );
      })}
    </div>
  );
}
