# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 06:34:40 2019

@author: Jiwitesh_Sharma
"""

from dao.DAO import DAO
from webscrapper.WebScrapper import WebScrapper
from webscrapperutils.WebScrapperUtils import WebScrapperUtils
class WebScrapperService:
   
    def __main__(self, url, dbName, collectionName, licenseKey):
        utils = WebScrapperUtils()
        webScrp = WebScrapper()
        if utils.isUrlValid(url):
            print("Inserted URL is valid ")
            url = utils.getUrl(url)
            
            webScrp.__getCleanedReviewFromRawInput__(url, dbName, collectionName, licenseKey)
           
        else:
            print('Invalid Url!!!!):')
    def __getReviewPropData__(self, propertyName, value, dbName, collectionName, licenseKey):
        daoObj = DAO(licenseKey)
        result = ''
        if propertyName is not None:
            result = daoObj.pullDataFieldWise(propertyName, value, dbName, collectionName)
        return result
    def __getCompleteReviewData__(self, dbName, collectionName, licenseKey):
        daoObj = DAO(licenseKey)
        result = ''
        result = daoObj.pullCompleteData(dbName, collectionName)
        
        return result
        
            
    
   
    

