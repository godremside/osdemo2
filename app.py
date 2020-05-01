from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def calvalute():
    fnum = request.form['fnum']
    snum = request.form['snum']
    operation = request.form['operation']
    if operation == 'add':
       sum = float(fnum) + float(snum)
       return render_template('index.html',sum=sum)
    elif operation == 'subtract':
       sum = float(fnum) - float(snum)
       return render_template('index.html',sum=sum)
    elif operation == 'multiply':
       sum = float(fnum) * float(snum)
       return render_template('index.html',sum=sum)
    elif operation == 'divide':
       sum = float(fnum) / float(snum)
       return render_template('index.html',sum=sum)
    else: 
       return render_template('index.html')


if __name__ == "__main__":
     app.run(debug=True)