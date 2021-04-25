# GitHub Checker
* HTTP server app for checking GitHub repos of a user.
* Written in Python using Bottle framework.
* Uses the POST method from HTTP.

### Features
* Taking any username and validating it.
* Listing repo names and star counts for any GitHub user.
* Displaying the total number of stars of a user.

### Requirements
* bottle (https://bottlepy.org/)
* re 
* requests

### Running
1. Start the server:
```
python server.py
```
2. Open a web browser:
> http://localhost:8080/
3. Type a GitHub username into the form and click the **Load repos** button
