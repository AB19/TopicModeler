#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" PreProcess.py: A class to perform preprocessing for the given data so that it could be 
fed into LDA.py"""

# libraries
import json
from nltk.corpus import stopwords
from string import ascii_letters
import pandas as pd

class PreProcess ():
    
    # constructor
    def __init__ (self, fileName):
        self.file = fileName
        self.data = None
        self.corpus = None
     
    # destructor
    def __del__ (self):
        print ('Deleting PreProcess object!')
    
    # function to read the json file and get a dataframe with ID and document as columns
    # each element of the list is a document
    def loadData (self):
    
        # read the data file
        with open (self.file) as f:
            lines = f.readlines ()
    
        # get a 2-D list with each containing the document ID and document
        dataList = []
        for line in lines:
            row = []
            line = json.loads (line)
            row.append (line ['_id'])
            row.append (line ['text'])
            dataList.append (row)
        
        # create a dataframe
        self.data = pd.DataFrame (dataList, columns = ['id', 'raw_text'])
        
        
    # function to remove numerical from an input text
    def removeNumericals (self, value):
        allowed = set (ascii_letters + ' ')
        return ''.join (filter (allowed.__contains__, value))
    
    # function to split the string one whitespace into a list of stringsin lowercase
    def splitString (self, value):
        value = value.split (' ')
        return [v.lower () for v in value if v != '' and len (v) > 2 and len (v) < 16]
    
    # function to remove stop words - needs more research and careful evaluation
    def stopWordRemoval (self, value):
        stopWords = stopwords.words ('english')
        stopWords.remove ('while')
        stopWords.extend (['x'])
        return [v for v in value if v not in stopWords]
    
    # function to preprocess the data 
    def preprocessText (self):
        print ('Reading file......')
        self.loadData ()
        print ('Cleaning data.....')
        self.data ['text'] = self.data ['raw_text'].apply (lambda x: self.removeNumericals (x))
        self.data ['text'] = self.data ['text'].apply (lambda x: self.splitString (x))
        self.data ['text'] = self.data ['text'].apply (lambda x: self.stopWordRemoval (x))
        self.corpus = self.data.text.values.tolist ()
     
    # function to return the corpus
    def getCorpus (self):
        return self.corpus
    
    # function to return the dataframe
    def getData (self):
        return self.data
    
    # function to return a column from the dataframe
    def getColumn (self, name):
        return self.data [name].values.tolist ()