# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 06:43:51 2019

@author: Jiwitesh_Sharma
"""

class WebScrapperUtils:
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
