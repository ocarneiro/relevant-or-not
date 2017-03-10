# coding: utf-8
import json
from glob import glob
from shutil import copyfile
import os

WORKDIR = '../work/'
OUTPUTDIR = '../output/'

todelete = []

with open('delete.json', 'r') as delfile:
    todelete = json.loads(delfile.read())
    
allfiles = glob(WORKDIR + '*.txt')
allfiles = [f.replace(WORKDIR,'').replace('.txt','') for f in allfiles]

output = [f for f in allfiles if f not in todelete]

# creates the work folder if it doesn't exist yet
if not os.path.exists(OUTPUTDIR):
    os.makedirs(OUTPUTDIR)

# TODO: check for invalid filenames
# found: web_archive_orgweb20120316092438http:aikilab_org.txt
#   and: wiki_richmondmakerlabs_ukindex_php?title=Main_Page.txt
for f in output:
    copyfile(WORKDIR + f + '.txt', OUTPUTDIR + f + '.txt')
