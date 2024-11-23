from mirascope.core import groq
from pydantic import BaseModel
from mirascope.core.groq import GroqCallParams

params = GroqCallParams(temperature=0.2,max_tokens=6144,top_p=0.5)
model = "llama-3.2-90b-vision-preview"

class CodeExplanation(BaseModel):
    """Structured explanation of code solution"""
    intuition: list[str]
    implementation: list[str]
    
class CodeComplexity(BaseModel):
    """Complexity analysis of code solution"""
    time_complexity: str
    space_complexity: str
    algorithm: str

class ComplexityAnalysis(BaseModel):
    """Complexity analysis of code solution"""
    time_complexity_explained: list[str]
    space_complexity_explained: list[str]

@groq.call(model=model, response_model=CodeExplanation, json_mode=True,call_params=params)
def generate_code_explanation(problem: str, solution: str) -> str:
    """Generate structured explanation using Groq LLM"""
    return f"""<|system|>You are an excellent logic and code explainer.You will explain the intuition in technical and easy to understand intuitive way. You will explain implementation using the solution snippet given.
    In implementation part you will use backticks to highlight the code snippets.
    Given this coding problem and solution, provide a detailed explanation:

Problem: {problem}

Solution Code:
{solution}

Provide an intuition about the approach and implementation details.
The intuition and implementation should be lists of clear bullet points.Each point should be short but may use multiple points. Give in JSON format<|system|>"""


@groq.call(model=model, response_model=CodeComplexity, json_mode=True)
def generate_code_complexity(solution: str) -> str:
    """Generate complexity analysis using Groq LLM"""
    return f"""<|system|>Ypu are an excellent code time and space complexity reviewer.Given the solution code, provide the time and space complexity analysis in one word. Example: O(nm), O(n^2) etc. Dont use * to indicate multiplication. Use brackets like this O(n) mandatorily. Give one word for algorithm which causes this complexity.
Solution Code:{solution}
The time and space complexity should be strings describing the complexity.
Give in JSON format<|system|>"""

@groq.call(model=model, response_model=ComplexityAnalysis, json_mode=True)
def generate_complexity_analysis(solution: str,complexity_values:CodeComplexity) -> str:
    """Generate complexity analysis using Groq LLM"""
    return f"""<|system|>Given the solution code and complexity calculations, provide a detailed explanation of the time and space complexity. Use code snippets to explain the complexity calculations. Use backticks to highlight the code snippets.
Solution Code:{solution}
Complexity dict: {complexity_values}
The time_complexity_explained and space_complexity_explained should be lists of clear bullet points. Each point should be short but may use multiple points.
The output needed is JSON format<|system|>"""


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
    def generate_complexity(self,solution_code:str) -> CodeComplexity:
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
                space_complexity="Error generating space complexity"
            )
            
    def generate_complexity_analysis(self,solution_code:str,complexity_values:CodeComplexity) -> ComplexityAnalysis:
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
                time_complexity_explained="Error generating time complexity explanation",
                space_complexity_explained="Error generating space complexity explanation"
            )