#!/usr/bin/env python2.5
#Noah Gift
import decimal
import wsgiref.handlers
import os
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.ext.webapp import template
class ChangeModel(db.Model):
user = db.UserProperty()
input = db.IntegerProperty()
date = db.DateTimeProperty(auto_now_add=True)
class MainPage(webapp.RequestHandler):
"""Main Page View"""
def get(self):
user = users.get_current_user()
if users.get_current_user():
url = users.create_logout_url(self.request.uri)
url_linktext = ‘Logout’
else:
url = users.create_login_url(self.request.uri)
Cloud Computing | 249
url_linktext = ‘Login’
template_values = {
‘url’: url,
‘url_linktext’: url_linktext,
}
path = os.path.join(os.path.dirname(__file__), ‘index.html')
self.response.out.write(template.render(path, template_values))
class Recent(webapp.RequestHandler):
"""Query Last 10 Requests"""
def get(self):
#collection
collection = []
#grab last 10 records from datastore
query = ChangeModel.all().order('-date')
records = query.fetch(limit=10)
#formats decimal correctly
for change in records:
collection.append(decimal.Decimal(change.input)/100)
template_values = {
'inputs': collection,
'records': records,
}
path = os.path.join(os.path.dirname(__file__), 'query.html')
self.response.out.write(template.render(path,template_values))
class Result(webapp.RequestHandler):
"""Returns Page with Results"""
def __init__(self):
self.coins = [1,5,10,25]
self.coin_lookup = {25: "quarters", 10: "dimes", 5: "nickels", 1: "pennies"}
def get(self):
#Just grab the latest post
collection = {}
#select the latest input from the datastore
change = db.GqlQuery("SELECT * FROM ChangeModel ORDER BY date DESC LIMIT 1")
for c in change:
change_input = c.input
#coin change logic
coin = self.coins.pop()
num, rem = divmod(change_input, coin)
if num:
collection[self.coin_lookup[coin]] = num
while rem > 0:
coin = self.coins.pop()
num, rem = divmod(rem, coin)
250 | Chapter 8: OS Soup
if num:
collection[self.coin_lookup[coin]] = num
template_values = {
'collection': collection,
'input': decimal.Decimal(change_input)/100,
}
#render template
path = os.path.join(os.path.dirname(__file__), 'result.html')
self.response.out.write(template.render(path, template_values))
class Change(webapp.RequestHandler):
def post(self):
"""Printing Method For Recursive Results and While Results"""
model = ChangeModel()
try:
change_input = decimal.Decimal(self.request.get('content'))
model.input = int(change_input*100)
model.put()
self.redirect('/result')
except decimal.InvalidOperation:
path = os.path.join(os.path.dirname(__file__), 'submit_error.html')
self.response.out.write(template.render(path,None))
def main():
application = webapp.WSGIApplication([('/', MainPage),
('/submit_form', Change),
('/result', Result),
('/recent', Recent)],
debug=True)
wsgiref.handlers.CGIHandler().run(application)
if __name__ == "__main__":
main()

#Greedy coin web application
#2.7 未整理 google应用 270页