#Amal Omar 
#CS 5001
#Project 9
import turtle 
import turtle_interpreter as it
import random
class Lsystem: 

    def __init__(self, filename=None): 
        self.base = ""
        self.rules = {}
        if filename != None:
            self.read(filename)
    # call the read method of self with filename as the argument
    def getBase(self ): #return the base string of an L-system.
    #The getBase function takes in just one argument--the L-system list. It returns the base string, which is the first item in the L-system list.
        return self.base
    def setBase( self, b): #set the value of the base of an L-system.
    #The setBase function takes in two arguments, an L-system list and a base string. It should assign to the base string field of the L-system list the new string provided in the base parameter.
        self.base = b
    def addRule( self, newrule ): 
        self.rules[newrule[0]] = newrule[1:]
    def getRule( self, index ): 
        pass

    def numRules(self):
        pass

    def read( self, filename ):
        self.rules = {}
        fp = open(filename, "r")
        for line in fp: 
            line = line.strip()
            words = line.split()
            if words[0] == "base":
                self.setBase(words[1])
            elif words[0]=="rule":
                self.addRule(words[1:])
        fp.close()
    
    def replace(self, istring):
        tstring = ""
        for c in istring:
            if c in self.rules: 
                tstring += random.choice(self.rules[c])
            else:
                tstring += c
        return tstring

    def buildString( self, iterations):
        nstring = self.base
        # rule = getRule(lsys,0)
        # symbol = rule[0]
        # replacement = rule[1]
        for i in range (iterations):
            nstring = self.replace(nstring)
        return nstring
       
                            