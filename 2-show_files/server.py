# coding: utf-8
from bottle import route, run, template, static_file, debug, view
import os

CODEDIR = '2-show_files'
curpath = '.'

@route('<:re:/+>')
def index():
    number_of_files = 333
    return template('There are {{files}} to be reviewed', 
                    files=number_of_files)

@route('/front')
@route('/front/')
@route('/front/<filename:path>')
def server_static(filename='index.html'):
    global curpath
    return static_file(filename, root=curpath+'/front')

@route('/img/<filename>')
def server_static(filename):
    global curpath
    return static_file(filename, root=curpath+'/../work')

@route('/template')
@route('/template/<text>')
@view('item')
def hello(text='Wassup!'):
    return {"text": text, "image": "032_la.png"}


if __name__ == '__main__':
    if os.path.exists(CODEDIR):
        curpath = CODEDIR

    debug(True)
    run(host='localhost', port=8080, reloader=True)
