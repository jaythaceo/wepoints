"""
Web Crawler 1.0
By: Jason Brooks
Email: jaythaceo@gmail.com

"""
import urllib2, cookielib
import urlparse
import BeautifulSoup
import sqlite3
import time, datetime
import threading, Queue
time.clock() # initializing clock

globalData = {
	'useragent': 'Crawler 1.0',
	'whitelist': [],
	'blacklist': [],
	'startURL': 'http://www.digitalldesk.com/',
	'threadLimit': 1,
	'requestInterval': 0.5,
	'queue': [],
	'debug':
}

class Crawl:
	def __init__(self):
		if globalData['debug']: print 'Crawl | init called'
		self.cookie = cookielib.CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
		
	def getURL(self):
		if globalData['debug']: print 'Crawl | init called'
		# check for start url
		if globalData['startURL']:
			url = [(0, globalData['startURL'])]
			globalData['startURL'] = None
		else:
			url = self.db.getURLFromQueue(globalData['threadLimit'])
		return url
	
	def requestURL(self):
		
