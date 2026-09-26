import React, { useState } from 'react';
import { api } from '../lib/api';

export default function AuthModal({ user, onClose, onAuthSuccess, onLogout }) {
  const [tab, setTab] = useState(user ? 'profile' : 'login'); // 'login' | 'register' | 'profile' | 'preferences'
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [fullName, setFullName] = useState('');
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  // Preferences state
  const [aiProvider, setAiProvider] = useState(user?.preferences?.ai_provider || 'builtin');
  const [geminiKey, setGeminiKey] = useState(user?.preferences?.gemini_key || '');
  const [openaiKey, setOpenaiKey] = useState(user?.preferences?.openai_key || '');

  const handleLogin = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    try {
      const data = await api.login(username, password);
      onAuthSuccess(data.user);
      onClose();
    } catch (err) {
      setError(err.message || 'Login failed.');
    } finally {
      setLoading(false);
    }
  };

  const handleRegister = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    try {
      const data = await api.register(username, email, password, fullName);
      onAuthSuccess(data.user);
      onClose();
    } catch (err) {
      setError(err.message || 'Registration failed.');
    } finally {
      setLoading(false);
    }
  };

  const handleSavePreferences = async () => {
    setLoading(true);
    try {
      await api.updatePreferences({
        ai_provider: aiProvider,
        gemini_key: geminiKey,
        openai_key: openaiKey,
      });
      alert('Preferences updated successfully!');
    } catch (err) {
      alert(`Error updating preferences: ${err.message}`);
    } finally {
      setLoading(false);
    }
  };

  const handleDeleteAccount = async () => {
    if (confirm('Are you sure you want to permanently delete your account and all associated project execution data? This action cannot be undone.')) {
      try {
        await api.deleteAccount();
        onLogout();
        onClose();
        alert('Your account and history have been permanently deleted.');
      } catch (err) {
        alert(`Error deleting account: ${err.message}`);
      }
    }
  };

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()} style={{ maxWidth: '520px' }}>
        <div className="modal-header">
          <h2 style={{ fontSize: '1.25rem' }}>
            {user ? 'User Profile & Preferences' : tab === 'login' ? 'Sign In to AI58' : 'Create AI58 Account'}
          </h2>
          <button className="modal-close-btn" onClick={onClose}>×</button>
        </div>

        {error && (
          <div style={{ padding: '0.75rem', background: 'rgba(244, 63, 94, 0.15)', border: '1px solid rgba(244, 63, 94, 0.3)', borderRadius: '6px', color: '#fca5a5', marginBottom: '1rem', fontSize: '0.85rem' }}>
            {error}
          </div>
        )}

        {/* Guest Mode: Login or Register */}
        {!user && (
          <div>
            <div style={{ display: 'flex', gap: '0.5rem', marginBottom: '1.5rem', borderBottom: '1px solid var(--border-subtle)', paddingBottom: '0.5rem' }}>
              <button
                className={`btn btn-sm ${tab === 'login' ? 'btn-primary' : 'btn-secondary'}`}
                onClick={() => setTab('login')}
              >
                Sign In
              </button>
              <button
                className={`btn btn-sm ${tab === 'register' ? 'btn-primary' : 'btn-secondary'}`}
                onClick={() => setTab('register')}
              >
                Register New Account
              </button>
            </div>

            {tab === 'login' ? (
              <form onSubmit={handleLogin}>
                <div className="form-group">
                  <label className="form-label">Username or Email</label>
                  <input
                    type="text"
                    required
                    className="form-input"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                  />
                </div>
                <div className="form-group">
                  <label className="form-label">Password</label>
                  <input
                    type="password"
                    required
                    className="form-input"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                  />
                </div>
                <button type="submit" className="btn btn-primary" style={{ width: '100%' }} disabled={loading}>
                  {loading ? 'Authenticating...' : 'Sign In'}
                </button>
              </form>
            ) : (
              <form onSubmit={handleRegister}>
                <div className="form-group">
                  <label className="form-label">Username</label>
                  <input
                    type="text"
                    required
                    className="form-input"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                  />
                </div>
                <div className="form-group">
                  <label className="form-label">Email Address</label>
                  <input
                    type="email"
                    required
                    className="form-input"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                  />
                </div>
                <div className="form-group">
                  <label className="form-label">Full Name</label>
                  <input
                    type="text"
                    className="form-input"
                    value={fullName}
                    onChange={(e) => setFullName(e.target.value)}
                  />
                </div>
                <div className="form-group">
                  <label className="form-label">Password</label>
                  <input
                    type="password"
                    required
                    className="form-input"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                  />
                </div>
                <button type="submit" className="btn btn-primary" style={{ width: '100%' }} disabled={loading}>
                  {loading ? 'Creating Account...' : 'Register Account'}
                </button>
              </form>
            )}
          </div>
        )}

        {/* Authenticated Mode: Profile & Preferences & Privacy Controls */}
        {user && (
          <div>
            <div style={{ marginBottom: '1.5rem', background: 'rgba(255, 255, 255, 0.03)', padding: '1rem', borderRadius: '8px' }}>
              <div style={{ fontWeight: '700', fontSize: '1.1rem', color: '#fff' }}>{user.full_name || user.username}</div>
              <div style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>@{user.username} • {user.email}</div>
              <div style={{ fontSize: '0.75rem', color: 'var(--cyan)', marginTop: '0.25rem' }}>Role: {user.role.toUpperCase()}</div>
            </div>

            <h3 style={{ fontSize: '1rem', marginBottom: '1rem' }}>AI Provider Configuration</h3>
            <div className="form-group">
              <label className="form-label">Active AI Provider</label>
              <select
                className="form-input"
                value={aiProvider}
                onChange={(e) => setAiProvider(e.target.value)}
              >
                <option value="builtin">Built-in Intelligence Engine (Fast, Local & High Precision)</option>
                <option value="gemini">Google Gemini 1.5</option>
                <option value="openai">OpenAI GPT-4o</option>
              </select>
            </div>

            {aiProvider === 'gemini' && (
              <div className="form-group">
                <label className="form-label">Gemini API Key</label>
                <input
                  type="password"
                  className="form-input"
                  placeholder="AIzaSy..."
                  value={geminiKey}
                  onChange={(e) => setGeminiKey(e.target.value)}
                />
              </div>
            )}

            {aiProvider === 'openai' && (
              <div className="form-group">
                <label className="form-label">OpenAI API Key</label>
                <input
                  type="password"
                  className="form-input"
                  placeholder="sk-..."
                  value={openaiKey}
                  onChange={(e) => setOpenaiKey(e.target.value)}
                />
              </div>
            )}

            <button className="btn btn-primary btn-sm" onClick={handleSavePreferences} style={{ marginBottom: '1.5rem' }}>
              Save Preferences
            </button>

            {/* Privacy Controls & Account Deletion (Section 6 requirement) */}
            <div style={{ borderTop: '1px solid var(--border-subtle)', paddingTop: '1.25rem' }}>
              <h4 style={{ fontSize: '0.9rem', color: '#fca5a5', marginBottom: '0.5rem' }}>Privacy Controls & Data Sovereignty</h4>
              <p style={{ fontSize: '0.8rem', color: 'var(--text-dim)', marginBottom: '1rem' }}>
                You have full control over your stored project execution history, saved outputs, and credentials.
              </p>
              <div style={{ display: 'flex', gap: '0.75rem' }}>
                <button className="btn btn-secondary btn-sm" onClick={onLogout}>
                  Sign Out
                </button>
                <button
                  className="btn btn-sm"
                  style={{ background: 'rgba(244, 63, 94, 0.2)', color: '#fca5a5', border: '1px solid rgba(244, 63, 94, 0.4)' }}
                  onClick={handleDeleteAccount}
                >
                  Delete Account & Data
                </button>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
