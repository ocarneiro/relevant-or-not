# coding: utf-8
from bottle import route, run, template, static_file, debug, view
from bottle import redirect
import os
import json
from glob import glob
from pathlib import Path


CODEDIR = '2-show_files'
curpath = '.'  # path where this file lives
all_items = []
cur_index = 1  # current index
to_be_deleted = []

def load_items():
    global all_items, curpath
    filenames = glob(curpath + '/../work/*.txt')
    filenames = [os.path.basename(x) for x in filenames]
    all_items = [i.replace('.txt','') for i in filenames]

@route('/meta/flagged')
def rt_flagged():
    global to_be_deleted
    return json.dumps(to_be_deleted)

@route('/meta/total')
def rt_total():
    global all_items
    number_of_items = len(all_items)
    return str(number_of_items)

@route('/meta/index')
def rt_index():
    global cur_index
    return str(cur_index)

@route('/meta/index/<index>')
def rt_index_num(index):
    global cur_index
    cur_index = int(index)
    return str(cur_index)

@route('/meta/flag/<index>')
def rt_flag(index):
    global to_be_deleted
    to_be_deleted.append(index)
    return "Deleted number %s" % index

@route('/meta/text')
def rt_text():
    global cur_index, curpath
    filename = all_items[cur_index-1]
    text = Path(curpath+'/../work/' + filename + '.txt').read_text()
    # text = "This is an awesome hackerspace!!"
    return text

@route('/meta/imgname')
def rt_imgname():
    global all_items, cur_index
    image_name = all_items[cur_index-1] + ".png"
    return image_name


@route('/front')
def rt_wrong():
    redirect('/front/')


@route('/front/')
@route('/front/<filename:path>')
def rt_front(filename='index.html'):
    global curpath
    return static_file(filename, root=curpath+'/front')

@route('/img/<filename>')
def rt_image(filename):
    global curpath
    return static_file(filename, root=curpath+'/../work')

@route('/template')
@route('/template/<text>')
@view('item')
def rt_template(text='Wassup!'):
    return {"text": text, "image": "032_la.png"}

@route('/template')
@route('/template/<text>')
@view('item')
def rt_template(text='Wassup!'):
    return {"text": text, "image": "032_la.png"}


if __name__ == '__main__':
    if os.path.exists(CODEDIR):
        curpath = CODEDIR

    load_items()
    debug(True)
    run(host='localhost', port=8080, reloader=True)
