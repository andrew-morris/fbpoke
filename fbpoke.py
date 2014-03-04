#!/usr/bin/python

from morris import mprint

try:
	import mechanize
except:
	print "[!] Error. Python Mechanize module not found"
	exit()

import time
import os
import cookielib
import sys

FACEBOOK_USERNAME = ""
FACEBOOK_PASSWORD = ""

mprint.update("Setting some variables")
MAX_DELAY = 5
delay = MAX_DELAY
totalPokes = 0
browser = mechanize.Browser()
mprint.update("Instantiating Mechanize browser")
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.61')]
browser.set_handle_robots(False)
browser.set_handle_equiv(True)
browser.set_handle_redirect(True)
browser.set_handle_referer(True)
browser.set_handle_refresh(False)
mprint.update("Requesting Facebook poke page to authenticate")
browser.open("https://m.facebook.com/pokes")
browser._factory.is_html = True
mprint.update("Filling username and password into fields")
browser.select_form(nr=0)
browser.form['email'] = FACEBOOK_USERNAME
browser.form['pass'] = FACEBOOK_PASSWORD
mprint.update("Submitting request with forms and storing response")
pokepage = str(browser.submit().read())
browser._factory.is_html = True
mprint.update("Starting auto-poke loop")
while True:
        try:
                tempPokeCount = 0
                pokepage = browser.open("https://m.facebook.com/pokes").read()
                browser._factory.is_html = True
                for l in browser.links(): 
                        result = True
                        browser._factory.is_html = True
                        if result:
                                browser.follow_link(text_regex="Poke Back",nr=0)
                                tempPokeCount += 1
                                totalPokes += 1
                                mprint.update("Poked! Total Pokes: " + str(totalPokes))
                if (tempPokeCount != 0 and delay > 1): delay /= 2
                if (tempPokeCount == 0 and delay < MAX_DELAY): delay *= 2
        except Exception as e:
                mprint.update("Waiting for poke...")
        try: 
                time.sleep(delay)
        except KeyboardInterrupt:
                mprint.error("Ctrl-C detected!")
                mprint.update("Terminating")
                print "="*100
                exit()
