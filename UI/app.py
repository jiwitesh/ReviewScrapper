# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 00:32:27 2019

@author: Jiwitesh_Sharma
"""
from webscrapperservice.WebScrapperService import WebScrapperService
from dao.DAO import DAO
#from webscrapperutils.WebScrapperUtils import WebScrapperUtils
from flask import Flask, flash, redirect, render_template, request, session, abort
import json
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
    """if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!  <a href='/logout'>Logout</a>'"""
@app.route('/pushData', methods=['GET'])
def pushReviewInDB():
    #utils = WebScrapperUtils()
    if request.method == 'POST':
        url = request.form['url']
         #return redirect(url_for('success',name = user))
    else:
        url = request.args.get('url')
    print('printing = '+url)
    """if isUrlValid(url):
        print("Inserted URL is valid ")
        url = getUrl(url)
    else:
        flash('Uh! oh! invalid url !')
        return home"""
    """if request.form['url'] == '' and request.form['username'] == 'admin':
       session['logged_in'] = True
    else:
       flash('wrong password!')"""
   
    #url = 'https://www.amazon.com/Lenovo-Thinkpad-20KH002FUS-2560x1440-Ultrabook/product-reviews/B079J59B77/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
    dbName = 'reviewData'
    collectionName = 'rawData'
    licenseKey = '239813079843747492KSFJKSDJ9243809490280'
    
    webScrpService = WebScrapperService()
    
    webScrpService.__main__(url, dbName, collectionName, licenseKey)
    
    """fieldData = webScrpService.__getReviewPropData__("userName", "Marin", dbName, collectionName, licenseKey)
    for x in fieldData:
        print(x)
    completeReview = webScrpService.__getCompleteReviewData__( dbName, collectionName, licenseKey)
    for x in completeReview:
        print(x)"""
    return home()
@app.route("/searchResult.html")
def searchPage():
    return render_template('searchResult.html')
    """if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!  <a href='/logout'>Logout</a>'"""
@app.route("/searchData", methods=['GET'])
def searchData():
    if request.method == 'POST':
        user = request.form['userName']
         #return redirect(url_for('success',name = user))
    else:
        user = request.args.get('userName')
         #return redirect(url_for('success',name = user))
    #userName = request.args.get('userName')
    #userName = request.__getattr__("UserName")
    #userName = request.form['user']
    #print("Printing = ",user)
    dbName = 'reviewData'
    collectionName = 'rawData'
    licenseKey = '239813079843747492KSFJKSDJ9243809490280'
    
    webScrpService = WebScrapperService()
    
    #webScrpService.__main__(url, dbName, collectionName, licenseKey)
    
    fieldData = webScrpService.__getReviewPropData__("userName", user, dbName, collectionName, licenseKey)
    #type(fieldData)
    """for x in fieldData:
        print(x)"""
    return render_template('searchResult.html', reviews=fieldData)
    
        
@app.route("/showData")
def showData():
    
    url = 'https://www.amazon.com/Lenovo-Thinkpad-20KH002FUS-2560x1440-Ultrabook/product-reviews/B079J59B77/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
    dbName = 'reviewData'
    collectionName = 'rawData'
    licenseKey = '239813079843747492KSFJKSDJ9243809490280'
    
    webScrpService = WebScrapperService()
    
    #webScrpService.__main__(url, dbName, collectionName, licenseKey)
    
    #fieldData = webScrpService.__getReviewPropData__("userName", "Marin", dbName, collectionName, licenseKey)
    """for x in fieldData:
        print(x)"""
    completeReview = webScrpService.__getCompleteReviewData__( dbName, collectionName, licenseKey)
    """for x in completeReview:
        print(x)"""
    #return render_template('review.html', records=temp, colnames=columnNames)
    return render_template('review.html', reviews=completeReview)


def isUrlValid(self,userInput):
    if('/'  in userInput):
        return True
    elif('.' in userInput):
        return True
    else:
        return False
        
def getUrl(self,userInput):
    if(userInput.startswith('http')):
        return userInput
    elif(userInput.startswith('https')):
        return userInput
    else:
        return 'Invalid Url!!!!!!!!'


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000)