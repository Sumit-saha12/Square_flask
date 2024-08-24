from flask import Flask,request,render_template
app = Flask(__name__)

@app.route('/'):
def welcome():
    return 'Welcome'

@app.route('/square',methods=['GET','POST'])
def square():
    if request.method=="POST":
        number = int(request.form['num'])
        return render_template('square.html',number=number)
    return render_template('form.html')

if __name__=='__main__':
    app.run(debug=True)
