import urllib
from google.appengine.api import urlfetch
import logging
import json

class Api():
	def __init__(self, bot_token):
		self.bot_token = bot_token
	
	def send(self, chatId, text, messageId = None, parse_mode = None):
		form_fields = {
		  'chat_id': chatId,
		  'text': text
		}
		if messageId:
			form_fields['reply_to_message_id'] = messageId		
		if parse_mode:
			form_fields['parse_mode'] = parse_mode

		url = 'https://api.telegram.org/bot%s/sendMessage' % self.bot_token
		result = urlfetch.fetch(url=url,
			payload= json.dumps(form_fields),
			method=urlfetch.POST,
			headers={'Content-Type': 'application/json'})
		if result.status_code != 200:
			logging.error(result.content)