from requests import post
from settings import TELEGRAM_API_URL, TELEGRAM_BOT_NAME, TELEGRAM_SECRET_URL, TELEGRAM_TOKEN


class Bot:

	@staticmethod
	def __default(chat_id, *args):
		return {"status": "OK"}

	@staticmethod
	def __echo(chat_id, *args):
		"""*echo(...)*:
		- /echo -  Uso del comando
		- /echo mensaje - Responde con <mensaje>"""
		if not args:
			text = Bot.__echo.__doc__
		else:
			text = " ".join(args)
		return Bot.__send_message(chat_id, text, parse_mode="Markdown")

	@staticmethod
	def __send_message(chat_id, text, disable_web_page_preview=False, parse_mode=None):
		params = {
			"chat_id": chat_id,
			"text": text,
			"parse_mode": parse_mode,
			"disable_web_page_preview": disable_web_page_preview
		}
		url = TELEGRAM_API_URL.format(TELEGRAM_TOKEN, "sendMessage")
		req = post(url, data=params)
		return req.json()

	@staticmethod
	def __validate_command(command):
		mention = "@{}".format(TELEGRAM_BOT_NAME)
		command = command if command.endswith(mention) else command + mention
		command = command[1:] if command.startswith("/") else str()
		command = "".join(command.rsplit(mention, 1))
		COMMANDS = {
			"echo": Bot.__echo
		}
		return COMMANDS.get(command, Bot.__default)

	@staticmethod
	def process_message(chat_id, text):
		text = text.encode("utf-8").decode("utf-8", "ignore")
		command = text.split(" ")
		bot_command = Bot.__validate_command(command[0])
		response = bot_command(chat_id, *command[1:])
		return response

	@staticmethod
	def valid_payload(payload):
		if type(payload) is not dict:
			return False
		if "message" not in payload:
			return False
		if type(payload["message"]) is not dict:
			return False
		if any(key not in payload["message"] for key in ("text", "chat")):
			return False
		if type(payload["message"]["text"]) is not str:
			return False
		if type(payload["message"]["chat"]) is not dict:
			return False
		if "id" not in payload["message"]["chat"]:
			return False
		return True
