"""
LeetCode API Client for scraping problem details and solutions.

This module provides functionality to fetch problem details from LeetCode's GraphQL API,
including problem descriptions, hints, difficulty, tags, and official solutions.
"""

import json
import requests
from requests.exceptions import RequestException
from constants import QUESTION_QUERY, SOLUTION_QUERY,GRAPHQL_BASE_URL

# API Constants
BASE_URL = GRAPHQL_BASE_URL

class LeetCodeScraper:
    """A class to scrape problem details from LeetCode's GraphQL API."""

    def __init__(self, title_slug: str) -> None:
        """
        Initialize the LeetCode scraper.

        Args:
            title_slug (str): The URL slug of the LeetCode problem
            e.g. "two-sum" for the problem "Two Sum"
        """
        self.title_slug = title_slug
    
    def get_question_details(self) -> dict[str, any]:
        """
        Scrape problem details from LeetCode.

        Returns:
            dict: A dictionary containing the problem details
            params:
                Title (str): The title of the problem
                Content (str): The problem description
                Difficulty (str): The difficulty level of the problem
                Hints (list[str]): A list of hints for solving the problem
                SimilarQuestions (list[str]): A list of similar questions
                CompanyTags (list[str]): A list of company tags associated with the problem
                TopicTags (list[str]): A list of topic tags associated with the problem
                IsPaidOnly (bool): Whether the problem is only available to premium users

        Raises:
            RequestException: If the API request fails
            ValueError: If the response cannot be parsed
        """
        try:
            # Fetch problem details
            data = {
                "query": QUESTION_QUERY,
                "variables": {"titleSlug": self.title_slug},
            }
            response = requests.post(BASE_URL, json=data)
            response.raise_for_status()
            
            response_data = response.json()
            question_data = response_data["data"]["question"]

            # Sanitize and structure the response data
            sanitized_data = {
                "QuestionFrontendId": question_data["questionFrontendId"],
                "Title": question_data["title"],
                "Content": question_data["content"],
                "Difficulty": question_data["difficulty"],
                "Hints": question_data["hints"],
                "SimilarQuestions": json.loads(question_data["similarQuestions"]),
                "CompanyTags": [tag["name"] for tag in question_data["companyTags"]] if question_data["companyTags"] else [],
                "TopicTags": [tag["name"] for tag in question_data["topicTags"]],
                "IsPaidOnly": question_data["isPaidOnly"]
            }

            return sanitized_data

        except requests.exceptions.RequestException as e:
            raise RequestException(f"Failed to retrieve problem details: {str(e)}")
        except (KeyError, json.JSONDecodeError) as e:
            raise ValueError(f"Failed to parse response: {str(e)}")
        
    def get_solution_details(self) -> dict[str, any]:
        """
        Scrape official solution details from LeetCode.

        Returns:
            dict: A dictionary containing the official solution details
            params:
                Title (str): The title of the official solution
                Content (str): The content of the official solution
                ContentTypeId (int): The content type ID of the official solution
                PaidOnly (bool): Whether the official solution is only available to premium users
                HasVideoSolution (bool): Whether the official solution has a video explanation

        Raises:
            RequestException: If the API request fails
            ValueError: If the response cannot be parsed
        """
        try:
            # Fetch official solution details
            data = {
                "query": SOLUTION_QUERY,
                "variables": {"titleSlug": self.title_slug},
            }
            response = requests.post(BASE_URL, json=data)
            response.raise_for_status()
            
            response_data = response.json()
            solution_data = response_data["data"]["question"]["solution"]

            # Sanitize and structure the response data
            sanitized_data = {
                "Title": solution_data["title"],
                "Content": solution_data["content"],
                "ContentTypeId": solution_data["contentTypeId"],
                "PaidOnly": solution_data["paidOnly"],
                "HasVideoSolution": solution_data["hasVideoSolution"]
            }

            return sanitized_data

        except requests.exceptions.RequestException as e:
            raise RequestException(f"Failed to retrieve solution details: {str(e)}")
        except (KeyError, json.JSONDecodeError) as e:
            raise ValueError(f"Failed to parse response: {str(e)}")
        
        
if __name__ == "__main__":
    # Example usage
    title_slug = "two-sum"
    leetcode_scraper = LeetCodeScraper(title_slug)
    question_details = leetcode_scraper.get_question_details()

    print("Question Details:")
    print(json.dumps(question_details, indent=4))