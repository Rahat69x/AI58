import React, { useState, useMemo } from 'react';

export default function DashboardView({
  projects,
  stats,
  currentTier,
  setCurrentTier,
  onOpenProject,
  onInstantRun,
  onToggleFavorite,
  runningProjectId
}) {
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('ALL');
  const [favoritesOnly, setFavoritesOnly] = useState(false);

  // Extract unique categories
  const categories = useMemo(() => {
    const set = new Set(projects.map(p => p.category));
    return ['ALL', ...Array.from(set)];
  }, [projects]);

  // Filtered projects list
  const filteredProjects = useMemo(() => {
    return projects.filter(p => {
      // Tier match
      if (currentTier !== 'ALL' && p.tier !== currentTier) return false;
      // Category match
      if (selectedCategory !== 'ALL' && p.category !== selectedCategory) return false;
      // Favorites filter
      if (favoritesOnly && !p.is_favorite) return false;
      // Search term
      if (searchTerm.trim()) {
        const q = searchTerm.toLowerCase();
        const inName = p.name.toLowerCase().includes(q);
        const inDesc = p.description.toLowerCase().includes(q);
        const inCaps = p.capabilities.some(c => c.toLowerCase().includes(q));
        const inTech = p.technologies.some(t => t.toLowerCase().includes(q));
        if (!inName && !inDesc && !inCaps && !inTech) return false;
      }
      return true;
    });
  }, [projects, currentTier, selectedCategory, favoritesOnly, searchTerm]);

  return (
    <div className="dashboard-view">
      {/* Platform Requirements Banner */}
      <section className="stats-banner">
        <div className="stat-box" onClick={() => setCurrentTier('ALL')} style={{ cursor: 'pointer' }}>
          <div>
            <div className="stat-label">Total Projects</div>
            <div className="stat-value stat-total">{stats?.total_projects || 58}</div>
          </div>
          <div className="stat-icon">🚀</div>
        </div>

        <div className="stat-box" onClick={() => setCurrentTier('BEGINNER')} style={{ cursor: 'pointer' }}>
          <div>
            <div className="stat-label">Beginner Tier</div>
            <div className="stat-value stat-beginner">{stats?.beginner_count || 19}</div>
          </div>
          <div className="stat-icon">🌱</div>
        </div>

        <div className="stat-box" onClick={() => setCurrentTier('INTERMEDIATE')} style={{ cursor: 'pointer' }}>
          <div>
            <div className="stat-label">Intermediate Tier</div>
            <div className="stat-value stat-intermediate">{stats?.intermediate_count || 20}</div>
          </div>
          <div className="stat-icon">⚡</div>
        </div>

        <div className="stat-box" onClick={() => setCurrentTier('ADVANCED')} style={{ cursor: 'pointer' }}>
          <div>
            <div className="stat-label">Advanced Tier</div>
            <div className="stat-value stat-advanced">{stats?.advanced_count || 19}</div>
          </div>
          <div className="stat-icon">🌌</div>
        </div>
      </section>

      {/* Filter and Search Bar: --bg-surface / --border, no tier color */}
      <div className="filter-bar">
        <div className="search-input-wrapper">
          <span className="search-icon-inside">🔍</span>
          <input
            type="text"
            className="search-input"
            placeholder="Search all 58 projects by name, capability, or tech..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
        </div>

        {/* Filter tabs: active tab uses matching tier color, inactive stays --text-muted */}
        <div className="filter-pills">
          <button
            className={`pill-btn ${currentTier === 'ALL' && !favoritesOnly ? 'active active-all' : ''}`}
            onClick={() => { setCurrentTier('ALL'); setFavoritesOnly(false); }}
          >
            All (58)
          </button>
          <button
            className={`pill-btn ${currentTier === 'BEGINNER' && !favoritesOnly ? 'active active-beginner' : ''}`}
            onClick={() => { setCurrentTier('BEGINNER'); setFavoritesOnly(false); }}
          >
            Beginner (19)
          </button>
          <button
            className={`pill-btn ${currentTier === 'INTERMEDIATE' && !favoritesOnly ? 'active active-intermediate' : ''}`}
            onClick={() => { setCurrentTier('INTERMEDIATE'); setFavoritesOnly(false); }}
          >
            Intermediate (20)
          </button>
          <button
            className={`pill-btn ${currentTier === 'ADVANCED' && !favoritesOnly ? 'active active-advanced' : ''}`}
            onClick={() => { setCurrentTier('ADVANCED'); setFavoritesOnly(false); }}
          >
            Advanced (19)
          </button>
          <button
            className={`pill-btn ${favoritesOnly ? 'active active-favorites' : ''}`}
            onClick={() => setFavoritesOnly(!favoritesOnly)}
          >
            ★ Favorites
          </button>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <label style={{ fontSize: '0.8rem', color: 'var(--text-muted)', fontWeight: '600' }}>Category:</label>
          <select
            className="category-select"
            value={selectedCategory}
            onChange={(e) => setSelectedCategory(e.target.value)}
          >
            {categories.map(cat => (
              <option key={cat} value={cat}>{cat}</option>
            ))}
          </select>
        </div>
      </div>

      {/* Active / Recently Run Pills → --accent */}
      {stats?.active_projects && stats.active_projects.length > 0 && (
        <div className="active-recent-bar">
          <span className="active-recent-label">
            ⚡ Active / Recently Run:
          </span>
          {stats.active_projects.map(p => (
            <button
              key={p.id}
              className="recent-pill"
              onClick={() => onOpenProject(p.id)}
            >
              #{String(p.id).padStart(2, '0')} {p.name}
            </button>
          ))}
        </div>
      )}

      {/* Showing count indicator */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
        <div style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>
          Showing <strong>{filteredProjects.length}</strong> of <strong>58</strong> projects
        </div>
        <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>
          Click <strong>[OPEN]</strong> to view workbench or <strong>[RUN]</strong> for instant execution
        </div>
      </div>

      {/* All 58 Projects Grid */}
      <div className="projects-grid">
        {filteredProjects.map((p) => {
          const tierClass =
            p.tier === 'BEGINNER'
              ? 'tier-beginner'
              : p.tier === 'INTERMEDIATE'
              ? 'tier-intermediate'
              : 'tier-advanced';

          const isRunning = runningProjectId === p.id;

          return (
            <div key={p.id} className="glass-card project-card">
              <div>
                <div className="card-top">
                  <div>
                    <span className="project-number">#{String(p.id).padStart(2, '0')}</span>
                    <h3 className="project-title">{p.name}</h3>
                  </div>
                  <span className={`tier-badge ${tierClass}`}>{p.tier}</span>
                </div>

                <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', fontWeight: '600', marginBottom: '0.5rem' }}>
                  {p.category}
                </div>

                <p className="project-desc">{p.description}</p>

                <div style={{ marginBottom: '0.75rem' }}>
                  <div style={{ fontSize: '0.72rem', fontWeight: '700', color: 'var(--text-muted)', marginBottom: '0.35rem', textTransform: 'uppercase' }}>
                    Core Capabilities:
                  </div>
                  <ul className="capabilities-list">
                    {p.capabilities.slice(0, 3).map((cap, idx) => (
                      <li key={idx} className="capability-item">
                        <span className="capability-dot"></span>
                        <span>{cap}</span>
                      </li>
                    ))}
                    {p.capabilities.length > 3 && (
                      <li className="capability-item">
                        +{p.capabilities.length - 3} more capabilities
                      </li>
                    )}
                  </ul>
                </div>

                <div className="tech-tags">
                  {p.technologies.slice(0, 4).map((tech, idx) => (
                    <span key={idx} className="tech-tag">{tech}</span>
                  ))}
                </div>
              </div>

              <div className="card-actions">
                <button
                  className="btn btn-secondary btn-sm"
                  onClick={() => onToggleFavorite(p.id)}
                  title={p.is_favorite ? 'Remove from favorites' : 'Add to favorites'}
                >
                  <span style={{ color: p.is_favorite ? 'var(--accent)' : 'var(--text-muted)' }}>
                    {p.is_favorite ? '★' : '☆'}
                  </span>
                </button>

                <div className="card-action-group">
                  <button
                    className="btn btn-secondary btn-sm"
                    onClick={() => onOpenProject(p.id)}
                  >
                    <span>📖</span> [OPEN]
                  </button>
                  <button
                    className="btn btn-run btn-sm"
                    disabled={isRunning}
                    onClick={() => onInstantRun(p.id)}
                  >
                    <span>{isRunning ? '⏳' : '▶'}</span> {isRunning ? 'Running...' : '[RUN]'}
                  </button>
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
