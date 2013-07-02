#coding=utf-8
import urllib
import re
import os.path as checkfile
import sys
reload(sys)
import sendemail
import string
import time
sys.setdefaultencoding('utf-8')
filePathName='linkrecord.txt'
urlOfwebsite='http://www.smzdm.com'
keylist = ["神价","手慢无"] #keyword for matching
mailList = ["1835xxx5605@139.com"];
#print strhtml[:1000]
def hasThisLink(newlink,filePathName):
    filehandle = open(filePathName,'r')
    isNewHyperlink=False
    try:
        hyperList_n=filehandle.readlines()
        #print hyperList
        #each of line has a \n in the bottom of lines
        hyperList=[]
        for singlelink_n in hyperList_n:
            tempstr=singlelink_n.rstrip()
            hyperList.append(tempstr)
        if newlink in hyperList:isNewHyperlink=True
    finally:filehandle.close()
    return isNewHyperlink
#start a loop
while True:
    #get the page
    sock = urllib.urlopen(urlOfwebsite)# get the content by url
    strhtml = sock.read()
    from bs4 import BeautifulSoup
    #parser the page
    soup = BeautifulSoup(strhtml)
    titlelist = soup.findAll('h2')
    mailContent = ""
    sendThisMail=False
    subjectTitle = ""
    if titlelist:
        #for each keyword we seek for the object news and links
        for key in keylist:
            print key
            matchstr=re.compile(str(key))
            for titstr in titlelist:
                #print type(titstr)
                tempstr = str(titstr)
                target = matchstr.findall(tempstr)
                #if soup's content has the target  key word
                if target:
                    subjectTitle=subjectTitle + key;
                    subsoup = BeautifulSoup(tempstr)
                    objectHyperlink = subsoup.a['href']
                    objectTitle = subsoup.a['title']
                    if not checkfile.exists(filePathName):
                        filehandle = open(filePathName,'w')
                        filehandle.close();
                    if not hasThisLink(objectHyperlink,filePathName):
                        mailContent = mailContent+objectHyperlink
                        mailContent = mailContent+"\n" #
                        mailContent = mailContent+objectTitle
                        mailContent = mailContent+"\n" #
                        sendThisMail=True
                        filehandle = open('linkrecord.txt','a')
                        try:
                            filehandle.writelines(objectHyperlink)
                            filehandle.write("\n")
                        finally:filehandle.close()
                    else:
                        print objectTitle,"but message has been sent"
#print mailContent,subjectTitle
#print type(mailContent)
    if sendThisMail:
        mailContentUtf8=mailContent.encode('utf-8','ignore')
        subjectTileUtf8=subjectTitle.encode('utf-8','ignore')
# def send_mail(to_list,sub,content)
        #print "subjectTileUtf8",subjectTileUtf8
        #print "mailContentUtf8",mailContentUtf8
        sendemail.send_mail(mailList,subjectTileUtf8,mailContentUtf8)
    time.sleep(20)
