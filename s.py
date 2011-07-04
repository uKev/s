# coding: utf8
'''
Created on 17.05.2011

s is an url shortener which is designed to be fast and small.

@author: Kevin Zuber
'''
import sys
sys.path.append("lib")

from bottle import route, run, static_file, view, abort, redirect, request

from service.shortener import Shortener
import config


shortener = Shortener(config.db_path)

@route("/")
@view("index")
def index():
    return dict()

@route("/", method="POST")
@view("add_url")
def add_url():
    url = request.forms.get("url")
    if url:
        key = shortener.add(url, request['REMOTE_ADDR'])
        return dict(key=key, url=request.url)
    else:
        abort(400, "You did not enter a valid URL")

@route("/:key")
@route("/s/:key")
def redirect_to_url(key):
    try:
        redirect(shortener.url[key])
    except KeyError:
        abort(404, "Key "+key+" not found")

@route('/static/:path#.+#')
def server_static(path):
    return static_file(path, root='./static')

if __name__ == '__main__':
    import bottle
    bottle.debug(True)
    run(host="localhost", port=8080, reloader=True)
else:
    import bottle
    bottle.TEMPLATE_PATH.insert(0,config.view_path)
    applications = {'':bottle.app()}