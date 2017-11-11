from flask import Flask, jsonify, json;
from myclasses import MyClass1, MyClass2;

# Load other.py
# Notice that the top-level code gets executed when the import happens:
import other;

# Load other2.py, but note that this is the second time (also imported from other.py).
# So the top-level code in other2.py doesn't get executed again.
import other2;

app = Flask(__name__);

# Testing to see what __name__ does (shows the name of the file, or __main__ if this is the entry point)
print("Our name: " + __name__);
# Calling a method from a different module:
print("Other name: " + other.name());
print("Other2 name: " + other2.name());


# ----- Demonstration of passing a function -----------------------------------
def sayhello():
    print("Hello!");


# Wrap the function above
wrappedsayhello = other2.wrapper(sayhello);
# Call the wrapped version
print("Calling wrappedaayhello:");
wrappedsayhello();


# ----- Demonstrate decoration (same as above) ---------------------------------
@other2.wrapper
def wrappedaayhello2():
    print("Hello2!");


# Call the wrapped version
print("Calling wrappedaayhello2:");
wrappedaayhello2();

# ----- Demonstrate instantiation of an object ----------------------------------
#
c = MyClass1("Bruce");
print("Method call: " + c.getname());
c = MyClass2();


# ----- Flask Stuff -------------------------------------------------------------
# The at sign here is a "function decorator"
#
# This is functionally equivalent to the following:
#
# def hello_world():
#   return "Hello World";
# hello_world = app.route('/')(hello_world)
#
@app.route('/')
def hello_world():
    return "Hello World ! Demo";


# An example of a Flask method that has more control over the response
@app.route('/json')
def summary():
    d = {
        "a": 6,
        "name": "Bruce"
    };
    response = app.response_class(
        response = json.dumps(d),
        status = 200,
        mimetype = "application/json")
    return response;


# This does exactly the same thing as the example above
@app.route('/json2')
def getjson():
    d = {
        "a": 6,
        "name": "Bruce"
    };
    return jsonify(d);


# This is is used to make sure that the app.run only happens from the top-level file:
if __name__ == '__main__':
    app.run();
