# server made using Bottle framework
from bottle import Bottle, template, request
import re
import requests

app = Bottle()


def get_github_repos(username):
    # regex based on https://github.com/regexhq/regex-username
    regex = re.search(r'^([A-Za-z\d]+-)*[A-Za-z\d]+$', username)
    repos = []

    if regex is not None:
        page = 1
        while page <= 10:  # increase the number to load more than a 1000 repos
            url = f"https://api.github.com/users/{username}/repos?page={page}&per_page=100"
            req = requests.get(url)
            if req.status_code == 200 and len(req.json()) != 0:
                repos.extend(req.json())
                page += 1
            else:
                break
        if len(repos) == 0:
            print("User does not exist or has no repos")
    else:
        print("Incorrect username")

    return repos


@app.route('/')
def index():
    html = html_template + html_completion
    return template(html)


@app.route('/', method="POST")
def form_handler():

    username = request.forms.get('username')
    print("Sending response for username:", username)
    html = html_template

    repos = get_github_repos(username)
    if len(repos) > 0:
        star_counter = 0
        html += f"<p>Repositories of user <b><a href=\"https://github.com/{username}\">{username}</a></b>:</p>\n"
        html += "<table>\n"
        html += "<tr><th>No.</th><th>Repo name</th><th>Stars</th></tr>\n"
        for i, r in enumerate(repos):
            stars = r['stargazers_count']
            star_counter += stars
            html += f"<tr><td>{i+1}</td><td>{r['name']}</td><td>{stars}</td></tr>\n"
        html += "</table>\n"
        if star_counter == 1:
            star_str = "star"
        else:
            star_str = "stars"
        html += f"<p><b>{username}</b> has {star_counter} {star_str}!</p>"
    else:
        html += "<p>Could not load repos for this username!</p>"
    html += html_completion

    return template(html)


hostName = "localhost"
serverPort = 8080
html_file = open("template.html", "r")
html_template = html_file.read()
html_completion = "\n</body>\n</html>"

app.run(host=hostName, port=serverPort)
