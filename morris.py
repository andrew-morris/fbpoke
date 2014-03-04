#!/usr/bin/python

class mprint:

  def update(self, string):
    self.string = string
    print "[+] %s" % string
  
  def error(self, string):
    self.string = string
    print "[X] %s" % string

  def important(self, string):
    self.string = string
    print "[!] %s" % string

  def tab(self, string):
  	self.string = string
  	print "\t[+] %s" % string

mprint = mprint()
