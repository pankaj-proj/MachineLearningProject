from flask import Flask

app=Flask(__name__)

@app.route("/",method=['GET','POST'])
def index():
    return "Starting machine learning project"

if __name__=="__main__"
    app.run(debug=True)
