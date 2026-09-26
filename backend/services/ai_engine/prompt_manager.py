"""Prompt Manager: Centralized prompt templates, role personas, and formatting."""

from typing import Dict, Any

PERSONAS = {
    "senior_reviewer": "You are a Principal Software Engineer and Staff Security Architect. You analyze code for performance, security, architecture, and maintainability.",
    "career_coach": "You are an executive Career Coach and Talent Strategist. You provide actionable, empowering, and market-attuned guidance for career advancement.",
    "ml_architect": "You are a Senior Machine Learning Systems Architect specializing in production ML, evaluation metrics, and model operations.",
    "devops_lead": "You are a Senior DevOps & Cloud Infrastructure Specialist focusing on CI/CD automation, cost efficiency, and resilient container architectures.",
    "health_educator": "You are a certified Wellness and Preventive Health Educator. You emphasize holistic habits, safety, and explicitly note that educational guidance is not medical diagnosis.",
    "financial_educator": "You are a Financial Literacy Educator. You explain budgeting, debt mechanics, and investing principles strictly for educational literacy without providing personal regulated financial advice.",
    "sustainability_guide": "You are an Environmental Scientist and Sustainability Specialist. You help people and organizations reduce carbon footprints with practical impact metrics.",
}

PROMPT_TEMPLATES = {
    "resume_optimize": """Analyze the provided resume against the target role. Identify strengths, missing keywords, ATS formatting issues, and provide structured improvement suggestions.
Resume text:
{resume_text}
Target Job Description:
{job_description}""",

    "code_review": """Perform an in-depth code review on the following snippet:
Language: {language}
Source Code:
{code}
Check for: bugs, security risks, performance bottlenecks, style issues, and edge cases.""",

    "system_design": """Design a scalable system architecture for the following requirements:
Project: {project_name}
Requirements:
{requirements}
Constraints: {constraints}""",

    "sql_helper": """Translate the following natural language request into a robust, safe SQL query:
Schema Context: {schema}
User Query: {query}
Dialect: {dialect}""",

    "symptom_triage": """Provide educational health categorization for the reported symptoms. Emphasize that this is informational and not medical advice.
Symptoms: {symptoms}
Duration: {duration}
Severity Notes: {severity}""",
}

class PromptManager:
    """Manages prompt templates, system instructions, and injection."""

    def __init__(self):
        self.personas = PERSONAS
        self.templates = PROMPT_TEMPLATES

    def get_persona(self, persona_key: str) -> str:
        return self.personas.get(persona_key, "You are an expert AI assistant specializing in technical problem solving.")

    def format_prompt(self, template_key: str, **kwargs) -> str:
        template = self.templates.get(template_key)
        if not template:
            return " ".join(f"{k}: {v}" for k, v in kwargs.items())
        return template.format(**kwargs)

    def register_template(self, key: str, template: str):
        self.templates[key] = template

prompt_manager = PromptManager()
