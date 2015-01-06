from httplib2 import Http
from urllib import urlencode
import json

def test2(query):
    jsonStr=json.dumps(query)
    # h=Http()
    # query_url="http://csclab11.cs.nthu.edu.tw:5000/?q="+query
    # resp, content = h.request(query_url,"GET")
    # data = dict(name="Joe",comment="A test comment")
    # resp, content=h.request("http://bitworking.org/news/223/Meet-Ares", "POST", urlencode(data))
    return jsonStr

if __name__ == "__main__":
    ques="åµåµ"
    print test2(ques)
