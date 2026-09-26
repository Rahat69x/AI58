/**
 * AI58 Frontend API Client
 * Centralized communication with the AI58 FastAPI backend.
 */

const API_BASE = '/api';

class ApiClient {
  constructor() {
    this.token = localStorage.getItem('ai58_token') || null;
  }

  setToken(token) {
    this.token = token;
    if (token) {
      localStorage.setItem('ai58_token', token);
    } else {
      localStorage.removeItem('ai58_token');
    }
  }

  getHeaders() {
    const headers = { 'Content-Type': 'application/json' };
    if (this.token) {
      headers['Authorization'] = `Bearer ${this.token}`;
    }
    return headers;
  }

  async request(endpoint, options = {}) {
    const url = `${API_BASE}${endpoint}`;
    const config = {
      ...options,
      headers: {
        ...this.getHeaders(),
        ...(options.headers || {}),
      },
    };

    try {
      const response = await fetch(url, config);
      const data = await response.json();
      if (!response.ok) {
        throw new Error(data.detail || `Request failed with status ${response.status}`);
      }
      return data;
    } catch (err) {
      console.error(`API Error on ${endpoint}:`, err);
      throw err;
    }
  }

  // Dashboard & Platform Metrics
  async getDashboardStats() {
    return this.request('/dashboard/stats');
  }

  // Projects Catalog & Discovery
  async listProjects(params = {}) {
    const query = new URLSearchParams();
    if (params.tier && params.tier !== 'ALL') query.set('tier', params.tier);
    if (params.category) query.set('category', params.category);
    if (params.search) query.set('search', params.search);
    if (params.favorites_only) query.set('favorites_only', 'true');
    const qs = query.toString() ? `?${query.toString()}` : '';
    return this.request(`/projects${qs}`);
  }

  async getProject(projectId) {
    return this.request(`/projects/${projectId}`);
  }

  // Workbench Execution
  async runProject(projectId, inputs, options = {}) {
    return this.request(`/projects/${projectId}/run`, {
      method: 'POST',
      body: JSON.stringify({ inputs, options }),
    });
  }

  async getProjectHistory(projectId) {
    return this.request(`/projects/${projectId}/history`);
  }

  async toggleFavorite(projectId) {
    return this.request(`/projects/${projectId}/favorite`, { method: 'POST' });
  }

  async updateChecklist(projectId, checklist) {
    return this.request(`/projects/${projectId}/checklist`, {
      method: 'PUT',
      body: JSON.stringify(checklist),
    });
  }

  async saveOutput(projectId, title, notes, payload) {
    return this.request(`/projects/${projectId}/save-output`, {
      method: 'POST',
      body: JSON.stringify({ project_id: projectId, title, notes, payload }),
    });
  }

  // Roadmap & Checklists
  async getRoadmap() {
    return this.request('/roadmap');
  }

  // Shared AI Engine
  async getSharedServices() {
    return this.request('/ai-engine/services');
  }

  async testLLM(prompt, system_prompt = null) {
    return this.request('/ai-engine/llm/generate', {
      method: 'POST',
      body: JSON.stringify({ prompt, system_prompt }),
    });
  }

  async analyzeCode(code, language = 'python') {
    return this.request('/ai-engine/code/analyze', {
      method: 'POST',
      body: JSON.stringify({ code, language }),
    });
  }

  async cleanCsv(csv_content) {
    return this.request('/ai-engine/data/clean-csv', {
      method: 'POST',
      headers: { 'Content-Type': 'text/plain' },
      body: csv_content,
    });
  }

  // User Auth & Accounts
  async register(username, email, password, full_name = '') {
    const data = await this.request('/auth/register', {
      method: 'POST',
      body: JSON.stringify({ username, email, password, full_name }),
    });
    this.setToken(data.access_token);
    return data;
  }

  async login(username_or_email, password) {
    const data = await this.request('/auth/login', {
      method: 'POST',
      body: JSON.stringify({ username_or_email, password }),
    });
    this.setToken(data.access_token);
    return data;
  }

  async getProfile() {
    if (!this.token) return null;
    return this.request('/auth/profile');
  }

  async updatePreferences(preferences) {
    return this.request('/auth/preferences', {
      method: 'PUT',
      body: JSON.stringify(preferences),
    });
  }

  async deleteAccount() {
    const res = await this.request('/auth/account', { method: 'DELETE' });
    this.setToken(null);
    return res;
  }

  logout() {
    this.setToken(null);
  }
}

export const api = new ApiClient();
