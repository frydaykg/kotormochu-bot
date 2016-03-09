from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import json
import urllib
import re
from google.appengine.api import urlfetch
from api import Api
from translator import Translator
import logging
import settings

class Main(webapp.RequestHandler):
	api = Api(settings.BOT_TOKEN)
	translator = Translator()
	
	def post(self):
		update = json.loads(self.request.body)
		if 'message' in update:
			message = update['message']
			if 'text' in message:
				text = message['text'].encode('utf-8') # from unicode to ascii
				chatId = message['chat']['id']
				messageId = message['message_id']
				
				if text == '/help':
					self.help(chatId)
				else:
					self.translate(text, chatId, messageId)

	def translate(self, text, chatId, messageId):
		translations = self.translator.translate(text)
		for translation in translations:
			encodedTranslation = translation.decode('utf-8')
			translationLen = len(encodedTranslation)
			if translationLen < 4096:
				self.api.send(chatId, encodedTranslation, messageId = messageId, parse_mode = 'HTML')
			else:
				self.api.send(chatId, encodedTranslation[:4096], messageId = messageId, parse_mode = 'HTML')
				for i in xrange(4096, translationLen, 4096):
					self.api.send(chatId, encodedTranslation[i:min(i + 4096, translationLen)], parse_mode = 'HTML')
	
	def help(self, chatId):
		text = 'Для перевода слова просто напишите его в ЛС боту и Вам придут возможные его переводы или сообщение о незнание перевода.'
		self.api.send(chatId, text)


application = webapp.WSGIApplication([('/.*', Main)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
