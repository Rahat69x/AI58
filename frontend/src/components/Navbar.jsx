import React from 'react';

export default function Navbar({ activeView, setActiveView, currentTier, setCurrentTier, user, onOpenAuth }) {
  return (
    <header className="navbar">
      <div className="navbar-inner">
        <div className="nav-brand" onClick={() => { setActiveView('dashboard'); setCurrentTier('ALL'); }}>
          <div className="brand-badge">AI58</div>
          <div className="brand-text">
            <span className="brand-title">AI Project Platform</span>
            <span className="brand-subtitle">58 Unified Systems</span>
          </div>
        </div>

        <nav className="nav-links">
          <button
            className={`nav-btn ${activeView === 'dashboard' && currentTier === 'ALL' ? 'active' : ''}`}
            onClick={() => { setActiveView('dashboard'); setCurrentTier('ALL'); }}
          >
            <span>🏠</span> Dashboard
          </button>
          <button
            className={`nav-btn ${activeView === 'dashboard' && currentTier === 'BEGINNER' ? 'active' : ''}`}
            onClick={() => { setActiveView('dashboard'); setCurrentTier('BEGINNER'); }}
          >
            <span className="nav-counter-badge tier-beginner">19</span> Beginner
          </button>
          <button
            className={`nav-btn ${activeView === 'dashboard' && currentTier === 'INTERMEDIATE' ? 'active' : ''}`}
            onClick={() => { setActiveView('dashboard'); setCurrentTier('INTERMEDIATE'); }}
          >
            <span className="nav-counter-badge tier-intermediate">20</span> Intermediate
          </button>
          <button
            className={`nav-btn ${activeView === 'dashboard' && currentTier === 'ADVANCED' ? 'active' : ''}`}
            onClick={() => { setActiveView('dashboard'); setCurrentTier('ADVANCED'); }}
          >
            <span className="nav-counter-badge tier-advanced">19</span> Advanced
          </button>
          <button
            className={`nav-btn ${activeView === 'roadmap' ? 'active' : ''}`}
            onClick={() => setActiveView('roadmap')}
          >
            <span>🗺️</span> Roadmap
          </button>
          <button
            className={`nav-btn ${activeView === 'ai-lab' ? 'active' : ''}`}
            onClick={() => setActiveView('ai-lab')}
          >
            <span>⚡</span> Shared AI Engine
          </button>
        </nav>

        <div className="nav-actions">
          {user ? (
            <button className="btn btn-secondary btn-sm" onClick={onOpenAuth}>
              <span>👤</span> {user.username}
            </button>
          ) : (
            <button className="btn btn-primary btn-sm" onClick={onOpenAuth}>
              <span>🔐</span> Sign In
            </button>
          )}
        </div>
      </div>
    </header>
  );
}
