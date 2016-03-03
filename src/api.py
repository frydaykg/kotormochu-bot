import urllib
from google.appengine.api import urlfetch
import settings

class Api():
	def send(self, chatId, text, messageId = None):
		form_fields = {
		  'chat_id': chatId,
		  'text': text
		}
		if messageId:
			form_fields['reply_to_message_id'] = messageId

		form_data = urllib.urlencode(form_fields)
		url = 'https://api.telegram.org/bot%s/sendMessage' % settings.BOT_TOKEN
		urlfetch.fetch(url=url,
			payload=form_data,
			method=urlfetch.POST,
			headers={'Content-Type': 'application/x-www-form-urlencoded'})