'''
Purpose: gain familiarity

'''
from flask import Flask
from flask import request #Flask global that represents the request that the client has made to your application. This contains things like cookies, the path, and, in our usage, the query string.

app = Flask(__name__) #use whatever the current namespace is

#the following is a decorator, a function that wraps around another function
#the '/' indicates to route to this function on the websites index ie www.website.com/ <-
@app.route('/')
#function/view
def index(name='Mark'):
    return 'Hello World, I <3 ' + name

app.run(debug=True, port=5000, host='127.0.0.1') #debug is true so that it updates when we make changes
