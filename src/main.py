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
				text = text = message['text'].encode('utf8')
				chat = message['chat']
				translations = Translator().translate(text)
				for translation in translations:
					translationLen = len(translation)
					if translationLen < 4096:
						Api().send(chat['id'], translation, messageId = message['message_id'], parse_mode = 'HTML')
					else:
						Api().send(chat['id'], translation[:4095], messageId = message['message_id'], parse_mode = 'HTML')
						for i in xrange(4095, translationLen, 4095):
							Api().send(chat['id'], translation[i:min(i + 4095, translationLen)], parse_mode = 'HTML')

application = webapp.WSGIApplication([('/.*', Main)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
