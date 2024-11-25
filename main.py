# main.py

import argparse
import sys
from blog_generator import ProblemOfTheDayBlogGenerator

def read_solution_file(file_path: str) -> str:
    """Read solution code from file"""
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading solution file: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Generate LeetCode solution blog posts')
    parser.add_argument('leetcode_url', help='URL of the LeetCode problem')
    parser.add_argument('solution_file', help='Path to the solution code file')
    parser.add_argument('--output-dir', default='content/posts', 
                      help='Output directory for blog posts')
    
    args = parser.parse_args()
    
    try:
        # Read solution code
        solution_code = read_solution_file(args.solution_file)
        
        # Initialize blog generator
        generator = ProblemOfTheDayBlogGenerator()
        
        # Generate and save blog post
        generator.save_blog_post(
            leetcode_url=args.leetcode_url,
            solution_code=solution_code,
            output_dir=args.output_dir
        )
        
    except Exception as e:
        print(f"Error generating blog post: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()