from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the one of the  best  my Flask App!"

@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/form" , methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        return f'Welcome {request.form["name"]}'
    return render_template('form.html')

@app.route("/success/<int:score>")
def some(score):
    res = "" 
    if score>=50:
        res ="Passed"
    else:
        res = "Failed"
    return render_template('result.html', result=res)

@app.route("/successres/<int:score>")
def success(score):
    res = "" 
    if score>=50:
        res ="Passed"
    else:
        res = "Failed"

    exp ={"results":res , "score":score}
    return render_template('result1.html', result=exp)



if __name__ == "__main__":
    app.run(debug=True)