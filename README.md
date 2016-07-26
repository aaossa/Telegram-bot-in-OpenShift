# Telegram bot in OpenShift

This is a template to host in [OpenShift](https://openshift.redhat.com) a Python 3 **Telegram bot** using [Flask](http://flask.pocoo.org/). Build over [aaossa/flask-openshift](https://github.com/aaossa/flask-openshift)


### Running on OpenShift

Create a Python application with this command

```shell
rhc app-create <project> python-3.3 --from-code https://github.com/aaossa/Telegram-bot-in-OpenShift.git
```


### Register your bot

To create a bot, you have to talk to [@BotFather](https://telegram.me/botfather) and follow [this guide (is official)](https://core.telegram.org/bots#6-botfather). As a recomendation, [learn everything you can about Telegram bots in their documentation](https://core.telegram.org/bots#). Anyway, this is the important part:

> #### Create a new bot
> Use the **`/newbot`** command to create a new bot. The BotFather will ask you for a name and username, then generate an authorization token for your new bot.
> 
> The **name** of your bot will be displayed in contact details and elsewhere.

> The **Username** is a short name, to be used in mentions and telegram.me links. Usernames are 5-32 characters long and are case insensitive, but may only include Latin characters, numbers, and underscores. Your bot's username **must** end in ‘bot’, e.g. ‘tetris_bot’ or ‘TetrisBot’.
> 
> The **token** is a string along the lines of `110201543:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw` that will be required to authorize the bot and send requests to the [Bot API](https://core.telegram.org/bots/api).


### Environment variables

Now we must set some environment variables in openshift: 

**`TELEGRAM_BOT_USERNAME`**: Used to detect mentions to your bot.

**`TELEGRAM_SECRET_URL`**: This bot works with [webhooks](https://core.telegram.org/bots/api#setwebhook), so we need to be notified of new messages. We don't want to be spammed or attacked, so this value should be secret. **Note:** Flask uses `/<secret_url>`, don't use the full url*

**`TELEGRAM_TOKEN`**: Is our authorization to use the [Bot API](https://core.telegram.org/bots/api)

```shell
rhc env set TELEGRAM_BOT_USERNAME=<username> TELEGRAM_SECRET_URL=<secret_url> TELEGRAM_TOKEN=<token> -a <project>
```

Once we do this, we must restart the app (you could do this [via web](https://openshift.redhat.com/app/console/applications) too):

```shell
rhc app restart <project>
```

###### If this does not work then try using `rhc app stop <project>` and then `rhc app start <project>`.

> **Recomended:** Use the Python 3.6 `secrets` module to create a random and secret url. [I made a `secrets` implementation](https://gist.github.com/aaossa/a4c83ad87cd61fbd4c06f37f5913d2e3) in case you want to use it.


### Connect OpenShift with Telegram

Now our bot is registered (in Telegram) and is ready to answer our commands (in OpenShift), but our messages to the bot are not sent to OpenShift, we must set the (webhook) url that Telegram will use to communicate with our OpenShift application.

We must use the [setWebhook](https://core.telegram.org/bots/api#setwebhook) method. Is simpole, is a GET request, so you can do this in your browser or using cURL:

```shell
curl https://api.telegram.org/bot<token>/setWebhook?url=https://<project>-<namespace>.rhcloud.com/<secret_url>
```

Telegram will answer with this:

```JSON
{
	"ok": true,
	"result": true,
	"description": "Webhook was set"
}
```


### Enjoy

Go to talk your bot (you should find it at **`telegram.me/<username>`**) and try the **`/echo`** command. 



# License

Code licensed under [GNU General Public License v3](http://opensource.org/licenses/GPL-3.0).
