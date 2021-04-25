# server made using Bottle framework
from bottle import Bottle, template, request
import re
import requests

app = Bottle()


def get_github_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    status_code = requests.head(url).status_code
    if status_code == 200:
        return requests.get(url).json()
    else:
        return []


@app.route('/')
def index():
    html = html_template + html_completion
    return template(html)


@app.route('/', method="POST")
def form_handler():

    username = request.forms.get('username')
    print("Sending response for username:", username)
    html = html_template

    # regex based on https://github.com/regexhq/regex-username
    regex = re.search(r'^([A-Za-z\d]+-)*[A-Za-z\d]+$', username)
    repos = get_github_repos(username)
    if regex is not None and len(repos) > 0:
        star_counter = 0
        html += f"<p>Repos of user <b><a href=\"https://github.com/{username}\">{username}</a></b>:</p>"
        html += "<table>"
        html += "<tr><th>Repo name</th><th>Stars</th></tr>"
        for r in repos:
            stars = r['stargazers_count']
            star_counter += stars
            html += f"<tr><td>{r['name']}</td><td>{stars}</td></tr>"
        html += "</table>"
        if star_counter == 1:
            star_str = "star"
        else:
            star_str = "stars"
        html += f"<p><b>{username}</b> has {star_counter} {star_str}!</p>"
    else:
        html += "<p>Wrong username!</p>"
    html += html_completion

    return template(html)


hostName = "localhost"
serverPort = 8080
html_file = open("template.html", "r")
html_template = html_file.read()
html_completion = "\n</body>\n</html>"

app.run(host=hostName, port=serverPort)
