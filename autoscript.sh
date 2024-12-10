#!/bin/bash

# Define colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check if GROQ_API_KEY is set in environment
if [ -z "$GROQ_API_KEY" ]; then
    echo -e "${RED}Error: GROQ_API_KEY environment variable is not set${NC}"
    exit 1
fi


# File containing the list of questions
QUESTION_FILE="questionlist.txt"
PROCESSED_FILE="processed_questions.txt"

# Create processed questions file if it doesn't exist
touch "$PROCESSED_FILE"

# Read each line from the question file, removing any carriage returns
while IFS= read -r question || [ -n "$question" ]; do
    # Remove carriage returns and trim whitespace
    question=$(echo "$question" | tr -d '\r' | xargs)
    
    # Skip empty lines
    [ -z "$question" ] && continue
    
    # Check if the question has already been processed
    if ! grep -Fxq "$question" "$PROCESSED_FILE"; then
        echo -e "${BLUE}Processing question: ${NC}$question"
        
        echo -e "${GREEN}Running script${NC}"
        python main.py "$question" "./ans.txt"
        
        
        # If Python script executed successfully, mark question as processed
        if [ $? -eq 0 ]; then
            echo "$question" >> "$PROCESSED_FILE"
            echo -e "${GREEN}Question processed successfully${NC}"
            # Exit after processing one question
            exit 0
        else
            echo -e "${RED}Error processing question${NC}"
            exit 1
        fi
    else
        echo -e "${YELLOW}Question already processed: ${NC}$question"
    fi
done < "$QUESTION_FILE"

echo -e "${BLUE}No new questions to process${NC}"