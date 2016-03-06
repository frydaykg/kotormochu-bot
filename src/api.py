import urllib
from google.appengine.api import urlfetch
import settings
import logging

class Api():
	def send(self, chatId, text, messageId = None, parse_mode = None):
		form_fields = {
		  'chat_id': chatId,
		  'text': text
		}
		if messageId:
			form_fields['reply_to_message_id'] = messageId		
		if parse_mode:
			form_fields['parse_mode'] = parse_mode

		form_data = urllib.urlencode(form_fields)
		url = 'https://api.telegram.org/bot%s/sendMessage' % settings.BOT_TOKEN
		result = urlfetch.fetch(url=url,
			payload=form_data,
			method=urlfetch.POST,
			headers={'Content-Type': 'application/x-www-form-urlencoded'})
		if result.status_code != 200:
			logging.error(result.content)