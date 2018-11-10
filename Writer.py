#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Writer.py: A class to format and ids and associated topics to a json file"""

class Writer ():
    
    def __init__ (self, file, vector, ids):
        self.file = file
        self.vector = vector
        self.ids = ids
        self.topics = []
     
    # function to extract topics from tuples of (topic, scores)
    def getTopics (self):
        for i in range (len (self.vector)):
            value = self.vector [i][0]
            value = sorted (value, key = lambda x: x [1], reverse = True)
            if len (value) > 5:
                value = value [:5]
            topic = [x [0] for x in value]
            topic = ['topic' + str (x) for x in topic]
            self.topics.append (topic)
     
    # function to write to the json file
    def writeJson (self):
        print ('Writing to file...')
        f = open (self.file, 'w')
        for i in range (len (self.ids)):
            eachRow = {}
            eachRow ['_id'] = self.ids [i]
            eachRow ['topics'] = self.topics [i]
            f.write (str (eachRow) + '\n')
        f.close ()