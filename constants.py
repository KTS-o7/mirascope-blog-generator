# GraphQL Queries
QUESTION_QUERY = """
query questionHints($titleSlug: String!) {
    question(titleSlug: $titleSlug) {
        questionFrontendId
        title
        hints
        difficulty
        companyTags {
            name
            slug
            imgUrl
        }
        topicTags {
            name
        }
        similarQuestions
        codeSnippets {
            lang
            langSlug
            code
        }
        content
        isPaidOnly
    }
}
"""

SOLUTION_QUERY = """
query officialSolution($titleSlug: String!) {
    question(titleSlug: $titleSlug) {
        solution {
            id
            title
            content
            contentTypeId
            paidOnly
            hasVideoSolution
            paidOnlyVideo
            canSeeDetail
            rating {
                count
                average
                userRating {
                    score
                }
            }
            topic {
                id
                commentCount
                topLevelCommentCount
                viewCount
                subscribed
                solutionTags {
                    name
                    slug
                }
                post {
                    id
                    status
                    creationDate
                    author {
                        username
                        isActive
                        profile {
                            userAvatar
                            reputation
                        }
                    }
                }
            }
        }
    }
}
"""

GRAPHQL_BASE_URL = "https://leetcode.com/graphql"