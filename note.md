# Flask

```py
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

```
### Add syntax highlight

Install module

```
pip install pygments
```

Generate css file

```
pygmentize -S one-dark -f html -a .codehilite > static/styles/one-dark-pro.css
```

In index.html

```html

<link
	rel="stylesheet"
	type="text/css"
	href="{{url_for('static', filename='styles/one-dark.css')}}"
/>
...
<body>
	{{ content |safe}}
</body>
```

