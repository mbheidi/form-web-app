from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    preference = request.args['preference'] 
    #The request object stores information about the request sent to the server.
    #args is an ImmutableMultiDict (like a dictionary but can have mutliple values for the same key and can't be changed)
    #The information in args is visible in the url for the page being requested. ex. .../response?color=blue
    if preference == 'Tell me a joke ':
        reply = "Why was the math book sad? Because it had so many problems hahaha"
    else:
        reply = "Try some of these! This link provides over 80 fun activities to do when you're bored! https://www.goodhousekeeping.com/life/a26872864/what-to-do-when-bored/ "
    return render_template('response.html', response = reply)
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
