# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 08:20:18 2019

@author: Jiwitesh_Sharma
"""
"""Making a Connection with MongoClient The first thing we need to do is import pymongo. 
The import should run without any errors to signify that we've done our installation well."""



#Establishing a connection in MongoDB requires us to create a MongoClient to the running MongoDB instance.
from pymongo import MongoClient

class DAO:
    client = object()
    def __init__(self, licenseKey):
        if licenseKey == '239813079843747492KSFJKSDJ9243809490280':
            client = MongoClient()
            """Creating a Database To create a database in MongoDB, we use the MongoClient instance and specify a database name. 
            MongoDB will create a database if it doesn't exist and connect to it."""
        else:
            print("Invalid LicenseKey")
            
        
    def insertDataInDB(self, data, dbName, collectionName):
        client = MongoClient()
        db = client[dbName]
        collections = db.collectionName
        result = collections.insert_one(data)
        #print(collections.find_one())
    def pullCompleteData(self, dbName, collectionName):
        client = MongoClient()
        db = client[dbName]
        collections = db.collectionName
        #cursor = collections.find()
        cursor = collections.find({},{ "_id": 0, "userName": 1, "Review_Title": 1, "Review_Star_Rating":1, "Review_Date":1, "Review_Body":1 })
        #x   = []
        """for i in cursor:
            x.append(i)
            print(x)"""
        return cursor
    def pullDataFieldWise(self, propertyName, value, dbName, collectionName):
        client = MongoClient()
        db = client[dbName]
        collections = db.collectionName
        #query =  { propertyName :  value }
        query = { propertyName: { "$regex": "^"+value+""} }
        cursor = collections.find(query)
        #x   = []
        #print(cursor)
        """for i in cursor:
            print(i)"""
        return cursor
    