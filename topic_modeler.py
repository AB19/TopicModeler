"""Copyright 2018 AB19

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" topic_modeler.py: main module. makes calls to LDA, writer and pre processing module.
assumes that all the python scripts are in the same folder."""

# libraries
from LDA import LDA
from PreProcess import PreProcess
from Writer import Writer
import sys

# function that creates a preprocess object and gets the preprocessed corpus to be passed
# into LDA. 
# arguments: input file path
# return values: corpus and ID column from the json
def preProcess (inputFile):
    
    pre = PreProcess (inputFile)
    pre.preprocessText ()
    text = pre.getCorpus ()
    ids = pre.getColumn ('id')
    del pre
    
    return text, ids

# function that makes calls to the LDA object and gets associated topics with the given corpus
# arguments: corpus
# return vaues: topics and probabilities
def lda (text):
    
    lda = LDA (text)
    lda.setTopics (10)
    lda.buildModel ()
    lda.writeTopics ()
    vector = lda.getTopics ()
    del lda
    
    return vector

# function to read arguments, make calls to the writer script to format and write the data
# to a json file.
# arguments: none - taken from command line
# return values: none - writes a file to disk
def main ():
    
    inputFile = sys.argv [1]
    outputFile = sys.argv [2]
    
    text, ids = preProcess (inputFile)
    vector = lda (text)

    w = Writer (outputFile, vector, ids)
    w.getTopics ()
    w.writeJson ()
    
    print ('Done!')
    
main ()
