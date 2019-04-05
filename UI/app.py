# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 00:32:27 2019

@author: Jiwitesh_Sharma
"""
from webscrapperservice.WebScrapperService import WebScrapperService
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
   
@app.route('/pushData', methods=['GET'])
def pushReviewInDB():
    if request.method == 'POST':
        url = request.form['url']
         
    else:
        url = request.args.get('url')
    print('printing = '+url)
   
    #url = 'https://www.amazon.com/Lenovo-Thinkpad-20KH002FUS-2560x1440-Ultrabook/product-reviews/B079J59B77/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
    dbName = 'reviewData'
    collectionName = 'rawData'
    licenseKey = '239813079843747492KSFJKSDJ9243809490280'
    
    webScrpService = WebScrapperService()
    
    webScrpService.__main__(url, dbName, collectionName, licenseKey)
   
    return home()
@app.route("/searchResult.html")
def searchPage():
    return render_template('searchResult.html')
   
@app.route("/searchData", methods=['GET'])
def searchData():
    if request.method == 'POST':
        user = request.form['userName']
         #return redirect(url_for('success',name = user))
    else:
        user = request.args.get('userName')
        
    dbName = 'reviewData'
    collectionName = 'rawData'
    licenseKey = '239813079843747492KSFJKSDJ9243809490280'
    
    webScrpService = WebScrapperService()
    
    fieldData = webScrpService.__getReviewPropData__("userName", user, dbName, collectionName, licenseKey)
    
    return render_template('searchResult.html', reviews=fieldData)
    
        
@app.route("/showData")
def showData():
    
    url = 'https://www.amazon.com/Lenovo-Thinkpad-20KH002FUS-2560x1440-Ultrabook/product-reviews/B079J59B77/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
    dbName = 'reviewData'
    collectionName = 'rawData'
    licenseKey = '239813079843747492KSFJKSDJ9243809490280'
    
    webScrpService = WebScrapperService()
    
   
    completeReview = webScrpService.__getCompleteReviewData__( dbName, collectionName, licenseKey)
    
   
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