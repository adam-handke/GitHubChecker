# GitHub Checker
* HTTP server app for checking GitHub repos of a user.
* Written in Python using Bottle framework.
* Uses the GitHub API without authentication (https://api.github.com/).

### Features
* Taking any username using a form and the POST method.
* Validating the username.
* Listing repository names and star counts for any (valid) GitHub user.
* Displaying the total number of stars of the user.
* Able to load up to 1000 repos per user - max 10 API pages with 100 repos each. Limited due to GitHub API rate limits (https://api.github.com/rate_limit).

## Requirements
* bottle (https://bottlepy.org/)
* re 
* requests

## Running
1. Start the server:
```
python server.py
```
2. Open a web browser:
> http://localhost:8080/
3. Type a GitHub username into the form and click the **Load repos** button

## Future enhancement ideas
* Using GitHub API with authentication for a higher rate limit.
* Improving appearance with better CSS styles.
* Displaying more info about the user and his repositories.
* Providing the username by GET method with URL parameters, e.g.:
> http://localhost:8080?username=adam-handke
