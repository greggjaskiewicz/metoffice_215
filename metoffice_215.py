#!/usr/bin/python

import mechanize
import cookielib


def openAndAuthorise():

  br = mechanize.Browser()
  cj = cookielib.LWPCookieJar()
  br.set_cookiejar(cj)
  br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
  br.set_handle_robots(False)
  br.set_handle_equiv(False)
  r = br.open('https://secure.metoffice.gov.uk/logon.jsp')

  br.select_form(name="LogonForm")
  br["username"] = "USER"
  br["password"] = "PASS!"
  response2 = br.submit()

  #print(response2.read())

  brief_charts = br.open("https://secure.metoffice.gov.uk/aviation/aviationProductList.do?action=sigwx")
  #print(brief_charts.read())

  return br


def downloadPdfFrom(browser, url, fileTo):

  pdf1doc = browser.open(url)

  pdf1 = pdf1doc.read()

  fpdf = open(fileTo, "w")
  fpdf.write(pdf1)
  fpdf.close()

files = [
  ["https://secure.metoffice.gov.uk/aviation/productcomponentserver?productId=8003&componentId=0&imageFile=F215_1800.pdf", "F215_1800.pdf"],
  ["https://secure.metoffice.gov.uk/aviation/productcomponentserver?productId=8002&componentId=0&imageFile=F215_1200.pdf", "F215_1200.pdf"],
  ["https://secure.metoffice.gov.uk/aviation/productcomponentserver?productId=8002&componentId=0&imageFile=F215_0600.pdf", "F215_0600.pdf"]
]

br = openAndAuthorise()
for x in files:
  downloadPdfFrom(br, x[0], x[1])

