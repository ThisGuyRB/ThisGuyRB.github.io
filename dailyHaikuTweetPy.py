# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 15:44:34 2015

@author: Roger Barker
"""


import tweepy
import re
from tempfile import mkstemp
from shutil import move
from os import remove, close

oauth_consumer_key="oWRIavQWvAVCqAFu19SiBzLOO"
cSec  = "2sTu1I1DyEnr3zVH5JbsuF3uHdQR6HZ0zq9J4wMtBoYkspBIXA"
oauth_token="381886161-o11AVtvERDKubua8BrdfFGdBwZfQ1MrSiL4Jfblp"
aTSec = "RDPzzh5WiN0h19D3l4zr2uLw3u8nS4dPe88MIFfO3kViW"


def updateInnerHtml():
    archiveFile=open("/Users/Admin/Documents/GitHub_Projects/dailyHaikuArchive/index.html","r+")
    activeFile=open("/Users/Admin/Documents/GitHub_Projects/ThisGuyRB.github.io/index.html","r+")
    newHaikuFile=open("/Users/Admin/Documents/GitHub_Projects/haiku.txt","r")
    
    pattern = '\s*<p\s*id="haikuP"\s*>'
    test = re.compile(pattern)
    c = 0
    for line in activeFile:
        t = test.match(line)
        if t:
            print "found the line:"
            print line
            c = 3
            continue
        if c ==3:
            stringOne = str(line)
            archWrite(archiveFile,stringOne,'i')
            replStr = newHaikuFile.readline()
            print replStr
            c = c-1
        if c == 2:
            stringTwo = str(line)
            archWrite(archiveFile,stringTwo,'t')
            replStr = newHaikuFile.readline()
            print replStr
            c = c-1
        if c == 1:
            stringThree = str(line)
            archWrite(archiveFile,stringThree,'f')
            replStr = newHaikuFile.readline()
            print replStr
            break
    archiveFile.close()
    activeFile.close()
    return

def replace(file_path, pattern, subst):
    #Create temp file
    fh, abs_path = mkstemp()
    with open(abs_path,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    close(fh)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)


def archWrite(f,s,ind):
    #if initial print start tag
    if ind=='i':
        f.write('<p>\n')
    
    #write the line    
    f.write(s)
    
    #if final print close tag
    if ind == 'f':
        f.write('\n</p>\n')

def tweet():
    statObj='Check out the Daily Haiku at http://bit.ly/1Bir5Rf #haiku4u'
        
    auth = tweepy.OAuthHandler(oauth_consumer_key,cSec)
    auth.set_access_token(oauth_token,aTSec)
    api = tweepy.API(auth)

    api.update_status(status=statObj)
    print "Updated Successfully"
    return

updateInnerHtml()