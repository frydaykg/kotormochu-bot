from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import json
import urllib
import re
from google.appengine.api import urlfetch
from api import Api
from translator import Translator
import logging

class Main(webapp.RequestHandler):
	def post(self):
		update = json.loads(self.request.body)
		if 'message' in update:
			message = update['message']
			if 'text' in message:
				text = message['text'].encode('utf-8') # from unicode to ascii
				chat = message['chat']
				translations = Translator().translate(text)
				for translation in translations:
					encodedTranslation = translation.decode('utf-8')
					translationLen = len(encodedTranslation)
					if translationLen < 4096:
						Api().send(chat['id'], encodedTranslation, messageId = message['message_id'], parse_mode = 'HTML')
					else:
						Api().send(chat['id'], encodedTranslation[:4096], messageId = message['message_id'], parse_mode = 'HTML')
						for i in xrange(4096, translationLen, 4096):
							Api().send(chat['id'], encodedTranslation[i:min(i + 4096, translationLen)], parse_mode = 'HTML')

application = webapp.WSGIApplication([('/.*', Main)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
