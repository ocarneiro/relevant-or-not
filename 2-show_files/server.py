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
cur_index = 0  # current index
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
    to_be_deleted.append(all_items[int(index)])
    return "Deleted number %s: %s" % (index, all_items[int(index)])

@route('/meta/text')
def rt_text():
    global cur_index, curpath
    filename = all_items[cur_index]
    text = Path(curpath+'/../work/' + filename + '.txt').read_text()
    # text = "This is an awesome hackerspace!!"
    return text

@route('/meta/filename')
def rt_filename():
    filename = all_items[cur_index]
    return filename

@route('/meta/imgname')
def rt_imgname():
    global all_items, cur_index
    image_name = all_items[cur_index] + ".png"
    return image_name


@route('/front')
def rt_wrong():
    redirect('/front/')


@route('/front/')
@route('/front/<filename:path>')
def rt_front(filename='index.html'):
    response = static_file(filename, root=curpath+'/front')
    # response.set_header("Cache-Control", "public, max-age=604800")
    return response

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
    # all_items = ["hackerspace_titusvillefl_net", "accessplus_com_phlogic", "tinycorelab_noblogs_org", "JMoonLabs_comMakerSpace", "www_wulfman_com", "space_flamingoeda_com", "logre_eu", "hackerspace-krk_pl", "makerspaceydbk_tistory_com", "emperor-team_org", "www_biznettechspace_comEn", "legend-h_org", "padirbtuves_lt", "www_ozberrypi_org", "www_makeplace_co_nz", "tijuanamakerspace_wordpress_comabout", "fikraspace_com", "www_techspace_cn", "www_karajbeirut_org", "hackest_org", "alpha_autodidaktikum_de", "www_sotechiespaces_com", "www_alexhacker_com", "hackspb_ru", "www_giovanniraco_com", "www_raleighmakerspace_com", "www_kufr_cz", "www_makeshopmiami_com", "Openspace_io", "vtdk_hacklab_lt", "www_phenixit_net", "www_mafralab_org", "miss-hack_org", "tetalab_org", "dp_idd_tamabi_ac_jphackerspace", "www_openlandlab_org", "foomatic_org", "www_kickstarter_comprofilejoplinhackspace", "hackerspace_pl", "teclab_gt", "trentonatelier_com", "www_bioclub_org", "www_antitronics_com", "www_osilab_org", "skillsyndicate_org", "innovation_ibu_edu_ba", "spc_org", "www_archubpnh_com", "www_chilebot_com", "www_Chaihuo_org", "www_hswro_org", "www_modulab_ro", "arjunhackingstuff_wordpress_com", "inventeaza_ro", "subspace_io", "seeqnce_com", "www_tinkertankmiami_com", "heliospace_ca", "www_hackerhub_com", "0x20_be", "www_hackerspacepp_org", "www_meetup_comLETHAL", "watershedpdx_com", "c-base_org", "www_intelirobot_com_mxmakerspace_html", "cowharf_com", "ideas-squared_biz", "www_rocklandsteelhouse_com", "www_makershive_org", "hackerspacesby_webstarts_com", "tilda_center", "www_hakkavelin_is", "simonsroom_neocities_org", "twitter_comgeekwine", "hackerspacecholula_org", "www_node-lab_org", "lugons_org", "macgyver_siliconhill_cz", "www_meetup_comStavanger-Hackerspace", "www_STEAMWorksLabs_com", "www_bangkokmakerspace_com", "www_siamlewisburg_com", "www_ljudmila_org", "www_jeannedhack_org", "www_buffalolab_orgblog", "www_Blindsecurity_org", "protoshed_ca", "nawaat_org"]
    debug(True)
    run(host='localhost', port=8080, reloader=True)
