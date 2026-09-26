"""Master Project Registry for AI58.
Defines all 58 projects across Beginner (19), Intermediate (20), and Advanced (19) tiers.
"""

from typing import Dict, Any, List

PROJECT_REGISTRY: List[Dict[str, Any]] = [
    # =========================================================================
    # BEGINNER TIER (19 Projects, 01 - 19)
    # =========================================================================
    {
        "id": 1,
        "slug": "01_ai_resume_optimizer",
        "tier": "BEGINNER",
        "name": "AI Resume Optimizer",
        "category": "Career & Professional",
        "description": "Reviews a resume and returns structured suggestions for improving it with ATS scoring, keyword alignment, and formatting guidance.",
        "capabilities": [
            "Resume upload & text extraction",
            "Section detection (Summary, Experience, Education, Skills)",
            "Skills extraction & taxonomy mapping",
            "Comparison against target job description",
            "Keyword density & ATS match analysis",
            "Formatting feedback & bullet-point impact assessment",
            "Structured improvement report",
            "Exportable optimized resume markdown"
        ],
        "technologies": ["NLP", "Pydantic", "TF-IDF Embeddings", "FastAPI", "Regex"],
        "default_input": {
            "resume_text": "Alex Morgan\nSoftware Engineer with 2 years of experience in Python and Flask.\nWorked on building REST APIs and bug fixes.\nSkills: Python, Git, SQL, HTML.",
            "target_job": "Senior Backend Engineer specializing in Python, FastAPI, Docker, PostgreSQL, Distributed Systems, and Microservices architecture."
        }
    },
    {
        "id": 2,
        "slug": "02_portfolio_builder",
        "tier": "BEGINNER",
        "name": "Portfolio Builder",
        "category": "Career & Professional",
        "description": "AI-assisted generator for personal portfolio sites with themes, live previews, and exportable layouts.",
        "capabilities": [
            "Personal info intake",
            "Project listings & achievements",
            "Skills matrix & proficiency tags",
            "Education & certifications",
            "Experience timeline",
            "AI-written compelling descriptions",
            "Theme picker (Modern Dark, Minimalist Light, Cyberpunk)",
            "Responsive layout generation & live preview",
            "Exportable static HTML/CSS/JS bundle"
        ],
        "technologies": ["Jinja2", "Prompt Engine", "Responsive HTML/CSS", "JSON Schema"],
        "default_input": {
            "full_name": "Jordan Lee",
            "headline": "Full-Stack AI Engineer & Distributed Systems Enthusiast",
            "bio_bullet_points": "5 years building cloud APIs; Loves Python and React; Contributed to open-source RAG pipelines.",
            "featured_projects": "1. DataFlow (Real-time analytics engine)\n2. NeuralNotes (AI-powered note summarizer)",
            "theme": "Modern Dark"
        }
    },
    {
        "id": 3,
        "slug": "03_interview_coach",
        "tier": "BEGINNER",
        "name": "Interview Coach",
        "category": "Career & Professional",
        "description": "AI assistant for interview practice featuring technical & behavioral simulations and answer evaluations.",
        "capabilities": [
            "Dynamic question generation",
            "Role-specific interview simulations",
            "Answer evaluation (STAR methodology)",
            "Constructive actionable feedback",
            "Intelligent follow-up questioning",
            "Technical interview mode",
            "Behavioral interview mode",
            "History of past practice sessions"
        ],
        "technologies": ["Prompt Manager", "NLP Scoring", "STAR Metric Engine"],
        "default_input": {
            "target_role": "Backend Engineer",
            "interview_type": "behavioral",
            "question": "Tell me about a time you encountered a major outage and how you resolved it.",
            "candidate_answer": "In my previous role, our payment service stopped responding during peak hours. I identified the database connection pool was exhausted, increased the pool limit, rolled out a patch, and added automated health checks."
        }
    },
    {
        "id": 4,
        "slug": "04_salary_negotiator",
        "tier": "BEGINNER",
        "name": "Salary Negotiator",
        "category": "Career & Professional",
        "description": "Helps prepare for compensation negotiations with market benchmarks, talking points, and package comparisons.",
        "capabilities": [
            "Job details intake & compensation parsing",
            "Experience & location benchmarking",
            "Skills premium evaluation",
            "Current offer breakdown (Base, Bonus, Equity, Benefits)",
            "Negotiation scenarios modeling",
            "Suggested talking points & counter-offer emails",
            "Side-by-side comparison of competing compensation packages",
            "Strict educational guidance disclaimer"
        ],
        "technologies": ["Compensation Parser", "Benchmarking Engine", "Scenario Modeling"],
        "default_input": {
            "job_title": "Senior Software Engineer",
            "location": "Remote / North America",
            "years_experience": 5,
            "offered_base": 140000,
            "offered_bonus": 15000,
            "offered_equity": 30000,
            "counter_target_base": 160000,
            "competing_offer_notes": "Competing offer has $155k base with better 401(k) matching."
        }
    },
    {
        "id": 5,
        "slug": "05_daily_productivity_manager",
        "tier": "BEGINNER",
        "name": "Daily Productivity Manager",
        "category": "Productivity & Lifestyle",
        "description": "AI productivity-management system with priority matrix, day planning, and daily recap analytics.",
        "capabilities": [
            "Daily task list management",
            "Eisenhower priority classification (Urgent/Important)",
            "Deadline tracking",
            "Suggested proactive tasks & batching",
            "Chronological day planning & time-blocking",
            "Progress & velocity tracking",
            "Productivity dashboard metrics",
            "Daily recap & tomorrow prep"
        ],
        "technologies": ["Time-Block Planner", "Priority Matrix", "Analytics Engine"],
        "default_input": {
            "work_hours": "09:00 - 17:00",
            "raw_tasks": "1. Deploy release v1.2 (urgent)\n2. Team sprint sync\n3. Review 3 pull requests\n4. Write design doc for auth service\n5. Clean up inbox"
        }
    },
    {
        "id": 6,
        "slug": "06_email_summarizer",
        "tier": "BEGINNER",
        "name": "Email Summarizer",
        "category": "Productivity & Lifestyle",
        "description": "Condenses lengthy emails and email threads into key points, action items, and priority flags.",
        "capabilities": [
            "Email & thread input",
            "Executive summary generation",
            "Key-point extraction",
            "Action items detection with assignees",
            "Deadline & milestone identification",
            "Urgency & priority flagging",
            "Search & tagging",
            "Historical digest logging"
        ],
        "technologies": ["Text Summarization", "Action Item Extractor", "Regex Date Parser"],
        "default_input": {
            "email_subject": "Q3 Infrastructure Migration and Budget Review",
            "email_body": "Hi team, regarding the cloud migration: we need dev instances migrated by Friday, Oct 12th. Alex is assigned to migrate the database clusters. Sarah must audit security group rules by next Tuesday. Please let me know if anyone foresees budget overruns exceeding our $5,000 threshold."
        }
    },
    {
        "id": 7,
        "slug": "07_meeting_memory",
        "tier": "BEGINNER",
        "name": "Meeting Memory",
        "category": "Productivity & Lifestyle",
        "description": "AI assistant that analyzes meeting transcripts to remember decisions, participants, and commitments.",
        "capabilities": [
            "Transcript intake (raw text / VTT / SRT)",
            "Concise meeting summary",
            "Decisions made log",
            "Action items & owners extraction",
            "Participant list & engagement detection",
            "Deadlines timeline",
            "Searchable archive of past meetings",
            "Follow-up email generator"
        ],
        "technologies": ["NLP Parser", "Transcript Chunking", "Decision Extractor"],
        "default_input": {
            "meeting_title": "Architecture Review: Payment Gateway Redesign",
            "transcript": "Dave: We need to decide whether to support Stripe or Adyen first.\nElena: Stripe has better webhooks for our current microservice stack.\nDave: Agreed, let's lock in Stripe for MVP.\nElena: I'll write the API contract by Wednesday.\nDave: I'll prepare the test environment by Thursday."
        }
    },
    {
        "id": 8,
        "slug": "08_career_path_recommender",
        "tier": "BEGINNER",
        "name": "Career Path Recommender",
        "category": "Career & Professional",
        "description": "Explores possible career directions, skill gaps, learning roadmaps, and target roles.",
        "capabilities": [
            "Current skills, education & experience intake",
            "Personal interests & preferred work style",
            "Target roles & market viability exploration",
            "Skill-gap analysis with delta scoring",
            "Milestone-based candidate learning paths",
            "Visual career roadmap progression",
            "Framed strictly as guidance, not guaranteed outcomes",
            "Quarterly skill checkpoints"
        ],
        "technologies": ["Skill Graph", "Gap Analyzer", "Career Roadmap Generator"],
        "default_input": {
            "current_role": "Junior Frontend Developer",
            "current_skills": ["JavaScript", "HTML/CSS", "React basics", "Git"],
            "target_role": "Full-Stack AI Application Engineer",
            "interests": "Generative AI, Python backend, building end-to-end products"
        }
    },
    {
        "id": 9,
        "slug": "09_learning_mentor",
        "tier": "BEGINNER",
        "name": "Learning Mentor",
        "category": "Education & Learning",
        "description": "AI mentor for self-directed learning with custom study plans, conceptual breakdowns, and quizzes.",
        "capabilities": [
            "Subject & domain selection",
            "Goal-oriented study planning",
            "Feynman-style simplified explanations",
            "Interactive practice questions & flashcards",
            "Progress & mastery tracking",
            "Personalized review suggestions",
            "Adaptive difficulty calibration"
        ],
        "technologies": ["Pedagogy Engine", "Quiz Generator", "Mastery Tracker"],
        "default_input": {
            "subject": "Vector Embeddings and Cosine Similarity in AI",
            "current_understanding": "Beginner - understands basic algebra",
            "goal": "Build an intuitive mental model and learn how similarity is computed"
        }
    },
    {
        "id": 10,
        "slug": "10_networking_assistant",
        "tier": "BEGINNER",
        "name": "Networking Assistant",
        "category": "Career & Professional",
        "description": "Helps manage professional contacts, draft warm outreach messages, and schedule follow-ups.",
        "capabilities": [
            "Contact management & relationship tags",
            "Networking goals & cadence settings",
            "Context-aware outreach message drafting",
            "Follow-up scheduling reminders",
            "Conversation notes & key mutual interests",
            "Relationship history & touchpoint log",
            "LinkedIn message templates"
        ],
        "technologies": ["Prompt Personalization", "Cadence Tracker", "Outreach Synthesizer"],
        "default_input": {
            "contact_name": "Dr. Sarah Chen",
            "contact_role": "VP of AI Research at SynthAI",
            "context": "Met briefly at the 2026 Tech Summit after her keynote on Agentic Workflows.",
            "networking_goal": "Request a 15-minute virtual coffee to ask for advice on transitioning into AI systems."
        }
    },
    {
        "id": 11,
        "slug": "11_personal_task_manager",
        "tier": "BEGINNER",
        "name": "Personal Task Manager",
        "category": "Productivity & Lifestyle",
        "description": "AI-assisted task management with intelligent prioritization, categorization, and recurring reminders.",
        "capabilities": [
            "Task creation, editing, and deletion",
            "Priority scoring (High, Medium, Low)",
            "Automatic smart categorizing",
            "Deadline tracking with countdown",
            "Recurring task configuration",
            "AI-assisted task breakdown into subtasks",
            "Completion velocity metrics"
        ],
        "technologies": ["Task Decomposition", "Categorizer", "SQLite Storage"],
        "default_input": {
            "task_title": "Launch Beta Version of SaaS Product",
            "category_hint": "Work / Startup",
            "due_date": "2026-10-15",
            "notes": "Need to ensure landing page, Stripe billing, and documentation are completely ready."
        }
    },
    {
        "id": 12,
        "slug": "12_smart_calendar",
        "tier": "BEGINNER",
        "name": "Smart Calendar",
        "category": "Productivity & Lifestyle",
        "description": "AI calendar assistant for scheduling, meeting conflict detection, and optimal time-slot recommendations.",
        "capabilities": [
            "Event creation & scheduling",
            "Conflict & overlap detection",
            "Suggested optimal focus and meeting time slots",
            "Daily agenda overview",
            "Weekly time allocation view",
            "Contextual reminders & buffer time enforcement",
            "Meeting fatigue warnings"
        ],
        "technologies": ["Interval Scheduling", "Conflict Engine", "Time Optimization"],
        "default_input": {
            "requested_event": "Design Sync (45 mins)",
            "preferred_day": "Tuesday",
            "working_hours": "09:00 - 17:00",
            "existing_events": [
                {"title": "Morning Standup", "start": "09:30", "end": "10:00"},
                {"title": "Client Presentation", "start": "11:00", "end": "12:30"},
                {"title": "1:1 with Manager", "start": "14:00", "end": "15:00"}
            ]
        }
    },
    {
        "id": 13,
        "slug": "13_study_planner",
        "tier": "BEGINNER",
        "name": "Study Planner",
        "category": "Education & Learning",
        "description": "AI-driven study planner with spaced repetition schedules, revision pacing, and weak topic detection.",
        "capabilities": [
            "Subject & syllabus intake",
            "Exam dates & milestone tracking",
            "Available study hours per day",
            "Spaced repetition study schedule",
            "Active revision planning",
            "Progress & confidence tracking",
            "Identification & prioritization of weak topics"
        ],
        "technologies": ["Spaced Repetition Engine", "Schedule Optimizer", "Confidence Scoring"],
        "default_input": {
            "exam_name": "AWS Certified Solutions Architect",
            "exam_date_days_remaining": 21,
            "daily_available_hours": 3,
            "topics_and_confidence": {
                "VPC & Networking": "Low",
                "S3 & Storage Classes": "High",
                "IAM & Security": "Medium",
                "ECS & Kubernetes": "Low",
                "Cost Management": "Medium"
            }
        }
    },
    {
        "id": 14,
        "slug": "14_job_application_tracker",
        "tier": "BEGINNER",
        "name": "Job Application Tracker",
        "category": "Career & Professional",
        "description": "Full job-application tracking system with status pipelines, interview logs, and application conversion analytics.",
        "capabilities": [
            "Company & position recording",
            "Application date & status pipeline (Applied, Screening, Tech Interview, Offer, Rejected)",
            "Interview stage logging & notes",
            "Follow-up reminders",
            "Document attachment tracking (resume version, cover letter)",
            "Application analytics & funnel conversion rates",
            "Salary expectations comparison"
        ],
        "technologies": ["Pipeline Engine", "Funnel Analytics", "CRUD Repository"],
        "default_input": {
            "company": "Stripe",
            "position": "Infrastructure Engineer",
            "status": "Tech Interview",
            "applied_date": "2026-09-10",
            "next_interview_date": "2026-09-30",
            "notes": "Passed initial recruiter screen. Recruiter emphasized distributed systems and rate limiting questions."
        }
    },
    {
        "id": 15,
        "slug": "15_freelancing_proposal_writer",
        "tier": "BEGINNER",
        "name": "Freelancing Proposal Writer",
        "category": "Career & Professional",
        "description": "AI assistant for writing winning freelance proposals with skill matching, tone tuning, and hook generation.",
        "capabilities": [
            "Job description intake & requirements parsing",
            "Skill & portfolio matching",
            "Persuasive proposal generation with strong hooks",
            "Tone selection (Confident, Friendly, Technical, Direct)",
            "Custom pricing & milestone structure generation",
            "Proposal history & winning metrics",
            "Exportable text/markdown"
        ],
        "technologies": ["Prompt Engineering", "Tone Calibration", "Proposal Synthesizer"],
        "default_input": {
            "platform": "Upwork",
            "client_job_post": "Need an experienced Python developer to build a web scraper and automated data pipeline into Supabase. Must handle proxy rotation and deliver clean JSON data.",
            "freelancer_skills": "Python, BeautifulSoup, Scrapy, Supabase, PostgreSQL, Docker",
            "tone": "Technical & Confident",
            "turnaround_days": 5
        }
    },
    {
        "id": 16,
        "slug": "16_work_life_balance_manager",
        "tier": "BEGINNER",
        "name": "Work-Life Balance Manager",
        "category": "Productivity & Lifestyle",
        "description": "Analyzes workload, sleep, and personal activities to detect burnout risks and recommend balance adjustments.",
        "capabilities": [
            "Work hours tracking",
            "Study & personal activities logging",
            "Task load & context switching assessment",
            "Calendar distribution analysis",
            "Workload visualization",
            "Burnout risk score",
            "Actionable balance improvement suggestions"
        ],
        "technologies": ["Workload Metrics", "Burnout Risk Index", "Time Distribution"],
        "default_input": {
            "daily_work_hours": 10.5,
            "weekend_work_hours": 4.0,
            "sleep_hours_avg": 5.8,
            "personal_time_hours": 1.2,
            "stress_self_rating": 8
        }
    },
    {
        "id": 17,
        "slug": "17_research_assistant",
        "tier": "BEGINNER",
        "name": "Research Assistant",
        "category": "Education & Learning",
        "description": "Organizes literature, synthesizes academic notes, extracts citations, and builds structured research briefs.",
        "capabilities": [
            "Research question input & decomposition",
            "Document & literature organization",
            "Evidence notes & key takeaways synthesis",
            "Citation management (BibTeX, APA, IEEE formats)",
            "Hypothesis formulation & literature critique",
            "Dedicated research workspace",
            "Exportable research brief"
        ],
        "technologies": ["Literature Synthesizer", "Citation Formatter", "Decomposition Engine"],
        "default_input": {
            "research_question": "What are the most effective retrieval strategies for reducing hallucinations in RAG systems?",
            "sample_sources": "1. Lewis et al. (2020) Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.\n2. Gao et al. (2024) Retrieval Augmented Generation for Large Language Models: A Survey."
        }
    },
    {
        "id": 18,
        "slug": "18_remote_work_buddy",
        "tier": "BEGINNER",
        "name": "Remote Work Buddy",
        "category": "Productivity & Lifestyle",
        "description": "Built for remote workers: daily kickoff, focus pomodoros, asynchronous communication reminders, and shutdown recap.",
        "capabilities": [
            "Daily kickoff planning",
            "Async meeting & standup organization",
            "Task management with focus session timers",
            "Communication reminders (pinging teammates, status updates)",
            "End-of-day shutdown routine",
            "Isolation & engagement check-in",
            "Daily productivity summary"
        ],
        "technologies": ["Focus Timer Model", "Async Status Generator", "Daily Shutdown Routine"],
        "default_input": {
            "timezone": "EST (UTC-5)",
            "top_priorities": "Finish API documentation, review PR #42, participate in async standup",
            "meetings_scheduled": 2,
            "current_feeling": "Slightly scattered, need focus"
        }
    },
    {
        "id": 19,
        "slug": "19_personal_branding_assistant",
        "tier": "BEGINNER",
        "name": "Personal Branding Assistant",
        "category": "Career & Professional",
        "description": "AI assistant for building a personal brand: bio optimization, thought-leadership post drafting, and portfolio positioning.",
        "capabilities": [
            "Profile analysis (LinkedIn, GitHub, X/Twitter)",
            "Multi-platform bio generation",
            "Content ideas & topic brainstorming",
            "Thought-leadership post drafting",
            "Skill presentation & positioning suggestions",
            "Portfolio highlight curation",
            "Personal brand consistency dashboard"
        ],
        "technologies": ["Brand Voice Tuner", "Social Post Generator", "Bio Synthesizer"],
        "default_input": {
            "current_title": "Software Engineer",
            "niche": "High-throughput backend systems & AI engineering",
            "target_audience": "Tech founders, engineering leaders, and fellow developers",
            "key_recent_win": "Optimized database query performance by 400% on a production microservice."
        }
    },

    # =========================================================================
    # INTERMEDIATE TIER (20 Projects, 20 - 39)
    # =========================================================================
    {
        "id": 20,
        "slug": "20_code_reviewer",
        "tier": "INTERMEDIATE",
        "name": "Code Reviewer",
        "category": "Developer Tools",
        "description": "AI code-review system with AST parsing, bug detection, style analysis, security checks, and line-level comments.",
        "capabilities": [
            "Code upload & snippet ingestion",
            "Git repository integration schemas",
            "Bug & logic flaw detection",
            "Style & idiomatic convention analysis",
            "Maintainability & complexity scoring",
            "Security vulnerability checks",
            "Line-by-line review comments",
            "Severity classification (Critical, Major, Minor, Info)"
        ],
        "technologies": ["Python AST", "Code Analysis Service", "Linting Engine"],
        "default_input": {
            "language": "python",
            "source_code": "def process_user_data(user_id, raw_query):\n    import sqlite3\n    conn = sqlite3.connect('app.db')\n    cursor = conn.cursor()\n    # Potential SQL injection vulnerability\n    query = \"SELECT * FROM users WHERE id = '\" + user_id + \"' AND info = '\" + raw_query + \"'\"\n    cursor.execute(query)\n    results = cursor.fetchall()\n    eval(\"print('Debug log: ' + str(results))\")\n    return results"
        }
    },
    {
        "id": 21,
        "slug": "21_bug_hunter",
        "tier": "INTERMEDIATE",
        "name": "Bug Hunter",
        "category": "Developer Tools",
        "description": "Automated bug-finding tool that classifies defects, suggests minimal-diff fixes, and generates regression tests.",
        "capabilities": [
            "Source-code static & semantic analysis",
            "Error & race condition detection",
            "Bug classification (NullPointer, Off-by-one, ResourceLeak, Injection)",
            "Automated patch & suggested fix generation",
            "Regression test-case generation",
            "Bug history & resolution tracking",
            "Confidence scoring for identified bugs"
        ],
        "technologies": ["Static Bug Classifier", "Patch Generator", "Pytest Generator"],
        "default_input": {
            "language": "python",
            "source_code": "def calculate_average(numbers):\n    total = 0\n    for i in range(len(numbers)):\n        total += numbers[i]\n    # Bug: Division by zero when list is empty\n    return total / len(numbers)\n\ndef find_element(items, target):\n    # Bug: Off by one error in loop bound\n    for i in range(len(items) - 1):\n        if items[i] == target:\n            return i\n    return -1"
        }
    },
    {
        "id": 22,
        "slug": "22_pr_reviewer",
        "tier": "INTERMEDIATE",
        "name": "PR Reviewer",
        "category": "Developer Tools",
        "description": "Reviews Git pull requests by analyzing unified diffs, detecting regressions, and producing executive PR summaries.",
        "capabilities": [
            "Unified Git diff analysis",
            "Breaking change detection",
            "Regression risk scoring",
            "Automated PR summary & impact assessment",
            "Suggested inline GitHub comments",
            "Test coverage gap alerts",
            "Merge approval recommendation (Approve, Request Changes, Comment)"
        ],
        "technologies": ["Diff Parser", "Risk Scoring Engine", "GitHub Review Synthesizer"],
        "default_input": {
            "pr_title": "feat: switch payment processor to async webhook",
            "git_diff": "--- a/services/payment.py\n+++ b/services/payment.py\n@@ -10,6 +10,12 @@ def charge_card(user_id, amount):\n-    res = sync_stripe_charge(user_id, amount)\n+    # Remove timeout safeguard and fire async without error boundary\n+    res = stripe.PaymentIntent.create(amount=int(amount*100), currency='usd')\n+    if not res.get('id'):\n+        return False\n     return res"
        }
    },
    {
        "id": 23,
        "slug": "23_api_tester",
        "tier": "INTERMEDIATE",
        "name": "API Tester",
        "category": "Developer Tools",
        "description": "AI-assisted API-testing platform: generates test suites, validates response schemas, and checks auth edge cases.",
        "capabilities": [
            "Endpoint specification management",
            "Automated request payload generation",
            "Response status & schema validation",
            "Boundary & edge-case test case generation",
            "Authentication & authorization testing",
            "Error handling validation",
            "Exportable Postman / pytest-httpx test suites"
        ],
        "technologies": ["OpenAPI Parser", "Schema Validator", "HTTPX Runner"],
        "default_input": {
            "endpoint": "POST /api/v1/orders",
            "auth_type": "Bearer Token",
            "request_schema": "{\"item_id\": \"string (required)\", \"quantity\": \"integer (> 0)\", \"coupon_code\": \"string (optional)\"}",
            "expected_response": "{\"order_id\": \"string\", \"status\": \"pending\", \"total_price\": \"float\"}"
        }
    },
    {
        "id": 24,
        "slug": "24_code_explainer",
        "tier": "INTERMEDIATE",
        "name": "Code Explainer",
        "category": "Developer Tools",
        "description": "Explains complex code snippets line-by-line, analyzes time/space complexity, and generates documentation.",
        "capabilities": [
            "Multi-language code ingestion",
            "Line-by-line walk-throughs",
            "High-level conceptual architectural explanations",
            "Big-O time and space complexity analysis",
            "Beginner mode (plain English, analogies)",
            "Advanced mode (memory models, algorithmic invariants)",
            "Automated docstring & markdown documentation"
        ],
        "technologies": ["Complexity Analyzer", "AST Explainer", "Docstring Generator"],
        "default_input": {
            "language": "python",
            "mode": "beginner",
            "code": "def quicksort(arr):\n    if len(arr) <= 1:\n        return arr\n    pivot = arr[len(arr) // 2]\n    left = [x for x in arr if x < pivot]\n    middle = [x for x in arr if x == pivot]\n    right = [x for x in arr if x > pivot]\n    return quicksort(left) + middle + quicksort(right)"
        }
    },
    {
        "id": 25,
        "slug": "25_code_refactorer",
        "tier": "INTERMEDIATE",
        "name": "Code Refactorer",
        "category": "Developer Tools",
        "description": "Refactors legacy code to improve maintainability, reduce cognitive complexity, and preserve behavioral contracts.",
        "capabilities": [
            "Code smell & anti-pattern detection",
            "Refactoring proposals (Extract Function, Replace Conditional with Polymorphism)",
            "Side-by-side before/after code comparison",
            "Cognitive & cyclomatic complexity delta",
            "Maintainability score improvements",
            "Test preservation guarantees",
            "Modular drop-in replacements"
        ],
        "technologies": ["Refactoring Rules", "Complexity Delta", "AST Transformer"],
        "default_input": {
            "language": "python",
            "code": "def process_order(order):\n    if order['status'] == 'pending':\n        if order['total'] > 100:\n            if order['customer_type'] == 'VIP':\n                discount = 0.2\n            else:\n                discount = 0.1\n        else:\n            if order['customer_type'] == 'VIP':\n                discount = 0.05\n            else:\n                discount = 0\n        final_price = order['total'] * (1 - discount)\n        print('Final price calculated: ' + str(final_price))\n        return final_price\n    else:\n        return None"
        }
    },
    {
        "id": 26,
        "slug": "26_system_design_partner",
        "tier": "INTERMEDIATE",
        "name": "System Design Partner",
        "category": "System Architecture & Security",
        "description": "AI assistant for architecting scalable distributed systems with component diagrams, trade-off analysis, and DB design.",
        "capabilities": [
            "Functional & non-functional requirements intake",
            "Distributed architecture topology generation",
            "Component breakdown (Gateway, Services, Message Queues, Cache)",
            "Database schema & data modeling (SQL vs NoSQL)",
            "API design (REST/gRPC)",
            "Scalability, availability & bottleneck discussion",
            "Mermaid architecture diagram generation",
            "Trade-off analysis (CAP theorem, latency vs consistency)"
        ],
        "technologies": ["System Design Engine", "Mermaid Diagram Generator", "CAP Trade-off Model"],
        "default_input": {
            "system_name": "Global URL Shortener (Bitly clone)",
            "scale": "100 Million daily active users, 10,000 writes/sec, 100,000 reads/sec (10:1 read-to-write ratio)",
            "key_requirements": "High availability, <50ms read latency, customizable short aliases, click analytics"
        }
    },
    {
        "id": 27,
        "slug": "27_documentation_writer",
        "tier": "INTERMEDIATE",
        "name": "Documentation Writer",
        "category": "Developer Tools",
        "description": "Generates production-grade README files, API specifications, and architecture documents from source code.",
        "capabilities": [
            "Source-code & repository structure analysis",
            "Comprehensive README.md generation",
            "OpenAPI / Swagger endpoint documentation",
            "Function & module docstrings generation",
            "Installation & quickstart guides",
            "Configuration environment tables",
            "Architecture overview docs"
        ],
        "technologies": ["Doc Generator", "AST Docstring Extractor", "Markdown Synthesizer"],
        "default_input": {
            "project_name": "HyperCache",
            "description": "In-memory distributed key-value store built in Python with TTL expiration and LRU eviction policy.",
            "sample_code": "class HyperCache:\n    def __init__(self, capacity: int = 1000):\n        self.capacity = capacity\n    def get(self, key: str) -> any:\n        pass\n    def put(self, key: str, val: any, ttl_seconds: int = 3600) -> bool:\n        pass"
        }
    },
    {
        "id": 28,
        "slug": "28_dsa_practice_buddy",
        "tier": "INTERMEDIATE",
        "name": "DSA Practice Buddy",
        "category": "Education & Learning",
        "description": "AI system for mastering Data Structures & Algorithms with dynamic problem generation, hints, and complexity audits.",
        "capabilities": [
            "Topic selection (Trees, Graphs, DP, Sliding Window, Greedy)",
            "Difficulty calibration (Easy, Medium, Hard)",
            "Problem prompt & test-case generator",
            "Progressive multi-tier hint system",
            "Optimal solution explanation & code walk-through",
            "Time and space complexity analysis",
            "Tracking weak topic patterns"
        ],
        "technologies": ["Algorithm Taxonomy", "Progressive Hint Engine", "Test-Case Builder"],
        "default_input": {
            "topic": "Dynamic Programming",
            "difficulty": "Medium",
            "preferred_language": "Python",
            "specific_pattern": "Longest Increasing Subsequence or Knapsack variation"
        }
    },
    {
        "id": 29,
        "slug": "29_learning_tracker",
        "tier": "INTERMEDIATE",
        "name": "Learning Tracker",
        "category": "Education & Learning",
        "description": "Tracks curriculum progress, logs study sessions, computes retention curves, and recommends revision sprints.",
        "capabilities": [
            "Course & syllabus taxonomy tracking",
            "Topic mastery progression",
            "Study session logging with duration & focus rating",
            "Learning analytics & velocity metrics",
            "Retention curve estimation",
            "Personalized review recommendations",
            "Interactive learning streak dashboard"
        ],
        "technologies": ["Retention Modeling", "Curriculum Tracker", "Analytics Engine"],
        "default_input": {
            "track_name": "Machine Learning Foundations",
            "completed_modules": ["Linear Algebra", "Calculus for ML", "Supervised Learning (Regression/Classification)"],
            "current_module": "Unsupervised Learning & Clustering",
            "hours_studied_this_week": 12.5,
            "quiz_scores": [85, 92, 78]
        }
    },
    {
        "id": 30,
        "slug": "30_code_debugger",
        "tier": "INTERMEDIATE",
        "name": "Code Debugger",
        "category": "Developer Tools",
        "description": "Analyzes stack traces, identifies root causes in source code, and suggests precise verification steps.",
        "capabilities": [
            "Stack-trace parsing & exception classification",
            "Source code correlation",
            "Root-cause diagnostic explanation",
            "Suggested minimal-diff code fixes",
            "Step-by-step debugging instructions",
            "Fix verification test cases",
            "Prevention tips for future regressions"
        ],
        "technologies": ["Traceback Parser", "Diagnostic Engine", "Patch Verifier"],
        "default_input": {
            "error_message": "IndexError: list index out of range",
            "stack_trace": "Traceback (most recent call last):\n  File \"pipeline.py\", line 42, in process_batch\n    current_item = items[idx + 1]\nIndexError: list index out of range",
            "code_snippet": "def process_batch(items):\n    for idx in range(len(items)):\n        current_item = items[idx + 1]\n        print(current_item)"
        }
    },
    {
        "id": 31,
        "slug": "31_repo_summarizer",
        "tier": "INTERMEDIATE",
        "name": "Repo Summarizer",
        "category": "Developer Tools",
        "description": "Analyzes repository directory trees, explains system architecture, dependencies, and entry-points.",
        "capabilities": [
            "Repository directory tree analysis",
            "Architecture pattern identification (Monolith, Microservices, Hexagonal)",
            "Dependency graph analysis",
            "Automated repository overview README",
            "Key entry-points & critical files identification",
            "Tech-stack breakdown",
            "Onboarding guide for new developers"
        ],
        "technologies": ["File Tree Parser", "Architecture Detector", "Dependency Mapper"],
        "default_input": {
            "repo_name": "FastE-Commerce",
            "file_tree": "backend/\n  api/\n    v1/\n      auth.py\n      cart.py\n      orders.py\n  core/\n    config.py\n    database.py\n  models/\n    user.py\n    order.py\nfrontend/\n  src/\n    pages/\n      Checkout.tsx\n      Store.tsx\npackage.json\nrequirements.txt\ndocker-compose.yml"
        }
    },
    {
        "id": 32,
        "slug": "32_devops_automator",
        "tier": "INTERMEDIATE",
        "name": "DevOps Automator",
        "category": "Developer Tools",
        "description": "Generates production CI/CD workflows, Dockerfiles, and deployment scripts with log diagnosis.",
        "capabilities": [
            "GitHub Actions / GitLab CI pipeline generation",
            "Optimized multi-stage Dockerfile scaffolding",
            "Kubernetes manifests & docker-compose configurations",
            "CI/CD build failure log analysis",
            "Deployment status checklists",
            "Infrastructure documentation",
            "Security hardening tips (non-root users, slim images)"
        ],
        "technologies": ["Docker Generator", "CI/CD Synthesizer", "Log Diagnostic Engine"],
        "default_input": {
            "app_type": "Node.js & Express REST API with PostgreSQL",
            "target_environment": "Docker & GitHub Actions CI/CD",
            "requirements": "Lint, test with Jest, build minimal Docker image, push to DockerHub"
        }
    },
    {
        "id": 33,
        "slug": "33_testing_assistant",
        "tier": "INTERMEDIATE",
        "name": "Testing Assistant",
        "category": "Developer Tools",
        "description": "Generates unit tests, integration tests, mock fixtures, and boundary cases to maximize code coverage.",
        "capabilities": [
            "Unit-test generation (pytest / jest / mocha)",
            "Integration test suite scaffolding",
            "Edge-case & boundary value generation",
            "Mock fixtures & dependency injection setups",
            "Test assertions explanation",
            "Coverage gap analysis",
            "Test report generation"
        ],
        "technologies": ["Pytest Generator", "Boundary Value Analyzer", "Mock Scaffolder"],
        "default_input": {
            "framework": "pytest",
            "source_code": "def transfer_funds(source_account, dest_account, amount):\n    if amount <= 0:\n        raise ValueError('Amount must be positive')\n    if source_account['balance'] < amount:\n        raise ValueError('Insufficient funds')\n    source_account['balance'] -= amount\n    dest_account['balance'] += amount\n    return {'status': 'transferred', 'amount': amount}"
        }
    },
    {
        "id": 34,
        "slug": "34_cloud_cost_optimizer",
        "tier": "INTERMEDIATE",
        "name": "Cloud Cost Optimizer",
        "category": "Developer Tools",
        "description": "Analyzes cloud resource utilization, flags idle assets, forecasts monthly spend, and provides actionable cost reductions.",
        "capabilities": [
            "Cloud resource inventory intake (AWS, GCP, Azure)",
            "Cost breakdown by service & tag",
            "Idle & underutilized resource detection",
            "Right-sizing recommendations (EC2, RDS, VMs)",
            "Monthly cost forecasting",
            "Savings plans & reserved instance recommendations",
            "Executive cost optimization summary"
        ],
        "technologies": ["Cloud Spend Engine", "Utilization Profiler", "Cost Forecaster"],
        "default_input": {
            "cloud_provider": "AWS",
            "monthly_spend_usd": 8500,
            "resources": [
                {"type": "EC2 (m5.4xlarge)", "count": 6, "avg_cpu_percent": 8.2, "monthly_cost": 3200},
                {"type": "RDS Postgres (db.r5.2xlarge)", "count": 2, "avg_cpu_percent": 14.5, "monthly_cost": 2100},
                {"type": "EBS Volumes (gp2 unattached)", "count": 15, "size_gb": 4000, "monthly_cost": 400},
                {"type": "NAT Gateway Data Transfer", "count": 3, "monthly_cost": 1800}
            ]
        }
    },
    {
        "id": 35,
        "slug": "35_data_cleaner",
        "tier": "INTERMEDIATE",
        "name": "Data Cleaner",
        "category": "Data & ML",
        "description": "AI-assisted data-cleaning platform: detects missing values, duplicates, outliers, normalizes types, and exports clean CSVs.",
        "capabilities": [
            "CSV upload & parsing",
            "Missing value detection & smart imputation",
            "Duplicate record identification & deduplication",
            "Outlier detection using IQR & Z-score metrics",
            "Data-type inference & standardization",
            "Comprehensive cleaning audit report",
            "Exportable cleaned dataset (CSV/JSON)"
        ],
        "technologies": ["Pandas", "NumPy", "Data Engine", "Statistical Profiler"],
        "default_input": {
            "csv_content": "id,name,age,salary,department\n1,Alice,29,75000,Engineering\n2,Bob,,82000,Engineering\n3,Charlie,35,95000,Marketing\n4,Alice,29,75000,Engineering\n5,David,42,120000,Finance\n6,Eve,24,520000,Finance\n7,Frank,,61000,Sales"
        }
    },
    {
        "id": 36,
        "slug": "36_sql_query_helper",
        "tier": "INTERMEDIATE",
        "name": "SQL Query Helper",
        "category": "Developer Tools",
        "description": "Translates natural language to SQL, explains execution plans, optimizes slow queries, and enforces safety checks.",
        "capabilities": [
            "Natural-language-to-SQL generation",
            "SQL query plain-English explanation",
            "Query syntax correction & debugging",
            "Optimization suggestions & index advice",
            "Database schema awareness (Postgres, MySQL, SQLite)",
            "SQL query formatting & beautification",
            "Safe-query validation (flags destructive DROP/DELETE without WHERE)"
        ],
        "technologies": ["SQL AST Engine", "Safety Validator", "NL2SQL Generator"],
        "default_input": {
            "dialect": "PostgreSQL",
            "schema": "TABLE users (id SERIAL PRIMARY KEY, name VARCHAR, created_at TIMESTAMP);\nTABLE orders (id SERIAL PRIMARY KEY, user_id INT, amount DECIMAL, status VARCHAR, created_at TIMESTAMP);",
            "request": "Find the top 5 users who spent the most money on completed orders in the last 30 days."
        }
    },
    {
        "id": 37,
        "slug": "37_ai_project_builder",
        "tier": "INTERMEDIATE",
        "name": "AI Project Builder",
        "category": "Developer Tools",
        "description": "Scaffolds new software architectures from ideas: tech stack, folder hierarchy, task breakdown, and technical roadmap.",
        "capabilities": [
            "Project idea intake & requirement expansion",
            "Functional specifications generation",
            "System architecture design",
            "Production folder structure scaffolding",
            "Optimal tech-stack selection with trade-offs",
            "Epic & sprint task breakdown",
            "Development roadmap timeline",
            "Starter documentation and config generation"
        ],
        "technologies": ["Scaffolding Engine", "Tech Stack Evaluator", "Roadmap Synthesizer"],
        "default_input": {
            "project_idea": "Real-time collaborative markdown documentation tool with AI autocomplete and team workspaces",
            "target_users": "Software engineering teams and technical writers",
            "target_scale": "5,000 active concurrent users",
            "preferred_stack": "Next.js / Python / Redis / WebSockets"
        }
    },
    {
        "id": 38,
        "slug": "38_model_evaluator",
        "tier": "INTERMEDIATE",
        "name": "Model Evaluator",
        "category": "Data & ML",
        "description": "ML model-evaluation platform: calculates classification/regression metrics, confusion matrix, ROC-AUC, and feature rankings.",
        "capabilities": [
            "Model predictions & ground-truth dataset intake",
            "Classification metrics (Precision, Recall, F1-Score, Accuracy)",
            "Regression metrics (RMSE, MAE, R-squared)",
            "Confusion matrix calculation & analysis",
            "ROC-AUC curve metric evaluation",
            "Feature importance ranking",
            "Model comparison leaderboard",
            "Experiment tracking metadata"
        ],
        "technologies": ["Scikit-Learn", "Metrics Engine", "Confusion Matrix Calculator"],
        "default_input": {
            "task_type": "classification",
            "y_true": [1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1],
            "y_pred": [1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
            "feature_names": ["age", "account_balance", "num_logins", "support_tickets"],
            "model_name": "RandomForestClassifier_v2"
        }
    },
    {
        "id": 39,
        "slug": "39_security_vulnerability_finder",
        "tier": "INTERMEDIATE",
        "name": "Security Vulnerability Finder",
        "category": "System Architecture & Security",
        "description": "Defensive security analysis tool: scans source code, analyzes dependencies, identifies CVE patterns, and suggests remediation.",
        "capabilities": [
            "Source-code static defensive scanning",
            "Dependency & package vulnerability analysis",
            "Vulnerability identification (OWASP Top 10)",
            "Severity classification (Critical, High, Medium, Low)",
            "Concrete remediation patches & safe alternatives",
            "Comprehensive defensive security report",
            "Strict limitation to authorized defensive analysis"
        ],
        "technologies": ["Security Linter", "OWASP Rules", "Defensive Code Scanner"],
        "default_input": {
            "language": "python",
            "source_code": "import os, subprocess\ndef run_ping(target_host):\n    # Command injection hazard\n    return subprocess.check_output('ping -c 1 ' + target_host, shell=True)\n\ndef auth_user(token):\n    secret = 'SUPER_SECRET_KEY_12345' # Hardcoded secret\n    if token == secret:\n        return True\n    return False"
        }
    },

    # =========================================================================
    # ADVANCED TIER (19 Projects, 40 - 58)
    # =========================================================================
    {
        "id": 40,
        "slug": "40_fitness_coach",
        "tier": "ADVANCED",
        "name": "Fitness Coach",
        "category": "Health & Well-being",
        "description": "AI fitness-coaching assistant: personalizes workout regimens, progressive overload schedules, and safety boundaries.",
        "capabilities": [
            "Fitness goals intake (Strength, Hypertrophy, Endurance, Mobility)",
            "Equipment & schedule constraints consideration",
            "Structured periodized workout planning",
            "Exercise form cues & alternatives",
            "Progress & volume tracking",
            "Weekly schedule optimization",
            "Mandatory physical safety limitations & non-medical disclaimer"
        ],
        "technologies": ["Workout Periodizer", "Volume Calculator", "Safety Boundary Engine"],
        "default_input": {
            "goal": "Build functional strength and upper-body muscle",
            "experience_level": "Intermediate (1 year lifting)",
            "available_equipment": "Barbell, Squat Rack, Bench, Dumbbells",
            "days_per_week": 4,
            "session_duration_minutes": 60,
            "injuries_or_limitations": "Mild lower-back tightness after deadlifts"
        }
    },
    {
        "id": 41,
        "slug": "41_nutrition_planner",
        "tier": "ADVANCED",
        "name": "Nutrition Planner",
        "category": "Health & Well-being",
        "description": "AI nutrition assistant: builds balanced meal plans, calculates macronutrient targets, and compiles shopping lists.",
        "capabilities": [
            "Dietary preferences & allergy intake (Vegan, Keto, Mediterranean, Gluten-Free)",
            "Daily caloric & macronutrient target calculation",
            "7-day balanced meal planning",
            "Nutritional breakdown per meal",
            "Categorized grocery shopping list generator",
            "Meal prep & batch cooking instructions",
            "Clear separation of general planning from registered dietetic advice"
        ],
        "technologies": ["Macro Engine", "Meal Planner", "Dietary Guardrails"],
        "default_input": {
            "target_calories": 2400,
            "macro_split": "40% Carbs, 30% Protein, 30% Fat",
            "dietary_style": "High-protein Mediterranean",
            "allergies": "Peanuts",
            "meals_per_day": 3
        }
    },
    {
        "id": 42,
        "slug": "42_habit_tracker",
        "tier": "ADVANCED",
        "name": "Habit Tracker",
        "category": "Productivity & Lifestyle",
        "description": "Intelligent habit-tracking system: calculates streaks, detects behavioral drop-offs, and suggests habit stacking.",
        "capabilities": [
            "Habit creation with cue, routine, and reward structure",
            "Streak calculation & resilience scoring",
            "Completion rate analytics",
            "Smart contextual reminders",
            "Behavioral pattern & drop-off analysis",
            "Habit stacking suggestions (Atomic Habits framework)",
            "Monthly consistency dashboard"
        ],
        "technologies": ["Habit Stacking Engine", "Streak Calculator", "Behavioral Analyzer"],
        "default_input": {
            "habits": [
                {"name": "Morning Cold Shower / Hydration", "frequency": "daily", "streak_days": 18, "success_rate": 0.90},
                {"name": "30 Minutes LeetCode / Coding Practice", "frequency": "daily", "streak_days": 5, "success_rate": 0.72},
                {"name": "Evening Meditation (10m)", "frequency": "daily", "streak_days": 2, "success_rate": 0.45}
            ]
        }
    },
    {
        "id": 43,
        "slug": "43_mood_journal",
        "tier": "ADVANCED",
        "name": "Mood Journal",
        "category": "Health & Well-being",
        "description": "Private, AI-assisted reflective journaling: extracts sentiment trends, cognitive distortions, and promotes mindful self-awareness.",
        "capabilities": [
            "Private journal entry logging",
            "Sentiment & emotional valence tracking",
            "Identification of positive drivers & stressors",
            "Cognitive reframing suggestions",
            "Mood trend visualization over time",
            "Private encrypted local storage controls",
            "Strict safety policy: does not diagnose mental health conditions"
        ],
        "technologies": ["Sentiment Analyzer", "Cognitive Reframer", "Valence Tracker"],
        "default_input": {
            "journal_text": "Had a stressful day at work. The production deployment failed and I felt like it was entirely my fault, even though the whole team reviewed the PR. I felt overwhelmed and skipped my afternoon walk, which made me feel sluggish all evening."
        }
    },
    {
        "id": 44,
        "slug": "44_book_summarizer",
        "tier": "ADVANCED",
        "name": "Book Summarizer",
        "category": "Education & Learning",
        "description": "AI system for deep document & book analysis: extracts chapter outlines, core mental models, and actionable takeaways.",
        "capabilities": [
            "Long-form document & chapter ingestion",
            "Executive summary synthesis",
            "Chapter-by-chapter concept extraction",
            "Key mental models & frameworks identification",
            "Actionable quotes & takeaways",
            "Concept search & thematic index",
            "Strict copyright respect & fair-use conceptual abstraction"
        ],
        "technologies": ["Hierarchical Summarizer", "Concept Extractor", "Mental Model Synthesizer"],
        "default_input": {
            "book_title": "Designing Data-Intensive Applications by Martin Kleppmann",
            "focus_topic": "Chapter on Replication and Distributed Consensus",
            "text_sample": "Replication means keeping a copy of the same data on multiple machines that are connected via a network. Why replicate? High availability, disconnected operation, latency reduction, and scalability. The three main approaches are single-leader, multi-leader, and leaderless replication."
        }
    },
    {
        "id": 45,
        "slug": "45_meditation_guide",
        "tier": "ADVANCED",
        "name": "Meditation Guide",
        "category": "Health & Well-being",
        "description": "AI-guided mindfulness and meditation assistant: generates calming session scripts, breathing pacing, and stress relief exercises.",
        "capabilities": [
            "Session theme selection (Focus, Stress Relief, Sleep, Body Scan)",
            "Configurable duration (3m, 5m, 10m, 20m)",
            "Paced breathing cycles (Box breathing, 4-7-8, Pranayama)",
            "Full immersive guided meditation scripts",
            "Mindfulness progress & streak tracking",
            "Calming voice TTS audio synthesis specs",
            "Personalized relaxation recommendations"
        ],
        "technologies": ["TTS Audio Spec", "Paced Breathing Engine", "Mindfulness Script Generator"],
        "default_input": {
            "theme": "Deep Focus and Mental Clarity",
            "duration_minutes": 5,
            "breathing_technique": "Box Breathing (4s Inhale, 4s Hold, 4s Exhale, 4s Hold)",
            "experience_level": "Beginner"
        }
    },
    {
        "id": 46,
        "slug": "46_skill_coach",
        "tier": "ADVANCED",
        "name": "Skill Coach",
        "category": "Education & Learning",
        "description": "Systematic coach for mastering any target skill: builds deliberate practice drills, milestone checkpoints, and objective feedback.",
        "capabilities": [
            "Skill taxonomy intake (e.g. Public Speaking, Rust Programming, Chess)",
            "Current baseline assessment",
            "Target competency definition",
            "Deliberate practice drills generation",
            "Milestone-based mastery roadmap",
            "Objective feedback loop & error analysis",
            "Long-term skill retention tracking"
        ],
        "technologies": ["Deliberate Practice Engine", "Skill Matrix", "Mastery Roadmap"],
        "default_input": {
            "skill_name": "Rust Systems Programming",
            "current_level": "Beginner (knows basic syntax, struggling with Borrow Checker and lifetimes)",
            "target_goal": "Build a multi-threaded TCP chat server in idiomatic Rust",
            "weekly_hours_dedicated": 8
        }
    },
    {
        "id": 47,
        "slug": "47_time_audit_tool",
        "tier": "ADVANCED",
        "name": "Time Audit Tool",
        "category": "Productivity & Lifestyle",
        "description": "Audits time expenditures across deep work, shallow tasks, meetings, and breaks to eliminate time leaks.",
        "capabilities": [
            "Activity log ingestion",
            "Categorization into Deep Work, Shallow Work, Meetings, Leisure, Overhead",
            "Daily & weekly time distribution analysis",
            "Productivity ratio & context switching cost",
            "Time allocation visual charts",
            "High-impact recommendations for reclaiming hours",
            "Weekly audit summary report"
        ],
        "technologies": ["Time Category Engine", "Context Switch Metric", "Audit Profiler"],
        "default_input": {
            "week_logs": [
                {"category": "Deep Work (Coding)", "hours": 14.5},
                {"category": "Meetings & Syncs", "hours": 12.0},
                {"category": "Shallow Work (Slack/Emails)", "hours": 9.5},
                {"category": "Administrative / Overhead", "hours": 4.0},
                {"category": "Unplanned Distractions", "hours": 5.0}
            ]
        }
    },
    {
        "id": 48,
        "slug": "48_language_learning_buddy",
        "tier": "ADVANCED",
        "name": "Language Learning Buddy",
        "category": "Education & Learning",
        "description": "Interactive language coach: conversational roleplay, grammar error correction, vocabulary flashcards, and pronunciation tips.",
        "capabilities": [
            "Target language & CEFR level selection (A1 - C2)",
            "Contextual conversational roleplay scenarios",
            "Grammar & syntax error correction with explanations",
            "Vocabulary expansion lists with spaced repetition tags",
            "Pronunciation guidance & phonetic transcripts",
            "Interactive comprehension quizzes",
            "Progress & fluency velocity tracking"
        ],
        "technologies": ["CEFR Grader", "Grammar Corrector", "Roleplay Dialogue Engine"],
        "default_input": {
            "target_language": "Spanish",
            "user_level": "A2 (Elementary)",
            "scenario": "Ordering food in a restaurant in Madrid",
            "user_utterance": "Hola camarero, yo querer una paella de mariscos y un agua fria por favor."
        }
    },
    {
        "id": 49,
        "slug": "49_sleep_coach",
        "tier": "ADVANCED",
        "name": "Sleep Coach",
        "category": "Health & Well-being",
        "description": "Analyzes sleep schedules, circadian rhythms, sleep debt, and recommends optimal wind-down routines.",
        "capabilities": [
            "Sleep & wake timestamp tracking",
            "Circadian consistency scoring",
            "Sleep debt calculation",
            "Pre-sleep wind-down routine design",
            "Sleep hygiene environmental recommendations (light, temperature, caffeine cut-off)",
            "Sleep trend visualization",
            "Strict educational non-medical disclaimer"
        ],
        "technologies": ["Circadian Rhythm Model", "Sleep Debt Calculator", "Hygiene Engine"],
        "default_input": {
            "average_bedtime": "01:30 AM",
            "average_wake_time": "07:15 AM",
            "sleep_consistency_rating": "Erratic (varies by 3 hours on weekends)",
            "caffeine_intake": "3 cups of coffee, last cup at 5:00 PM",
            "screen_time_before_bed": "Looking at phone in bed for 45 minutes"
        }
    },
    {
        "id": 50,
        "slug": "50_emergency_overload_predictor",
        "tier": "ADVANCED",
        "name": "Emergency Overload Predictor",
        "category": "Public Good & Civic",
        "description": "Research-oriented time-series anomaly detection for server clusters, hospital wards, or emergency response loads.",
        "capabilities": [
            "Telemetry & time-series data ingestion",
            "Rolling anomaly detection & threshold alerts",
            "Early warning risk indicators",
            "Overload probability calculation",
            "Capacity bottleneck visualization",
            "Resource reallocation recommendations",
            "Clear disclaimer: research predictions are not guaranteed emergencies"
        ],
        "technologies": ["Time Series Anomaly", "Z-Score Profiler", "Risk Classifier"],
        "default_input": {
            "system_type": "Regional Emergency Dispatch Service",
            "metric_name": "Active Emergency Calls / Minute",
            "time_series_data": [42, 45, 48, 50, 52, 49, 53, 98, 112, 125, 138, 145],
            "max_safe_capacity": 80
        }
    },
    {
        "id": 51,
        "slug": "51_disaster_relief_coordinator",
        "tier": "ADVANCED",
        "name": "Disaster Relief Coordinator",
        "category": "Public Good & Civic",
        "description": "Assists crisis teams in organizing supply routes, volunteer dispatch, and priority queues with human oversight.",
        "capabilities": [
            "Incident records & disaster location mapping",
            "Resource & supply inventory tracking (Water, Medical, Food, Shelter)",
            "Urgency priority queue computation (Triage priority)",
            "Volunteer skill-to-need dispatch coordination",
            "Supply delivery route optimization",
            "Executive situation room dashboard",
            "Human decision-makers remain in control at all times"
        ],
        "technologies": ["Triage Dispatcher", "Priority Queue", "Resource Allocator"],
        "default_input": {
            "disaster_type": "Flash Flood in Sector 7",
            "affected_population": 4500,
            "critical_needs": "Drinkable water, insulin cold storage, inflatable rescue boats",
            "available_supplies": "300 water filtration packs, 5 emergency medical kits, 4 rescue teams",
            "evacuation_status": "65% of vulnerable residents sheltered"
        }
    },
    {
        "id": 52,
        "slug": "52_eco_friendly_living_guide",
        "tier": "ADVANCED",
        "name": "Eco-Friendly Living Guide",
        "category": "Public Good & Civic",
        "description": "Calculates carbon footprints across transit, home energy, and diet, providing high-impact sustainability steps.",
        "capabilities": [
            "Lifestyle consumption intake (Home energy, Transit, Food, Goods)",
            "Carbon footprint estimation (Metric tons CO2e / year)",
            "Breakdown by emission category",
            "High-impact vs low-effort reduction steps",
            "Personalized eco-friendly alternatives",
            "Lifetime emission savings visualization",
            "Environmental sustainability milestones"
        ],
        "technologies": ["Carbon Calculator", "Emission Factors", "Sustainability Engine"],
        "default_input": {
            "home_heating": "Natural gas / 1200 sq ft apartment",
            "commute_type": "Gasoline vehicle, 25 miles roundtrip, 5 days/week",
            "diet": "Omnivore (meat 5-6 times per week)",
            "flights_per_year": 3
        }
    },
    {
        "id": 53,
        "slug": "53_traffic_flow_optimizer",
        "tier": "ADVANCED",
        "name": "Traffic Flow Optimizer",
        "category": "Public Good & Civic",
        "description": "Simulates urban road networks, forecasts congestion choke points, and models adaptive signal timing.",
        "capabilities": [
            "Road network graph & node intake",
            "Vehicle throughput & speed metrics",
            "Bottleneck & congestion choke point detection",
            "Traffic flow forecasting",
            "Adaptive traffic light cycle optimization",
            "Green corridor simulation for emergency vehicles",
            "Flow efficiency report"
        ],
        "technologies": ["Network Graph Flow", "Congestion Detector", "Signal Timing Optimizer"],
        "default_input": {
            "corridor_name": "Main Street & Metro Boulevard Arterial",
            "num_intersections": 4,
            "peak_hour_volume_vph": 2400,
            "current_green_time_seconds": 45,
            "queue_lengths_vehicles": [35, 48, 52, 28]
        }
    },
    {
        "id": 54,
        "slug": "54_job_matcher",
        "tier": "ADVANCED",
        "name": "Job Matcher",
        "category": "Career & Professional",
        "description": "Semantic resume-to-job matching engine: computes semantic similarity, extracts skill overlap, and ranks candidate fit.",
        "capabilities": [
            "Candidate resume parsing",
            "Job specification requirements parsing",
            "Semantic cosine similarity calculation via vector embeddings",
            "Skill overlap & gap matrix",
            "Fit percentage score (0 - 100%)",
            "Transparent match explanation breakdown",
            "Clear disclaimer: does not make final autonomous hiring decisions"
        ],
        "technologies": ["Semantic Vector Matcher", "TF-IDF Embeddings", "Skill Matrix"],
        "default_input": {
            "candidate_profile": "Full-stack engineer with 4 years experience. Expertise in Python, FastAPI, React, PostgreSQL, Docker, and Redis. Built high-scale microservices and optimized database queries.",
            "job_posting": "Looking for a Senior Backend Engineer to lead cloud infrastructure. Must be proficient in Python, FastAPI, Kubernetes, Docker, and PostgreSQL. Experience with distributed caching (Redis) is a strong plus."
        }
    },
    {
        "id": 55,
        "slug": "55_education_tutor",
        "tier": "ADVANCED",
        "name": "Education Tutor",
        "category": "Education & Learning",
        "description": "Adaptive AI tutoring platform: dynamically adjusts explanations, asks Socratic follow-ups, and diagnoses misconceptions.",
        "capabilities": [
            "Subject selection (STEM, Humanities, Computer Science)",
            "Student grade level & learning style profile",
            "Adaptive conceptual explanations",
            "Socratic questioning method",
            "Step-by-step hint scaffolding without giving away answers",
            "Diagnostic misconception detection",
            "Mastery analytics & learning velocity"
        ],
        "technologies": ["Socratic Dialogue Engine", "Pedagogical Scaffolder", "Misconception Diagnostic"],
        "default_input": {
            "subject": "Physics: Newton's Third Law of Motion",
            "student_grade_level": "High School / College Prep",
            "student_question": "If every action has an equal and opposite reaction, why doesn't everything cancel out and nothing ever moves?",
            "student_current_guess": "I think the heavier object exerts more force so it pushes through."
        }
    },
    {
        "id": 56,
        "slug": "56_healthcare_symptom_checker",
        "tier": "ADVANCED",
        "name": "Healthcare Symptom Checker",
        "category": "Health & Well-being",
        "description": "Research and educational symptom-information platform: categorizes symptoms, notes red flags, and guides urgency.",
        "capabilities": [
            "Symptom intake & structured questioning",
            "Duration & severity classification",
            "Possible informational health categories",
            "Red-flag emergency warning signs check",
            "Triage urgency guidance (Self-care, Primary care, Urgent care, Emergency ER)",
            "Preparation checklist for doctor visits",
            "Strict safety guarantee: NEVER claims to diagnose and urges professional clinical consultation"
        ],
        "technologies": ["Triage Categorizer", "Red Flag Screener", "Medical Disclaimer Engine"],
        "default_input": {
            "reported_symptoms": "Moderate sore throat, dry cough, low-grade fever (99.8 F), mild fatigue",
            "duration_days": 3,
            "has_chest_pain_or_shortness_of_breath": False,
            "patient_age": 28
        }
    },
    {
        "id": 57,
        "slug": "57_accessibility_assistant",
        "tier": "ADVANCED",
        "name": "Accessibility Assistant",
        "category": "Public Good & Civic",
        "description": "Evaluates accessibility: converts complex text to plain language, generates image alt-text, and checks WCAG contrast.",
        "capabilities": [
            "Text simplification (plain-language transformation for cognitive access)",
            "Descriptive alt-text generation for complex visual media",
            "WCAG 2.1 contrast ratio verification",
            "Screen-reader structure analysis (headings, landmarks)",
            "Keyboard navigation audit checklist",
            "Text-to-speech phonetic speech preparation",
            "Strict user privacy and control preservation"
        ],
        "technologies": ["WCAG Auditor", "Plain Language Transformer", "Alt-Text Synthesizer"],
        "default_input": {
            "complex_text": "Notwithstanding the aforementioned stipulations, the party of the second part shall indemnify and hold innocuous the principal against any encumbrances arising from non-compliance.",
            "ui_element_for_alt_text": "A bar chart showing quarterly cloud expenditures decreasing from $12,000 in Q1 to $7,500 in Q4 after optimization."
        }
    },
    {
        "id": 58,
        "slug": "58_financial_literacy_guide",
        "tier": "ADVANCED",
        "name": "Financial Literacy Guide",
        "category": "Public Good & Civic",
        "description": "AI financial education platform: compound interest calculators, debt snowball vs avalanche simulations, and budget frameworks.",
        "capabilities": [
            "Fundamental financial concept tutorials",
            "50/30/20 budgeting framework builder",
            "Compound interest & investment growth calculator",
            "Debt repayment strategies (Snowball vs Avalanche comparison)",
            "Emergency fund planning formula",
            "Interactive financial math simulations",
            "Strictly educational guidance disclaimer (not personalized regulated financial advice)"
        ],
        "technologies": ["Financial Math Engine", "Debt Payoff Simulator", "Educational Guardrails"],
        "default_input": {
            "monthly_income_net": 4500,
            "fixed_expenses": 2300,
            "current_savings": 3000,
            "debts": [
                {"name": "Credit Card A", "balance": 4500, "interest_rate_percent": 21.5, "min_payment": 150},
                {"name": "Student Loan", "balance": 18000, "interest_rate_percent": 4.8, "min_payment": 210}
            ],
            "monthly_extra_for_debt": 400
        }
    }
]

# Helper lookups
PROJECTS_BY_ID: Dict[int, Dict[str, Any]] = {p["id"]: p for p in PROJECT_REGISTRY}
PROJECTS_BY_SLUG: Dict[str, Dict[str, Any]] = {p["slug"]: p for p in PROJECT_REGISTRY}

def get_projects(tier: str = None, category: str = None, search: str = None) -> List[Dict[str, Any]]:
    """Filter projects by tier, category, or search term."""
    results = PROJECT_REGISTRY
    if tier:
        results = [p for p in results if p["tier"].upper() == tier.upper()]
    if category:
        results = [p for p in results if p["category"].lower() == category.lower()]
    if search:
        s = search.lower()
        results = [
            p for p in results
            if s in p["name"].lower() or s in p["description"].lower() or any(s in c.lower() for c in p["capabilities"])
        ]
    return results

def get_project_by_id(project_id: int) -> Dict[str, Any]:
    return PROJECTS_BY_ID.get(project_id)

def get_project_by_slug(slug: str) -> Dict[str, Any]:
    return PROJECTS_BY_SLUG.get(slug)
