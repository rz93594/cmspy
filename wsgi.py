from flask import Flask
from flask import request
import json
import markdown2
import codecs
import requests

# demo
application = Flask(__name__)

@application.route('/tos')
def tos():
    lang = 'es-ES'
    lang = request.args.get('lang')
    if lang == 'es-ES':
	print "lang 'es-ES'"
        url = 'https://cdn.contentful.com/spaces/56hstk4a7t1c/entries/4pmKwn7Y52YaQ062ek4A8W?access_token=22bf1287429a7155ff1553e480eac8c40b97b03a749d5bd4a88e3633ea3c0f6c&locale=es-ES'
    else:
	print "lang == 'en-US'"
        url = 'https://cdn.contentful.com/spaces/56hstk4a7t1c/entries/4pmKwn7Y52YaQ062ek4A8W?access_token=22bf1287429a7155ff1553e480eac8c40b97b03a749d5bd4a88e3633ea3c0f6c&locale=en-US'
    r = requests.get(url)
    html =  r.json()
    tos = html['fields']['policy']
    tos_html = markdown2.markdown(tos)
    return tos_html

@application.route('/privacy')
def privacyPolicy():
    lang = 'es-ES'
    lang = request.args.get('lang')
    if lang == 'es-ES':
	print "lang 'es-ES'"
        url = 'https://cdn.contentful.com/spaces/56hstk4a7t1c/entries/48d55Mc0YECqk8yy6WyMSM?access_token=22bf1287429a7155ff1553e480eac8c40b97b03a749d5bd4a88e3633ea3c0f6c&locale=es-ES'
    else:
	print "lang == 'en-US'"
        url = 'https://cdn.contentful.com/spaces/56hstk4a7t1c/entries/48d55Mc0YECqk8yy6WyMSM?access_token=22bf1287429a7155ff1553e480eac8c40b97b03a749d5bd4a88e3633ea3c0f6c&locale=en-US'
    r = requests.get(url)
    html =  r.json()
    pp = html['fields']['terms']
    pp = markdown2.markdown(tos)
    return pp





if __name__ == "__main__":
    application.run(debug = "True")
