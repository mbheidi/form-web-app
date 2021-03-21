from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    list = request.args['list'] 
    #The request object stores information about the request sent to the server.
    #args is an ImmutableMultiDict (like a dictionary but can have mutliple values for the same key and can't be changed)
    #The information in args is visible in the url for the page being requested. ex. .../response?color=blue
    if list == 'Tell me a joke':
        reply = "Sure! Why was the math book sad? Because it had so many problems hahaha"
    else:
        reply = "Try some of these! Here are some cool activities that you can try if you are bored!
1. Play a card game
2. Play a board game 
3. Play a computer game 
4. Play a sport 
5. Watch a movie 
6. Binge a series 
7. Watch funny YouTube videos
8. Sing along to your favorite hits 
9. Play with your pet 
10. Try new hairstyles
11. Fly a kite 
12. Visit an arcade 
13. Hunt some ghosts – research some haunted places nearby and have a spooky time visiting them.
14. Learn a magic trick 
15. Go roller skating 
16. Go on a road trip 
17. Go for a picnic
18. Go bowling
19. Have a water fight
20. Create a playlist 
21. Make a slip ‘n slide 
22. Make a gift list 
23. Play Twister 
24. Browse AskReddit 
25. Daydream"

    return render_template('response.html', response = reply)
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
