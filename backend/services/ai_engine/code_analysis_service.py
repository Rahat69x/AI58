"""Code Analysis Service: AST parsing, static metrics, vulnerability detection, and refactoring tips."""

import ast
import re
from typing import Dict, Any, List

class CodeAnalysisService:
    """Performs static code analysis, complexity evaluation, and security linting."""

    def analyze_python_ast(self, source_code: str) -> Dict[str, Any]:
        """Parses Python code into an AST and extracts metrics."""
        try:
            tree = ast.parse(source_code)
        except SyntaxError as e:
            return {
                "valid_syntax": False,
                "error": str(e),
                "line": e.lineno,
                "offset": e.offset,
            }

        num_functions = sum(1 for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)))
        num_classes = sum(1 for node in ast.walk(tree) if isinstance(node, ast.ClassDef))
        num_imports = sum(1 for node in ast.walk(tree) if isinstance(node, (ast.Import, ast.ImportFrom)))

        # Simple cyclomatic complexity approximation
        branch_nodes = sum(1 for node in ast.walk(tree) if isinstance(node, (ast.If, ast.For, ast.While, ast.ExceptHandler, ast.With)))
        estimated_complexity = 1 + branch_nodes

        return {
            "valid_syntax": True,
            "num_functions": num_functions,
            "num_classes": num_classes,
            "num_imports": num_imports,
            "estimated_complexity": estimated_complexity,
            "lines_of_code": len(source_code.splitlines()),
        }

    def scan_security_issues(self, source_code: str, language: str = "python") -> List[Dict[str, Any]]:
        """Scans code for common security smells, hardcoded credentials, and dangerous calls."""
        issues = []
        lines = source_code.splitlines()

        patterns = [
            (r"(?:eval|exec)\s*\(", "CRITICAL", "Dynamic code execution via eval/exec"),
            (r"(?:password|secret|api_key|token)\s*=\s*['\"][A-Za-z0-9_\-\.]{8,}['\"]", "HIGH", "Potential hardcoded credential or token"),
            (r"SELECT\s+.*\s+FROM\s+.*\+.*", "HIGH", "Possible SQL string concatenation (SQL injection vulnerability)"),
            (r"shell\s*=\s*True", "HIGH", "Subprocess execution with shell=True enabled"),
            (r"pickle\s*\.\s*loads?\s*\(", "MEDIUM", "Unsafe deserialization using pickle"),
            (r"except\s*:\s*pass", "LOW", "Bare except clause masking potential runtime errors"),
            (r"0\.0\.0\.0", "LOW", "Binding service to all network interfaces"),
        ]

        for line_no, line in enumerate(lines, start=1):
            for pat, severity, msg in patterns:
                if re.search(pat, line, re.IGNORECASE):
                    issues.append({
                        "line": line_no,
                        "severity": severity,
                        "rule": msg,
                        "snippet": line.strip()[:100],
                        "recommendation": "Refactor to use parameterized queries, secure secret stores, or safe alternative libraries.",
                    })

        return issues

    def calculate_maintainability_index(self, source_code: str) -> Dict[str, Any]:
        """Calculates a heuristic maintainability score (0 - 100)."""
        loc = len([line for line in source_code.splitlines() if line.strip() and not line.strip().startswith("#")])
        if loc == 0:
            return {"score": 100, "rating": "A"}

        issues = self.scan_security_issues(source_code)
        penalty = len(issues) * 12
        if loc > 250:
            penalty += 15
        elif loc > 100:
            penalty += 5

        score = max(20, min(100, 100 - penalty))
        rating = "A" if score >= 85 else ("B" if score >= 70 else ("C" if score >= 50 else "D"))

        return {
            "score": score,
            "rating": rating,
            "loc": loc,
            "issues_count": len(issues),
        }

code_analysis_service = CodeAnalysisService()
