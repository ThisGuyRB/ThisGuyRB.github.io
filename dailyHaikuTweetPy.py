# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 15:44:34 2015

@author: Roger Barker
"""

#file = open('/Users/Admin/Documents/GitHub_Projects/ThisGuyRB.github.io/index.html','')

import tweepy
oauth_consumer_key="oWRIavQWvAVCqAFu19SiBzLOO"
cSec  = "2sTu1I1DyEnr3zVH5JbsuF3uHdQR6HZ0zq9J4wMtBoYkspBIXA"
oauth_token="381886161-o11AVtvERDKubua8BrdfFGdBwZfQ1MrSiL4Jfblp"
aTSec = "RDPzzh5WiN0h19D3l4zr2uLw3u8nS4dPe88MIFfO3kViW"

def updateInnerHtml():
    archiveFile=open("/Users/Admin/Documents/GitHub_Projects/dailyHaikuArchive/index.html","r+")
    activeFile=open("/Users/Admin/Documents/GitHub_Projects/ThisGuyRB.github.io/index.html","r+")
    
        
    
    archiveFile.close()
    activeFile.close()
    return

def tweet():
    statObj='Check out the Daily Haiku at http://bit.ly/1Bir5Rf #haiku4u'
        
    auth = tweepy.OAuthHandler(oauth_consumer_key,cSec)
    auth.set_access_token(oauth_token,aTSec)
    api = tweepy.API(auth)

    api.update_status(status=statObj)
    print "Updated Successfully"
    return
tweet()
