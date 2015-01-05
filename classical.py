from flask import Flask
from flask import render_template, request, url_for
app = Flask(__name__)

namelist=[]
resultlist=[]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def hello():
    name = request.form['checking']
    result = "QQ"+name
    namelist.append(name)
    resultlist.append(result)
    # result = get_result(name)
    return render_template('index.html', name=name,result=result, namelist=namelist[1:], resultlist=result[1:])


if __name__ == '__main__':
    app.run(debug=True)
