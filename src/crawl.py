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
		if globalData['debug']: print 'Crawl | getURL called'
		# check for start url
		if globalData['startURL']:
			url = [(0, globalData['startURL'])]
			globalData['startURL'] = None
		else:
			url = self.db.getURLFromQueue(globalData['threadLimit'])
		return url
	
	def requestURL(self):
		if globalData['debug']: print 'Crawl | requestURL called'
		url = data['full_url']
		request = urllib2.REquest(url)
		self.cookie.add_cookie_header(request)
		visitedtime = datetime.datetime.utcnow()
		try:
			start = time.clock()
			response = urllib2.urlopen(request)
			response = response.read()
			end = time.clock()
			loadtime = end - start 
		except (urllib2.HTTPError, urllib2.URLError), e:
			response = None
			data.update({'error': e})
			loadtime = 0
		data.update({'source': response, 'loadtime': loadtime, 'request_url': url, 'visitedtime': visitedtime})
		return data

class DBops(object):
	def __init__(self):

		
	def create(self):
	

	def getURLFromQueue(self, limit):





	
		