# server made using Bottle framework
from bottle import Bottle, template, request
import re

app = Bottle()


@app.route('/')
def index():
    html = html_template + html_completion
    return template(html)


@app.route('/', method="POST")
def form_handler():

    username = request.forms.get('username')
    print("Username:", username)
    html = html_template

    # regex based on https://github.com/regexhq/regex-username
    regex = re.search(r'^([A-Za-z\d]+-)*[A-Za-z\d]+$', username)
    if regex is not None:
        html += f"<p>Repos of user <b>{username}</b>:</p>"
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
