"""Copyright 2018 AB19
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" LDA.py: A class to perform Latent Dirichlet Allocation on given data"""

# libraries
import gensim
import gensim.corpora as corpora
from gensim.models import CoherenceModel

class LDA ():
    # constructor
    def __init__ (self, data, numPasses = 500):
        self.data = data
        self.passes = numPasses
        self.tdf = None
        self.id2word = None
        self.model = None
     
    # destructor
    def __del__ (self):
        print ('Deleting LDA object')
    
    # set the number of topics for clustering, default is 5
    def setTopics (self, topics = 5):
        self.topics = topics
        
    # function to build LDA model from the preprocessed data    
    def buildModel (self):
        print ('Building LDA model with ' + (str (self.topics)) + ' topics...\n')
        self.id2word = corpora.Dictionary (self.data)
        self.id2word.filter_extremes (no_below = 40)
        # build a term document frequency model
        self.tdf = [self.id2word.doc2bow (text) for text in self.data]
        # LDA model parameter
        self.model = gensim.models.ldamodel.LdaModel (corpus = self.tdf,
                                                     id2word = self.id2word,
                                                     num_topics = self.topics, 
                                                     update_every = 1,
                                                     chunksize = 100,
                                                     passes = self.passes,
                                                     alpha = 'auto',
                                                     per_word_topics = True)
    # prints all the topics of the LDA model   
    def printTopics (self):
        for i, topic in enumerate (self.model.print_topics ()):
            print ('Topic-' + str (i) + ':\n')
            print (topic [1])
            print ('\n')
    
    # write topics to a file on disk       
    def writeTopics (self):
        print ('Writing to topics to file...')
        f = open ('topics.txt', 'w')
        for i, topic in enumerate (self.model.print_topics ()):
            f.write ('Topic-' + str (i) + ":\n")
            f.write (topic [1])
            f.write ('\n')
        f.close ()
    
    # get perplexity of the model, lower the perlexity -> better the model       
    def getPerplexity (self):
        return self.model.log_perplexity (self.tdf)
    
    # get coherence value of the model, higher the coherence -> better the model
    def getCoherence (self):
        coherenceModel = CoherenceModel (model = self.model, texts = self.data, dictionary = self.id2word, coherence = 'c_v')
        return coherenceModel.get_coherence ()
    
    # function to return the term document frequency matrix
    def getTDF (self):
        return self.tdf
    
    # function to return the trained model
    def getModel (self):
        return self.model
    
    # function to return the id to word dictionary
    def getID2Word (self):
        return self.id2word
    
    # function to get the topics for each document to which LDA has been trained
    def getTopics (self):
        return self.model [self.tdf]
