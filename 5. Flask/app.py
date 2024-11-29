from flask import Flask

### WSGI Application
app= Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this Flask course. Mboh"


@app.route("/index")
def index():
    return "Ini index"

if __name__=="__main__":
    app.run(debug= True)