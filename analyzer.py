class EgoAnalyzer:
    """
    Analyzes code to calculate an 'ego score' and detect over-engineering.
    """
    def __init__(self, code_snippet: str):
        self.code = code_snippet
        
    def analyze(self) -> dict:
        lines = self.code.strip().split('\n')
        line_count = len(lines)
        
        # Simple heuristic for ego/over-engineering score based on length and keywords
        complexity_keywords = ['lambda', 'class', 'def', 'import', 'async', 'await']
        keyword_count = sum(self.code.count(kw) for kw in complexity_keywords)
        
        ego_score = min(100, (line_count * 2) + (keyword_count * 10))
        
        issues = []
        if ego_score > 70:
            issues.append("High over-engineering detected.")
        elif ego_score > 40:
            issues.append("Moderate complexity.")
        else:
            issues.append("Clean and simple.")
            
        return {
            "line_count": line_count,
            "ego_score": ego_score,
            "issues": issues
        }