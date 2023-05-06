# print(__name__) -to print where it is invoked from-->main

from flask import Flask

app=Flask(__name__)
@app.route("/") #To apply which path to match

def hello_world():
  return "Helloo Ghana"

if(__name__ == '__main__'):
  app.run(host='0.0.0.0',debug=True)