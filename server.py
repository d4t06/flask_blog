from flask import Flask, render_template
import markdown
# import re

app = Flask(__name__)

@app.route("/")
def hello_world():
    f = open('./note.md', 'r')

    text = f.read()
    # cleaned_text = re.sub(r'\s+', '', text)
    content = markdown.markdown(text, extensions=['fenced_code', 'attr_list', 'codehilite'])

    f.close()
    return render_template('index.html', content=content)

app.run(host = '0.0.0.0', port=5000)