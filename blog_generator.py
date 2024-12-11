# blog_generator.py

import os
from datetime import datetime
import re
from leetcode_client import LeetCodeScraper
from groq_client import GroqLLMClient,CodeComplexity,CodeExplanation,ComplexityAnalysis,IntuitionBuilder

class ProblemOfTheDayBlogGenerator:
    def __init__(self):
        self.groq_client = GroqLLMClient()  
    
    def extract_title_slug(self, leetcode_url: str) -> str:
        """Extract title slug from LeetCode URL"""
        match = re.search(r"problems/([^/]+)/", leetcode_url)
        if not match:
            raise ValueError("Invalid LeetCode URL format")
        return match.group(1)
    
    def generate_front_matter(self, problem_details: dict) -> str:
        """Generate Hugo front matter"""
        current_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+05:30")
        tags = [tag.lower() for tag in problem_details["TopicTags"]]
        
        return f"""+++
title = 'Problem {problem_details["QuestionFrontendId"]} {problem_details["Title"]}'
date = {current_date}
draft = false
series = 'leetcode'
tags = {tags}
toc = false
math = false
+++\n"""

    def generate_blog_post(self, leetcode_url: str, solution_code: str) -> str:
        """Generate complete blog post"""
        # Extract title slug and get problem details
        title_slug = self.extract_title_slug(leetcode_url)
        leetcode_client = LeetCodeScraper(title_slug)
        problem_details = leetcode_client.get_question_details()
        
        # Get explanations from Groq
        explanations = self.groq_client.generate_explanation(problem_details, solution_code)
        complexity = self.groq_client.generate_complexity(solution_code)
        complexity_explaination = self.groq_client.generate_complexity_analysis(solution_code,complexity)
        general_intuition = self.groq_client.generate_general_intuition(problem_details, solution_code)
        
        exceptions = [CodeExplanation(intuition=["Error generating intuition"], implementation=["Error generating implementation details"]),
                      CodeComplexity(time_complexity="Error generating time complexity", space_complexity="Error generating space complexity", algorithm="Error determining algorithm"),
                      ComplexityAnalysis(time_complexity_explained=["Error generating time complexity explanation"], space_complexity_explained=["Error generating space complexity explanation"]),
                      IntuitionBuilder(initial_thoughts="Error generating initial thoughts", intuitive_analysis="Error generating intuitive analysis")]
        
        if explanations in exceptions or complexity in exceptions or complexity_explaination in exceptions or general_intuition in exceptions:
            raise Exception("Error generating explanations")
        
        
        # Build blog content
        blog_content = [
            self.generate_front_matter(problem_details,),
            "# Problem Statement\n",
            f"**Link** - [Problem {problem_details['QuestionFrontendId']}]({leetcode_url})\n",
            "## Question\n",
            f"{problem_details['Content']}\n",
            "## Solution\n",
            "```cpp",
            solution_code,
            "```\n",
            "## Complexity Analysis\n",
            "```markdown",
            "| Algorithm | Time Complexity | Space Complexity |",
            "| --------- | --------------- | ---------------- |",
            f"| {complexity.algorithm}  | {complexity.time_complexity}           | {complexity.space_complexity}             |",
            "```\n",
            "## Explanation\n",
            "#### Intial Thoughts\n",
            "\n".join([f"{general_intuition.initial_thoughts}"]),
            "\n",
            "#### Intuitive Analysis\n",
            "\n".join([f"{general_intuition.intuitive_analysis}"]),
            "\n",
            "### 1. Intuition\n",
            "\n".join([f"- {point}" for point in explanations.intuition]),
            "\n",
            "### 2. Implementation\n",
            "\n".join([f"- {point}" for point in explanations.implementation]),
            "\n",
            "<hr>\n",
            "## Complexity Analysis\n",
            f"### Time Complexity: \n{"\n".join([f"- {point} " for point in complexity_explaination.time_complexity_explained])}\n",
            f"### Space Complexity: \n{"\n".join([f"- {point} " for point in complexity_explaination.space_complexity_explained])}\n",
        ]
        
        blog_content.extend([
            "<hr>\n",
            "### Footnote\n",
            f"> This question is rated as **{problem_details['Difficulty']}** difficulty.\n",
        ])
        if problem_details['Hints']:
            blog_content.extend([
            "#### Hints\n",
            "\n".join([f"> {point}\n" for point in problem_details['Hints']]),
            ])
        if problem_details['SimilarQuestions']:
            similar_questions_list =[]
            leetcode_problem_base_url = "https://leetcode.com/problems/"
            for item in problem_details["SimilarQuestions"]:
                item_dict = {}
                item_dict["title"] = item["title"]
                item_dict["slug"] = item["titleSlug"]
                item_dict["difficulty"] = item["difficulty"]
                item_dict["url"] = f"{leetcode_problem_base_url}{item_dict['slug']}"
                similar_questions_list.append(item_dict)
            blog_content.extend([
            "<hr>\n",
            "### Similar Questions:\n",
            "| Title | URL | Difficulty |",
            "| ----- | --- | --- |",
            "".join([f"| {point['title']} | {point['url']} |{point["difficulty"]}|\n" for point in similar_questions_list]),
            ])
            
        if problem_details['CompanyTags']:
            blog_content.extend([
            "<hr>\n",
            f"### Company Tags: \n",
            "\n".join([f"- {point} " for point in problem_details['CompanyTags']]),
            ])
        
        return "\n".join(blog_content)
    
    def save_blog_post(self, leetcode_url: str, solution_code: str, output_dir: str) -> None:
        """Generate and save blog post to file"""
        try:
            blog_content = self.generate_blog_post(leetcode_url, solution_code)
            title_slug = self.extract_title_slug(leetcode_url)
            problem_details = LeetCodeScraper(title_slug).get_question_details()
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, f"Problem {problem_details["QuestionFrontendId"]} {title_slug}.md")
            
            with open(output_path, 'w') as f:
                f.write(blog_content)
                
            print(f"Blog post generated successfully: {output_path}")
            
        except Exception as e:
            print(f"Error generating blog post: {e}")