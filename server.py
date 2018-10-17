
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime
import socket
import os	
import re	
import urllib
from urllib import unquote	
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler  

chrome_options = Options()
chrome_options.add_argument('--disable-gpu')

browser = webdriver.Chrome(executable_path ="C:\Users\Administrator\Desktop\html\chromedriver",chrome_options=chrome_options)

def getHtml(urlPath):
	print datetime.datetime.now()
	browser.get(urlPath)
	print datetime.datetime.now()
	return browser.page_source.encode('utf-8')

class TestHTTPHandler(BaseHTTPRequestHandler):
	def do_GET(self):	
		pattern = re.compile(r'/html/(.*)')
		match = pattern.match(self.path)
		if match and match.group(1) != '':
			self.protocal_version = 'HTTP/1.1'	
			self.send_response(200)		
			self.end_headers()
			print unquote(match.group(1))
			self.wfile.write(getHtml('http://noxue.com/'+match.group(1)))

def start_server(port):
    http_server = HTTPServer(('', int(port)), TestHTTPHandler)
    http_server.serve_forever()	
 	
start_server(80)
