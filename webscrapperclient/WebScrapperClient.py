# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 05:47:40 2019

@author: Jiwitesh_Sharma
"""
from webscrapperservice.WebScrapperService import WebScrapperService
class WebScrapperClient:
    url = 'https://www.amazon.com/Lenovo-Thinkpad-20KH002FUS-2560x1440-Ultrabook/product-reviews/B079J59B77/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
    dbName = 'reviewData'
    collectionName = 'rawData'
    licenseKey = '239813079843747492KSFJKSDJ9243809490280'
    
    webScrpService = WebScrapperService()
    
    webScrpService.__main__(url, dbName, collectionName, licenseKey)
    
    webScrpService.__getReviewPropData__("userName", "Marin", dbName, collectionName, licenseKey)
    
    webScrpService.__getCompleteReviewData__( dbName, collectionName, licenseKey)
    