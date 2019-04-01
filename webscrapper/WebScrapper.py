# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 06:35:10 2019

@author: Jiwitesh_Sharma
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 03:54:57 2019

@author: Jiwitesh_Sharma
"""

from bs4 import BeautifulSoup as bs
import urllib.request
import urllib.parse
import urllib.error
import ssl
import json
from dao.DAO import DAO


"""
At the beginning of your Python script, import the library
Now you have to pass something to BeautifulSoup to create a soup object. 
That could be a document or an URL. 
BeautifulSoup does not fetch the web page for you, you have to do that yourself. 
That's why I use urllib2 in combination with the BeautifulSoup library."""
class WebScrapper:
    daoObject = object()
    
    #def __init__(self, licenseKey):
        #daoObject = DAO(licenseKey)
        
    def __accessUrl__(self,url):
        # For ignoring SSL certificate errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = bs(html, 'html.parser')
        html = soup.prettify('utf-8')
        #html = HTMLEntitiesToUnicode(html)
        return html
    
    
    def __getCleanedReviewFromRawInput__(self, url, dbName, collectionName, licenseKey):
        daoObject = DAO(licenseKey)
        #jsonObjList = []
        # For ignoring SSL certificate errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = bs(html, 'html.parser')
        html = soup.prettify('utf-8')
        #reviews = []
        for outerdiv in soup.findAll('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'}):
            for secondOuterdiv in outerdiv.findAll('div', attrs={'class': 'a-section review aok-relative'}):
                user_json = {}
                #review = ''
                for innerdiv in secondOuterdiv.findAll('div', attrs={'class': 'a-profile-content'}):
                    #print('UserName = '+innerdiv.find('span', attrs={'class': 'a-profile-name'}).text)
                    #review = 'UserName = '+innerdiv.find('span', attrs={'class': 'a-profile-name'}).text
                    user_json['userName'] = innerdiv.find('span', attrs={'class': 'a-profile-name'}).text
                for innerdiv in secondOuterdiv.findAll('a', attrs={'data-hook': 'review-title'}):
                    #print('Review Title = '+innerdiv.find('span', attrs={'class': ''}).text)
                    #review += ','+'Review Title = '+innerdiv.find('span', attrs={'class': ''}).text
                    user_json['Review_Title'] = innerdiv.find('span', attrs={'class': ''}).text
                for innerdiv in secondOuterdiv.findAll('i', attrs={'data-hook': 'review-star-rating'}):
                    #print('Review Start rating = '+innerdiv.find('span', attrs={'class': 'a-icon-alt'}).text)
                    #review += ','+'Review Start rating = '+innerdiv.find('span', attrs={'class': 'a-icon-alt'}).text
                    user_json['Review_Star_Rating'] = innerdiv.find('span', attrs={'class': 'a-icon-alt'}).text
                for innerdiv in secondOuterdiv.findAll('div', attrs={'class': 'a-section celwidget'}):
                    #print('Review Date = '+innerdiv.find('span', attrs={'data-hook': 'review-date'}).text)
                    #review += ','+'Review Date = '+innerdiv.find('span', attrs={'data-hook': 'review-date'}).text
                    user_json['Review_Date'] = innerdiv.find('span', attrs={'data-hook': 'review-date'}).text
                for innerdiv in secondOuterdiv.findAll('div', attrs={'class': 'a-row a-spacing-small review-data'}):
                    #print('Review body = '+innerdiv.find('span', attrs={'class': ''}).text)
                    #review += ','+'Review body = '+innerdiv.find('span', attrs={'class': ''}).text
                    user_json['Review_Body'] = innerdiv.find('span', attrs={'class': ''}).text
                    
                    
                daoObject.insertDataInDB(user_json, dbName, collectionName)
                
                #review = json.dumps(user_json)
                #jsonObjList.append(user_json)
                #collections.insert_one(user_json)
                
            
        #return jsonObjList
           
#print(soup.findAll('div', attrs={'class': 'a-section review aok-relative'}))
# This block of code will help extract the Brand of the item

    #print(divs)