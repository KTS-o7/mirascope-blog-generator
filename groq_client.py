from mirascope.core import groq, Messages
from pydantic import BaseModel,Field
from mirascope.core.groq import GroqCallParams

params = GroqCallParams(temperature=0.2, max_tokens=6144, top_p=0.5)
model = "llama-3.3-70b-versatile"

class CodeExplanation(BaseModel):
    """Structured explanation of code solution"""
    intuition: list[str] = Field(description="Intuition building for code solution")
    implementation: list[str] = Field(description="Implementation details of code solution")
    
class CodeComplexity(BaseModel):
    """Complexity analysis of code solution"""
    time_complexity: str = Field(description="Time complexity of the code solution")
    space_complexity: str = Field(description="Space complexity of the code solution")
    algorithm: str = Field(description="Algorithm used in the code solution")

class ComplexityAnalysis(BaseModel):
    """Complexity analysis of code solution"""
    time_complexity_explained: list[str] = Field(description="Time complexity explained")
    space_complexity_explained: list[str] = Field(description="Space complexity explained")
    
class IntuitionBuilder(BaseModel):
    """Intuition building for code solution"""
    initial_thoughts: str = Field(description="Initial thoughts on how to approach the problem")
    intuitive_analysis: str = Field(description="Analysis of how to intuitively solve the problem")
    
@groq.call(model=model, response_model=CodeExplanation, json_mode=True, call_params=params)
def generate_code_explanation(problem: str, solution: str) -> str:
    return [
        Messages.System("""
You are a code explanation expert. Follow these rules strictly:
- Return JSON with exactly two fields: 'intuition' and 'implementation' as string arrays
- Each array must contain 6-9 clear, concise points
- Use backticks to reference specific code parts; e.g., `function`, `variable_1`
- Keep explanations technical but accessible
- Focus on core algorithms and data structures used
- No conversational language or filler text
"""),
        Messages.User(f"""
Input:
Problem: {problem}
Solution: {solution}

Required JSON Format:
{{
    "intuition": [
        "Point 1 about the logical way to approach the problem",
        "Point 2 about why to think in a certain direction",
        "Point 3 about why other directions wont work",
        "Point 4 about the key insight needed"
        "Point 5 about why this solution works",
        "Point 6 about algorithmic choices",
        "..."
    ],
    "implementation": [
        "Detail 1 with `code snippet` of code block 1",
        "Detail 2 with `code snippet` of code block 2",
        "...",
        "Details with tradeoffs"
    ]
}}
""")
    ]

@groq.call(model=model, response_model=CodeComplexity, json_mode=True)
def generate_code_complexity(solution: str) -> str:
    return [
        Messages.System("""
You are a complexity analysis expert. Follow these rules strictly:
- Return JSON with exactly three fields: 'time_complexity', 'space_complexity', 'algorithm'
- Use strict Big O notation format: O(n), O(1), O(n log n), etc.
- No mathematical operators, use 'log' instead of '*'
- Identify the most specific algorithm name possible
- Always justify your complexity assessment
"""),
        Messages.User(f"""
Analyze this code:
{solution}

Required JSON Format:
{{
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "algorithm": "Two-pointer traversal"
}}
""")
    ]

@groq.call(model=model, response_model=ComplexityAnalysis, json_mode=True)
def generate_complexity_analysis(solution: str, complexity_values: CodeComplexity) -> str:
    return [
        Messages.System("""
You are a complexity explanation expert. Follow these rules strictly:
- Return JSON with exactly two fields: 'time_complexity_explained' and 'space_complexity_explained'
- Each field must be an array of 2-3 technical explanation points
- Reference specific code parts using backticks
- Include mathematical reasoning for each complexity
- Explain worst, average, and best cases where applicable
"""),
        Messages.User(f"""
Code: {solution}

Analysis:
Time Complexity: {complexity_values.time_complexity}
Space Complexity: {complexity_values.space_complexity}
Algorithm: {complexity_values.algorithm}

Required JSON Format:
{{
    "time_complexity_explained": [
        "Step-by-step analysis of time complexity",
        "Explanation of dominant operations",
        "Justification of Big O classification"
    ],
    "space_complexity_explained": [
        "Analysis of memory usage",
        "Explanation of data structure impact",
        "Justification of space complexity"
    ]
}}
""")
    ]

@groq.call(model=model, response_model=IntuitionBuilder, json_mode=True)
def generate_intuition(problem: str, solution: str, ) -> str:
    return [
        Messages.System("""You are an intuition building expert. Follow these rules strictly:
- Return JSON with exactly two fields: 'initial_thoughts' and 'intuitive_analysis' as strings
- Each field must contain 4-6 clear, concise points
- Use non-technical language and analogies
- Focus on problem-solving strategies
- No code-specific explanations
- Focus on building problem-solving intuition
"""),
        Messages.User(f"""Here is the problem statement:
```{problem}```
Here is the solution:
```{solution}```

Required JSON Format:
{{
    "initial_thoughts": "Initial thoughts on how to approach the problem",
    "intuitive_analysis": "Analysis of how to intuitively solve the problem"
}}
""")
    ]


class GroqLLMClient:
    def generate_explanation(self, problem_details: dict, solution_code: str) -> CodeExplanation:
        """Generate explanation for given problem and solution"""
        try:
            response = generate_code_explanation(
                problem=problem_details['Content'],
                solution=solution_code
            )
            return response
        except Exception as e:
            print(f"Error generating explanation: {e}")
            return CodeExplanation(
                intuition=["Error generating intuition"],
                implementation=["Error generating implementation details"]
            )

    def generate_complexity(self, solution_code: str) -> CodeComplexity:
        """Generate complexity analysis for given solution"""
        try:
            response = generate_code_complexity(
                solution=solution_code
            )
            return response
        except Exception as e:
            print(f"Error generating complexity analysis: {e}")
            return CodeComplexity(
                time_complexity="Error generating time complexity",
                space_complexity="Error generating space complexity",
                algorithm="Error determining algorithm"
            )
            
    def generate_complexity_analysis(self, solution_code: str, complexity_values: CodeComplexity) -> ComplexityAnalysis:
        """Generate complexity analysis for given solution"""
        try:
            response = generate_complexity_analysis(
                solution=solution_code,
                complexity_values=complexity_values
            )
            return response
        except Exception as e:
            print(f"Error generating complexity analysis: {e}")
            return ComplexityAnalysis(
                time_complexity_explained=["Error generating time complexity explanation"],
                space_complexity_explained=["Error generating space complexity explanation"]
            )
            
    def generate_general_intuition(self, problem_details: dict, solution_code: str) -> IntuitionBuilder:
        """Generate general intuition for given problem and solution"""
        try:
            response = generate_intuition(
                problem=problem_details['Content'],
                solution=solution_code
            )
            return response
        except Exception as e:
            print(f"Error generating general intuition: {e}")
            return IntuitionBuilder(
                initial_thoughts="Error generating initial thoughts",
                intuitive_analysis="Error generating intuitive analysis"
            )
            