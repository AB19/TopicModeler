"""Copyright 2018 AB19
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""
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
