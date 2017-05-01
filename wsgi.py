from flask import Flask
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import contentful
import json 
import ezmarkdown as md
import urlparse
from pprint import pprint
import markdown2
application = Flask(__name__)

def getPolicy(entry_id):
	client = contentful.Client('fu002ykhvufg', '809aae87325edb4f8c044500363ed3ce271a458785ac802f48d726cd50cd8213')
	entries = client.entries()
	entries = client.entries({'content_type': 'document'})

	#entry_id = '2wXQlSZiq0mOGk2MgOw4CM'
	#entry_id  = '7eYnixg5vaqWQQSe420MKy'
	htmlize = client.entry(entry_id)
		
	policy = client.entry(entry_id)
	global content
	content =  htmlize.policy
	#content_u = content.decode("utf-8")
	#content = content_u.encode("ascii","ignore")
	#content = md.md_to_html(content)
	content = markdown2.markdown(content)
	print content
	return content
	

#getPolicy()


@application.route("/")
def hello():
    lang = request.args.get('lang')
    if lang == "en-US":
		lang == "2wXQlSZiq0mOGk2MgOw4CM"
    elif lang == "en-ES":
		lang == "4QQXiqQOVqyC8mu4S2Ow6u"
    else:
	 	lang == "2wXQlSZiq0mOGk2MgOw4CM"
    getPolicy(lang)
    print "Pulling content"
    #print "content: %s" % content
    return content

if __name__ == "__main__":
    application.run()
