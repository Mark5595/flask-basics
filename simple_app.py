'''
Purpose: gain familiarity

'''
from flask import Flask
from flask import render_template #allows us to access/use the templates
#from flask import request #Flask global that represents the request that the client has made to your application. This contains things like cookies, the path, and, in our usage, the query string.

app = Flask(__name__) #use whatever the current namespace is

#the following is a decorator, a function that wraps around another function
#the '/' indicates to route to this function on the websites index ie www.website.com/ <-
@app.route('/')
@app.route('/<name>') #views can have more than one route!, this tells flask to capture what comes after as a variable
#function/view to display name that is passed in after url, defaults to 'Mark'
def index(name='Mark'):

    '''

    query string: (ugly) The part of a URL that comes after the ?. You'll notice that the information after this looks like keyword arguments.
    name = request.args.get('name', name) #if we get a name will use that, if we dont use the default name
                                        #i.e. url/?name=Bill is how Bill will be passed into the function

    '''

    return render_template('index.html', name = name)

#when passing arguments via the route url they are of type string unless otherwise specified
#if something is a typed cased wrong we will get a 404 error
@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
#function/view to return the sum of the two numbers (either floats or ints) entered
def add(num1, num2):
    return render_template("add.html", num1 = num1, num2 = num2)


@app.route('/multiply/<int:num1>/<int:num2>')
#view to multiply two ints
def multiply(num1, num2):
    product = num1 * num2
    return '{} x {} = {}'.format(num1,num2,product)

app.run(debug=True, port=5000, host='127.0.0.1') #debug is true so that it updates when we make changes
