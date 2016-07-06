# Step by step

This is a guide explaining the process to create this template.

<<<<<<< HEAD
<<<<<<< HEAD
### Share repo between GitHub and Openshift (optional)

http://stackoverflow.com/a/12669112/3281097

### Create a Python application

https://developers.openshift.com/languages/python/getting-started.html

### Flask says "Hello World!"
=======
- Create a Python application, as explained in [OpenShift's Getting Started guide](https://developers.openshift.com/languages/python/getting-started.html) (Step 1)
=======
**1)** Create a Python application, as explained in [OpenShift's Getting Started guide](https://developers.openshift.com/languages/python/getting-started.html) (Step 1)
>>>>>>> 98a517d... Add wsgi to README

```bash
$ rhc app create <project> python-3.3
```

**2)** If you are using a GitHub remote you may want to push to GitHub and OpenShift with different commands. [This answer](http://stackoverflow.com/a/12669112/3281097) in [this StackOverflow question](http://stackoverflow.com/q/12657168/3281097)could be helpful.

```bash
$ git push
$ git push openshift HEAD
``` 

**3)** Add Flask dependency in `<project>/requirements.txt`

```
Flask==0.11
```


**4)** Personalize `<project>/setup.py` by just replacing the `setup()` arguments to fit your project.

<<<<<<< HEAD
<<<<<<< HEAD
- wsgi
>>>>>>> 7adfcda... New steps in step by step guide
=======
**5)** We create a Flask app in another file (`<project>/<flaskapp>.py`). In this case, we use `flask_openshift_template.py, with a "Hello World!" example.
>>>>>>> 98a517d... Add wsgi to README
=======
**5)** We create a Flask app in another file (`<project>/<flaskapp>.py`). In this case, we use `flask_openshift_template.py`, with a "Hello World!" example.
>>>>>>> 48c9b39... Typo closing code 'tag'

```python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
```

**6)** In `<project>/wsgi.py` we must change the server argument from a function (default) to our Flask app. We'll delete everything except our main code and import our Flask app.

```python
import os
from flask_openshift_template import app


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 8051, app)
    httpd.serve_forever()
```

<<<<<<< HEAD
<<<<<<< HEAD
- folders

- Flask says "Hello World!"

- Environment variables
=======
**7)** Go to `https://<project>-<namespace>.rhcloud.com`
>>>>>>> 904a16e... Step by step guide ends with link to functional app
=======
**7)** Go to `https://<project>-<namespace>.rhcloud.com`

# Optional

If you want to use Environment Variables, you can set variables with:

```bash
rhc env set <var1>=<value> <var2>=<value> -a <project>
```

and you can list them,

```bash
rhc env list -a <project>
```

view one or more,

```bash
rhc env show <var1> <var2> -a <project>
```

and remove a variable

```bash
rhc env unset <var> -a <project>
```
>>>>>>> d4d02d1... Add Environment Variables info to Step-by-step.md
