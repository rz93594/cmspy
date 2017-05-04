from flask import Flask
from flask import request
import json
import markdown2
import codecs
import requests


app = Flask(__name__)

@app.route('/')
def hello_world():
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

if __name__ == "__main__":
    app.run()
