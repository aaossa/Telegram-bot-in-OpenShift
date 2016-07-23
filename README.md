# Telegram bot in OpenShift

This is a template to host in [OpenShift](https://openshift.redhat.com) a Python 3.x **Telegram bot** using [Flask](http://flask.pocoo.org/). Using [aaossa/flask-openshift](https://github.com/aaossa/flask-openshift)

### Running on OpenShift

Create a Python application with this command

```bash
rhc app-create <project> python-3.3 --from-code https://github.com/aaossa/Telegram-bot-in-OpenShift.git
```

### Register and use of your bot

> Describe conversation with @BotFather and setting up webhook

# License

Code licensed under [GNU General Public License v3](http://opensource.org/licenses/GPL-3.0).
