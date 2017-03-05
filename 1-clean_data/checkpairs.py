# coding: utf-8
from glob import glob
from shutil import copyfile
import os

INPUTDIR = 'input'
WORKDIR = 'work'
png, txt, unpaired = [],[],[]

def checkpairs():
    global png, txt, unpaired
    print(os.getcwd())
    filenames = glob(INPUTDIR + '/*')
    l = filenames
    l = [x.replace(INPUTDIR + '/','') for x in l]
    png = [x for x in l if x.endswith('.png')]
    txt = [x for x in l if x.endswith('.txt')]
    unpaired = [x for x in txt if x.replace('.txt','.png') not in png]
    unpaired.extend([x for x in png if x.replace('.png','.txt') not in txt])

def copypairs():
    global INPUTDIR, WORKDIR, png, txt, unpaired
    
    # creates a list of files containing images and text files, but only
    #     if both exists in the input folder
    c = list(png)  # files to be copied to the work dir
    c.extend(txt)
    c = [x for x in c if x not in unpaired]
    
    # creates the work folder if it doesn't exist yet
    if not os.path.exists(WORKDIR):
        os.makedirs(WORKDIR)
    
    # copy files selected to the work folder
    for filename in c:
        copyfile(INPUTDIR + '/' + filename, WORKDIR + '/' + filename)


if __name__ == '__main__':
    if not os.path.exists('input'):
        raise FileNotFoundError('You need an input folder')

    checkpairs()
    copypairs()


