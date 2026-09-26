import React, { useState, useEffect } from 'react';
import Navbar from './components/Navbar';
import DashboardView from './components/DashboardView';
import ProjectWorkbench from './components/ProjectWorkbench';
import RoadmapView from './components/RoadmapView';
import AiEngineLab from './components/AiEngineLab';
import AuthModal from './components/AuthModal';
import { api } from './lib/api';

export default function App() {
  const [activeView, setActiveView] = useState('dashboard'); // 'dashboard' | 'workbench' | 'roadmap' | 'ai-lab'
  const [currentTier, setCurrentTier] = useState('ALL'); // 'ALL' | 'BEGINNER' | 'INTERMEDIATE' | 'ADVANCED'
  const [projects, setProjects] = useState([]);
  const [stats, setStats] = useState(null);
  const [selectedProjectId, setSelectedProjectId] = useState(null);
  const [user, setUser] = useState(null);
  const [showAuthModal, setShowAuthModal] = useState(false);
  const [runningProjectId, setRunningProjectId] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    bootstrapPlatform();
  }, []);

  const bootstrapPlatform = async () => {
    setLoading(true);
    try {
      // 1. Check logged-in user profile
      try {
        const profile = await api.getProfile();
        setUser(profile);
      } catch (e) {
        setUser(null);
      }

      // 2. Fetch Projects catalog
      const projData = await api.listProjects();
      setProjects(projData.projects || []);

      // 3. Fetch Dashboard statistics
      const statsData = await api.getDashboardStats();
      setStats(statsData);
    } catch (err) {
      console.error("Platform bootstrap error:", err);
    } finally {
      setLoading(false);
    }
  };

  const handleOpenProject = (projectId) => {
    setSelectedProjectId(projectId);
    setActiveView('workbench');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleInstantRun = async (projectId) => {
    setRunningProjectId(projectId);
    try {
      const proj = projects.find(p => p.id === projectId);
      if (!proj) return;
      await api.runProject(projectId, proj.default_input);
      // Refresh dashboard stats to reflect run
      const statsData = await api.getDashboardStats();
      setStats(statsData);
      // Open project to show result
      setSelectedProjectId(projectId);
      setActiveView('workbench');
    } catch (err) {
      alert(`Execution error on project #${projectId}: ${err.message}`);
    } finally {
      setRunningProjectId(null);
    }
  };

  const handleToggleFavorite = async (projectId) => {
    if (!user) {
      setShowAuthModal(true);
      return;
    }
    try {
      const res = await api.toggleFavorite(projectId);
      setProjects(prev =>
        prev.map(p => (p.id === projectId ? { ...p, is_favorite: res.is_favorite } : p))
      );
      const statsData = await api.getDashboardStats();
      setStats(statsData);
    } catch (err) {
      console.error("Failed to toggle favorite:", err);
    }
  };

  const selectedProject = projects.find(p => p.id === selectedProjectId);

  return (
    <div className="app-container">
      <Navbar
        activeView={activeView}
        setActiveView={setActiveView}
        currentTier={currentTier}
        setCurrentTier={setCurrentTier}
        user={user}
        onOpenAuth={() => setShowAuthModal(true)}
      />

      <main className="main-content">
        {loading ? (
          <div style={{ textAlign: 'center', padding: '5rem', color: 'var(--text-muted)' }}>
            <div style={{ fontSize: '2.5rem', marginBottom: '1rem', animation: 'spin 1.5s linear infinite' }}>🌐</div>
            <h2 style={{ fontSize: '1.25rem', color: 'var(--text-primary)' }}>Initializing AI58 Platform Core...</h2>
            <p style={{ fontSize: '0.85rem', color: 'var(--text-muted)', marginTop: '0.5rem' }}>
              Connecting to 58 AI project runners and shared services...
            </p>
          </div>
        ) : (
          <>
            {activeView === 'dashboard' && (
              <DashboardView
                projects={projects}
                stats={stats}
                currentTier={currentTier}
                setCurrentTier={setCurrentTier}
                onOpenProject={handleOpenProject}
                onInstantRun={handleInstantRun}
                onToggleFavorite={handleToggleFavorite}
                runningProjectId={runningProjectId}
              />
            )}

            {activeView === 'workbench' && selectedProject && (
              <ProjectWorkbench
                project={selectedProject}
                onBack={() => setActiveView('dashboard')}
                onToggleFavorite={handleToggleFavorite}
                onOpenProject={handleOpenProject}
              />
            )}

            {activeView === 'roadmap' && (
              <RoadmapView
                onOpenProject={handleOpenProject}
              />
            )}

            {activeView === 'ai-lab' && (
              <AiEngineLab />
            )}
          </>
        )}
      </main>

      {showAuthModal && (
        <AuthModal
          user={user}
          onClose={() => setShowAuthModal(false)}
          onAuthSuccess={(userData) => {
            setUser(userData);
            bootstrapPlatform();
          }}
          onLogout={() => {
            api.logout();
            setUser(null);
            bootstrapPlatform();
          }}
        />
      )}
    </div>
  );
}
