from flask import Flask
from flask import render_template, request, url_for
from flaskext.markdown import Markdown
#from outer_test import test2
import urllib2
import json

app = Flask(__name__)
Markdown(app)
namelist=[]
resultlist=[]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def hello():
    name = request.form['checking']
    temp_name = name
    name = name.encode('utf-8')
    name = urllib2.quote(name)
    url_tem= "http://csclab11.cs.nthu.edu.tw:5000/?q=%s"%name
    result = urllib2.urlopen(url_tem).read()
    #result = json.load(result)
    print type(result)
    d = json.loads(result)
    print d["result"]
    namelist.append(temp_name)
    resultlist.append(d["result"])
    # result = get_result(name)

    return render_template('index.html', name=temp_name,result=d["result"])

@app.route('/about')
def about():
    # return "about"
    return render_template('about.md')

#@app.route('/test')
#def test():
#    result= test2()
#    json_form=json.load(result)
#    return json_form

if __name__ == '__main__':
    app.run(debug=True)
