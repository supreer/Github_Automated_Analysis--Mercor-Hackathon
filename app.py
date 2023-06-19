# app.py
import streamlit as st
import re
import requests
import time
#from main import main
def extract_username(github_url):
    # Extract the username from the GitHub URL using regular expressions
    pattern = r"github\.com/([^/]+)"
    match = re.search(pattern, github_url)

    if match:
        return match.group(1)

    # If the URL doesn't match the expected format, return None or raise an exception
    return None
def fetch_user_repositories(github_url):
    # Extract the username from the GitHub URL
    username = extract_username(github_url)
    # Fetch the repositories using GitHub API
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    repositories = response.json()

    # Extract the relevant information from the repositories
    extracted_repositories = []
    for repo in repositories:
        name = repo['name']
        description = repo['description']
        url = repo['html_url']
        extracted_repositories.append({'name': name, 'description': description, 'url': url})

    return extracted_repositories
def sample(complexity_scores):
    max_name = max(complexity_scores, key=complexity_scores.get)
    return max_name
    
def main():
    st.title("URL Processor")

    # Text input for URL
    url = st.text_input("Enter user name of the github profile")
    repos = fetch_user_repositories(url)
    complexity_scores = {}
    for i in repos.items():
        complexity_scores[i['name']]=main(i['url'])
    st.text('thinking')
    max_name = sample(complexity_scores)
    st.text(max_name)
    


    # Check if URL is entered
    #extracted_repositories = fetch_user_repositories(url)
    
    

        
    
    
if __name__ == "__main__":
    main()