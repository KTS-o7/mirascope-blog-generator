# LeetCode Blog Post Generator

## Motivation

Solving LeetCode problems is a great way to improve your coding skills and prepare for technical interviews. However, documenting your solutions and sharing them as blog posts can be time-consuming. This project aims to automate the process of generating detailed blog posts for LeetCode problems, allowing you to focus more on solving problems rather than writing about them.

## Project Description

This project leverages the LeetCode GraphQL API to fetch problem details and solutions. It uses Mirascope and Groq for LLM (Large Language Model) usage to generate explanations and complexity analyses for the solutions. The generated content is then formatted into a markdown file suitable for publishing as a blog post.

### Key Features

- **Automated Blog Post Generation**: Automatically generate detailed blog posts for LeetCode problems, including problem statements, solutions, explanations, and complexity analyses.
- **LeetCode GraphQL API Integration**: Fetch problem details and solutions directly from LeetCode using their GraphQL API.
- **Mirascope and Groq Integration**: Use advanced LLMs to generate intuitive explanations and complexity analyses for the solutions.
- **Markdown Formatting**: Generate blog posts in markdown format, ready to be published on platforms like Hugo.

## Usage

### Prerequisites

- Python 3.12+
- Install required packages:
  - mirascope
  - groq
  - requests

1. Clone the repository:

```bash
git clone https://github.com/yourusername/mirscope-blog-agent.git
cd mirscope-blog-agent
```

2. Generating a Blog Post:

```bash
python main.py <leetcode_url> <solution_file> --output-dir <output_directory>
```

- `<leetcode_url>`: URL of the LeetCode problem you want to generate a blog post for.
- `<solution_file>`: Path to the file containing your solution code.
- `<output_directory>`: Directory where the generated blog post will be saved.

Example:

```bash
python main.py "https://leetcode.com/problems/rotating-the-box/" "./solution.cpp" --output-dir content/posts
```

This will generate a markdown file in the `content/posts` directory with the blog post content.

> This will need you to have `GROQ_API_KEY` in your environment variables.

### What's Next?

I am currently working on adding a custom template and latex support for the generated blog posts. Stay tuned for more updates!

Footnotes:
This project automates the process of generating detailed blog posts for LeetCode problems, allowing you to focus on solving problems rather than writing about them.
By leveraging the LeetCode GraphQL API and advanced LLMs, it provides comprehensive explanations and complexity analyses for your solutions.

Feel free to contribute to this project by submitting issues or pull requests on GitHub. Happy coding! 🚀
